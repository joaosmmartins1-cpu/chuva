import sys
import time
from rich import print
from playsound3 import playsound
playsound("leu-chuva-1-119168.mp3",block=False)
def print_terminal(texto, usuario="zangets", delay=0.07):

    prompt = f"[purple4]{usuario}[/]: "
    print(prompt, end="", flush=True)
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(delay)
    print()

print_terminal("ichigo...")
time.sleep(1)
print_terminal("voce sabe como eu odeio a chuva.")
time.sleep(1)
print_terminal("e chove neste mundo tambem.")
time.sleep(1)
print_terminal("se o seu coração tiver problemas...")
time.sleep(1)
print_terminal("o ceu ficara nublado.")
time.sleep(1)
print_terminal("se voce sofrer...")
time.sleep(1)
print_terminal("sempre chovera muito facilmente.")
time.sleep(1)
print_terminal("eu me pergunto se voce pode entender")
time.sleep(1)
print_terminal("o medo da chuva deste mundo solitario.")
time.sleep(1)