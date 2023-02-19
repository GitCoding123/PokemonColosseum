import random
import Pokemon as pkmn
import colors as clr
import sys
import time
import MovesData as md
from pygame import mixer


def printPokemon():
   print(clr.Colors.YELLOWRAPIDBLINK + r"""
                                  ,'\ 
    _.----.        ____         ,'  _\   ___    ___     ____ 
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`. 
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  | 
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  | 
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  | 
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     | 
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    | 
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   | 
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   | 
        \_.-'       |__|    `-._ |              '-.|     '-.| |   | 
                                `'                            '-._| 
    """)
def printColosseum():
    fasttitleprint(clr.Colors.RED + r"""
                  .__   
      _____  ____ |  |   ____  ______ ______ ____  __ __  _____ 
     /  ___\/  _ \|  |  /  _ \/  ___//  ___// __ \|  |  \/     \ 
     \  \__(  <_> )  |_(  <_> )___ \ \___ \\  ___/|  |  /  Y Y  \ 
      \___  >____/|____/\____/____  >____  >\___  >____/|__|_|  / 
          \/                      \/     \/     \/            \/   
    """ + clr.Colors.RESET)

def print_thanks():
    fasttitleprint(clr.Colors.WHITERAPIDBLINK + r"""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⡀⠀⢄⠈⢙⢒⠲⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠶⠚⠃⢣⠀⠸⣶⠋⢈⠇⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⠤⢄⡀⠀⠀⢀⣤⣶⢖⣿⣏⡷⠰⠞⠉⠉⢺⣇⠀⢹⠀⢸⡀⠋⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⠤⠶⣚⣋⡅⠀⠀⠙⣻⡟⠋⡔⠛⠉⠁⠙⣷⠀⠰⣿⡄⠀⢻⡆⠀⢧⠀⠙⢦⠀⡿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣯⡵⠛⠛⠉⠈⣷⠀⠘⠉⠀⠙⢦⡀⠀⣾⣆⠀⢻⣇⠀⢳⣳⡀⠘⣷⣀⣨⠙⢲⣒⣤⢣⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡿⡇⢴⠀⠀⣿⠈⣇⠀⢸⣣⡀⠘⣧⡀⠙⠿⠀⠈⣿⣄⣸⡏⢻⣾⣥⢨⣿⣿⠿⠛⠛⠉⠀⠀⣀⣤⣤⠤⠤⣒⡲⠤⠤⣤⣤⣤⣤⣀⡀⢧⡀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⠻⡆⢧⠀⠹⡄⢹⡄⠘⢏⢧⠀⢸⡷⣤⣤⣶⣚⠋⢸⠛⢳⣿⡅⠘⢇⢷⣿⠀⠀⣤⢔⣻⡯⠶⠛⠛⠋⠉⠉⠉⠉⣉⣉⣛⡛⠓⢲⣬⡝⣷⣤⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢿⡘⡆⠀⢻⠀⢳⣄⣼⠛⢳⣾⢥⣴⠛⠉⠁⠉⢻⡄⠈⢣⢣⠀⠸⡎⠈⣧⣯⡾⠋⠁⠀⣠⣤⣴⣾⣿⣿⣿⣿⠿⢛⣭⣴⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢧⡛⠀⠚⢰⣿⣿⠛⠳⣼⡇⠀⣿⠀⠘⣟⡄⠈⢳⡀⠘⠿⠃⢠⡇⣠⣿⠛⢀⣤⣾⣿⣿⣿⣿⣿⡿⠟⣫⣤⣞⡯⠚⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠛⠪⠖⢻⣝⣦⠀⠘⠇⠀⡟⣦⠀⠛⠿⠀⡼⠓⡦⠤⠴⣫⣤⣿⡁⣠⣿⣿⣿⣿⣿⡿⢿⣡⡴⣿⡭⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢎⠳⡄⠀⠀⡇⢈⣓⣦⡴⢛⡥⣺⡿⠿⢿⣿⣿⠁⣵⣿⣿⣿⡿⠟⣡⣴⣿⣳⣛⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠤⠒⢦⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠈⠆⠀⡧⢸⣿⠛⠛⠛⠛⠁⠀⣠⣾⣿⠃⣼⣿⣿⣿⢋⣴⠞⠋⠀⠴⠿⠿⣿⣯⣹⣀⣀⣀⡀⠀⠀⠀⠀⠀⣘⣦⣤⣀⠈⠑⢦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⣴⣃⡬⣿⣁⡀⠀⠀⠀⣼⣿⢿⡇⡴⠋⠀⣻⡿⠛⠁⠀⠀⠀⠀⠀⠀⠉⢙⣶⡿⠿⠿⠭⣍⣒⣶⢤⣀⣏⣀⠉⠓⣝⡄⠈⢧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢷⡿⠋⢉⣿⠀⢀⣞⡿⠃⠸⠃⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢦⣤⣀⣀⡀⠈⠉⠳⢮⣝⠯⣶⡀⠈⣿⠦⠼⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣰⡟⠀⣰⡿⠋⢹⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣿⣿⣿⣿⣷⣶⣄⡀⠉⠳⣝⢿⡉⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣽⣿⣿⣏⣿⠀⠀⣿⠁⢠⣿⢻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣝⠿⣿⣿⣿⣿⣿⣿⣷⣄⠘⢷⣙⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⡿⠞⠉⠸⢏⣾⡟⠉⢷⡀⣿⣦⣼⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⣶⣌⡙⠿⣿⣿⣿⣿⣿⣷⣄⠻⣍⢦⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⡿⠋⠀⠀⠀⠀⢸⣿⡇⠀⠈⢉⣿⢿⣿⣫⣿⠀⠀⠀⠀⠀⣀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣱⠁⠙⠯⢿⡶⣤⣉⡻⠿⣿⣿⣿⣦⠙⣮⢦⠀⠀⠀                   ⠀  ⠀⠀⢠⣶⠀⠀⠀
⠀⠀⠀⣴⣿⠟⠀⠀⠀⠀⠀⠀⠘⣟⣇⣀⣶⡯⠟⠋⠉⠀⢹⣆⠀⠀⠀⠀⠻⣦⣄⣀⣤⡶⠀⠀⠀⠀⠀⢐⠶⢀⣴⣿⠁⠀⠀⠀⠀⠉⠙⠯⢽⣷⡶⣍⣙⠻⣷⠈⢯⣣⡀⠀             ⠀  ⠀⠀ ⠀⠀ ⠀⢰⠛⢿⠀⠀⠀
⠀⠀⡼⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠹⣾⣿⣋⠀⠀⠀⠀⠀⠀⢻⣆⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⢀⣀⠀⠘⠷⠛⣿⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠻⢿⣶⣤⣜⢯⣣⡀                  ⠀ ⠀⠀⠀⡏⠀⢸⠀⠀
⠀⢸⣿⠃⢰⠀⣀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠖⠀⠀⠀⠀⠀⠀⠀⢹⣷⣤⡀⠀⠀⠀⠀⣷⣄⣀⣀⣈⡉⣀⡀⠀⢠⡿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣟⠇⠇                   ⠀ ⠀⣰⠃⠀⠼⣄⡀⠀
⢀⣿⡟⠀⠀⠀⣿⠀⢰⣇⠀⡴⠂⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⠉⠛⠶⣤⣤⡀⠀⠉⠉⠁⠈⠙⢋⣠⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁             ⠀⡴⠋⠳⣄⠀⠀⢀⢎⣔⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀
⢸⣿⡇⠀⠀⠀⠻⣄⣸⠙⢦⡀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠛⠛⠛⢿⣷⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀            ⢠⠞⠁⠀⠀⠀⠹⣶⢛⠘⡋⠀⢠⣎⣦⠀⠀⠈⠙⠲⢤⡀⠀
⢸⣿⡇⠀⠀⠀⠀⠙⠋⠀⠀⠹⠀⠀⢸⡿⣦⠀⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀           ⣰⠏⠀⠀⠀⠀⠀⠀⢰⠀⠰⡤⡀⠀⢛⣋⠀⠀⠰⣄⣀⣠⣿⣆
⠸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠈⢷⣄⢀⣄⢰⣷⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀            ⠛⠒⠶⠶⢶⡶⠄⢀⣨⢦⡀⠢⠃⠀⠸⣿⠇⠀⢰⠃⠉⠉⠉⠉⠉
⠀⢹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⠀⠙⠟⣿⣿⠻⣿⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀            ⠀⠀ ⠀⠰⠿⣤⣀⠛⢧⣌⡇⠀⠀⠀⠀⠀⠰⠉⠙⢳⠀⠀⠀
⠀⠀⢷⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠲⣿⠀⠉⠹⣿⣦⠀⠀⠀⠀⠀⠀⢀⡀⢀⣰⣷⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                 ⠀⠀⣼⣣⣞⣽⣇⠀⠈⠑⢄⠀⠐⢄⣀⣸⠀⠀
⠀⠀⠀⠙⢟⣷⣄⡀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⢹⣇⠀⠀⠈⢙⣿⣷⡀⠀⢀⣴⣿⣴⣟⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀           ⠀⠀⠀  ⠀⠀⠈⠛⣿⣿⠁⠉⠠⡀⠀⠀⡆⠀⠀⠀⢹⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠿⢟⣶⣤⣄⣀⣀⣀⣨⣿⣦⣀⣀⣀⣀⣀⣿⡄⠀⠀⠈⠉⣿⣿⡶⠛⠉⠀⣾⡝⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀             ⠀⠀⠹⡿⠇⠀⠀⢈⠁⠊⠀⠀⠀⠀⠈⣇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠒⠚⠛⠓⠊⠉⠿⣿⣿⡋⢹⡁⣸⢷⡄⠀⠀⠀⠸⣆⣀⠀⠀⣾⣽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       ⠀⠀           ⠀⣧⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠯⠭⠭⠭⢽⣿⣦⡀⠰⣄⢺⣿⣆⣾⣽⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀          ⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⣸⠗⠀⣀⣦⣀⣤⣤⠴⠾⣄⡀⠺⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠚⠛⠲⣻⣛⣿⡿⣿⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀          ⠀    ⠀⠀⠀⠀ ⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀
    """)


