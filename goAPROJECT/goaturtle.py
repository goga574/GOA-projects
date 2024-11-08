from turtle import *

#lets biuld a bank 

speed(100)
width(2)

penup()
goto(-500, -350)
pendown()


#საძირკველი

forward(900) #მთლიანი ბანკის სიგანე -------- 200 კარის უნდა იყოს

color("RosyBrown4")
begin_fill()
left(90)
forward(50) #საძრკველის სიმაღლე  |
left(90)
forward(350) #erti sadzirkvelis sigane
left(90)
forward(50)
end_fill()

#საძირკველის ზევითა მხარე წითლი როა

right(180)
forward(50)


color("red4")
begin_fill()
forward(20)
right(90)
forward(355)
right(90)
forward(20)
right(90)
forward(355)
end_fill()


#meore sadzirkveli daviwyot
penup()
goto(-500, -350)
pendown()

right(180)

color("RosyBrown4")
begin_fill()
forward(350)
left(90)
forward(50) #საძრკველის სიმაღლე  |
left(90)
forward(350) #erti sadzirkvelis sigane
left(90)
forward(50)
end_fill()
#end



#meore sadzirkvelis zevita witeli

right(180)
forward(50)

begin_fill()
color("red4")
left(90)
forward(5)
right(90)
forward(20)
right(90)
forward(355)
right(90)
forward(20)
left(90)
end_fill()
#end


#bankis shuanawili

right(180)
forward(350)
right(90)
forward(21)


begin_fill()
color("sienna1")

forward(350) #bankis shua nawilis simagale
right(90)
forward(900)
right(90)
forward(350)
right(90)
forward(350)
left(90)
forward(70)
right(90)
forward(200)
right(90)
forward(70)
left(90)
forward(350)

end_fill()
#end 

color("black")

penup()
goto(-150, -350)
pendown()
right(90)

#door
begin_fill()
color("AntiqueWhite2")
forward(230)  #karis simagle
right(30)
forward(20)
right(60)
forward(180)
right(60)
forward(20)
right(30)
forward(230)
right(90)
forward(200)
end_fill()

right(180)
forward(10)
left(90)

begin_fill()
color("OrangeRed1")
forward(220)
right(30)
forward(20)
right(60)
forward(160)
right(60)
forward(20)
right(30)
forward(220)
right(90)
forward(95)
end_fill()

color("black")

width(1)
right(90)
forward(238)
right(180)
forward(10)
right(90)

#first glass
color("OrangeRed1")
forward(10)

color("turquoise1")
begin_fill()
forward(60)
left(60)
forward(20)
left(30)
forward(120)
left(90)
forward(70)
left(90)
forward(138)
end_fill()

right(90)
color("OrangeRed1")
forward(23)

color("turquoise1")
begin_fill()
forward(60)
right(60)
forward(20)
right(30)
forward(120)
right(90)
forward(70)
right(90)
forward(138)
end_fill()
#end

penup()
goto(-65, -350)
pendown()

color("OrangeRed1")
forward(10)
color("chocolate1")


#charcho
begin_fill()
forward(60)
left(90)
forward(70)
left(90)
forward(60)
left(90)
forward(70)
end_fill()


penup()
goto(-500, -350)
pendown()

width(3)
color("black")
forward(900)
right(180)
forward(372)

right(90)
forward(3)

color("OrangeRed1")

forward(7)
width(1)
color("chocolate1")
begin_fill()
forward(60)
left(90)
forward(70)
left(90)
forward(60)
left(90)
forward(70)
end_fill()
#end


penup()
goto(-500, -350)
pendown()


width(1)
color("black")

forward(350)

penup()
goto(-150, -85)
pendown()

color("AntiqueWhite2")

#karis magla fanjara

begin_fill()
forward(200)
left(90)
forward(100)
left(30)
forward(30)
left(60)
forward(170)
left(60)
forward(30)
left(30)
forward(100)
end_fill()
#end

#glasses of middle window

left(90)
forward(10)
left(90)
forward(15)

begin_fill()
color("turquoise1")
forward(80)
right(30)
forward(20)
right(60)
forward(160)
right(60)
forward(20)
right(30)
forward(80)
right(90)
forward(180)
end_fill()


right(180)
forward(85)

begin_fill()
color("black")
width(2)
left(90)

forward(96)

right(90)
forward(5)
right(90)
forward(96)
right(90)
forward(5)
end_fill()

penup()
goto(-485, -280)
pendown()

#first akldama

begin_fill()
color("cornsilk3")
right(92)
forward(330)
left(30)
forward(24)
right(118)
forward(50)
right(118)
forward(24)
left(30)
forward(330)
end_fill()
#end


penup()
goto(-230, -280)
pendown()

right(90)


#second akldama
begin_fill()
right(93)
forward(330)
left(30)
forward(24)
right(118)
forward(50)
right(118)
forward(24)
left(30)
forward(330)
end_fill()
#end


penup()
goto(90, -280)
pendown()

right(90)


# third akldama

begin_fill()
right(94)
forward(330)
left(30)
forward(24)
right(118)
forward(50)
right(118)
forward(24)
left(30)
forward(330)
end_fill()
#end




penup()
goto(320, -280)
pendown()

right(90)

