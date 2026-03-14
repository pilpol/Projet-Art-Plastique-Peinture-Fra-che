# / ___/ _ \|  _ \| ____| |  _ \| ____|         
#| |  | | | | | | |  _|   | | | |  _|           
#| |__| |_| | |_| | |___  | |_| | |___             l'art ascii de fouuu wowww trop beauuu
# \____\___/|____/|_____|_|____/|_____|_  _____ 
#|  _ \| ____|_ _| \ | |_   _| | | |  _ \| ____|
#| |_) |  _|  | ||  \| | | | | | | | |_) |  _|  
#|  __/| |___ | || |\  | | | | |_| |  _ <| |___ 
#|_|___|_____|___|_| \_|_|_|__\___/|_|_\_\_____|
#|  ___|  _ \    / \  |_ _/ ___| | | | ____|    
#| |_  | |_) |  / _ \  | | |   | |_| |  _|      
#|  _| |  _ <  / ___ \ | | |___|  _  | |___     
#|_|   |_| \_\/_/   \_\___\____|_| |_|_____|    


import os
import time
import secrets
from datetime import datetime
import math

# === CONFIG RAHHH BOBOBOBOBO JDEVIENS FOUUUUU  ===
message_base = ["Peinture", "Coup de pinceau"]
messages_weird = ["Vous regardez encore ?", "Est-ce vraiment de l'art ?", "Pourquoi ?", "Peinture fraîche"]
glitch_chars = "!@#$%^&*<>?\\/|~"
eye_ascii = [
"        _____        ",
"     .-`     `-.     ",
"   .'           `.   ",
"  /   .       .   \\ ",
" |                  | ",
" |                  | ",
"  \\     _____      / ",
"   `.           .'  ",
"     `-._____.-'    "]


# Terminal assez gros et infos de base avec OS (Windows psk personne utilise linux ni mac os booohhh vive windows [je hais windows et je suis obligé de faire ça pour que ça marche chez les gens qui utilisent windows mais bon c'est pas grave hein])
os.system("mode con: cols=200 lines=60")
os.system("title Peinture Fraîche - Pierre-Louis Corbin")
os.system("cls")

reset = "\033[0m"

# === FONCTIONS BOBOBOBOBOBOBO MAGNIFIQUEEEEEE  ===
def vortex_eye():
    size = os.get_terminal_size()
    center_row = size.lines // 2
    center_col = size.columns // 2

    # spirale
    for t in range(60):
        angle = t * 0.3
        radius = t * 0.25

        row = int(center_row + math.sin(angle) * radius)
        col = int(center_col + math.cos(angle) * radius * 2)

        if 1 <= row <= size.lines:
            print(f"\033[{row};{col}H{random_rgb()}◉{reset}", end="", flush=True)

        time.sleep(0.01)

    # apparition de l'œil
    start_row = center_row - len(eye_ascii)//2
    start_col = center_col - len(eye_ascii[0])//2

    for i, line in enumerate(eye_ascii):
        print(f"\033[{start_row+i};{start_col}H{random_rgb()}{line}{reset}", end="", flush=True)

def vortex():
    size = os.get_terminal_size()
    center_row = size.lines // 2
    center_col = size.columns // 2

    text = secrets.choice(messages_weird)

    for t in range(80):
        angle = t * 0.3
        radius = t * 0.25

        row = int(center_row + math.sin(angle) * radius)
        col = int(center_col + math.cos(angle) * radius * 2)

        # évite de sortir de l'écran
        if 1 <= row <= size.lines and 1 <= col <= size.columns - len(text):
            print(f"\033[{row};{col}H{random_rgb()}{text}{reset}", end="", flush=True)

        time.sleep(0.01)

def random_rgb():
    r = secrets.randbelow(256)
    g = secrets.randbelow(256)
    b = secrets.randbelow(256)
    return f"\033[38;2;{r};{g};{b}m"

def random_position():
    size = os.get_terminal_size()
    row = secrets.randbelow(size.lines) + 1
    col = secrets.randbelow(max(1, size.columns - 40)) + 1
    return row, col

def mutate(msg):
    if len(msg) == 0: return msg
    index = secrets.randbelow(len(msg))
    c = chr(secrets.randbelow(94)+33)
    return msg[:index] + c + msg[index+1:]

def chaotic_delay():
    x = secrets.randbelow(1000)/1000
    r = 3.99
    for _ in range(5):
        x = r * x * (1-x)
    return x * 3  #  vitesse ajustable mais pas trop rapide sinon c'est illisible et pas trop lent sinon c'est annooooyingggg asf

# JSAIS MEME PAS CE QUE CA FAITTT MDMDDMRMRRRR 
print("\033[2J\033[?25l")

# === BOUCLE PRINCIPALE POUR LE TEXTEEEEE RAHAHAHA ===
while True:
    now = datetime.now().strftime("%H:%M:%S")

    # vortex rare je sais même pas si il marche ?
    if secrets.randbelow(500) == 0:
        vortex()

    # vortex œil très rare donc encore plus rare que le vortex normal et je sais même pas si il marche non plus mdrrr
    if secrets.randbelow(800) == 0:
        vortex_eye()

    # NORMAL OU PAS NORMAL LE TEXTE ?
    if secrets.randbelow(10) == 0:
        msg = secrets.choice(messages_weird)
    else:
        msg = secrets.choice(message_base)
        if secrets.randbelow(4) == 0:
            msg = mutate(msg)

    # couleurs du texte pour faire comme de la peinture
    color = random_rgb()

    # position du texte
    row, col = random_position()

    # apparition bizarre 
    glitch = ""
    if secrets.randbelow(3) == 0:
        for _ in range(secrets.randbelow(5)+1):
            glitch += secrets.choice(glitch_chars)

    # affichage de je sais pas quoi 
    print(f"\033[{row};{col}H{color}{msg}{glitch} — {now}{reset}", end="", flush=True)

    # apparition flash (fantôme) (rapide) (flash) jsp comment dire mais personne fouille dans le code source donc j'ai rien a me reprocher a faire des commentaires... hein ? vous regardez pas le code source ?
    if secrets.randbelow(5) == 0:
        time.sleep(secrets.randbelow(2)/10)  # 0.0 à 0.2 sec
    else:
        time.sleep(chaotic_delay())

#Bon programme je crois ? j'ai pris du temps pour faire le code j'avais jamais utilisé python comme ça, j'ai l'impression de l'avoir poussé a bout xD
#imagine utilier les commentaires pour organiser le code et parler comme si c'etait un journal intime mdrrr j'aime bien faire ça
#les messages sont pas pour vous. Ils sont même pas pour moi. 
# "this is not for you" - Mark Z. Danielewski, La Maison des feuilles. J'adore ce livre
#                                               .--.
#                                               `.  \
#                                                 \  \
#                                                  .  \
#                                                  :   .
#                                joli chat hein ?  |    .
#                                                  |    :
#                                                  |    |
#  ..._  ___                                       |    |
# `."".`''''""--..___                              |    |
# ,-\  \             ""-...__         _____________/    |
# / ` " '                    `""""""""                  .
# \                                                      L
# (>                                                      \
#/                                                         \
#\_    ___..---.                                            L
#  `--'         '.                                           \
#                 .                                           \_
#                _/`.                                           `.._
#             .'     -.                                             `.
#            /     __.-Y     /''''''-...___,...--------.._            |
#           /   _."    |    /                ' .      \   '---..._    |
#          /   /      /    /                _,. '    ,/           |   |
#          \_,'     _.'   /              /''     _,-'            _|   |
#                  '     /               `-----''               /     |
#                  `...-'                                       `...-'
