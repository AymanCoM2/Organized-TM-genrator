import pyautogui
import time
import pyperclip

screenWidth, screenHeight = pyautogui.size()
# print(screenWidth, screenHeight)
currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX, currentMouseY)


def hideEveryThing():
    # This Funtion Closes / Minimize All Screens To see the Desktop
    pyautogui.moveTo(1363, 742)
    pyautogui.click()


def openBrowser():
    # This Function Opens The Browser On the Desktop
    # It requires the Icon Of Browser To Be On Top Right Corner On the Screen
    # and If the Browser Screen is Minimized It will Maximize it
    pyautogui.moveTo(1319, 29)
    pyautogui.doubleClick()
    time.sleep(2)
    pyautogui.hotkey("win", "up")  # Maximize PAGE


def openWhatasppLinkAndSendMSG(phoneNumber='01126517150'):

    # This Function Opens Whataspp Web To send a Message For a Person
    # It Requires Being Logged in To Whataspp Web && The "RECEIVER NUMBER"
    # instead Of Being Hard-Coded in the Link
    # The Function Will Create / Open Conversation with this Phone Number and Write "File" Word
    time.sleep(4)
    intndedLink = "https://api.whatsapp.com/send/?phone=%2B201126517150&text=File&type=phone_number&app_absent=1"
    pyperclip.copy(intndedLink)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(4)
    # pyautogui.press('enter')


def handleUPload():
    pyautogui.moveTo(508, 702)
    time.sleep(4)
    pyautogui.click()
    time.sleep(6)
    pyautogui.moveTo(508, 565)
    time.sleep(6)
    pyautogui.moveTo(506, 565)
    time.sleep(6)
    pyautogui.doubleClick(button='left')
    fileName = "result_with_page_numbers.pdf"
    pyperclip.copy(fileName)
    pyautogui.moveTo(376, 418)
    pyautogui.doubleClick()
    time.sleep(2)
    pyautogui.hotkey("win", "v")
    pyautogui.press('enter')
    pyperclip.paste()
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')  # ! THIS IS THE SENDING ENTER !!!!
    # Then Close it  & Close the Browser
    time.sleep(10)
    pyautogui.hotkey("alt", "f4")  # CLOSING WHATASPP desktop
    time.sleep(2)
    pyautogui.hotkey("alt", "f4")  # CLOSING WHATASPP web


# hideEveryThing()  # ! OK
# openBrowser()  # ! OK
# openWhatasppLinkAndSendMSG()  # ! OK
# handleUPload()
