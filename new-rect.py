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

	def Insert(self,width,height):
		score1=0
		score2=0
		newNode,score1,score2=self.FindPositionFornewNode(width,height,score1,score2)

		#if rectangle packing is unsuccessful
		if newNode.height==0:		
			return newNode
		size=len(self.freeRectangles)
		i=0
		while i < size:
			if self.SplitfreeNode(self.freeRectangles[i],newNode):	#the splitting
				del self.freeRectangles[i]							#deletes the rectangles after it's been split up
				i=i-1
				size=size-1
			i=i+1

		#checks for redundant entries
		self.prunefreelist()										
		self.usedRectangles.append(newNode)
		return newNode

	def prunefreelist(self):
		i=0
		while (i<len(self.freeRectangles)):
			j=i+1
			while(j<len(self.freeRectangles)):
				if self.IsContainedIn(self.freeRectangles[i],self.freeRectangles[j]):
					del self.freeRectangles[i]
					i=i-1
					break
				if self.IsContainedIn(self.freeRectangles[j],self.freeRectangles[i]):
					del self.freeRectangles[j]
					j=j-1
				j=j+1
			i=i+1
	
	def IsContainedIn(self,a,b):
		#evaluates co-ordinates and measures of both the rectangles
		k1=a.x >= b.x and a.y >= b.y
		k2=a.x + a.width <= b.x + b.width
		k3=a.y + a.height <= b.y + b.height
		return k1 and k2 and k3			
	
	def SplitfreeNode(self,freeNode,usedNode):
		#checking if the rectangles intersect
		if usedNode.x>=freeNode.x+freeNode.width or usedNode.x+usedNode.width<=freeNode.x or usedNode.y>=freeNode.y+freeNode.height or usedNode.y+usedNode.height <= freeNode.y:
			return False
		
		#splitting begins
		if	usedNode.x<freeNode.x+freeNode.width and usedNode.x+usedNode.width>freeNode.x:
			if usedNode.y > freeNode.y and usedNode.y<freeNode.y+freeNode.height:
				#if usedNode is at the top side
				newNode=Rect(freeNode)
				newNode.height=usedNode.y-newNode.y
				self.freeRectangles.append(newNode)
			if usedNode.y+usedNode.height<freeNode.y+freeNode.height:
				#if usedNode is at the top side
				newNode=Rect(freeNode)
				newNode.y=usedNode.y+usedNode.height
				newNode.height=freeNode.y + freeNode.height- (usedNode.y+usedNode.height)
				self.freeRectangles.append(newNode)
		if usedNode.y<freeNode.y+freeNode.height and usedNode.y+usedNode.height>freeNode.y:
			if usedNode.x > freeNode.x and usedNode.x<freeNode.x+freeNode.height:
				#if usedNode is on the left
				newNode=Rect(freeNode)
				newNode.width=usedNode.x-newNode.x
				self.freeRectangles.append(newNode)
			if usedNode.x + usedNode.width < freeNode.x + freeNode.width:
				#if usedNode on the right
				newNode=Rect(freeNode)
				newNode.x=usedNode.x+usedNode.width
				newNode.width=freeNode.x+freeNode.width-(usedNode.x+usedNode.width)
				self.freeRectangles.append(newNode)
		return True


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

	for i in range (0,n):
		print "**********************************"
		print "packing bin of size",items[i][1],"   ",items[i][2]
		packedrect=Rect()
		packedrect=maxbin.Insert(items[i][1],items[i][2])
		if packedrect.height>0:
			print "bin packed successfully"
		else :
			print "no space"

	# saving output to bokeh file
	html_title="height=%r and width='%r'"%(height,width)
	bk.output_file("maxrects.html",title="MAXRECTS")				
	bk.figure(plot_width=600,plot_height=600,title=html_title)
	bk.hold()														
	x_cor=[]
	y_cor=[]
	b_width=[]
	b_height=[]

	# plotting
	bk.rect([width/2],
		[int(height)/2],
		[width],
		[int(height)],fill_color="crimson")

	#disables overwriting of any previous glyph
	bk.hold()

	#gets centre co-ordinates of each used rectangle
	for pr in maxbin.usedRectangles:								
		b_x=pr.x+pr.width/2
		b_y=pr.y+pr.height/2
		x_cor.append(int(b_x))
		y_cor.append(int(b_y))
		b_width.append(int(pr.width))
		b_height.append(int(pr.height))

	#plot on a browser and save output 
	bk.rect(x_cor,
		y_cor,
		b_width,
		b_height,fill_color="black")

	# open browser and save plot
	bk.show()
	bk.save()
