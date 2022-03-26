import pyautogui as pg

pg.FAILSAFE = True


def img_is_in(img):
    try:
        pg.locateAllOnScreen(img, confidence=0.9)
        return True
    except Exception as e:
        return False


def last_page():
    try:
        x, y = pg.locateOnScreen('end.PNG',  confidence=0.9)
        pg.moveTo(x-4, y, duration=0.5)
        pg.click()
        return False
    except Exception as e:
        return True


while last_page():
    # if img_is_in('next_page.PNG')==True:
    #     x, y = pg.locateCenterOnScreen('next_page.PNG')
    #     pg.moveTo(x-4, y, duration=0.5)
    #     pg.click()
    # else:
    try:
        for pos in pg.locateAllOnScreen('check.PNG', confidence=0.95):
            pg.moveTo(pos[0]+20, pos[1]+15, duration=0.5)
            pg.click()
        pg.scroll(-300)
    except Exception as e:
        print(e)
        pg.scroll(-300)
    for pos in pg.locateAllOnScreen('next_page.PNG', confidence=0.9):
        pg.moveTo(pos[0]+2, pos[1]+1, duration=0.5)
        pg.click()
