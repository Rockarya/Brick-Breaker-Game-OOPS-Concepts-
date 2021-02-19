class Block():

	def __init__(self):
		self.empty_structure = " "
		self.wall_structure = "#"
		self.paddle_structure = "=========="
		self.short_paddle_structure = "====="
		self.long_paddle_structure = "==============="
		self.ball_structure = "o"
		self.brick1_structure = "%"
		self.brick2_structure = "&"
		self.brick3_structure = "@"
		self.Ubrick_structure = "#"
		self.Ebrick_structure = "$"
		self.Expandpaddle_structure = "E"
		self.Shrinkpaddle_structure = "S"
		self.Ballmultiplier_structure = "B"
		self.Fastball_structure = "F"
		self.Thuruball_structure = "T"
		self.Paddlegrab_structure = "P"

	def getBlock(self,a):
		
		if a == ' ':
			return self.empty_structure

		elif a == '#':
			return self.wall_structure

		elif a == 'p':
			return self.paddle_structure

		elif a == 'SP':
			return self.short_paddle_structure

		elif a == 'LP':
			return self.long_paddle_structure

		elif a == 'b':
			return self.ball_structure

		elif a == 'b1':
			return self.brick1_structure

		elif a == 'b2':
			return self.brick2_structure

		elif a == 'b3':
			return self.brick3_structure

		elif a == 'U':
			return self.Ubrick_structure

		elif a == '$':
			return self.Ebrick_structure

		elif a == 'E':
			return self.Expandpaddle_structure

		elif a == 'S':
			return self.Shrinkpaddle_structure

		elif a == 'B':
			return self.Ballmultiplier_structure

		elif a == 'F':
			return self.Fastball_structure

		elif a == 'T':
			return self.Thuruball_structure

		elif a == 'P':
			return self.Paddlegrab_structure
								
		else :
			return "errr"

	def getColor(self,a):
		if a == ' ':
			return None

		elif a == '#':
			return 'white'

		elif a == 'b':
			return 'yellow'

		elif a == 'p':
			return 'blue'

		elif a == 'SP':
			return 'blue'

		elif a == 'LP':
			return 'blue'

		elif a == 'b3' :
			return 'blue'

		elif a == 'b2' :
			return 'green'

		elif a == 'b1' :
			return 'red'

		elif a == 'U':
			return 'white'	

		elif a == '$':
			return 'yellow'	

		elif a == 'E':
			return 'red'

		elif a == 'S':
			return 'green'

		elif a == 'B':
			return 'blue'			

		elif a == 'F':
			return 'yellow'	

		elif a == 'T':
			return 'white'	

		elif a == 'P':
			return 'yellow'	
								
		else :
			return 'black'