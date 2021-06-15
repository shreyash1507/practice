from itertools import cycle
from random import randrange
from tkinter import Tk,Canvas, messagebox,font

canvas_width=800
canvas_height=400

w=Tk()

####Background####
back=Canvas(w,width=canvas_width,height=canvas_height,background='deep sky blue')
back.create_rectangle(-5,canvas_height-100,canvas_width+5,canvas_height+5,fill='sea green',width=0)
back.create_oval(-80,-80,120,120,fill='orange',width=0)
back.pack()

###EGG####
color_cycle=cycle(['light blue','light pink','light yellow','purple','red','blue','green','black'])
egg_width=45
egg_height=55
eggscore=10
egg_speed=500
egg_interval=4000
difficulty_factor=0.95

###CATCHER##
catcher_color='blue'
catcher_width=100
catcher_height=100

catcher_start_x=canvas_width/2-catcher_width/2
catcher_start_y=canvas_height-catcher_height-20
catcher_end_x=catcher_start_x+catcher_width
catcher_end_y=catcher_start_y+catcher_height
catcher=back.create_arc(catcher_start_x,catcher_start_y,catcher_end_x,catcher_end_y,start=200,extent=140,style='arc',outline=catcher_color,width=3)

#####SCORE#########
score=0 
score_text=back.create_text(10,25,anchor='nw',font=('Helvatica',15,'bold'),fill='dark blue',text='Score : '+str(score))

##########Lives######
live_remain=3
lives_text=back.create_text(canvas_width-10,25,anchor='ne',font=('Helvatica',15,'bold'),fill='dark blue',text='Lives : '+str(live_remain))

eggs=[]
def create_eggs():
    x=randrange(10,740)
    y=20
    new_egg=back.create_oval(x,y,x+egg_width,y+egg_height,fill=next(color_cycle),width=0)
    eggs.append(new_egg)
    w.after(egg_interval,create_eggs)
def move_eggs():
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2)=back.coords(egg)
        back.move(egg,0,10)
        if egg_y2>canvas_height:
            egg_drop(egg)
    w.after(egg_speed,move_eggs)

def egg_drop(egg):
    eggs.remove(egg)
    back.delete(egg)
    lose_life()
    if live_remain==0:
        messagebox.showinfo('Game Over', 'Final Score :' +str(score))
        
def lose_life():
    global live_remain
    live_remain-=1
    back.itemconfigure(lives_text ,text='Lives : '+str(live_remain))

def catch_check():
    (catcher_x,xatxher_y,catcher_x2,catcher_y2)=back.coords(catcher)
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2)=back.coords(egg)
        if catcher_x<egg_x and egg_x2<catcher_x2 and catcher_y2-egg_y2<40:
            eggs.remove(egg)
            back.delete(egg)
            increase_score(eggscore)
    w.after(100,catch_check)
def increase_score(points):
    global score,egg_speed,egg_interval
    score+=points
    egg_speed=int(egg_speed*difficulty_factor)
    egg_interval=int(egg_interval*difficulty_factor)
    back.itemconfigure(score_text,text='Score : '+str(score))

def move_left(event):
    (x1,y1,x2,y2)=back.coords(catcher)
    if x1>0:
        back.move(catcher,-20,0)
def move_right(event):
    (x1,y1,x2,y2)=back.coords(catcher)
    if x2<canvas_width:
        back.move(catcher,20,0)

back.bind('<Left>',move_left)
back.bind('<Right>',move_right)
back.focus_set()
w.after(1000,create_eggs)
w.after(1000,move_eggs)
w.after(1000,catch_check)

w.mainloop()