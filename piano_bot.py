import mss
import pyautogui, time
from selenium import webdriver


user = input('Write your user name:\n')

driver = webdriver.Chrome(executable_path='C:\\Users\\{}\\Downloads\\chromedriver_win32\\chromedriver.exe'.format(user))
driver.get("https://www.yad.com/Magic-Tiles-3-Online")
driver.maximize_window()

amount = 1
first_20 = True

y = 610
x = 770
width = 1
height = 1

mouse_cors = [(i, y) for i in range(x, 1146, 125)]

monitors = [{"top": y, "left": x, "width": width, "height": height},
            {"top": y, "left": x + 125, "width": width, "height": height},
            {"top": y, "left": x + 250, "width": width, "height": height},
            {"top": y, "left": x + 375, "width": width, "height": height}]

limits = (range(150, 220), range(140, 200), range(190, 260))
interval = 0.1

def inLimits(*rgb):
    for i in range(3):
        if rgb[i] not in limits[i]:
            return False 
    return True

def screenShot():
    with mss.mss() as sct:
        imgs = [sct.grab(i) for i in monitors]
        pixelss = [list(zip(img.raw[2::4], img.raw[1::4], img.raw[0::4])) for img in imgs]
        
    return pixelss


pyautogui.alert('Skip ad, maximize piano screen and click <OK> if you ready')

while True:
    index = 1
    
    if amount % 20 == 0:
        if first_20:
            interval = interval*2/10
            first_20 = False
        else:
            interval = interval**2/10

    pixelss = screenShot()

    for pixels in pixelss:
        for pixsel in pixels:
            if not inLimits(*pixsel):
                pyautogui.click(*mouse_cors[index-1], _pause = False)
                amount += 1
                continue
        index += 1
            
    
    time.sleep(interval)
    