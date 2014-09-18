Source code for multi-view autostereoscopic display based on pico projectors, and Raspberry Pi boards.

Author(s):

- Kaan Akşit

File descriptions:

- rc.local : to be used as /etc/rc.local in Raspbian.
- ip.sh : Gets the ip value, and initiate automatic ip sending python script.
- startup_mailer.py : A python script to send ip via email.
- con2fb.c : Script to assign TTY to framebuffer devices.

- offsets.csv dosyasında projektör numaralandırması (Projektörlerin mems aynasına dışardan bakarken):

-------a3---------- -------a2---------- -------a1----------
******************* ******************* *******************
*O1*O5*O4*O3*O2*OO* *O1*O5*O4*O3*O2*OO* *O1*O5*O4*O3*O2*OO*
******************* ******************* *******************

How to make con2fb:

 gcc con2fb.c -o con2fb
