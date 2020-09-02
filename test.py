# coding: utf-8
from tkinter import *
import random
import threading
import time
import sys
import math

WIDTH = 600  #cm
HEIGHT = 600
SIGMA = 10
BUZZ = 2
RADIUS = 5
LAMBDA = 10
FILL = ['red','orange','yellow','green','cyan',
      'blue','purple','pink','magenta','brown']
stop = 0

np = 16
cut=5

x=[None for i in range(1,20)]
y=[None for i in range(1,20)]

for i in range(0,cut-1):
    for j in range(0,cut-1):
        x[i*(cut-1)+j]=WIDTH/cut*(j+1)
        y[i*(cut-1)+j]=WIDTH/cut*(i+1)

nodes=[ None for i in range(1,np)]

safedis=35

isFirst=False

def particle(canvas,color,x,y):
  r = RADIUS
#   x = random.randint(80,320)
#   y = random.randint(80,220)
  p = canvas.create_oval(x-r, y-r, x+r, y+r, fill=color)
  return p
def process(canvas,p):
    vx = random.randint(0,40)-20
    vy = random.randint(0,40)-20
    dt = random.randint(1,2)
    while not stop:
        if(isSafe(canvas,p)==False):
            # if(random.randint(0,1)==0):TR
            if(1):
                # vx=0-vx
                # vy=0-vy
                vx,vy=vy,vx
                vy=0-vy
                #print("peng")
            else:
                vx=0-vx
                vy=0-vy
        elif(random.randint(1,10)<3):
            vx = random.randint(0,40)-20
            vy = random.randint(0,40)-20
            print("safe")
        else:
            print("safe")
        #dt = random.randint(1,2)
        dt=1
        try:
            canvas.move(p, vx*dt, vy*dt)
        except TclError:
            print(TclError)
            break
        time.sleep(dt)

def caldis(canvas,p1,p2):
    pos1=canvas.coords(p1)
    pos2=canvas.coords(p2)
    return math.sqrt(math.pow(pos1[0]-pos2[0],2)+math.pow(pos1[1]-pos2[1],2))

def isSafe(canvas,p):
    pos1=canvas.coords(p)
    if(math.sqrt(math.pow(pos1[0]-WIDTH/2,2)+math.pow(pos1[1]-HEIGHT/2,2))>WIDTH/2-safedis):
        print("peng wall")
        return False
    for item in nodes:
        if(item==p):
            continue
        if(caldis(canvas,p,item)<safedis):
            print("peng uav")
            return False
    return True
def main(nodes):
  global stop
  root = Tk()
  canvas = Canvas(root, width=WIDTH, height=HEIGHT)
  canvas.pack(fill='both', expand=1)
  np = 16
  for i in range(0,np-1):
    nodes[i]=particle(canvas,FILL[i%9],x[i],y[i])

  if sys.argv[1:]:
    np = int(sys.argv[1])
  for j in range(0,np-1):
    t = threading.Thread(target=process, args=(canvas,nodes[j],))
    #print("tes")
    t.start()
  try:
    root.mainloop()
  finally:
    stop = 1
if __name__ == '__main__':
    main(nodes)