#fourth akldama
begin_fill()
right(94)
forward(330)
left(30)
forward(24)
right(118)
forward(50)
right(118)
forward(24)
left(30)
forward(330)
end_fill()
#end



penup()
goto(-290, -230)
pendown()

right(93)

# first window in middle


begin_fill()
color("HoneyDew2")
forward(80)
right(90)
forward(200)
right(30)
forward(20)
right(60)
forward(60)
right(60)
forward(20)
right(30)
forward(200)
end_fill()

right(90)
forward(10)
right(90)
forward(10)



#window blue color inside
width(3)
begin_fill()
color("turquoise1")
forward(180)
left(30)
forward(20)
left(60)
forward(40)
left(60)
forward(20)
left(30)
forward(180)
left(90)
forward(60)
end_fill()

right(180)
forward(30)
right(90)

color("black")
forward(198)

right(180)
forward(30)
right(90)
forward(30)
right(180)
forward(60)

right(180)
forward(30)
left(90)
forward(40)
right(90)

forward(30)
right(180)
forward(60)
right(180)
forward(30)
left(90)
forward(40)
right(90)
forward(30)
right(180)
forward(60)


right(180)
forward(30)
left(90)
forward(40)
right(90)

forward(30)
right(180)
forward(60)
right(180)
forward(30)
left(90)
forward(35)
right(90)
forward(30)
right(180)
forward(60)

#end


#second middle window

penup()
goto(270, -230)
pendown()

right(180)

begin_fill()
color("HoneyDew2")
forward(80)
right(90)
forward(200)
right(30)
forward(20)
right(60)
forward(60)
right(60)
forward(20)
right(30)
forward(200)
end_fill()

right(90)
forward(10)
right(90)
forward(10)



#window blue color inside
width(3)
begin_fill()
color("turquoise1")
forward(180)
left(30)
forward(20)
left(60)
forward(40)
left(60)
forward(20)
left(30)
forward(180)
left(90)
forward(60)
end_fill()

right(180)
forward(30)
right(90)

color("black")
forward(198)

right(180)
forward(30)
right(90)
forward(30)
right(180)
forward(60)

right(180)
forward(30)
left(90)
forward(40)
right(90)

forward(30)
right(180)
forward(60)
right(180)
forward(30)
left(90)
forward(40)
right(90)
forward(30)
right(180)
forward(60)


right(180)
forward(30)
left(90)
forward(40)
right(90)

forward(30)
right(180)
forward(60)
right(180)
forward(30)
left(90)
forward(35)
right(90)
forward(30)
right(180)
forward(60)
#end

penup()
goto(-500, 72)
pendown()

color("red2")


#bankis zevita witeli akldamtebtan

begin_fill()
forward(905)
right(180)
forward(910)
right(90)
forward(15)
right(90)
forward(910)
right(90)
forward(15)
end_fill()
# end


right(180)
forward(15)
left(90)
forward(5)
right(90)
forward(2)


#bankis zevita sartuli banki ro weria


begin_fill()
color("sienna1")
forward(100)
left(90)
forward(900)
left(90)
forward(100)
left(90)
forward(900)
end_fill()

#end
width(3)
color("black")
forward(5)
right(90)
forward(18)
right(90)
forward(910)
right(90)
forward(18)
right(90)
forward(910)
#end

penup()
goto(-500, 190)
pendown()


#shavi shemogobili mere dagvchirdeba filebis gareshed

width(2)
color("red2")
begin_fill()
right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

left(90)
forward(15)
left(90)
forward(935)
left(90)
forward(15)
left(90)
forward(15)
end_fill()


color("black")
right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

right(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
right(90)
forward(20)

left(90)
forward(15)
left(90)
forward(935)
left(90)
forward(15)
left(90)
forward(15)

#end



penup()
goto(-50, 360)
pendown()


right(30)


#es dagvchirdeba shemosaxaazad


begin_fill()
color("red2")
forward(310)
right(150)
forward(40)
right(30)
forward(260)
left(60)
forward(260)
right(30)
forward(40)
right(150)
forward(305)
end_fill()
#end

width(2)
color("black")
right(60)
forward(305)
right(150)
forward(40)
right(30)
forward(257)
left(60)
forward(255)
right(30)
forward(43)
right(150)
forward(305)


right(60)
forward(305)
right(150)
forward(48)

width(3)
begin_fill()
color("sienna1")
right(30)
forward(250)
left(60)
forward(248)
left(150)
forward(430)
end_fill()

color("black")
forward(40)
right(180)
forward(515)
right(150)
forward(300)

width(2)
right(180)

forward(140)


#es dagvchirdeba

color("red2")
begin_fill()
right(30)
forward(200)
left(90)
forward(20)
left(90)
width(1)
forward(167)
left(30)
forward(40)
right(180)
end_fill()


color("black")
width(3)
right(30)
forward(200)
left(90)
forward(20)
left(90)
forward(164)
left(30)
forward(40)
right(180)
forward(42)


color("sienna1")
width(1)
begin_fill()
forward(120)
right(30)
forward(45)
right(90)
forward(60)
end_fill()







penup()
goto(400, 205)
pendown()


color("black")

left(90)
forward(180)
right(30)
forward(120)
right(250)
forward(120)





exitonclick()
