#Your task is to draw a gradient bar.
#You can make the color progression as simple (e.g., just green intensities changing) or sophisticated (e.g., linear equations manipulating the red, green, and blue intensities independently) as you desire. Your main requirements are this:

#The window you draw the bar in must be 400 pixels wide and the progression must be horizontal.
#There can be no gaps or overlaps in the progression: no spaces between the rectangles, no spaces from the edges of the window, no bars drawn on top of one another.
#The number of bars you use must be a multiple of 6 (i.e., 6 bars, 12 bars, 18 bars, etc.)
#The bars must have no outline (hint: setWidth method)
#All bars must have a width within one pixel of the same width. For example, if we have 6 bars in a 400-pixel window, then each bar should be 66 or 67 pixels wide. This goes along with the no overlaps constraint
import graphics as g
win = g.GraphWin("Gradient Bar", 400,200)
bar_1 = g.Rectangle(g.Point(0,0), g.Point(66,200))
bar_1.draw(win)


bar_2 = bar_1.clone()
bar_2.move(67,0)
bar_2.draw(win)

bar_3 = bar_2.clone()
bar_3.move(67,0)
bar_3.draw(win)

bar_4 = bar_3.clone()
bar_4.move(67,0)
bar_4.draw(win)

bar_5 = bar_4.clone()
bar_5.move(67,0)
bar_5.draw(win)

bar_6 = bar_5.clone()
bar_6.move(67,0)
bar_6.draw(win)