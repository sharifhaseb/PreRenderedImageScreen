# Before running this scipt, open goose.blend.
# Vector comes with mathutils.
import mathutils
# Set Camera object to a variable.
cam    = bpy.data.objects['Camera']
# Set the gooses to variables.
goose1 = bpy.data.objects['goose1']
goose2 = bpy.data.objects['goose2']
goose3 = bpy.data.objects['goose3']
# Rotate the gooses according to the image set number.
goose1.rotation_euler = (pi/2,0,0)
goose2.rotation_euler = (pi/2,0,0)
goose3.rotation_euler = (pi/2,0,0)
# Changes image set number.
for SetNo in range(0,10):
    # Loop to create images from different perspectives.
    for counter in range(0,36):  
        # Angle is calculated according to counter.
        alpha = -5*(counter-SetNo)
        # Radius of the circle.
        h     = -0.7
        # Coordinates for the new camera location.
        x     = sin(radians(alpha))*h; y= cos(radians(alpha))*h; z= 0
        # Set Camera location.
        cam.location = (x,y,z)
        # Camera rotation is set accordingly to new location.
        cam.rotation_euler = (pi/2+radians(alpha),pi/2,0)
        # Rotate the gooses according to the image set number.
        goose1.rotation_euler = (pi/2,0,0)
        goose2.rotation_euler = (pi/2,0,0)
        goose3.rotation_euler = (pi/2,0,0)
        # Determines where to save image.
        bpy.data.scenes['Scene'].render.filepath = '/home/oml/pi3b/Blender/v%d/image%s.jpg' % (SetNo,counter) 
        #windows dizini icin /xxx seklinde olmali
        # Renders image.
        bpy.ops.render.render(write_still=True)
        # Increment counter.
        counter += 1
