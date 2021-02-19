import os
from termcolor import *
import colorama
colorama.init()

def instructions():
	os.system("clear")
	cprint("###############################################################",'red',attrs=['bold'])
	cprint("#                        ..:::::::::..                        #",'red',attrs=['bold']) 
	cprint("#                   ..:::aad8888888baa:::..                   #",'red',attrs=['bold'])  
	cprint("#                .::::d:?88888888888?::8b::::.                #",'red',attrs=['bold'])  
	cprint("#              .:::d8888:?88888888??a888888b:::.              #",'red',attrs=['bold'])   
	cprint("#            .:::d8888888a8888888aa8888888888b:::.            #",'red',attrs=['bold'])   
	cprint("#           ::::dP::::::::88888888888::::::::Yb::::           #",'red',attrs=['bold'])   
	cprint("#          ::::dP:::::::::Y888888888P:::::::::Yb::::          #",'red',attrs=['bold'])      
	cprint("#         ::::d8:::::::::::Y8888888P:::::::::::8b::::         #",'red',attrs=['bold'])      
	cprint("#        .::::88::::::::::::Y88888P::::::::::::88::::.        #",'red',attrs=['bold'])     
	cprint("#        :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::        #",'red',attrs=['bold'])     
	cprint("#        :::::::Y88888888888P::|::Y88888888888P:::::::        #",'red',attrs=['bold'])     
	cprint("#        ::::::::::::::::888:::|:::888::::::::::::::::        #",'red',attrs=['bold'])     
	cprint("#        `:::::::::::::::8888888888888b::::::::::::::'        #",'red',attrs=['bold'])      
	cprint("#         :::::::::::::::88888888888888::::::::::::::         #",'red',attrs=['bold'])    
	cprint("#          :::::::::::::d88888888888888:::::::::::::          #",'red',attrs=['bold'])     
	cprint("#           ::::::::::::88::88::88:::88::::::::::::           #",'red',attrs=['bold'])   
	cprint("#            `::::::::::88::88::88:::88::::::::::'            #",'red',attrs=['bold'])     
	cprint("#              `::::::::88::88::P::::88::::::::'              #",'red',attrs=['bold'])   
	cprint("#                `::::::88::88:::::::88::::::'                #",'red',attrs=['bold']) 
	cprint("#                   ``:::::::::::::::::::''                   #",'red',attrs=['bold'])
	cprint("#                        ``:::::::::''                        #",'red',attrs=['bold'])
	cprint("###############################################################",'red',attrs=['bold'])

	cprint("			\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3",'blue',attrs=['bold'])	
	cprint("			\U0001F4A3BrickBreaker\U0001F4A3","blue",attrs=['bold','underline'])	
	cprint("			\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\n",'blue',attrs=['bold'])			

	cprint("Goal is to break all the bricks with the use of ball")
	cprint("Be carefull that ball do not strike the ground.Make the ball collide to the paddle\n")
	cprint("collide the ball at suitable position on paddle to gain more spped\n")
	cprint("There are 4 types of bricks:\n%(red) : Can be broken after 1 strike(+1)\n&(green) : Can be broken after 2 strikes(+2)\n@(blue) : Can be broken after 3 strikes(+3)\n#(white) : Unbreakable bricks(These bricks repels the ball in opposite direction)\n")
	cprint("Keys")
	cprint("a : Left\nd : Right\ns : Shoot the ball after every new life\n")
	cprint("q : exit the program\np : pause\n")
	print("Press any key to continue")


def thankyou():
	cprint("		        88                                 88                                              ",'green')  
	cprint("		  ,d    88                                 88                                              ",'green')    
	cprint("		  88    88                                 88                                              ",'green')   
	cprint("		MM88MMM 88,dPPYba,  ,adPPYYba, 8b,dPPYba,  88   ,d8 8b       d8  ,adPPYba,   88	       88  ",'green')   
	cprint("		  88    88P'    \"8a \"\"     `Y8 88P'   `\"8a 88 ,a8\"  `8b     d8' a8\"     \"8a  88        88 ",'green')
	cprint("		  88    88       88 ,adPPPPP88 88       88 8888[     `8b   d8'  8b       d8  88        88  ",'green')    
	cprint("		  88,   88       88 88,    ,88 88       88 88`\"Yba,   `8b,d8'   \"8a,   ,a8\"  88a      a88  ",'green')     
	cprint("		  \"Y888 88       88 `\"8bbdP\"Y8 88       88 88   `Y8a    Y88'     `\"YbbdP\"'    `\"YbbdP'Y8   ",'green')    
	cprint("		                                                        d8'                                ",'green')   
	cprint("		                                                       d8'                   ",'green')

def trophy():
	
        cprint("     ___________   ",'yellow',attrs=['bold']) 
        cprint("    '._==_==_=_.'  ",'yellow',attrs=['bold']) 
        cprint("    .-\:      /-.  ",'yellow',attrs=['bold']) 
        cprint("   | (|:.     |) | ",'yellow',attrs=['bold']) 
        cprint("    '-|:.     |-'  ",'yellow',attrs=['bold']) 
        cprint("      \::.    /    ",'yellow',attrs=['bold']) 
        cprint("       '::. .'     ",'yellow',attrs=['bold']) 
        cprint("         ) (       ",'yellow',attrs=['bold']) 
        cprint("       _.' '._     ",'yellow',attrs=['bold']) 
        cprint("      `\"\"\"\"\"\"\"`	   ",'yellow',attrs=['bold']) 