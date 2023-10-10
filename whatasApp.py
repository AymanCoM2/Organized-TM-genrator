import pyautogui
import time
import pyperclip

screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)


def hideEveryThing():
    pyautogui.moveTo(1363, 742)
    pyautogui.click()


def openBrowser():
    pyautogui.moveTo(1319, 29)
    pyautogui.doubleClick()
    time.sleep(2)
    pyautogui.hotkey("win", "up")  # Maximize PAGE
# phoneNumber, fileName


def openWhatasppLinkAndSendMSG():
    time.sleep(2)
    intndedLink = "https://api.whatsapp.com/send/?phone=%2B14155238886&text=File&type=phone_number&app_absent=1"
    pyperclip.copy(intndedLink)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')


def handleUPload():
    pyautogui.moveTo(508, 702)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(508, 565)
    time.sleep(2)
    pyautogui.moveTo(506, 565)
    time.sleep(6)
    pyautogui.doubleClick(button='left')
    fileName = "DDL - DATA.xlsx"
    pyperclip.copy(fileName)
    pyautogui.moveTo(376, 418)
    pyautogui.doubleClick()
    time.sleep(2)
    pyautogui.hotkey("win", "v")
    pyautogui.press('enter')
    # pyperclip.paste()
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')



