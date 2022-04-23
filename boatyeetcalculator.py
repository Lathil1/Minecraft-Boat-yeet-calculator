import time
import pyperclip
import keyboard

print('Waiting for boat position...', end="\r")

def yeet(cx, cz):
    disx = abs(cx[1]-cx[0])
    disz = abs(cz[1]-cz[0])
    disx *= 1.666666
    disz *= 1.666666
    if cx[1] > 0 and cx[0] < 0:
        posx = cx[0]+(disx)
    elif  cx[1] < 0 and cx[0] > 0:
        posx = cx[0]-(disx)
    elif cx[1]<0 and cx[0]<0 and abs(cx[1])>abs(cx[0]):
        posx = cx[0]-(disx)
    elif cx[1]<0 and cx[0]<0 and abs(cx[1])<abs(cx[0]):
        posx = cx[0]+(disx)
    elif abs(cx[1])>abs(cx[0]):
        posx = cx[0]+(disx)
    elif abs(cx[1])<abs(cx[0]):
        posx = cx[0]-disx
    else:
        posx = (cx[0])
    if cz[1] > 0 and cz[0] < 0:
        posz = cz[0]+(disz)
    elif cz[1] < 0 and cz[0] > 0:
        posz = cz[0]-(disz)
    elif cz[1]<0 and cz[0]<0 and abs(cz[1])>abs(cz[0]):
        posz = cz[0]-(disz)
    elif cz[1]<0 and cz[0]<0 and abs(cz[1])<abs(cz[0]):
        posz = cz[0]+(disz)
    elif abs(cz[1])>abs(cz[0]):
        posz = cz[0]+(disz)
    elif abs(cz[1])<abs(cz[0]):
        posz = cz[0]-disz
    else:
        posz = (cz[0])

    return int(posx), int(posz)

coordinates_x = []
coordinates_z = []
string = "pull at "

recent_value = ""
while True:
    def copy():
        time.sleep(0.1)
        location = (pyperclip.paste())
        coords = (location.split(' '))
        coordinates_x.append(float(coords[6]))
        coordinates_z.append(float(coords[8]))
        print('current positon: ' + coords[6], coords[8])
        if  len(coordinates_x) == 1:
            print('Waiting for land position...', end="\r")
        if  len(coordinates_x) == 2:
            result = yeet(coordinates_x, coordinates_z)
            print(string + str(result))
            coordinates_z.clear()
            coordinates_x.clear()
            print('Waiting for boat position...', end="\r")


    keyboard.add_hotkey('f3+c', copy)
    keyboard.wait()