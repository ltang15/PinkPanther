

import turtle
 

pen = turtle.Turtle()
 

def circ(col, rad):
 
    # Set the fill
    pen.fillcolor(col)
 
    # Start filling the color
    pen.begin_fill()
 
    # Draw a circle
    pen.circle(rad)
 
    # Ending the filling of the color
    pen.end_fill()
 
   



# set pen size
pen.pensize(2)

##### Draw ears #####

## Outer ears
# Right
pen.up()
pen.setpos(-70, 90)
pen.down()
circ('HotPink', 25)
 
# Left
pen.up()
pen.setpos(70, 90)
pen.down()
circ('HotPink', 25)

## Inner ears

# Right
pen.up()
pen.setpos(-65, 90)
pen.down()
circ('pink', 15)
 
# Left
pen.up()
pen.setpos(65, 90)
pen.down()
circ('pink', 15)
 


##### Draw chin #####

pen.up()
pen.setpos(-28, -50)
pen.seth(0)
pen.down()
pen.fillcolor("pink")
pen.begin_fill()

pen.right(90)
pen.circle(30, 180)
pen.end_fill()

##### Draw face #####
pen.up()
pen.setpos(65, 100)
pen.seth(0)
pen.down()

pen.fillcolor('HotPink')
  
# Start filling the color
pen.begin_fill()

pen.left(180)
pen.forward(130)

#left side

#big curve
for i in range(18):
  
        # Defining step by step curve motion
        pen.left(10)
        pen.forward(10)

pen.left(280)
pen.forward(20)

#small curve
for i in range(6):
  
        # Defining step by step curve motion
        pen.left(15)
        pen.forward(10)


pen.up()
pen.setpos(65, 100)
pen.seth(0)
pen.down()


# right side

#big curve
for i in range(18):
  
        # Defining step by step curve motion
        pen.right(10)
        pen.forward(10)

pen.right(280)
pen.forward(20)

#small curve
for i in range(6):
  
        # Defining step by step curve motion
        pen.right(15)
        pen.forward(10)

pen.seth(0)
pen.left(180)
pen.forward(6.94)

pen.end_fill()


# Draw yellow eyes

# right
pen.fillcolor("LemonChiffon")
pen.begin_fill()

pen.up()
pen.setpos(40,80)
pen.seth(90)
pen.down()
a = 2.0

for i in range(120):
   if 0 <= i < 30 or 60 <= i < 90:
       
       a -= 0.05
       pen.lt(3)
       pen.fd(a)
   else:
       a += 0.05
       pen.lt(3)
       pen.fd(a)

pen.end_fill()

# left

pen.fillcolor("LemonChiffon")
pen.begin_fill()

pen.up()
pen.setpos(-4,80)
pen.seth(90)
pen.down()
a = 2.0

for i in range(120):
   if 0 <= i < 30 or 60 <= i < 90:
       
       a -= 0.05
       pen.lt(3)
       pen.fd(a)
   else:
       a += 0.05
       pen.lt(3)
       pen.fd(a)

pen.end_fill()


  
 
##### Draw eye balls (black) #####
 
# right
pen.up()
pen.setpos(-17, 70)
pen.down()
circ('black', 10)
 
# left
pen.up()
pen.setpos(30, 70)
pen.down()
circ('black', 10)
 
##### Draw eyes (white dots) #####
 
# right
pen.up()
pen.setpos(-22, 68)
pen.down()
circ('white', 4)
 
# left
pen.up()
pen.setpos(20, 68)
pen.down()
circ('white', 4)
 

##### Draw nose #####
pen.up()
pen.setpos(0, -20)
pen.seth(0)
pen.down()
circ('IndianRed', 15)
 

##### Draw mouth #####
pen.up()
pen.setpos(0, -20)
pen.down()
pen.right(90)
pen.circle(10, 180)

pen.up()
pen.setpos(0, -20)
pen.down()
pen.left(360)
pen.circle(10, -180)


##### Draw beard #####

#left
pen.up()
pen.setpos(-25, 0)
pen.seth(165)
pen.down()
pen.fd(60)

pen.up()
pen.setpos(-25, -10)
pen.seth(180)
pen.down()
pen.fd(80)


pen.up()
pen.setpos(-25, -20)
pen.seth(193)
pen.down()
pen.fd(70)

# right
pen.up()
pen.setpos(25, 0)
pen.seth(15)
pen.down()
pen.fd(70)

pen.up()
pen.setpos(25, -10)
pen.seth(0)
pen.down()
pen.fd(80)

pen.up()
pen.setpos(25, -20)
pen.seth(-13)
pen.down()
pen.fd(60)

##### Draw cheekbones #####
pen.pensize(4)
pen.pencolor("DeepPink")
pen.up()
pen.setpos(55, 30)
pen.seth(0)
pen.down()

pen.right(90)
pen.circle(15, 180)

pen.up()
pen.setpos(-55, 30)
pen.down()
pen.left(360)
pen.circle(15, -180)

##### Draw eyebrows #####

pen.pencolor("black")

pen.up()
pen.setpos(-15, 115)
pen.seth(160)
pen.down()
pen.fd(25)

pen.up()
pen.setpos(15, 115)
pen.seth(20)
pen.down()
pen.fd(25)


##### Texts #####
pen.up()
pen.setpos(0,180)
pen.down()
pen.color('blue')
style = ('Courier', 30, 'italic')
pen.write('Hello, V!', font=style, align='center')
pen.hideturtle()


# Keep the screen on
turtle.mainloop()

 

