from graphics import*
def main():
   win = GraphWin("First Program")
   
   rect = Rectangle(Point(30,30), Point(70,70))
   rect.draw(win)
   win.getMouse()
   win.close()


main()
