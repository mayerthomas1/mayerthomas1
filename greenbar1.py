import graphics as g
winX = 400
winY = 200
numberColors = 48

Width_of_rectangle = winX/numberColors
#Height_of_rectangle = winY/numberColors
hues_green = 255//numberColors
win = g.GraphWin('Gradient Bar', winX, winY)
x = 0
green = 0

for gradientGreen in range (numberColors):
    green_1 = g.Rectangle(g.Point (x,0), g.Point(x + Width_of_rectangle, winY))
    #green_1 = g.Rectangle(g.Point(x,(green / Width_of_rectangle)), g.Point( x + Height_of_rectangle, winY))
    green_1.setFill (g.color_rgb(0, green ,0))
    green_1.setWidth (0)
    green_1.draw (win)
    green = green + hues_green
    x = x + Width_of_rectangle
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  
    
    