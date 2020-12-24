import turtle
import random

wn = turtle.Screen()
wn.bgcolor('green')



turtle.register_shape('openedbox.gif')
turtle.register_shape('gift_box(not open)1.gif')
turtle.register_shape('diamond.gif')
turtle.register_shape('volcano.gif')


gifts = 'volcano.gif','diamond.gif'


gift_box = turtle.Turtle()
gift_box.shape('gift_box(not open)1.gif')


present_inside = turtle.Turtle()


def change_gift():
   present_inside.shape(random.choice(gifts))

def start():
   gift_box.shape('openedbox.gif')

turtle.listen()
turtle.onkeypress(change_gift,'c')
turtle.onkeypress(start,'s')

wn.mainloop()