# Function to write characters to a line with a time delay
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./4)

def fasttitleprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./500)

def midprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./18)


def get_names():
    names = ["Rocket"]
    midprint("Please Enter Player Name: ")
    player_name = input("$> ")
    mixer.music.stop()
    while True:
        if player_name == "Rocket":
            midprint(
                clr.Colors.BRIGHTRED + f"Team {player_name}" + clr.Colors.RESET + " is the enemy team. Please choose a different name.")
            midprint("Please Enter Player Name: ")
            player_name = input("$> ")
            continue
        else:
            names.append(player_name)
            break
    return names

def determine_starter(names, player_name):
    starter = random.choice(names)
    if starter != "Rocket":
        midprint(f"Coin toss goes to " + clr.Colors.BRIGHTGREEN + f"Team {player_name} " + clr.Colors.RESET + "to start the attack!\n")
        time.sleep(1)
    else:
        midprint(f"Coin toss goes to " + clr.Colors.BRIGHTRED + f"Team Rocket" + clr.Colors.RESET + " to start the attack!\n")
        time.sleep(1)
    return starter

def enter_battle(player_q, rocket_q, player_name):
    midprint(
        f"\nTeam Rocket enters with {rocket_q[0].get_name()}, {rocket_q[1].get_name()}, and {rocket_q[2].get_name()}\n")
    time.sleep(0.75)
    midprint(
        f"Team {player_name} enters with {player_q[0].get_name()}, {player_q[1].get_name()}, and {player_q[2].get_name()}\n")
    time.sleep(0.75)
    midprint(
        f"{rocketQueue[0].get_name()} for Team Rocket and {playerQueue[0].get_name()} for Team {player_name} have entered battle!\n")
    time.sleep(1)

    mixer.music.load("Battle! (Trainer Battle).wav")
    mixer.music.play()
    midprint("Let the battle begin!")
    slowprint(".\n.\n.")
    time.sleep(1)

