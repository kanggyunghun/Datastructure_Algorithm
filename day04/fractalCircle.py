# from tkinter import *
#
# window = Tk()
# canvas = Canvas(window, height=1000, width=1000, bg='white')
# canvas.pack()
#
# cx=1000//2
# cy=1000//2
# r = 400
# print(cx,cy,r)
# canvas.create_oval(cx-r, cy-r, cx+r, cy+r, width=2, outline="red")
#
# window.mainloop()

from tkinter import *

## 함수 선언 부분 ##
def drawCircle(x, y, r) :
    global count
    count += 1
    canvas.create_oval(x-r, y-r, x+r, y+r)
    canvas.create_text(x, y-r, text=str(count), font=('', 30))
    if r >= radius/2 :
        drawCircle(x-r//2, y, r//2)
        drawCircle(x+r//2, y, r//2)

## 전역 변수 선언 부분 ##
count = 0
wSize = 1000
radius = 400

## 메인 코드 부분 ##
window = Tk()
canvas = Canvas(window, height=wSize, width=wSize, bg='white')

drawCircle(wSize//2, wSize//2, radius)

canvas.pack()
window.mainloop()