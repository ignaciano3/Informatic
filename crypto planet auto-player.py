'''
This code was programmed by Ignacio Garcia
It is adapted to a 1920x1080 screen for PC
No restrictions in use or share
Make your own personalized code!!
For other python aplications: https://github.com/ignaciano3/Informatic.git
'''

from pynput.mouse import Button, Controller #install module by using pip3 install pynput in cmd
import time
mouse = Controller()

# check the values below by executing i.e.:
# mouse.position=rocket
# mouse.position=(newX,newY)
# rocket =(newX,newY)

button_rocket = (610,880)
shot_rocket = (150,500)
yes = (1030,740)
time_between_rocket = 0.3 #seconds
back_rocket=(1700,100)
start_tap = (400,530)
do_tap = (1350,600)
time_between_tap  = 0.6 #seconds

def rocket (times=230):
	mouse.position=button_rocket
	mouse.click(Button.left)
	time.sleep(1)
	mouse.position=yes
	mouse.click(Button.left)
	time.sleep(1)
	
	mouse.position=shot_rocket
	for i in range(times):
		time.sleep(time_between_rocket)
		mouse.click(Button.left)
	
	time.sleep(1)
	mouse.position=back_rocket
	mouse.click(Button.left)
	time.sleep(1)
	mouse.position=yes
	mouse.click(Button.left)
	time.sleep(0.5)

	return

def tap (times=200):
	mouse.position=start_tap
	mouse.click(Button.left)
	time.sleep(0.2)
	mouse.position=yes
	mouse.click(Button.left)
	mouse.position=do_tap

	for x in range(times):
		time.sleep(time_between_tap)
		mouse.click(Button.left)
	
	return

# to start write rocket() or tap()

#I bet you to program the same but with ads
