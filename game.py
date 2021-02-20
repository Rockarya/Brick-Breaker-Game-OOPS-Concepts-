from Board import Board 
from Paddles import Paddles
from Balls import Balls
from Bricks import Bricks
from PowerUps import PowerUps 
from Elements import BricksArray, PowerUpArray
from drawings import instructions , thankyou, trophy
from termcolor import *
import colorama
colorama.init()
import random, sys, os, time, copy, signal

try:
	import tty, termios
except ImportError:
	try:
		import msvcrt
	except ImportError:
		raise ImportError('getch not available')
	else:
		getch = msvcrt.getch
else:
	def getch():
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(fd)
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

def alarmHandler(signum, frame):
	raise AlarmException

class AlarmException(Exception):
	pass

class Game():
	# __init__ is a constructor and is used to initalize the attributes of the class.
	def __init__(self,f,TIME,X,Y,orignal,BRICK,POWER,points):
		# Thses all written below are instance variables
		# methods are the functions which are defined in the class to manipulate these attributes
		# self is an object
		self.x = X
		self.y = Y
		self.f = f
		self.orignal = orignal
		self.bricks = BRICK
		self.power = POWER
		self.points = points
		self.paddle = Paddles(self.x,self.y,self.orignal,self.bricks,self.power,self.points)
		self.ball = Balls(self.x,self.y,self.orignal,self.bricks,self.power,self.points,self.paddle)
		self.brick = Bricks(self.x,self.y,self.orignal,self.bricks,self.power,self.points,self.paddle,self.ball)
		self.powerup = PowerUps(self.x,self.y,self.orignal,self.bricks,self.power,self.points,self.paddle,self.ball,self.brick)
		self.board = Board(self.x,self.y,self.orignal,self.bricks,self.power,self.points,self.paddle,self.ball,self.brick,self.powerup)
		self.time = TIME
		self.GAMEOVER = False


	def input(self,timeout=1):
		signal.signal(signal.SIGALRM, alarmHandler)
		signal.alarm(timeout)	
		
		try:
			inp = getch()
			signal.alarm(0)

			if inp == 'q':
				sys.exit()

			if inp == 'p':
				getch()	
	
			if inp == 'a':			
				self.paddle.movePaddle(self,-2)

			elif inp == 'd':		
				self.paddle.movePaddle(self,2)			

			elif inp == 's':		
				self.f=1	

			else:
				pass 

			return ''	

		except AlarmException:
			signal.signal(signal.SIGALRM, signal.SIG_IGN)
			return ''

	def update(self):
		self.time = self.time + 1
		self.brick.Ball_Brick_Collision(self)
		self.powerup.Update_PowerUp(self)
		self.powerup.Remove_PowerUp(self)

		if self.f == 1:
			self.ball.moveBall(self)
			self.f = self.ball.Update_Flag(self)
		else:
			self.ball.Ball_on_Paddle(self)
		os.system("clear")


	def updatedboard(self):
		return self.board.Updated_org_Array(self)


	def updatedbricks(self):
		return self.board.Updated_Bricks_Array(self)

	def updatedpoints(self):
		return self.brick.Updated_Points(self)


	def updatedpower(self):
		return self.board.Updated_Power_Array(self)


	def gameOver(self):
		os.system("clear")
		self.board.display()
		print("Ball missed the paddle :-(")
		self.GAMEOVER = True
		print("Press any key to continue")
		getch()
	

	def gameWon(self):
		print("Congrats you won the game")
		trophy()	
		getch()

	def scoreboard(self):
		print("Lives:",end='')
		for _ in range(lives):
			cprint("\u2764 ",'red',attrs=['bold'],end='')
		
		points=self.brick.Updated_Points(self)
		print("     SCORE:",points,"     time:",self.time)

if __name__ == "__main__":

	instructions()
	getch()

	points = 0 
	lives = 3 
	TIME = 0

	# BOARD SIZE
	X = 65
	Y = 43
	orignal = [ [' ' for j in range(X)] for i in range(Y)]
	orignal[0] = ['#']*X
	orignal[Y-1] = ['#']*X

	for j in range(1,Y-1):	
		for i in range(X):
			if j==Y - 3:
				if i==0 or i==X-10:
					orignal[j][i] = '#'
				else:
					orignal[j][i] = ' '
			else:
				if i==0 or i==X-1:
					orignal[j][i] = '#'
				else:
					orignal[j][i] = ' '


	BRICK=BricksArray(orignal)
	POWER=PowerUpArray(orignal,X,Y)


	while lives > 0:
		os.system("clear")
		# Flag f=0 indicates that ball should be on paddle.When f is rasised to 1 then it means that ball can move freely now
		f=0
		game = Game(f,TIME,X,Y,orignal,BRICK,POWER,points)

		while(1):
			os.system("clear")
			game.board.display()		
			game.scoreboard() 
			game.input()

			if(game.GAMEOVER == True):
				break

			game.update()	
			TIME+=1
			
		if game.GAMEOVER == True:		
			lives = lives -1	
			# We need to update the orginal array and Brick' array because both of them have changed over time so in next life u have to transfer the updated one
			orignal = game.updatedboard()
			BRICK = game.updatedbricks()
			points = game.updatedpoints()
			POWER = game.updatedpower()

	thankyou()		