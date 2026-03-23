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
#|_|   |_| \\/_/   \_\___\____|_| |_|_____|    


import os
import time
import secrets
import sys
from datetime import datetime
import math
import platform

# === CONFIG RAHHH BOBOBOBOBO JDEVIENS FOUUUUU  ===
message_base = ["Peinture", "Coup de pinceau", "Peinture fraîche"]
messages_weird = ["Vous regardez encore ?", "Est-ce vraiment de l'art ?", "Pourquoi ?"]
glitch_chars = "!@#$%^&*<>?\/|~"
eye_ascii = [
"        _____        ",
"     .-`     `-.     ",
"   .'           `.   ",
"  /   .       .   \ ",
" |                  | ",
" |                  | ",
"  \     _____      / ",
"   `.           .'  ",
"     `-._____.-'    "]


# === INIT TERMINAL (cross-platform) ===
def init_terminal():
    """Initialize terminal for all platforms"""
    try:
        if platform.system() == "Windows":
            os.system("mode con: cols=200 lines=60")
            os.system("title Peinture Fraîche - Pierre-Louis Corbin")
            os.system("cls")
        else:
            # Linux et macOS
            os.system("clear")
            print("\033]0;Peinture Fraîche - Pierre-Louis Corbin\007", end="", flush=True)
    except Exception as e:
        print(f"Erreur lors de l'initialisation du terminal: {e}")

init_terminal()

reset = "\033[0m"

# === FONCTIONS BOBOBOBOBOBOBO MAGNIFIQUEEEEEE  ===
def clamp(value, min_val, max_val):
    """Clamp a value between min and max"""
    return max(min_val, min(max_val, value))

def vortex_eye():
    try:
        size = os.get_terminal_size()
        center_row = size.lines // 2
        center_col = size.columns // 2

        # spirale trop har
        for t in range(60):
            angle = t * 0.3
            radius = t * 0.25

            row = int(center_row + math.sin(angle) * radius)
            col = int(center_col + math.cos(angle) * radius * 2)

            # Vérification des limites
            if 1 <= row <= size.lines and 1 <= col <= size.columns:
                print(f"\033[{row};{col}H{{random_rgb()}}◉{{reset}}", end="", flush=True)

            time.sleep(0.01)

        # apparition du visage que j'ai appelé oeil ????? tf ?
        start_row = clamp(center_row - len(eye_ascii)//2, 1, size.lines - len(eye_ascii))
        start_col = clamp(center_col - len(eye_ascii[0])//2, 1, size.columns - len(eye_ascii[0]))

        for i, line in enumerate(eye_ascii):
            if start_row + i <= size.lines:
                print(f"\033[{start_row+i};{start_col}H{{random_rgb()}}{{line}}{{reset}}", end="", flush=True)
    except Exception as e:
        pass  # Silently continue on error

def vortex():
    try:
        size = os.get_terminal_size()
        center_row = size.lines // 2
        center_col = size.columns // 2

        text = secrets.choice(messages_weird)

        for t in range(80):
            angle = t * 0.3
            radius = t * 0.25

            row = int(center_row + math.sin(angle) * radius)
            col = int(center_col + math.cos(angle) * radius * 2)

            # faire en sorte que le texte évite de sortir de l'écran
            if (1 <= row <= size.lines and 
                1 <= col <= size.columns - len(text)):
                print(f"\033[{row};{col}H{{random_rgb()}}{{text}}{{reset}}", end="", flush=True)

            time.sleep(0.01)
    except Exception as e:
        pass  # Silently continue on error

def random_rgb():
    r = secrets.randbelow(256)
    g = secrets.randbelow(256)
    b = secrets.randbelow(256)
    return f"\033[38;2;{{r}};{{g}};{{b}}m"

def random_position():
    try:
        size = os.get_terminal_size()
        row = secrets.randbelow(max(1, size.lines - 1)) + 1
        col = secrets.randbelow(max(1, size.columns - 40)) + 1
        return clamp(row, 1, size.lines), clamp(col, 1, size.columns - 40)
    except Exception:
        return 10, 10  # Fallback position

def mutate(msg):
    if len(msg) == 0: 
        return msg
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
try:
    while True:
        try:
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

            # décider la position du texte
            row, col = random_position()

            # les caracteres bizzares qui apparaissent dans les messages de temps en temps
            glitch = ""
            if secrets.randbelow(3) == 0:
                for _ in range(secrets.randbelow(5)+1):
                    glitch += secrets.choice(glitch_chars)

            # affichage de je sais pas quoi 
            print(f"\033[{row};{col}H{{color}}{{msg}}{{glitch}} — {{now}}{{reset}}", end="", flush=True)

            # apparition flash (fantôme) (rapide) (flash) jsp comment dire
            if secrets.randbelow(5) == 0:
                time.sleep(secrets.randbelow(2)/10)  # 0.0 à 0.2 sec
            else:
                time.sleep(chaotic_delay())
        except Exception:
            # Continue meme avc erreur
            time.sleep(0.1)
except KeyboardInterrupt:
    # ct,c pour enlever
    print("\033[?25h")  # Show cursor again
    print("\nPeinture finie.")
    sys.exit(0)
