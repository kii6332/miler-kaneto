import pyautogui
import numpy as np
import cv2
import sys
from transformers import pipeline
from transformers import AutoImageProcessor, AutoModelForImageClassification
import torch
def ind_sc_fd(ref="discord",full_sc=True,size=(0,0,1,1),fake=False,fk=(10,10)):
	fil = (f"ref/{ref}.png")
	if full_sc:
		ind = pyautogui.screenshot()
		ph = np.array(ind)
	else:
		ind = pyautogui.screenshot(region=size)
		ph = np.array(ind)
	ph = cv2.cvtColor(ph,cv2.COLOR_RGB2BGR)
	tem = cv2.imread(fil,0)
	bph = cv2.cvtColor(ph,cv2.COLOR_BGR2GRAY)
	res = cv2.matchTemplate(bph,tem, cv2.TM_CCOEFF_NORMED)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	h, w = tem.shape
	if fake:
		cen = (max_loc[0] + fk[1]//2,max_loc[1] +fk[0]//2)
		return cen
	else:
		cen = (max_loc[0] + w//2,max_loc[1] +h//2)
		return cen
def ind_sc_chk(ref="discord",full_sc=True,size=(0,0,1,1),t = 0.6,r=False):
	fil = (f"ref/{ref}.png")
	if full_sc:
		ind = pyautogui.screenshot()
		ind = np.array(ind)
	else:
		ind = pyautogui.screenshot(region=size)
		ind = np.array(ind)
	tem = cv2.imread(fil,0)
	ind = cv2.cvtColor(ind,cv2.COLOR_RGB2BGR)
	tem = cv2.cvtColor(tem,cv2.COLOR_RGB2BGR)
	
	ind_g = cv2.cvtColor(ind,cv2.COLOR_BGR2GRAY)
	tem_g = cv2.cvtColor(tem,cv2.COLOR_BGR2GRAY)
	res = cv2.matchTemplate(ind_g,tem_g, cv2.TM_CCOEFF_NORMED)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	thershold = t
	if r:
		return max_val
	else:
		return max_val >= thershold
def ind_sc_cls(full_sc=True,size=(0,0,1,1)):
	processor = AutoImageProcessor.from_pretrained("google/vit-base-patch16-224")
	model = AutoModelForImageClassification.from_pretrained("google/vit-base-patch16-224")
	if full_sc:
		image = pyautogui.screenshot()
	else:
		image = pyautogui.screenshot(region=size)
	inputs = processor(images=image, return_tensors="pt", use_fast=True)
	with torch.no_grad():
		outputs = model(**inputs)
	logits = outputs.logits
	predicted_class_idx = logits.argmax(-1).item()
	return model.config.id2label[predicted_class_idx]
