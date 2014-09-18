#!/usr/bin/python
# -*- coding: utf-8 -*-
#/CONTENT/ klasörü altındaki image0,1,2... dosyalarını slitlere bölüp uygun offsete göre ekranlara yazar.

__author__ = ('Kaan Akşit')

import sys,os,time,pygame,socket,csv
from pygame.locals import *

# CSV reader to read offset positions of the pico projectors.
def ReadCSV(filename,BlockNumber):
    # Open a socket to read CSV.
    ifile   = open(filename, "rb")
    reader  = csv.reader(ifile)
    offsets = []
    # Skip header
    next(reader)
    # Read the CSV row by row.
    for row in reader:
        # Avoid empty lines in CSV
        if len(row) > 0:
            # Strip white spaces from CSV file.
            row = ([element.strip() for element in row])
            # Match the block number to get the related data into the array.
            if row[0] == BlockNumber:
                offsets.append(row)
    # Close the socket.
    ifile.close()
    return offsets

# If ShowImage is set to yes, the content is created using sample input under Content folder.
# BlockNumber determines the position of the six pico projector.
def ConvertContent(ShowImage='yes',SetNo=0):
    # Number of views.
    NumberOfViews = 6
    # Recognize Raspberry PI.
    NameOfTheHost = socket.gethostname()
    if NameOfTheHost == 'PI3B01':
        BlockNumber          = 'a1'
        ImageCounterConstant = 0
    elif NameOfTheHost == 'PI3B02':
        BlockNumber          = 'a2'
        ImageCounterConstant = NumberOfViews
    elif NameOfTheHost == 'PI3B03':
        BlockNumber          = 'a3'
        ImageCounterConstant = 2*NumberOfViews  
    # Reading offsets.csv to retrieve the offset values.
    offsets = ReadCSV("offsets.csv",BlockNumber)
    # Width, and height of the desired image.
    width         = 848
    height        = 480
    # Colors are defined.
    colors     = [
                 (255,0,0),
                 (0,255,0),
                 (0,0,255),
                 (255,255,0),
                 (255,0,255),
                 (0,255,255),
                 (100,20,50),
                 (255,255,255),
                 (127,100,0),
                 (0,255,100),
                 (0,100,127),
                 (127,127,0),
                 (127,255,127),
                 (0,127,127),
                 (200,0,50),
                 (50,255,0),
                 (100,50,100),
                 (150,150,0),
                 (0,150,150),
                 (100,200,0),
                 (0,100,200),
                 (200,0,100),
                 (100,0,200),
                 (200,100,0),
                 (50,0,255),
                 (100,150,50),
                 (0,255,150),
                 (50,100,70),
                 (0,30,200),
                 (100,100,0),
                 (40,10,23),
                 (70,80,90),
                 (138,56,190),
                 (123,23,10),
                 (234,123,34),
                 (4,4,233),
                 (23,56,12),
                 (43,34,34),
                 (43,255,34),
                 (65,45,23),
                 (90,90,56),
                 (45,122,56),
                 (230,120,42),
                 (45,45,200),
                 (80,0,255),
                 (100,200,67),
                 (200,0,34),
                 (100,250,230),
                 (45,12,32),
                 (12,99,200),
                 (234,234,53),
                 (43,89,75),
                 ]
    # Slit is defined geometrically.
    SlitHeight      = 13
    SlitSize        = [0, SlitHeight]
    # Load multiview images and slice them into pieces.
    ImageSlices     = []
    ImageCounter    = []
    # List of image files to be used.
    MultiViewImages = []
    hup             = 36
    for no in xrange(0,hup):
        MultiViewImages.append('./Blender/v%d/image%s.png' % (SetNo,no))
    # Reverse order the images for correct registration on the screen.
    MultiViewImages = reversed(MultiViewImages)
    # Create Image Slices to be displayed by each pico projector.
    for ImageName in MultiViewImages:
        # Adding a new slice to the slices matrix.
        ImageSlices.append(LoadImage(ImageName,SlitHeight))
    # Number of slits calculated. +10 to avoid missing slit.
    NumberOfSlits = height / SlitSize[1] + 10
    # ImageCounter vector is built.
    for z in xrange(0,NumberOfSlits):
        # ImageCounter used in displaying right images.
       ImageCounter.append(ImageCounterConstant)
    # Loop to create each view.
    for j in xrange(0,NumberOfViews):
        # Setting offset
        OffsetLeft  = int(offsets[j][2])
        OffsetTop   = int(offsets[j][3])
        SlitSize[0] = int(offsets[j][4])
        # Creating the new surface.
        NewSurface = pygame.Surface((width, height))
        # Loop to create each slit.
        for i in xrange(0,NumberOfSlits):
            if (i*SlitSize[1] + OffsetTop) > 0:
                slit       = pygame.Rect((OffsetLeft,(i*SlitSize[1] + OffsetTop)), SlitSize)
            else:
                slit       = pygame.Rect((OffsetLeft,((NumberOfSlits + i)*SlitSize[1] + OffsetTop)), SlitSize)
            pygame.draw.rect(NewSurface, colors[i], slit, 0)
            # Check if the OffsetLeft is calibrated by drawing a line at the center.
            pygame.draw.rect(NewSurface, (255,255,255), pygame.Rect(slit.centerx-100,slit.centery,SlitHeight,slit.height) ,0)
            # If image display is desired, this if loop takes on.
            if ShowImage == 'yes':
                # Specify which color is replaced with an image.
                a = i 
                # Choosing the specific slices in the image for correct image registration.
                for c in xrange(0,hup):
                    if colors[i] == colors[c]:
                        ChosenImage = ImageSlices[c]                    
                        # Adjusting image according to the image height.
                        ChosenImage[ImageCounter[a]] = pygame.transform.scale(ChosenImage[ImageCounter[a]],(SlitSize[0], SlitSize[1]))
                        # Necessary slice is being place accordingly.
                        NewSurface.blit(ChosenImage[ImageCounter[a]], slit)                
                        # Increasing the image counter to take right slice in the next step.
                        ImageCounter[a] += 1
        pygame.image.save(NewSurface, './Content/v%d/samplescreen%d.png' % (SetNo,j))
    os.system("mv ./Content/v%d/samplescreen1.png ./Content/v%d/samplescreen12.png" % (SetNo,SetNo))
    os.system("mv ./Content/v%d/samplescreen5.png ./Content/v%d/samplescreen1.png"  % (SetNo,SetNo))
    os.system("mv ./Content/v%d/samplescreen2.png ./Content/v%d/samplescreen13.png" % (SetNo,SetNo))
    os.system("mv ./Content/v%d/samplescreen3.png ./Content/v%d/samplescreen14.png" % (SetNo,SetNo))
    os.system("mv ./Content/v%d/samplescreen4.png ./Content/v%d/samplescreen15.png" % (SetNo,SetNo))
    os.system("mv ./Content/v%d/samplescreen12.png ./Content/v%d/samplescreen2.png" % (SetNo,SetNo))
    os.system("mv ./Content/v%d/samplescreen13.png ./Content/v%d/samplescreen3.png" % (SetNo,SetNo))
    os.system("mv ./Content/v%d/samplescreen14.png ./Content/v%d/samplescreen4.png" % (SetNo,SetNo))
    os.system("mv ./Content/v%d/samplescreen15.png ./Content/v%d/samplescreen5.png" % (SetNo,SetNo))
    return True

