from random import randint

# Parent class for Elements in game 
class Elements():
	def __init__(self,etype,x,y):
		self.etype = etype
		self.x = x
		self.y = y

# derived class for PowerUp
class PowerUp():
	def __init__(self,powtype,x,y):
		Elements.__init__(self,powtype,x,y)
		self.ptype = powtype
		self.previous = " "
		self.status = 0
		self.ptime = 100
		# 100 secs of powerup and status will tell us that the power-up has to be kept activated or not?

# derived class for Paddle
class Paddle():
	def __init__(self,ptype):
		Elements.__init__(self,ptype,25,40)


# derived class for Ball
class Ball():
	def __init__(self,x,y):
		Elements.__init__(self,'b',x,y)
		self.dirx=1
		self.diry=-1
		self.speed=1

# derived class for Brick1
class Brick():
	def __init__(self,btype,x,y):
		Elements.__init__(self,btype,x,y)
	

# Stroing all the PowerUps in an array
def PowerUpArray(board,x,y):
	power = []
	a=0
	b=0
	# power.append(PowerUp('T',24,35))
	for i in range(6):
		while(1):
			a = randint(1,40)
			b = randint(5,7)
			if (board[b][a] == 'b1' or board[b][a] == 'b2' or board[b][a] == 'b3'):
				break
		ch = ''
		if i==0:
			ch = 'E'
		elif i==1:
			ch = 'S'
		elif i==2:
			ch = 'B'
		elif i==3:
			ch = 'F'
		elif i==4:
			ch = 'T'
		elif i==5:
			ch = 'P'
		power.append(PowerUp(ch,a,b))

	return power

# Just a lazy optimization ;-)
def make_brick(a,b,bricks,board,flag):
	for i in range(1,11):
		for j in range(i):
			f = randint(1,3)
			ch = ''
			if f==1:
				ch = 'b1'
			elif f==2:
				ch = 'b2'
			else:
				ch = 'b3'

			bricks.append(Brick(ch,a+flag*j,b-i))
			board[b-i][a+flag*j] = ch

	return bricks

# function to assign bricks to the board
def BricksArray(board):
	bricks = []

	bricks = make_brick(5,15,bricks,board,1)
	bricks = make_brick(58,15,bricks,board,-1)

	a = 15
	b = 18
	for i in range(30):
		bricks.append(Brick('b1',a+i,b))
		board[b][a+i] = 'b1'

	a = 31
	b = 14
	for i in range(10):
		if i<5:
			for j in range(2*i+1):
				bricks.append(Brick('U',a-j+i,b-i))
				board[b-i][a-j+i] = 'U'

		elif i == 5:
			for j in range(2*i+1):
				bricks.append(Brick('$',a-j+i,b-i))
				board[b-i][a-j+i] = '$'

		else:
			for j in range(2*i+1):
				f = randint(1,3)
				ch = ''
				if f==1:
					ch = 'b1'
				elif f==2:
					ch = 'b2'
				else:
					ch = 'b3'
				bricks.append(Brick(ch,a-j+i,b-i))
				board[b-i][a-j+i] = ch

	# These set of bricks are just used to test the power-ups
	# Take the right corner to explode the explode brick
	# a= 15
	# b= 35
	# for i in range(10):
	# 	bricks.append(Brick('b1',a+i,b))
	# 	board[b][a+i] = 'b1'

	return bricks