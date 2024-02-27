import graphics as g
win = g.GraphWin("My House", 600,600)

day_sky = g.Rectangle(g.Point(0,0), g.Point(600,600))
day_sky.setFill('lightblue')
day_sky.setOutline('lightblue')
day_sky.draw(win)

center_roof_point = g.Point (290,220)
roof = g.Polygon(g.Point (150,310),center_roof_point,(g.Point(450, 310)))
roof.setFill('brown')
roof.setOutline('gray')
roof.draw(win)

ground = g.Rectangle(g.Point (-1,500),(g.Point (600,600)))
ground.setFill('green')
ground.setOutline('green')
ground.draw(win)

House_wall1 = g.Rectangle( g.Point(200, 300), g.Point(300, 500))
House_wall1.setFill('purple')
House_wall1.setOutline('purple')
House_wall1.draw( win)

House_wall2 = House_wall1.clone()
House_wall2.move(100,0)
House_wall2.draw(win)

Front_door = g.Rectangle( g.Point(356,430), g.Point(300,500))
Front_door.setFill('tan')
Front_door.setOutline('gray')
Front_door.draw(win)

center_sun = g.Point( 50, 150)
sun = g.Circle( center_sun,50 )
sun.setFill('orange')
sun.setOutline( 'darkred')
sun.draw(win)
sun_rays1= g.Line( g.Point(70, 200), g.Point(90,350))
sun_rays1.setOutline('gold')
sun_rays1.draw(win)
sun_rays2= sun_rays1.clone()
sun_rays2.move(25, -25),(65,-95)
sun_rays2.draw(win)



