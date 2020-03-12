'''
This code was programmed by Ignacio Garcia
It is adapted to a 1920x1080 screen for PC
No restrictions in use or share
Make your own personalized code!!
'''

from pynput.mouse import Button, Controller #install module by using pip3 install pynput in cmd
import time
mouse = Controller()

# check this by position previously:
# mouse.position=rocket
# mouse.position=(newX,newY)
# rocket =(newX,newY)

button_rocket = (780,500)
shot_rocket = (1310,330)
yes_rocket = (1050,430)
time_between_rocket = 0.3 #seconds

start_tap = (650,300)
yes_tap = (1020,420)
do_tap = (1165,350)
time_between_tap  = 0.6 #seconds

def rocket (times=240):
	mouse.position=button_rocket
	mouse.click(Button.left)
	mouse.position=yes_rocket
	time.sleep(0.2)
	mouse.click(Button.left)
	
	mouse.position=shot_rocket
	for i in range(times):
		time.sleep(time_between_rocket)
		mouse.click(Button.left)
	
	return

def tap (times=200):
	mouse.position=start_tap
	mouse.click(Button.left)
	time.sleep(0.2)
	mouse.position=yes_tap
	mouse.click(Button.left)
	mouse.position=do_tap

	for x in range(times):
		time.sleep(time_between_tap)
		mouse.click(Button.left)
	
	return

# to start write rocket() or tap()

#I bet you to program the same but with ads