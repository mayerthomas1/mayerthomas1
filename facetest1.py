import graphics as g
win = g.GraphWin("Happy Face", 250,250)

leftpupil = g.Point(50,75)

rightpupil = g.Point(150,75)

lefteye = g.Circle( leftpupil, 25)
lefteye.setFill('white')
lefteye.setOutline( 'brown')
lefteye.draw(win)
leftpupil.draw( win )

righteye = g.Circle( rightpupil, 25)
righteye.setFill('white')
righteye.setOutline( 'brown')
righteye.draw(win)
rightpupil.draw( win)

nose = g.Rectangle( g.Point(75, 125), g.Point(125, 150))
nose.draw( win)

centermouthpoint = g.Point (100,175)
leftmouthline = g.Line(g.Point(40, 155), centermouthpoint)
leftmouthline.draw(win)
rightmouthline = g.Line( centermouthpoint, g.Point(160,155))
rightmouthline.draw(win)


win.getMouse()
win.close()
