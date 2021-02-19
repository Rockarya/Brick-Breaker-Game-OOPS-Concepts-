# Take right corner to explode the exploding brick
from random import randint

# Parent class for Elements in game 
class Elements():
	def __init__(self,etype,x,y):
		self.etype = etype
		self.x = x
		self.y = y

# Child class for Paddle
class Paddle():
	def __init__(self):
		Elements.__init__(self,'p',25,37)

# Child class for short paddle
class ShortPaddle():
	def __init__(self):
		Elements.__init__(self,'SP',25,37)
		
# Child class for long paddle
class LongPaddle():
	def __init__(self):
		Elements.__init__(self,'LP',25,37)


# Child class for Ball
class Ball():
	def __init__(self,x,y):
		Elements.__init__(self,'b',x,y)
		self.dirx=1
		self.diry=-1
		self.speed=1

# Child class for Brick1
class Brick1():
	def __init__(self,x,y):
		Elements.__init__(self,'b1',x,y)
		self.btype='b1'

# Child class for Brick2
class Brick2():
	def __init__(self,x,y):
		Elements.__init__(self,'b2',x,y)
		self.btype='b2'
		
# Child class for Brick3
class Brick3():
	def __init__(self,x,y):
		Elements.__init__(self,'b3',x,y)
		self.btype='b3'
		
#Child class for Unbreakable brick
class UBrick():
	def __init__(self,x,y):
		Elements.__init__(self,'U',x,y)
		self.btype='U'

#Child class for Explodable brick brick
class EBrick():
	def __init__(self,x,y):
		Elements.__init__(self,'$',x,y)
		self.btype='$'


# Parent class for PowerUp
class PowerUp():
	def __init__(self,ptype,x,y):
		self.ptype = ptype
		self.x = x
		self.y = y
		self.previous = " "
		self.status = 0
		self.ptime = 100
		# 100 secs of powerup and status will tell us that the power-up has to be kept activated or not?

class E_PowerUp():
	def __init__(self,x,y):
		PowerUp.__init__(self,'E',x,y)
		self.ptype = 'E'

class S_PowerUp():
	def __init__(self,x,y):
		PowerUp.__init__(self,'S',x,y)
		self.ptype = 'S'

class B_PowerUp():
	def __init__(self,x,y):
		PowerUp.__init__(self,'B',x,y)
		self.ptype = 'B'

class F_PowerUp():
	def __init__(self,x,y):
		PowerUp.__init__(self,'F',x,y)
		self.ptype = 'F'

class T_PowerUp():
	def __init__(self,x,y):
		PowerUp.__init__(self,'T',x,y)
		self.ptype = 'T'

class P_PowerUp():
	def __init__(self,x,y):
		PowerUp.__init__(self,'P',x,y)
		self.ptype = 'P'
	

# Stroing all the PowerUps in an array
def PowerUpArray(board,x,y):
	power = []
	a=0
	b=0
	# power.append(E_PowerUp(24,35))
	for i in range(7):
		while(1):
			a = randint(1,x-2)
			b = randint(1,y-2)
			# Some of values of b are removed because these will be exploded by explodable bricks
			if (board[b][a] == 'b1' or board[b][a] == 'b2' or board[b][a] == 'b3') and b!=5 and b!=4:
				break
		if i==0:
			power.append(E_PowerUp(a,b))
		elif i==1:
			power.append(S_PowerUp(a,b))
		elif i==2:
			power.append(B_PowerUp(a,b))
		elif i==3:
			power.append(B_PowerUp(a,b))
		elif i==4:
			power.append(F_PowerUp(a,b))
		elif i==5:
			power.append(T_PowerUp(a,b))
		elif i==6:
			power.append(P_PowerUp(a,b))

	return power

# function to assign bricks to the board
def BricksArray(board):
	bricks = []

	a = 5
	b = 15
	for i in range(1,11):
		for j in range(i):
			f = randint(1,3)

			if f==1:
				bricks.append(Brick1(a+j,b-i))
				board[b-i][a+j] = 'b1'

			elif f==2:
				bricks.append(Brick2(a+j,b-i))
				board[b-i][a+j] = 'b2'

			else:
				bricks.append(Brick3(a+j,b-i))
				board[b-i][a+j] = 'b3'
	
	a = 58
	b = 15
	for i in range(1,11):
		for j in range(i):
			f = randint(1,3)

			if f==1:
				bricks.append(Brick1(a-j,b-i))
				board[b-i][a-j] = 'b1'

			elif f==2:
				bricks.append(Brick2(a-j,b-i))
				board[b-i][a-j] = 'b2'

			else:
				bricks.append(Brick3(a-j,b-i))
				board[b-i][a-j] = 'b3'
		
	a = 31
	b = 19
	bricks.append(Brick1(a,b))
	board[b][a] = 'b1'
	for i in range(1,15):
		bricks.append(Brick1(a+i,b-i))
		board[b-i][a+i] = 'b1'
		bricks.append(Brick1(a-i,b-i))
		board[b-i][a-i] = 'b1'


	a = 31
	b = 14
	for i in range(10):
		if i<5:
			for j in range(2*i+1):
				bricks.append(UBrick(a-j+i,b-i))
				board[b-i][a-j+i] = 'U'

		elif i == 5:
			for j in range(2*i+1):
				bricks.append(EBrick(a-j+i,b-i))
				board[b-i][a-j+i] = '$'

		else:
			for j in range(2*i+1):
				f = randint(1,3)

				if f==1:
					bricks.append(Brick1(a-j+i,b-i))
					board[b-i][a-j+i] = 'b1'

				elif f==2:
					bricks.append(Brick2(a-j+i,b-i))
					board[b-i][a-j+i] = 'b2'

				else:
					bricks.append(Brick3(a-j+i,b-i))
					board[b-i][a-j+i] = 'b3'

	# a= 15
	# b= 35
	# for i in range(10):
	# 	bricks.append(Brick1(a+i,b))
	# 	board[b][a+i] = 'b1'

	return bricks