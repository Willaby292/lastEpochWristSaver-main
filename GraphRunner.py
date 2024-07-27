from Graph import *
import pyautogui
import random
import keyboard
from tkinter import *

screenWidth, screenHeight = pyautogui.size()

# def snapToClosestNode():

def create_random_poi(screenWidth=screenWidth, screenHeight=screenHeight, num_dicts=random.randint(15, 30)):
    POI = []
    for i in range(num_dicts):
        POI.append({
            'name': i,
            'x': random.randint(20, screenWidth-20),
            'y': random.randint(20, screenHeight-20)
        })
    return POI

# Example usage
random_poi = create_random_poi()

POIGraph = Graph(random_poi)


def moveMouse(direction, currNode, POIGraph):
    #save position
    #check current nodes neighbor in __ direction
    #move to new x,y
    nodeId = currNode.getNeighbors(direction)
    x = POIGraph[nodeId].getX()
    y = POIGraph[nodeId].getY()
    pyautogui.moveTo(x, y)

# def getCurrNode(POIGrapgh):
#     for i in POIGrapgh:
#         if

keyboard.add_hotkey('up', moveMouse, args=(Direction.UP, POIGraph))
keyboard.add_hotkey('down', moveMouse, args=(Direction.DOWN, POIGraph))
keyboard.add_hotkey('left', moveMouse, args=(Direction.LEFT, POIGraph))
keyboard.add_hotkey('right', moveMouse, args=(Direction.RIGHT, POIGraph))


################## app window
root = Tk()

geo = str(screenWidth)+'x'+str(screenHeight)
root.geometry(geo)

root.attributes('-fullscreen', True)
root.attributes('-alpha', 1) #opacity

w = Canvas(root, width=screenWidth, height=screenHeight)
w.pack()

def quit_win():
   root.destroy()
button=Button(root,text="Quit", font=('Times New Roman', 13, 'bold'), command=quit_win)
button.place(x=screenWidth/2,y=10)

for c in POIGraph.getGraph(): ##WHY WONT THIS ITERATE OVER OBJECTS WTF
    print(str(POIGraph.getGraph()[c].getX()) + " : "+ str(POIGraph.getGraph()[c].getY()))
    x = POIGraph.getGraph()[c].getX()
    y = POIGraph.getGraph()[c].getY()

    x_start = x
    inverse_x_start = x

    y_start = y
    inverse_y_start = y
    for dx in range(0, screenWidth - x, 10):
        dy = math.log10(dx + 1) * 100

        draw_line = w.create_line(x + dx, y + dy, x_start, y_start)
        draw_line = w.create_line(x + dx, y - dy, x_start, inverse_y_start)
        draw_line = w.create_line(x - dx, y + dy, inverse_x_start, y_start)
        draw_line = w.create_line(x - dx, y - dy, inverse_x_start, inverse_y_start)


        x_start = x + dx
        inverse_x_start = x - dx
        y_start = y + dy
        inverse_y_start = y - dy

    x_start = x
    inverse_x_start = x

    y_start = y
    inverse_y_start = y
    for dy in range(0, screenHeight - y, 10):
        dx = math.log10(dy + 1) * 100

        draw_line = w.create_line(x + dx, y + dy, x_start, y_start)
        draw_line = w.create_line(x - dx, y + dy, inverse_x_start, y_start)
        draw_line = w.create_line(x + dx, y - dy, x_start, inverse_y_start)
        draw_line = w.create_line(x - dx, y - dy, inverse_x_start, inverse_y_start)

        x_start = x + dx
        inverse_x_start = x - dx
        y_start = y + dy
        inverse_y_start = y - dy
    w.create_oval(x - 20, y - 20, x + 20, y + 20, fill='blue', activefill='red', width=3)
mainloop()

#git test

#when hovered calculate 'math.log10(abs(dx))' increaing slowly and drawing a line each time
