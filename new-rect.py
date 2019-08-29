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
	
	def FindPositionFornewNode(self,width,height,s1,s2):
		bestnode=Rect()
		#std::numeric_limits<int>::max()  max value of int
		bestshortsidefit=2147483647
		bestlongsidefit=s2
		bestnode.x=bestnode.y=bestnode.height=bestnode.width=0
		for i in range(0,len(self.freeRectangles)):
			if self.freeRectangles[i].width >= width and self.freeRectangles[i].height >= height:
				leftoverHoriz=self.freeRectangles[i].width - width
				leftoverVert=self.freeRectangles[i].height - height
				shortsidefit=min(leftoverHoriz,leftoverVert)
				longsidefit=max(leftoverHoriz,leftoverVert)
				
				if shortsidefit < bestshortsidefit or (shortsidefit == bestshortsidefit and longsidefit < bestlongsidefit):
					bestnode.x=self.freeRectangles[i].x
					bestnode.y=self.freeRectangles[i].y
					bestnode.width=width
					bestnode.height=height
					bestshortsidefit=shortsidefit
					bestlongsidefit=longsidefit
			
			#checks if rotation can get a better fit
			if self.freeRectangles[i].width >= height and self.freeRectangles[i].height>=width:	
				flippedLeftoverHoriz=abs(self.freeRectangles[i].width-height)
				flippedLeftoverVert=abs(self.freeRectangles[i].height-width)
				flippedShortSideFit=min(flippedLeftoverHoriz,flippedLeftoverVert)
				flippedLongSideFit=max(flippedLeftoverHoriz,flippedLeftoverVert)
				
				if flippedShortSideFit<bestshortsidefit or (flippedShortSideFit == bestshortsidefit and flippedLongSideFit<bestlongsidefit):
					bestnode.x=self.freeRectangles[i].x
					bestnode.y=self.freeRectangles[i].y
					bestnode.width=height
					bestnode.height=width
					bestshortsidefit=flippedShortSideFit
					bestlongsidefit=flippedLongSideFit
		return bestnode,bestshortsidefit,bestlongsidefit


if __name__ == "__main__":

	print """BEST SHORT SIDE FIT"""
	print """The format of the data files should be:
	number n of items
	width W for the strip 
	for each item (i=0,1,......n-1):
	index i, width of item i, height of item i"""
	# print ("enter the filename containing the data")
	# fname=input()
	k=open("zdf1.txt")
	items=[]
	for line in k:
		items.append([int (x) for x in line.split(" ")])  
	for j in items:
		j=[int(k) for k in j]
	# print "enter the height"
	# height=raw_input(">")
	n=items[0][0]
	width=items[1][0]
	height=items[2][0]
	del items[0:3]
	maxbin=MaxRectsBinPack(int(width),int(height))