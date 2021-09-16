import time
import pgzero

sonic = Actor('sonic-stop')
sonic.topright = 0, 10

TITLE = "Aero Sonic Catcher/Catch Sonic if you can! [Sonic] 'Catch me if you can!'"

WIDTH = 1000
HEIGHT = sonic.height + 50

def draw():
    screen.clear()
    sonic.draw()
    
    
def set_sonic_normal():
    sonic.image = 'sonic-stop'
    
def update():
    sonic.left += 2
    if sonic.left > WIDTH:
        sonic.right = 0
    
    
def on_mouse_down(pos):
    if sonic.collidepoint(pos):
        print("OOF!")
        sonic.image = 'sonic-agachado-direita'
        sounds.oof.play()
        clock.schedule_unique(set_sonic_normal, 1)
    else:
        print("You missed me!")
        sounds.you_missed_me.play()
        
       