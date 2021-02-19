import random, sys, os, time, copy 
from Block import Block
from Elements import Paddle, Ball, ShortPaddle, LongPaddle
from random import randint
from termcolor import *
import colorama
colorama.init()


class Board():
	def __init__(self,x,y,BRICKS,POWER,orignal,points):
		self.x = x
		self.y = y
		self.orignal = orignal
		self.block = Block()
		self.paddle = Paddle()
		self.ShortPaddle = ShortPaddle()
		self.LongPaddle = LongPaddle()
		self.ball = Ball(self.paddle.x+5,self.paddle.y-1)
		self.bricks = BRICKS
		self.power = POWER
		self.points = points

		self.orignal[self.paddle.y][self.paddle.x] = self.paddle.etype
		self.orignal[self.ball.y][self.ball.x] = self.ball.etype


	def Updated_org_Array(self,game):
		return self.orignal

	def Updated_Bricks_Array(self,game):
		return self.bricks

	def Updated_Points(self,game):
		return self.points

	def Update_PowerUp(self,game):
		for pup in self.power:
			if self.orignal[pup.y][pup.x] == pup.ptype:

				if pup.y + 1 == self.y-1:
					self.orignal[pup.y][pup.x] = ' '
					self.power.remove(pup)

				# Only obstacle which will hinder is the ball only in path	
				elif self.orignal[pup.y+1][pup.x] != 'b':
					self.orignal[pup.y][pup.x] = pup.previous
					pup.previous = self.orignal[pup.y+1][pup.x]
					self.orignal[pup.y+1][pup.x] = pup.ptype
					pup.y+=1


	def Remove_PowerUp(self,game):
		for pup in self.power:
			if pup.status == 1:

				if pup.ptype == 'S' and pup.ptime == 100:
					self.orignal[self.LongPaddle.y][self.LongPaddle.x] = ' '
					self.orignal[self.paddle.y][self.paddle.x] = 'SP'
					self.orignal[self.ShortPaddle.y][self.ShortPaddle.x] = ' '
					self.ShortPaddle.y = self.paddle.y
					self.ShortPaddle.x = self.paddle.x
					self.orignal[self.y-3][self.x-5] = '#'
					self.orignal[self.y-3][self.x-10] = ' '
					self.orignal[self.y-3][self.x-15] = ' '

				if pup.ptype == 'E' and pup.ptime == 100:
					self.orignal[self.ShortPaddle.y][self.ShortPaddle.x] = ' '
					self.orignal[self.paddle.y][self.paddle.x] = 'LP'
					self.orignal[self.LongPaddle.y][self.LongPaddle.x] = ' '
					self.LongPaddle.y = self.paddle.y
					self.LongPaddle.x = self.paddle.x
					self.orignal[self.y-3][self.x-5] = ' '
					self.orignal[self.y-3][self.x-10] = ' '
					self.orignal[self.y-3][self.x-15] = '#'

				if pup.ptime == 0:
					if pup.ptype == 'S' or pup.ptype == 'E':
						if pup.ptype == 'S':
							self.orignal[self.ShortPaddle.y][self.ShortPaddle.x] = 'p'
							self.paddle.y = self.ShortPaddle.y
							self.paddle.x = self.ShortPaddle.x
							
						if pup.ptype == 'E':
							self.orignal[self.LongPaddle.y][self.LongPaddle.x] = 'p'
							self.paddle.y = self.LongPaddle.y
							self.paddle.x = self.LongPaddle.x

						self.orignal[self.y-3][self.x-5] = ' '
						self.orignal[self.y-3][self.x-10] = '#'
						self.orignal[self.y-3][self.x-15] = ' '

					pup.status = 0
					self.power.remove(pup)
				else:
					pup.ptime -= 1


	def movePaddle(self,game,dirx):
		direction = dirx//abs(dirx)  

		paddle_flag = 0
		for pup in self.power:
			if pup.ptype == 'S' and pup.status == 1:
				paddle_flag = -1
			elif pup.ptype == 'E' and pup.status == 1:
				paddle_flag = 1

		if paddle_flag == 0:
			x = self.paddle.x
			y = self.paddle.y
			k = 0
			for i in range(1,1+abs(dirx)):
				if self.orignal[y][x + i*direction] == ' ': 
					k+=1
				else:
					break

			self.orignal[y][x] = ' '
			self.paddle.x = x + k*direction
			self.paddle.y = y 
			self.orignal[self.paddle.y][self.paddle.x] = 'p'

		elif paddle_flag == -1:
			x = self.ShortPaddle.x
			y = self.ShortPaddle.y
			k = 0
			for i in range(1,1+abs(dirx)):
				if self.orignal[y][x + i*direction] == ' ': 
					k+=1
				else:
					break

			self.orignal[y][x] = ' '
			self.ShortPaddle.x = x + k*direction
			self.ShortPaddle.y = y 
			self.orignal[self.ShortPaddle.y][self.ShortPaddle.x] = 'SP'

		else:
			x = self.LongPaddle.x
			y = self.LongPaddle.y
			k = 0
			for i in range(1,1+abs(dirx)):
				if self.orignal[y][x + i*direction] == ' ': 
					k+=1
				else:
					break

			self.orignal[y][x] = ' '
			self.LongPaddle.x = x + k*direction
			self.LongPaddle.y = y 
			self.orignal[self.LongPaddle.y][self.LongPaddle.x] = 'LP'


	def Ball_on_Paddle(self,game):
		paddle_flag = 0
		for pup in self.power:
			if pup.ptype == 'S' and pup.status == 1:
				paddle_flag = -1
			elif pup.ptype == 'E' and pup.status == 1:
				paddle_flag = 1

		if paddle_flag == 0:
			if self.ball.x != self.paddle.x:
				self.orignal[self.ball.y][self.ball.x] = ' '

				self.ball.y = self.paddle.y - 1
				self.ball.x = self.paddle.x + 5
				self.orignal[self.ball.y][self.ball.x] = 'b'

		elif paddle_flag == -1:
			if self.ball.x != self.ShortPaddle.x:
				self.orignal[self.ball.y][self.ball.x] = ' '

				self.ball.y = self.Shortpaddle.y - 1
				self.ball.x = self.Shortpaddle.x + 3
				self.orignal[self.ball.y][self.ball.x] = 'b'

		else:
			if self.ball.x != self.LongPaddle.x:
				self.orignal[self.ball.y][self.ball.x] = ' '

				self.ball.y = self.Longpaddle.y - 1
				self.ball.x = self.Longpaddle.x + 8
				self.orignal[self.ball.y][self.ball.x] = 'b'
	
	def Update_Flag(self,game):
		paddle_flag = 0
		for pup in self.power:
			if pup.ptype == 'S' and pup.status == 1:
				paddle_flag = -1
			elif pup.ptype == 'E' and pup.status == 1:
				paddle_flag = 1

		flag = 1
		for pup in self.power:
			if (pup.ptype == 'P') and (pup.status == 1):
				if (paddle_flag == 0) and (self.ball.y+self.ball.diry == self.paddle.y):
					for i in range(10):			
						if self.paddle.x + i == self.ball.x:
							flag = 0
							break
				elif (paddle_flag == -1) and (self.ball.y+self.ball.diry == self.ShortPaddle.y):
					for i in range(5):			
						if self.ShortPaddle.x + i == self.ball.x:
							flag = 0
							break
				elif (paddle_flag == 1) and (self.ball.y+self.ball.diry == self.LongPaddle.y):
					for i in range(15):			
						if self.LongPaddle.x + i == self.ball.x:
							flag = 0
							break
		return flag

	def moveBall(self,game):
		x = self.ball.x
		y = self.ball.y
		UP = 0
		DOWN = self.y -1
		LEFT = 0
		RIGHT = self.x-1	

		dirx = self.ball.dirx
		diry = self.ball.diry
		speed = self.ball.speed

		IS_GAMEOVER_FLAG = 0

		k=0
		# flag will be non-zero if ball collides the paddle.On colliding paddle we need to change the ball speed and if flag is 0 that means ball is in air
		flag=0
		for i in range(1,speed+1):
			# No need to make a change here as y co=ordinate of all types of paddle will remain same
			if self.orignal[y+i*diry][x+i*dirx] == ' ' and y+i*diry < self.paddle.y:
				k+=1
			else:
				break

		self.orignal[y][x] = ' '
		self.orignal[y+k*diry][x+k*dirx] = 'b'
		self.ball.x = x + k*dirx
		self.ball.y = y + k*diry

		for _ in range(k+1,speed+1):

			x = self.ball.x
			y = self.ball.y
			dirx = self.ball.dirx
			diry = self.ball.diry

			paddle_flag = 0
			for pup in self.power:
				if pup.ptype == 'S' and pup.status == 1:
					paddle_flag = -1
				elif pup.ptype == 'E' and pup.status == 1:
					paddle_flag = 1		
					

			if paddle_flag == 0:	
				if y+diry == self.paddle.y:
					f=0
					for i in range(10):			#Taking width of paddle for a total of lenght 10
						if (self.paddle.x + i == x) or (self.paddle.x + i+1 == x):
							f=1
							self.ball.diry*=(-1)

							# Only 5 values of i are possible that's why skipped other positions(see the i+=1 thing)
							if i==0 or i==8:
								flag = 3
							elif i==2 or i==6:
								flag = 2
							else:
								flag = 1

							i+=1
							break;
					if f==0:
						self.orignal[y][x] = ' '
						self.orignal[self.paddle.y][self.paddle.x] = ' '
						IS_GAMEOVER_FLAG = 1
						game.gameOver()		


				elif self.orignal[y + diry][x + dirx] == ' ':
					self.orignal[y][x] = ' '
					self.ball.x = x + dirx
					self.ball.y = y + diry
					self.orignal[y + diry][x + dirx] = 'b'

				elif y+diry==DOWN or y+diry==UP:
					self.ball.diry*=(-1)

				elif x+dirx==LEFT or x+dirx==RIGHT:
					self.ball.dirx*=(-1)


			elif paddle_flag == -1:
				if y+diry == self.ShortPaddle.y:
					f=0
					for i in range(5):			
						if self.ShortPaddle.x + i == x:
							f=1
							self.ball.diry*=(-1)

							if i==0 or i==4:
								flag = 3
							elif i==1 or i==3:
								flag = 2
							else:
								flag = 1

							break
					if f==0:
						self.orignal[y][x] = ' '
						self.orignal[self.ShortPaddle.y][self.ShortPaddle.x] = ' '
						IS_GAMEOVER_FLAG = 1
						game.gameOver()
						

				elif self.orignal[y + diry][x + dirx] == ' ':
					self.orignal[y][x] = ' '
					self.ball.x = x + dirx
					self.ball.y = y + diry
					self.orignal[y + diry][x + dirx] = 'b'

				elif y+diry==DOWN or y+diry==UP:
					self.ball.diry*=(-1)

				elif x+dirx==LEFT or x+dirx==RIGHT:
					self.ball.dirx*=(-1)


			else:
				if y+diry == self.LongPaddle.y:
					f=0
					for i in range(15):			
						if (self.LongPaddle.x + i == x) or (self.LongPaddle.x + i+1 == x) or (self.LongPaddle.x + i+2 == x):
							f=1
							self.ball.diry*=(-1)

							if i==0 or i==12:
								flag = 3
							elif i==3 or i==9:
								flag = 2
							else:
								flag = 1

							i+=2
							break;
					if f==0:
						self.orignal[y][x] = ' '
						self.orignal[self.LongPaddle.y][self.LongPaddle.x] = ' '
						IS_GAMEOVER_FLAG = 1
						game.gameOver()


				elif self.orignal[y + diry][x + dirx] == ' ':
					self.orignal[y][x] = ' '
					self.ball.x = x + dirx
					self.ball.y = y + diry
					self.orignal[y + diry][x + dirx] = 'b'

				elif y+diry==DOWN or y+diry==UP:
					self.ball.diry*=(-1)

				elif x+dirx==LEFT or x+dirx==RIGHT:
					self.ball.dirx*=(-1)


		# Power-Up enabler
		for pup in self.power:
			if pup.y+1 == self.paddle.y:
				for i in range(10):
					if self.paddle.x + i == pup.x:
						self.orignal[pup.y][pup.x] = ' '
						pup.status = 1

		if IS_GAMEOVER_FLAG == 1:
			self.orignal[self.y-3][self.x-5] = ' '
			self.orignal[self.y-3][self.x - 10] = '#'
			self.orignal[self.y-3][self.x-15] = ' '
			# removing power-ups if game get's over
			for pup in self.power:
				if self.orignal[pup.y][pup.x] == pup.ptype:
					self.orignal[pup.y][pup.x] = ' '
					self.power.remove(pup)
				# removing acquired power-up after life-loss
				if pup.status == 1:
					pup.status = 0
					self.power.remove(pup)

		# Assigning ball-speed if status is 1
		for pup in self.power:
			if pup.ptype == 'F' and pup.status == 1:
				flag = 5

		if flag!=0:
			self.ball.speed = flag


	def Ball_Brick_Collision(self,game):
		x = self.ball.x
		y = self.ball.y
		dirx = self.ball.dirx
		diry = self.ball.diry

		flag = 0
		for pup in self.power:
			if pup.ptype == 'T' and pup.status == 1:
				flag = 1
				break

		for bri in self.bricks:

			# Unbreakable bricks
			if self.orignal[bri.y][bri.x] == 'U':
				if (x + dirx == bri.x) and (y + diry == bri.y):
					if flag == 1:
						self.orignal[bri.y][bri.x] = ' '
						self.points += 10

					if diry == 1:	
						self.ball.diry*=(-1)
						self.ball.dirx*=(-1)
					else:
						self.ball.diry*=(-1)

			else:
				if (((x == bri.x) and (y + diry == bri.y)) or ((x + dirx == bri.x) and (y == bri.y)) or ((x + dirx == bri.x) and (y + diry == bri.y))) and self.orignal[bri.y][bri.x]!=' ':
					if self.orignal[bri.y][bri.x] == 'b3':
						if flag == 0:
							self.orignal[bri.y][bri.x]='b2'
							self.points += 3
						else:
							self.orignal[bri.y][bri.x]=' '
							self.points += 6

					elif self.orignal[bri.y][bri.x] == 'b2':
						if flag == 0:
							self.orignal[bri.y][bri.x]='b1'
							self.points +=2
						else:
							self.orignal[bri.y][bri.x]=' '
							self.points += 3

					elif self.orignal[bri.y][bri.x] == 'b1':
						f=0
						for pup in self.power:
							if pup.x == bri.x and pup.y == bri.y:
								f=1
								self.orignal[bri.y][bri.x] = pup.ptype

						if f==0:
							self.orignal[bri.y][bri.x] = ' '
						self.points +=1

					elif self.orignal[bri.y][bri.x] == '$':
						self.points += 100

						rx = 0
						while(self.orignal[bri.y][bri.x + rx] == '$'):
							self.orignal[bri.y][bri.x + rx] = ' '
							self.orignal[bri.y+1][bri.x + rx] = ' '
							self.orignal[bri.y-1][bri.x + rx] = ' '
							self.orignal[bri.y-1][bri.x + rx+1] = ' '
							self.orignal[bri.y-1][bri.x + rx-1] = ' '
							self.orignal[bri.y+1][bri.x + rx-1] = ' '
							self.orignal[bri.y+1][bri.x + rx+1] = ' '
							rx += 1

						rx = -1
						while(self.orignal[bri.y][bri.x + rx] == '$'):
							self.orignal[bri.y][bri.x + rx] = ' '
							self.orignal[bri.y+1][bri.x + rx] = ' '
							self.orignal[bri.y-1][bri.x + rx] = ' '
							self.orignal[bri.y-1][bri.x + rx+1] = ' '
							self.orignal[bri.y-1][bri.x + rx-1] = ' '
							self.orignal[bri.y+1][bri.x + rx-1] = ' '
							self.orignal[bri.y+1][bri.x + rx+1] = ' '
							rx -= 1

					if (x == bri.x) and (y + diry == bri.y):
						self.ball.dirx*=(-1)
					elif (x + dirx == bri.x) and (y == bri.y):
						self.ball.diry*=(-1)
					else:
						self.ball.diry*=(-1)
						self.ball.dirx*=(-1)


	def move_Power_Up(self,game):
		for pup in self.power:
			if pup.ptype == 'F' and self.F == 1:
				x = pup.x
				y = pup.y
				self.orignal[y][x] = pup.previous
				pup.previous = self.orignal[y+1][x]
				self.orignal[y+1][x] = 'F'

	
	def display(self):
		for i in range(self.y):
			for j in range(self.x):
				cprint(self.block.getBlock(self.orignal[i][j]),self.block.getColor(self.orignal[i][j]),attrs=['bold'],end='')		
			print(" ")	