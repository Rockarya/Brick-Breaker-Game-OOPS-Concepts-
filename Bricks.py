from Elements import Brick

class Bricks():
	def __init__(self,x,y,orignal,bricks,power,points,paddle,ball):
		self.x = x
		self.y = y
		self.orignal = orignal
		self.bricks = bricks
		self.power = power
		self.points = points
		self.paddle = paddle.paddle
		self.ball = ball.ball


	def Updated_Points(self,game):
		return self.points

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