def print_battle_visual(player_poke, rocket_poke, player_name):
    print("+" + clr.Colors.CROSSED + "                                      " + clr.Colors.RESET + "+")
    print("|                        " + clr.Colors.BRIGHTREDBOLDUNDERLINE + "Team Rocket" + clr.Colors.RESET + "   |")
    print(f"|                         {rocket_poke.get_name():<13}|")
    print(f"|                         HP: {rocket_poke.get_HP():<9}|")
    print("|-----------------vs.------------------|")
    print("|   " + clr.Colors.BRIGHTGREENBOLDUNDERLINE + f"Team {player_name}" + clr.Colors.RESET + "                         |")
    print(f"|    {player_poke.get_name():<34}|")
    print(f"|    HP: {player_poke.get_HP():<30}|")
    print("+" + clr.Colors.CROSSED + "                                      " + clr.Colors.RESET + "+")

def rocket_battle_sequence():
    print("hi")

def player_battle_sequence():
    print("hi")

def get_damage():
    """Damage(M,A,B) = P(M) * (A(A)/D(B)) * STAB * TE(M,B) * Random"""

# Function to print move option for Magikarp
def mag_moves(m1):
    print("1. " + m1 + "\n")

# Function to print move options for all pokemon except Magikarp
def player_moves(m1, m2, m3, m4, m5, c_list):
        if c_list.__len__() == 5:
            print("1. " + m1 + "\n2. " + m2 + "\n3. " + m3 + "\n4. " + m4 + "\n5. " + m5 + "\n")
        else:
            if 1 not in c_list:
                print("1. " + m1 + " (N/A)\n2. " + m2 + "\n3. " + m3 + "\n4. " + m4 + "\n5. " + m5 + "\n")
            elif 2 not in c_list:
                print("1. " + m1 + "\n2. " + m2 + " (N/A)\n3. " + m3 + "\n4. " + m4 + "\n5. " + m5 + "\n")
            elif 3 not in c_list:
                print("1. " + m1 + "\n2. " + m2 + "\n3. " + m3 + " (N/A)\n4. " + m4 + "\n5. " + m5 + "\n")
            elif 4 not in c_list:
                print("1. " + m1 + "\n2. " + m2 + "\n3. " + m3 + "\n4. " + m4 + " (N/A)\n5. " + m5 + "\n")
            else:
                print("1. " + m1 + "\n2. " + m2 + "\n3. " + m3 + "\n4. " + m4 + "\n5. " + m5 + " (N/A)\n")



