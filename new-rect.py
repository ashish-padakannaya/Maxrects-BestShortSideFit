import bokeh.plotting as bk					
import random


#each rectangle in the bin will be initialized in this class
class Rect:
	def __init__(self,k=None):
		if k is None:
			return							
		self.x=k.x
		self.y=k.y
		self.width=k.width
		self.height=k.height
	
class MaxRectsBinPack:
    #which rotation will get the best fit
	score1=0
	score2=0
	usedRectangles=[]						
	freeRectangles=[]

    #initializing bin
	def __init__(self,width=0,height=0):
		self.width=width					
		self.height=height
		n=Rect()
		n.x=0
		n.y=0
		n.width=width
		n.height=height

        #adds first bin to the free rectangle list after initialization
		self.freeRectangles.append(n)