import con
import ind
import pyautogui as pag
import random
import time
maps = [[] for _ in range(9)]
if ind.ind_sc_chk("minesweeper/main"):
	pag.press('1')
	#94px
	print("press:1")
con.mov((699,429),0.0025)
pag.click()
time.sleep(0.025)
for y in range(8):
	for x in range(8):
		bky = 107+(94*y)+10
		bkx = 374+(94*x)+20
		con.mov((bkx,bky),0)
		pag.click(button='right', clicks=2, interval=0.1)
con.mov((445,183),0.0025)
for y in range(8):
	for x in range(8):
		bky = 107+(94*y)-2
		bkx = 374+(94*x)+2
		con.mov((bkx,90),0)
		o = ind.ind_sc_chk("minesweeper/open",False,(bkx,bky,94,94),0,True)*100
		u = ind.ind_sc_chk("minesweeper/mark",False,(bkx,bky,94,94),0,True)*100
		n1 = ind.ind_sc_chk("minesweeper/1",False,(bkx,bky,94,94),0,True)*100
		n2 = ind.ind_sc_chk("minesweeper/2",False,(bkx,bky,94,94),0,True)*100
		n3 = ind.ind_sc_chk("minesweeper/3",False,(bkx,bky,94,94),0,True)*100
		n4 = ind.ind_sc_chk("minesweeper/4",False,(bkx,bky,94,94),0,True)*100
		n5 = ind.ind_sc_chk("minesweeper/5",False,(bkx,bky,94,94),0,True)*100
		n6 = ind.ind_sc_chk("minesweeper/6",False,(bkx,bky,94,94),0,True)*100
		n7 = ind.ind_sc_chk("minesweeper/7",False,(bkx,bky,97,97),0,True)*100
		n8 = ind.ind_sc_chk("minesweeper/8",False,(bkx,bky,97,97),0,True)*100
		mx = max(o,u,n1,n2,n3,n4,n5,n6,n7,n8)
		if o == mx:
			maps[y].append("o")
		elif u == mx:
			maps[y].append("u")
		elif n1 == mx:
			maps[y].append(1)
		elif n2 == mx:
			maps[y].append(2)
		elif n3 == mx:
			maps[y].append(3)
		elif n4 == mx:
			maps[y].append(4)
		elif n5 == mx:
			maps[y].append(5)
		elif n6 == mx:
			maps[y].append(6)
		elif n7 == mx:
			maps[y].append(7)
		elif n8 == mx:
			maps[y].append(8)
for i in range(8):
	print(f"{maps[i]}")
con.mov((135,163),0.0025)