midprint("\nWelcome to...\n\n")
time.sleep(1)
mixer.init()
mixer.music.load("Obtained a Badge!.wav")
mixer.music.play()
printPokemon()
time.sleep(1)
printColosseum()
time.sleep(1)

# Open the moves file to create moveData objects
moveInfo = []
file1 = 'moves-data.csv'
with open(file1) as f_object:
    next(f_object)
    for line in f_object:
        info = line.split(',')
        moves_data = md.MovesData(info[0], info[1], info[2], info[3], info[4], info[5], info[6])
        moveInfo.append(moves_data)
        #print(moves_data.name)

pokeQueue = []
file2 = 'pokemon-data.csv'
with open(file2) as file_object:
    next(file_object)
    for line in file_object:
        strip1 = line.replace('"', '').replace('[', '').replace("'", "").replace(']', '').replace('\n', '')
        info = strip1.split(',')

        if info.__len__() == 8:
            moves = [info[7]]
            pokemon = pkmn.Pokemon(info[0], info[1], info[2], info[3], info[4], info[5], info[6], moves)
            pokeQueue.append(pokemon)
        else:
            moves = [info[7], info[8], info[9], info[10], info[11]]
            pokemon = pkmn.Pokemon(info[0], info[1], info[2], info[3], info[4], info[5], info[6], moves)
            pokeQueue.append(pokemon)


# Generate 3 random pokemon for each team
r_queue = random.sample(pokeQueue, 6)
playerQueue = []
rocketQueue = []
for i in range(3):
    playerQueue.append(r_queue.pop(0))
    rocketQueue.append(r_queue.pop(0))

names = get_names()
starter = determine_starter(names, names[1])
enter_battle(playerQueue, rocketQueue, names[1])

s = 0
if starter == "Rocket":
    s = 1
print_battle_visual(playerQueue[0], rocketQueue[0], names[1])
# while True:
#     print_battle_visual(playerQueue[0], rocketQueue[0], names[1])
#     if s == 1:
#         rocket_battle_sequence()
#         s = 0
#     else:
#         player_battle_sequence()
#         s = 1

print_thanks()
a = input("end? (y/n)\n$> ")