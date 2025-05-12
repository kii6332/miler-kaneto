import pyautogui
def mov(at = (0,0),ti = 1,shift = (0,0)):
	x = at[0] + shift[0]
	y = at[1] + shift[1]
	pyautogui.moveTo(x, y, duration=ti)
def mov_sc(at = (0,0),ti = 1,shift = (0,0)):
	x = at[0]
	y = at[1]
	if y>40 and y<870:
		mov(at,ti,shift)
	else:
		return
