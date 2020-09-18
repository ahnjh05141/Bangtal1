from bangtal import *

#====== <<Scenes>>
scene1 = Scene('Room1 - North','images/bg1.png')
scene2 = Scene('Room1 - East','images/bg1.png')
scene3 = Scene('Room1 - South','images/bg1.png')
scene4 = Scene('Room1 - West','images/bg1.png')
scene_Safe = Scene('Safe','images/safe_Open.png')

#====== <<Arrows>>
arrL1 = Object('images/arrow_left.png')
arrL1.locate(scene1, 0+60-32, 120-32)
arrL1.show()
arrL2 = Object('images/arrow_left.png')
arrL2.locate(scene2, 0+60-32, 120-32)
arrL2.show()
arrL3 = Object('images/arrow_left.png')
arrL3.locate(scene3, 0+60-32, 120-32)
arrL3.show()
arrL4 = Object('images/arrow_left.png')
arrL4.locate(scene4, 0+60-32, 120-32)
arrL4.show()

arrR1 = Object('images/arrow_Right.png')
arrR1.locate(scene1, 1280-60-32, 120-32)
arrR1.show()
arrR2 = Object('images/arrow_Right.png')
arrR2.locate(scene2, 1280-60-32, 120-32)
arrR2.show()
arrR3 = Object('images/arrow_Right.png')
arrR3.locate(scene3, 1280-60-32, 120-32)
arrR3.show()
arrR4 = Object('images/arrow_Right.png')
arrR4.locate(scene4, 1280-60-32, 120-32)
arrR4.show()

arrD = Object('images/arrow_Down.png')
arrD.locate(scene_Safe, 600, 100)
arrD.show()

sceneNum=1
def arrL(x,y,action):
    global sceneNum
    if sceneNum==1:
        sceneNum=4
        scene4.enter()
    elif sceneNum==2:
        sceneNum=1
        scene1.enter()
    elif sceneNum==3:
        sceneNum=2
        scene2.enter()
    elif sceneNum==4:
        sceneNum=3
        scene3.enter()
def arrR(x,y,action):
    global sceneNum
    if sceneNum==1:
        sceneNum=2
        scene2.enter()
    elif sceneNum==2:
        sceneNum=3
        scene3.enter()
    elif sceneNum==3:
        sceneNum=4
        scene4.enter()
    elif sceneNum==4:
        sceneNum=1
        scene1.enter()
def arrD(x,y,action):
    scene1.enter()

arrL1.onMouseAction = arrL
arrL2.onMouseAction = arrL
arrL3.onMouseAction = arrL
arrL4.onMouseAction = arrL
arrR1.onMouseAction = arrR
arrR2.onMouseAction = arrR
arrR3.onMouseAction = arrR
arrR4.onMouseAction = arrR
arrD.onMouseAction = arrD

#====== <<Objects>>
desk = Object('images/desk.png')
desk.locate(scene4, 600, 110)
desk.show()

bed = Object('images/bed.png')
bed.locate(scene2, 300, 10)
bed.setScale(1.1)
bed.show()

def bed_Click(x,y,action):
    bed.setImage('images/bed2.png')
    battery.show()
bed.onMouseAction = bed_Click

remote = Object('images/remote.png')
remote.locate(scene4, 800, 270)
remote.show()

def remote_Click(x,y,action):
    remote.pick()
remote.onMouseAction = remote_Click

battery = Object('images/battery.png')
battery.locate(scene2, 440, 160)
battery.setScale(0.6)
battery.hide()

def battery_Click(x,y,action):
    battery.pick()
battery.onMouseAction = battery_Click

remote2 = Object('images/remote2.png')
remote2.defineCombination(remote, battery)

tv = Object('images/tv.png')
tv.locate(scene1, 400, 200)
tv.setScale(2)
tv.show()

def tv_Click(x,y,action):
    if remote2.inHand():
        tv.setImage('images/tv2.png')
tv.onMouseAction = tv_Click

safe = Object('images/safe.png')
safe.locate(scene4, 200, 120)
safe.show()

safe_Locked = True
def safe_Click(x,y,action):
    global safe_Locked
    if safe_Locked:
        showKeypad('8542',safe)
safe.onMouseAction = safe_Click

def safe_Keypad():
    showMessage('철컥!.. 금고가 열렸다...')
    safe.setImage('images/safe_Open.png')
    driver.show()
safe.onKeypad = safe_Keypad

driver = Object('images/driver.png')
driver.locate(scene4, 220, 100)
driver.setScale(1.4)

def driver_Click(x,y,action):
    driver.pick()
driver.onMouseAction = driver_Click

plate = Object('images/plate.png')
plate.locate(scene2, 900, 500)
plate.show()

def plate_Click(x,y,action):
    if driver.inHand():
        plate.hide()
        key.show()
    else:
        showMessage('열리지 않는다...')
plate.onMouseAction = plate_Click

key = Object('images/key.png')
key.locate(scene2, 960, 560)
key.setScale(1.4)

def key_Click(x,y,action):
    key.pick()
key.onMouseAction = key_Click

doorExit = Object('images/doorExit.png')
doorExit.locate(scene3,300,200-45)
doorExit.setScale(1.5)
doorExit.show()
doorExit_Locked = True
doorExit_Closed = True

def door_Click(x,y,action):
    global doorExit_Locked
    global doorExit_Closed
    if doorExit_Locked and key.inHand():
        showMessage('철컥!.. 문이 열렸다...')
        doorExit_Locked = False
    elif doorExit_Locked:
        showMessage('잠겨있다...')
    elif doorExit_Closed:
        doorExit.setImage('images/doorExit_Open.png')
        doorExit_Closed = False
    else:
        endGame()
doorExit.onMouseAction = door_Click

#====== <<IN GAME CODE>>
startGame(scene1)