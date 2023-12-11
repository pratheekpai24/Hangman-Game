import os
import random
import sys
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def cls():
    os.system('cls')
cls()
l = 6
ww = "The word was = "
wl = ["apple", "banana", "orange", "grape", "kiwi", "melon", "strawberry", "blueberry",
    "peach", "plum", "pear", "cherry", "mango", "pineapple", "lemon", "lime",
    "carrot", "broccoli", "potato", "cucumber", "tomato", "lettuce", "spinach", "onion",
    "pepper", "garlic", "ginger", "cinnamon", "nutmeg", "vanilla", "chocolate", "coffee",
    "tea", "milk", "water", "juice", "soda", "wine", "beer", "whiskey", "vodka",
    "rum", "gin", "brandy", "cognac", "martini", "margarita", "mojito", "cosmopolitan",
    "sushi", "pizza", "pasta", "burger", "sandwich", "salad", "soup", "curry",
    "taco", "burrito", "nachos", "quesadilla", "salsa", "guacamole", "chips", "pretzel",
    "cookie", "cake", "pie", "brownie", "icecream", "candy", "popcorn", "marshmallow",
    "guitar", "piano", "violin", "trumpet", "drums", "flute", "saxophone", "clarinet",
    "bicycle", "car", "bus", "train", "airplane", "boat", "subway", "helicopter",
    "computer", "phone", "tablet", "keyboard", "mouse", "monitor", "printer", "scanner",
    "camera", "speaker", "headphones", "microphone", "clock", "watch", "calendar", "notebook",
    "pencil", "pen", "brush", "canvas", "easel", "sculpture", "statue", "painting",
    "novel", "poetry", "essay", "magazine", "newspaper", "journal", "diary", "blog",
    "movie", "music", "dance", "theater", "play", "opera", "concert", "festival",
    "beach", "mountain", "forest", "river", "lake", "desert", "canyon", "island",
    "city", "village", "market", "park", "zoo", "museum", "library", "school",
    "college", "university", "office", "hospital", "restaurant", "cafe", "bar", "club",
    "hotel", "motel", "apartment", "house", "home", "room", "bedroom", "bathroom",
    "kitchen", "livingroom", "diningroom", "garden", "garage", "balcony", "patio", "terrace"]
wd = random.choice(wl)
word = "Word = "
wlen = len(wd)
blk=[]
for i in range(0,wlen):
    blk.append('_')
wdo = []
for i in wd:
   wdo.append(i)
print(r'''  _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                      ''')
print(r''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :    
. .          `'       . .
''')
while blk!=wdo:
    print("\n\n-----------------------")
    ui = input("Guess the right word = ").lower()
    b = 0 
    x = 0
    se = 0
    for i in wd:
     if i == ui:
        x+=1
        if blk[b] == i:
           se+=1
        blk[b] = i
     b+=1

    if se>0:
       print(f'You have already guessed "{ui}", try guessing other words!!') 
    if x==0:
       l-=1
       print(f"{ui} is not in the word")
       print(stages[l])
       if l == 0:
          print(ww,end=" ")
          for f in wdo:
             print(f,end=" ")
          print("\nYou Loose")
          input("Press enter to exit")
          sys.exit(0)
    print(word,end=" ")
    for a in blk:
        print(a,end=" ")
print("\n\nYou win")
input("Press enter to exit")


        