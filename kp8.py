import tkinter as tk
import colorsys


root = tk.Tk()
root.title("Раскраска графа. КП8. Горохов Михаил")

width = 1600
height = 900

nodeRadius = 30

font = "Notomono 18"
fontNode = "Notomono 16"

# функции обработчики и Background
nodesColors = []
nodesCoord = []
edges = []

def update():
    canvas.delete("all")
    for edge in edges:
        x0 = nodesCoord[edge[0]]
        y0 = nodesCoord[edge[1]]
        x1 = nodesCoord[edge[0]]
        y1 = nodesCoord[edge[1]]

        canvas.create_line(x0, y0, x1, y1, fill='white', width = 5)

    for i in range(len(nodesCoord)):
        node = nodesCoord[i]
        x = node[0]
        y = node[1]

        canvas.create_oval(x-nodeRadius , y-nodeRadius , x+nodeRadius , y+nodeRadius , fill=nodesColors[i], outline='grey', width=3)
        canvas.create_text(x, y, text=str(i), font = fontNode)
def addNode(event):
    x = int(entryAddNodeX.get())
    y = int(entryAddNodeY.get())

    nodesCoord.append([x,y])

    if(len(nodesColors) != 0 and nodesColors[0] != 'white'):
        nodesColors.clear()
        for i in range(len(nodesCoord)):
            nodesColors.append('white')
    else:
        nodesColors.append('white')
    update()

    print("Добавил узел по координате", x,y)
def editNode(event):
    i = int(entryEditNodeId.get())
    x = int(entryEditNodeX.get())
    y = int(entryEditNodeY.get())

    nodesCoord[i][0] = x
    nodesCoord[i][1] = y
    update()
    print("Изменил узел c ID", i,"по координате", x, y)
def removeNode(event):
    i = int(entryRemoveNodeId.get())
    nodesCoord.pop(i)
    nodesColors.pop(i)
    update()
    print("Удалил узел по ID", int(entryRemoveNodeId.get()))
def addEdge(event):
    fromNode = int(entryAddEdgeFrom.get())
    toNode = int(entryAddEdgeTo.get())

    if(len(nodesColors) != 0 and nodesColors[0] != 'white'):
        nodesColors.clear()
        for i in range(len(nodesCoord)):
            nodesColors.append('white')
    edges.append((fromNode, toNode))
    update()
    print("Добавил ребро между", fromNode, "и", toNode)
def removeEdge(event):
    fromNode = int(entryRemoveEdgeFrom.get())
    toNode = int(entryRemoveEdgeTo.get())

    try:
        edges.remove((fromNode, toNode))
    except Exception:
        pass
    try:
        edges.remove((toNode, fromNode))
    except Exception:
        pass
    update()
    print("Удалил ребро между", int(entryRemoveEdgeFrom.get()), "и", int(entryRemoveEdgeTo.get()))
def colorIt(event):
    colors = 1

    isFound = False
    countEdges = len(edges)
    nodesIdColors = []
    for i in range(len(nodesCoord)):
        nodesIdColors.append(0)
    if(countEdges == 0):
        isFound = True
    while(not isFound):
        add = 1
        for j in range(len(nodesCoord)):
            nodesIdColors[j] += add
            add = nodesIdColors[j]//colors
            nodesIdColors[j] = nodesIdColors[j]%colors

        if(add == 1):
            colors+=1
            colorStep = 360/colors
            continue

        isFound = True
        for edge in edges:
            if(nodesIdColors[edge[0]] == nodesIdColors[edge[1]]):
                isFound = False

    hueStep = 1/colors
    hue = 0
    saturation = 1
    value = 1
    print(nodesColors)
    print(len(nodesColors))
    colorRGB = [0,0,0]
    for i in range(len(nodesColors)):
        nodeIdColor = nodesIdColors[i]
        red = 0
        green = 0
        blue = 0
        hue = hueStep*nodeIdColor

        colorNorRGB = colorsys.hsv_to_rgb(hue,saturation,value)
        print(colorNorRGB)
        colorStr = ''
        for j in range(3):
            colorRGB[j] = int(255*colorNorRGB[j]+0.4)
        print(colorRGB)
        print(hex(colorRGB[0]*256*256+colorRGB[1]*256+colorRGB[2]))
        print(hex(colorRGB[0]*256*256+colorRGB[1]*256+colorRGB[2])[2:])
        colorStr += hex(colorRGB[0]*256*256+colorRGB[1]*256+colorRGB[2])[2:]
        while(len(colorStr) < 6):
            colorStr = '0' + colorStr
        colorStr = '#' + colorStr
        print(colorStr)
        print(i)
        nodesColors[i] = colorStr
    print(nodesColors)
    update()
    print("Закрасил!")
def vanish(event):
    nodesCoord.clear()
    edges.clear()
    update()
    print("Очистил!")

# закончил функции обраотчики

