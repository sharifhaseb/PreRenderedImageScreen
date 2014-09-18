rm /home/pi/pi3b/Content/tty*
ffmpeg -loop 1 -i /home/pi/pi3b/Content/v%01d/samplescreen0.png -t 10 -b 10k -r 2 /home/pi/pi3b/Content/tty0.avi
ffmpeg -loop 1 -i /home/pi/pi3b/Content/v%01d/samplescreen1.png -t 10 -b 10k -r 2 /home/pi/pi3b/Content/tty1.avi
ffmpeg -loop 1 -i /home/pi/pi3b/Content/v%01d/samplescreen2.png -t 10 -b 10k -r 2 /home/pi/pi3b/Content/tty2.avi
ffmpeg -loop 1 -i /home/pi/pi3b/Content/v%01d/samplescreen3.png -t 10 -b 10k -r 2 /home/pi/pi3b/Content/tty3.avi
ffmpeg -loop 1 -i /home/pi/pi3b/Content/v%01d/samplescreen4.png -t 10 -b 10k -r 2 /home/pi/pi3b/Content/tty4.avi
ffmpeg -loop 1 -i /home/pi/pi3b/Content/v%01d/samplescreen5.png -t 10 -b 10k -r 2 /home/pi/pi3b/Content/tty5.avi
