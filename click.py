from pynput.mouse import Controller, Button
import time
mouse=Controller()

earn, gift, home, sports, notice, low, back= (1460,1000), (1625,525), (1170,1010), (1440,140), (1360,220), (1360,975), (1680,910)

def a(veces):
	mouse.position=home
	mouse.click(Button.left)
	time.sleep(1)

	mouse.position=sports
	mouse.click(Button.left)
	time.sleep(2.5)

	for i in range(veces):
		mouse.position=notice
		mouse.click(Button.left)
		time.sleep(6)

		mouse.position=low
		mouse.press(Button.left)

		for i in range(150):
			mouse.move(0,-8)
			time.sleep(0.01)
		time.sleep(6)

		for i in range (155):
			mouse.move(0,8)
			time.sleep(0.01)
		time.sleep(6)

		for i in range (265):
			mouse.move(0,-30)
			time.sleep(0.01)
		mouse.release(Button.left)
		mouse.position=low
		mouse.press(Button.left)

		for i in range (230):
			mouse.move(0,-30)
			time.sleep(0.01)
		time.sleep(4)

		mouse.release(Button.left)

		mouse.position=back
		mouse.click(Button.left)
		time.sleep(2)

		mouse.position=earn
		mouse.click(Button.left)
		time.sleep(2)

		mouse.position=gift
		mouse.click(Button.left)
		time.sleep(3)

		mouse.position=back
		mouse.click(Button.left)
		time.sleep(3.5)
	return