# Верстаю макет
frameControlPanel = tk.Frame(root, width=width//4, height=height)
canvas = tk.Canvas(root, width=3*width//4, height=height, bg='black')

frameControlPanel.grid(row=1, column=1)
canvas.grid(row=1, column=2)

frameAddNode = tk.Frame(frameControlPanel, width=width//4, height=height//6)
frameEditNode = tk.Frame(frameControlPanel, width=width//4, height=height//6)
frameRemoveNode = tk.Frame(frameControlPanel, width=width//4, height=height//6)
frameAddEdge = tk.Frame(frameControlPanel, width=width//4, height=height//6)
frameRemoveEdge = tk.Frame(frameControlPanel, width=width//4, height=height//6)
frameAction = tk.Frame(frameControlPanel, width=width//4, height=height//6)

frameAddNode.grid(row=1, column=1)
frameEditNode.grid(row=2, column=1)
frameRemoveNode.grid(row=3, column=1)
frameAddEdge.grid(row=4, column=1)
frameRemoveEdge.grid(row=5, column=1)
frameAction.grid(row=6, column=1)

buttonAddNode = tk.Button(frameAddNode, text="Добавить узел",  font=font)
buttonEditNode = tk.Button(frameEditNode, text="Изменить узел", font=font)
buttonRemoveNode = tk.Button(frameRemoveNode, text="Удалить узел", font=font)
buttonAddEdge = tk.Button(frameAddEdge, text="Добавить ребро", font=font)
buttonRemoveEdge = tk.Button(frameRemoveEdge, text="Удалить ребро", font=font)
buttonColorIt = tk.Button(frameAction, text="Закрасить", font=font)
buttonVanish = tk.Button(frameAction, text="Очистить поле", font=font)

labelAddNodeX = tk.Label(frameAddNode, text="X: ",font=font)
labelAddNodeY = tk.Label(frameAddNode, text="Y: ", font=font)
labelEditNodeId = tk.Label(frameEditNode, text="ID: ", font=font)
labelEditNodeX = tk.Label(frameEditNode, text="X: ", font=font)
labelEditNodeY = tk.Label(frameEditNode, text="Y: ", font=font)
labelRemoveNodeId = tk.Label(frameRemoveNode, text="ID: ", font=font)
labelAddEdgeFrom = tk.Label(frameAddEdge, text="From: ", font=font)
labelAddEdgeTo = tk.Label(frameAddEdge, text="To: ", font=font)
labelRemoveEdgeFrom = tk.Label(frameRemoveEdge, text="From: ", font=font)
labelRemoveEdgeTo = tk.Label(frameRemoveEdge, text="To: ", font=font)

entryAddNodeX = tk.Entry(frameAddNode, font=font)
entryAddNodeY = tk.Entry(frameAddNode, font=font)
entryEditNodeId = tk.Entry(frameEditNode, font=font)
entryEditNodeX = tk.Entry(frameEditNode, font=font)
entryEditNodeY = tk.Entry(frameEditNode, font=font)
entryRemoveNodeId = tk.Entry(frameRemoveNode, font=font)
entryAddEdgeFrom = tk.Entry(frameAddEdge, font=font)
entryAddEdgeTo = tk.Entry(frameAddEdge, font=font)
entryRemoveEdgeFrom = tk.Entry(frameRemoveEdge, font=font)
entryRemoveEdgeTo = tk.Entry(frameRemoveEdge, font=font)

buttonAddNode.grid(row=1, column=1, columnspan=2)
buttonEditNode.grid(row=1, column=1, columnspan=2)
buttonRemoveNode.grid(row=1, column=1, columnspan=2)
buttonAddEdge.grid(row=1, column=1, columnspan=2)
buttonRemoveEdge.grid(row=1, column=1, columnspan=2)
buttonColorIt.grid(row=1, column=1)
buttonVanish.grid(row=1, column=2)

labelAddNodeX.grid(row=2, column=1)
labelAddNodeY.grid(row=3, column=1)
labelEditNodeId.grid(row=2, column=1)
labelEditNodeX.grid(row=3, column=1)
labelEditNodeY.grid(row=4, column=1)
labelRemoveNodeId.grid(row=2, column=1)
labelAddEdgeFrom.grid(row=2, column=1)
labelAddEdgeTo.grid(row=3, column=1)
labelRemoveEdgeFrom.grid(row=2, column=1)
labelRemoveEdgeTo.grid(row=3, column=1)

entryAddNodeX.grid(row=2, column=2)
entryAddNodeY.grid(row=3, column=2)
entryEditNodeId.grid(row=2, column=2)
entryEditNodeX.grid(row=3, column=2)
entryEditNodeY.grid(row=4, column=2)
entryRemoveNodeId.grid(row=2, column=2)
entryAddEdgeFrom.grid(row=2, column=2)
entryAddEdgeTo.grid(row=3, column=2)
entryRemoveEdgeFrom.grid(row=2, column=2)
entryRemoveEdgeTo.grid(row=3, column=2)

# Закончил верстать макет

buttonAddNode.bind("<Button-1>", addNode)
buttonEditNode.bind("<Button-1>", editNode)
buttonRemoveNode.bind("<Button-1>", removeNode)
buttonAddEdge.bind("<Button-1>", addEdge)
buttonRemoveEdge.bind("<Button-1>", removeEdge)
buttonColorIt.bind("<Button-1>", colorIt)
buttonVanish.bind("<Button-1>", vanish)

root.mainloop()