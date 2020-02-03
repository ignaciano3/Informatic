from pynput.mouse import Controller, Button
import time


mouse=Controller()

#You have to adjust this measures to your screen, mine is 1920x1080. 
#Put the emulator in the right of your screen with some margin to the right and no margin to bottom
earn, gift, home, sports, notice, low, back= (1460,1000), (1625,525), (1170,1010), (1440,140), (1360,220), (1360,975), (1680,910)

def auto(times = 50):
# PRE: Have installed pynput library
# POST: Mouse journey

	# Starting operations
	mouse.position = home
	mouse.click(Button.left)
	time.sleep(1)

	mouse.position = sports
	mouse.click(Button.left)
	time.sleep(2.5)

	#Entire process
	for i in range(times):
		
		#First: Clicks the notice
		mouse.position = notice
		mouse.click(Button.left)
		
		#Wait some time for notice to load
		time.sleep(6)
		
		# Second: start by pressing the lowest part of the screen and dragging to the top
		mouse.position = low
		mouse.press(Button.left)
		for i in range(150):
			mouse.move(0,-8)
			time.sleep(0.01)
		time.sleep(6)
		
		#Go backwards
		for i in range (155):
			mouse.move(0,8)
			time.sleep(0.01)
		time.sleep(6)
		
		#Go forwards
		for i in range (265):
			mouse.move(0,-30)
			time.sleep(0.01)
		
		#Go even more forward by sliding through the lowest part againg
		mouse.release(Button.left)
		mouse.position=low
		mouse.press(Button.left)
		for i in range (230):
			mouse.move(0,-30)
			time.sleep(0.01)
		time.sleep(4)
		
		# Third: go back to home
		mouse.release(Button.left)
		mouse.position=back
		mouse.click(Button.left)
		time.sleep(2)

		#Fourth: go to earn
		mouse.position=earn
		mouse.click(Button.left)
		time.sleep(2)
		
		#Receive the gift
		mouse.position=gift
		mouse.click(Button.left)
		time.sleep(3)
	
		#Fifth: go back to home and wait to restart the process
		mouse.position=back
		mouse.click(Button.left)
		time.sleep(3.5)
	return
auto()
