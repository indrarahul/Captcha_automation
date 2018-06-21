from PIL import Image
import os
import cv2
import pytesseract
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
import re
import os

chromeOptions = Options()
prefs = {"plugins.plugins_disabled" : ["Chrome PDF Viewer"]}
chromeOptions.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(chrome_options=chromeOptions)
browser.maximize_window()

for i in range(1,10):
	browser.get('http://ceo.karnataka.gov.in/RollSearch/CodeCaputer1.aspx?field1=.%2fEnglish%2fAC150%2fAC150000{}.pdf'.format(i))
	sleep(2)
	p = pyautogui.screenshot(region=(616,489,119,34))
	p.save("Captcha.png")

	image = cv2.imread("Captcha.png")
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	#gray= cv2.threshold(gray,0,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename,gray)
	text = pytesseract.image_to_string(Image.open(filename))
	os.remove(filename)

	browser.find_element_by_id('ContentPlaceHolder1_txtcaptcha').send_keys(text)
	browser.find_element_by_id('ContentPlaceHolder1_b1').click()
	sleep(2)
	pyautogui.rightClick(x=598, y=497)
	pyautogui.press('down')
	pyautogui.press('enter')
	pyautogui.click(x=1079,y=717)
	pyautogui.press('enter')