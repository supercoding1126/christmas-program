import turtle

wn = turtle.Screen()
wn.bgcolor('green')

turtle.register_shape('openedbox.gif')
turtle.register_shape('gift_box(not open)1.gif')

gift_box = turtle.Turtle()
gift_box.shape('gift_box(not open)1.gif')


present_inside = turtle.Turtle()






wn.mainloop()