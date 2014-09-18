#!/usr/bin/python
# -*- coding: utf-8 -*-
# *******************************shutdownPi*******************************
# 28.03.2014 Selim Olcer 
# 

import time
import RPi.GPIO as GPIO
import os

def shutdown(buton):
	shutdown=0
	while True:
		mybutton = GPIO.input(buton)					#buton degerini okuyoruz.
		if mybutton == False:	
			t0 = time.clock()						#süre tutmak için t0'a o anki zamanı alıyoruz.
			fark=t0
			print "Baslangic: " + str(t0) 
			while GPIO.input(buton) == False:				#butona basılı tutulduğu sürece bekliyoruz
				t1 = time.clock()					#t1'e yeni zamanı alıyoruz
				if t1-t0>2 :						# kapatilacak sure
					shutdown=1					#buradan çıkıp raspberry pi yi kapatıyoruz
					break
				if t1-fark>1 :					#
					print str(t1-t0) +"sn"
					fark=t1					#geçen süredeki farkı bulmak için fark registerini güncelliyorum.
			t1 = time.clock()						#t1'e yeni zamanı alıyoruz
			print "t0: "
			print t0
			print "t1: "
			print t1
		if shutdown==1:							#while True'dan cikmak icin
			break
	if shutdown==1:
		print "bye bye..."
		os.system("sudo shutdown -h now")


buton = 11										#Buton'un baglanacagi pin numarasi
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buton,GPIO.IN,pull_up_down = GPIO.PUD_UP)				#buton'u input olarak tanımlıyorum. Pull up direncini aktif ediyorum.
GPIO.add_event_detect(buton, GPIO.FALLING, callback=shutdown, bouncetime=200)	#dusen kenarda 200ms bekleyip shutdown fonksiyonuna gidiyor
while True:
	time.sleep(.2)			
