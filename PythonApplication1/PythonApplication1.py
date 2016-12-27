from tkinter import *
import time
import random

def mouseClick(event):
    x = event.x
    y = event.y
    randomDirection()
    main()

def main():
    mainloop = True
    while mainloop: 
        moveBall(ballDirection[0], ballDirection[1])
        if checkCollision() == True:
            mainloop = False

def moveBall(movex, movey):
    canvas.move(ball, movex, movey)
    time.sleep(0.01)
    tk.update()

def randomDirection():
    randomCoor = [-3, -2, -1, 1, 2, 3]
    ballDirection[0] = randomCoor[random.randint(1, 4)]
    ballDirection[1] = randomCoor[random.randint(0, 5)]
        
def checkCollision():  
    ballPosition = canvas.coords(ball)
    if ballPosition[0] <= 0 or ballPosition[2] >= canvasWidth+2:     # links rechts
       # return True
        ballDirection[0] *= -1 
        print(ballPosition)
    if ballPosition[1] <= 0 or ballPosition[3] >= canvasHeight+2:    # boven onder
        ballDirection[1] *= -1
        print(ballPosition)

def init():
    ball = canvas.create_oval(ballCoor[0]-ballRadius, ballCoor[1]-ballRadius, ballCoor[0]+ballRadius, ballCoor[1]+ballRadius, fill="Orange Red")

canvasWidth = 800
canvasHeight = 600
ballRadius = 15
ballCoor = [canvasWidth/2, canvasHeight/2]
ballDirection = [-2, 1]

playerHeight = 100
playerWidth = 5
playerDistance = 50


tk = Tk()
canvas = Canvas(tk, width=canvasWidth, height=canvasHeight, bg="black")
canvas.bind("<Button-1>", mouseClick)
canvas.pack()

middleLine = canvas.create_line(canvasWidth/2, 0, canvasWidth/2, canvasHeight, fill="white", dash=(250, 5))
ball = canvas.create_oval(ballCoor[0]-ballRadius, ballCoor[1]-ballRadius, ballCoor[0]+ballRadius, ballCoor[1]+ballRadius, fill="Orange Red")

playerOne = canvas.create_line(playerDistance, (canvasHeight/2)-(playerHeight/2), playerDistance, (canvasHeight/2)+(playerHeight/2), fill="white", width=playerWidth)
playerOne = canvas.create_line(canvasWidth-playerDistance, (canvasHeight/2)-(playerHeight/2), canvasWidth-playerDistance, (canvasHeight/2)+(playerHeight/2), fill="white", width=playerWidth)

tk.mainloop()