# Function to load image and slice it
def LoadImage(path,SlitHeight=20,reverse=0,width=234,height=848,rotate='yes'):
    # Image load takes place.
    Image   = pygame.image.load(path)
    # Rotate Image.
    Image   = pygame.transform.rotate(Image, -90)
    # Mirror image horizontally.
    Image   = pygame.transform.flip(Image,True,False)
    # Transform the image into usable format.
    Image   = pygame.transform.scale(Image,(width, height))
    # Image properties are saved.
    ImgH    = Image.get_height()
    ImgW    = Image.get_width()
    Cropped = []
    # Producing the slices.
    for i in xrange(0,ImgW/SlitHeight):   
        # Cropping takes place. 
        Cropped.append(pygame.Surface((SlitHeight,ImgH)))
        Cropped[i].blit(Image, (0,0), (i*SlitHeight,0,SlitHeight,ImgH))
        # Rotating the each slice with 90.
        Cropped[i] = pygame.transform.rotate(Cropped[i], -90)
    # Reverse ordering slices.
    if reverse == 1:
        Cropped = Cropped[::-1]
    return Cropped

def MovingImages():
    ShowImage = 'yes'
    # Setting ShowImage through shell.
    if len(sys.argv) > 1:
        if sys.argv[1] == 'no':
            ShowImage = 'no'
    # Maximum set number.
    SetMax = 1
    # Processing all of the image sets.
    for SetNo in xrange(0,SetMax):
        # Create the corresponding folders.
        newpath = r'./Content/v%d/' % SetNo
        if not os.path.exists(newpath): os.makedirs(newpath)
        # Convert the image set into usable format.
        ConvertContent(ShowImage,SetNo)
        print 'Image set no: %d is processed.' % SetNo
    return True

if __name__ == '__main__':
    sys.exit(MovingImages())
