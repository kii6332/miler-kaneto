import pyautogui as pag
input("pos1:")
st = pag.position()
print(st)
input("pos2:")
en = pag.position()
print(en)
print(abs(abs(st[0])-abs(en[0])),abs(abs(st[1])-abs(en[1])))
