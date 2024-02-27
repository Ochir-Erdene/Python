from turtle import* 
speed (13)
width(1)
penup()
goto (-240, -80)
pendown()
for i in range (2): 
    fd (300)
    lt (90) 
    fd (20)
    lt (90)
lt(90)
fd(20)
rt(90)
fd(20)

circle(20,-150)
lt(150)
fd(260)
circle(20, 150)
lt(30)
fd(260)
rt(180)
circle(20,-150)
rt(-150)
fd(260)

rt(180)
circle(20,-150)
lt(150)
fd(260)
circle(20, 150)
lt(30)
fd(260)
rt(180)
circle(20,-150)
rt(-150)
fd(170)

# haalga
color('#000','#fff')
begin_fill()
for i in range (3):
    rt(90)
    fd(80)
end_fill()
penup()
goto(-60, -30)
pendown()
circle(5)
penup()

# deever
rt(180)
fd(82)
lt(90)
fd(35)
lt(90)
pendown()
shape("circle")
shapesize(13.5, 7, 2)














done()