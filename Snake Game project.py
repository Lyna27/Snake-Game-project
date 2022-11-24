import pygame 
import random 
import tkinter 
from tkinter import* # importer tout, pour eviter de mettre a chaque fois tkinter. "comme tkinter.Tk()"


window =Tk()      #creation de la fenetre 
window.title("Snake Game")   #donner un titre 
window.resizable(False,False) # pour ne pas pouvoir redimensionner 

# définir les constantes 

GAME_WIDTH=1000 # largeur 
GAME_HEIGHT=500 #hauteur 
SPEED=100 # plus le nombre est petit plus le jeu sera rapide
SPACE_SIZE = 50 # taille du serpent+ food
BODY_PARTS = 3 # how many parts does our snake have at the begining of the game
SNAKE_COLOR = "#00FF00" # vert
FOOD_COLOR = "#FF0000" # rouge
BACKGROUND_COLOR = "#000000" # noir

class Snake : 
	def __init__(self):
		self.body_size = BODY_PARTS 
		self.coordinates = []
		self.squares = []

		for i in range(0,BODY_PARTS): #
			self.coordinates.append([0,0]) # pour prendre les coordonnées les premieres cases du serpent

		for x,y in self.coordinates: #a chaque fosi que la tete touche la boule rouge une autre boule apparait
			square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
			self.squares.append(square) # pour ajouter une case verte 



class Food :
	def __init__(self):

		x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE)-1)*SPACE_SIZE # expliquer ce calcul ?
		y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE)-1)*SPACE_SIZE # combien de pixels en hauteur ?
	
		self.coordinates = [x , y] 
		canvas.create_oval( x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill= FOOD_COLOR, tag="food") # sans tag food, plusieurs boules rouges




def next_turn(snake,food):

	x, y = snake.coordinates[0] # the head of the snake
# pour permettre au serpent de bouger 
	if direction == "up":
		y -= SPACE_SIZE 
	elif direction == "down":
		y += SPACE_SIZE 
	elif direction == "left":
		x -= SPACE_SIZE
	elif direction == "right":
		x += SPACE_SIZE

	snake.coordinates.insert(0, (x, y))# ça devient les nouvelles coordonnées

	square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR) #créer une nouvelle case quand le serpent grandi

	snake.squares.insert(0, square) #juste inséré le nouveau carré 


	if x == food.coordinates[0] and y == food.coordinates[1]: # 
		global score

		score += 1

		label.config(text="Score:{}".format(score))

		canvas.delete("food")

		food = Food()

	else:
		del snake.coordinates[-1]

		canvas.delete(snake.squares[-1])

		del snake.squares[-1]

	if check_collision(snake):
		game_over()

	else:
		window.after(SPEED, next_turn, snake, food) # le temps 


def change_direction(new_direction):

	global direction # old direction

	if new_direction == 'left':
		if direction != 'right': 
			direction = new_direction

	elif new_direction == 'right':
		if direction != 'left':
			direction = new_direction

	elif new_direction == 'up':
		if direction != 'down':
			direction = new_direction

	elif new_direction == 'down':
		if direction != 'up':
			direction = new_direction


def check_collision(snake):
	
	x, y = snake.coordinates[0]

	if x < 0 or x>= GAME_WIDTH:
		print("GAME OVER")
		return True
	elif y < 0 or y>= GAME_HEIGHT:
		print("GAME OVER")
		return True

	for body_part in snake.coordinates[1:]:
		if x == body_part[0] and y == body_part[1]:
			print("GAME OVER")
			return True

	return False


def game_over():
	canvas.delete(ALL) # effacer tout ce qu'il y avait
	canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
		font = ('consolas',70,"italic"), text = "GAME OVER", fill = "red", tag = "gameover")

#initialisations
score = 0
direction = "down"


label = Label(window, text="Score:{}".format(score), font=("Times", 24,"bold italic")) 
		# Label est un widget pour créer la zone de texte dans une seule police
													# font = Police de caractere 
label.pack(side=BOTTOM) # pour deplacer le widget en bas 

canvas = Canvas(window, bg = BACKGROUND_COLOR, height = GAME_HEIGHT, width = GAME_WIDTH)
		# Canvas est un widget pour créer une surface rectangulaire
canvas.pack() # pack method pour afficher the canva

window.update() # fonction pour mettre a jour la fenetre

# récuperer la resolutions de l'ecran en pixels "screen"

screen_width = window.winfo_screenwidth() # nbr de pixels affichés en largeur de l'ecran
screen_height = window.winfo_screenheight() # nbr de pixels affichés en hauteur de l'ecran

window_width = window.winfo_width()  # nbr de pixels sur la largeur de la fenetre
window_height = window.winfo_height() # nbr de pixels sur la hauteur de la fenetre


#CENTRER LA FENETRE position

x = int((screen_width/2) - (window_width/2))     #largeur de l'ecan/2 - largeur de la fenetre/2
y = int((screen_height/2) - (window_height/2))   # hauteur de l'ecran/2 - hauteur de la  fenetre /2

window.geometry(f"{window_width}x{window_height}+{x}+{y}")    # pour fixer la taille

window.bind('<Left>', lambda event: change_direction('left') ) # bind method pour lier le bouton du clavier a l'action "event"
window.bind('<Down>', lambda event: change_direction('down') ) # de changer de direction, lambda ??
window.bind('<Right>', lambda event: change_direction('right') )
window.bind('<Up>', lambda event: change_direction('up') )


# Appel des classes 
snake = Snake() 
food = Food()

# Appel de la fonction
next_turn(snake,food)

window.mainloop() # boucle infinie, pour garder la fenetre ouverte jusqu'a ce que l'utilisateur quitte le programme 
