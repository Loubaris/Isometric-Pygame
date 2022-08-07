import pygame
from time import sleep
from audioplayer import AudioPlayer
import random
import time
from threading import Thread
pygame.init()


pygame.display.set_caption("Dreamland Battles")

screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((1000, 600))
screen_rect = screen.get_rect()
display = pygame.Surface((300, 300))
display_rect = display.get_rect()
print(display_rect)

print("LANCEMENT DE DREAMLAND BATTLES")

# CHARGEMENT DES IMAGES

background = pygame.image.load("assets/images/menubg.png").convert()
background = pygame.transform.scale(background, (1000, 600))

transition = pygame.image.load("assets/images/transition.png").convert()
transition = pygame.transform.scale(transition, (1000, 605))

transitiondead = pygame.image.load("assets/images/transitiondead.png").convert()
transitiondead = pygame.transform.scale(transitiondead, (1000, 605))

transitionbutin = pygame.image.load("assets/images/transitionbutin.png").convert_alpha()
transitionbutin = pygame.transform.scale(transitionbutin, (1000, 605))

# MAIN MENU BUTTON 

mainmenubutton = pygame.image.load("assets/images/buttons/mainmenu.png").convert_alpha()
mainmenubutton = pygame.transform.scale(mainmenubutton, (130, 20))
mainmenubuttonhover = pygame.image.load("assets/images/buttons/mainmenuhover.png").convert_alpha()
mainmenubuttonhover = pygame.transform.scale(mainmenubuttonhover, (130, 20))


# SETTINGS BUTTON

settingsbutton = pygame.image.load("assets/images/buttons/settings.png").convert_alpha()
settingsbutton = pygame.transform.scale(settingsbutton, (100, 20))
settingsbuttonhover = pygame.image.load("assets/images/buttons/settingshover.png").convert_alpha()
settingsbuttonhover = pygame.transform.scale(settingsbuttonhover, (110, 20))

# TUTORIAL BUTTON

tutorialbutton = pygame.image.load("assets/images/buttons/tutorial.png").convert_alpha()
tutorialbutton = pygame.transform.scale(tutorialbutton, (100, 20))
tutorialbuttonhover = pygame.image.load("assets/images/buttons/tutorialhover.png").convert_alpha()
tutorialbuttonhover = pygame.transform.scale(tutorialbuttonhover, (110, 20))

# TUTORIAL BUTTON

playbutton = pygame.image.load("assets/images/buttons/play.png").convert_alpha()
playbutton = pygame.transform.scale(playbutton, (60, 15))
playbuttonhover = pygame.image.load("assets/images/buttons/playhover.png").convert_alpha()
playbuttonhover = pygame.transform.scale(playbuttonhover, (110, 20))


# SETTINGS PAGE


settingsbg = pygame.image.load("assets/images/settings/settingsbg.png").convert_alpha()
settingsbg = pygame.transform.scale(settingsbg, (1000, 605))
settingsbg.set_alpha(100)

sliderbar = pygame.image.load("assets/images/settings/sliderbar.png").convert_alpha()
sliderbar = pygame.transform.scale(sliderbar, (500, 15))


sliderset = pygame.image.load("assets/images/settings/sliderset.png").convert_alpha()
sliderset = pygame.transform.scale(sliderset, (22, 38))

toggle_on = pygame.image.load("assets/images/settings/toggle_on.png").convert_alpha()
toggle_on = pygame.transform.scale(toggle_on, (25, 42))

toggle_off = pygame.image.load("assets/images/settings/toggle_off.png").convert_alpha()
toggle_off = pygame.transform.scale(toggle_off, (25, 42))


descsettings = pygame.image.load("assets/images/settings/descsettings.png").convert_alpha()
descsettings = pygame.transform.scale(descsettings, (400, 300))


controlsettings = pygame.image.load("assets/images/settings/controls.png").convert_alpha()
controlsettings = pygame.transform.scale(controlsettings, (400, 300))


# JEU ------------------------

     # MAP


direction = pygame.image.load('assets/map/direction.png').convert_alpha()
direction.set_colorkey((0, 0, 0))
direction.set_alpha(200)

broke_block_img = pygame.image.load('assets/map/broke_block.png').convert()
broke_block_img.set_colorkey((0, 0, 0))

red_block_img = pygame.image.load('assets/map/red_block.png').convert()
red_block_img.set_colorkey((0, 0, 0))

blue_block_img = pygame.image.load('assets/map/blue_block.png').convert()
blue_block_img.set_colorkey((0, 0, 0))

tresor_block_img = pygame.image.load('assets/map/tresor_block.png').convert()
tresor_block_img.set_colorkey((0, 0, 0))

portal_img = pygame.image.load('assets/map/portal.png').convert_alpha()
portal_img.set_colorkey((0, 0, 0))


    # PERSONNAGE ------------------------------

perso_droite = pygame.image.load('assets/map/perso/perso_droite.png').convert_alpha()
perso_spin = pygame.image.load('assets/map/perso/spin/spin_0.png').convert_alpha()

spinimg = []
for i in range(23):
    spinimg.append(pygame.image.load('assets/map/perso/spin/spin_{}.png'.format(i)))
    # POUVOIR RECHARGE

powerimg = pygame.image.load('assets/map/perso/power.png').convert_alpha()
powerimg = pygame.transform.scale(powerimg, (55, 25))


# MONSTRES -------------------------
monstre_1_right = pygame.image.load('assets/map/monstre/1/monstre_1_right.png').convert_alpha()


boss_1_image = pygame.image.load('assets/map/monstre/boss_1.png').convert_alpha()
boss_2_image = pygame.image.load('assets/map/monstre/boss_2.png').convert_alpha()
boss_3_image = pygame.image.load('assets/map/monstre/boss_3.png').convert_alpha()
# LOGO

dreamland = pygame.image.load("assets/images/dreamland.png").convert_alpha()
dreamland = pygame.transform.scale(dreamland, (780, 160))

running = True

# CHARGEMENT DES SONS


mainmenusound = AudioPlayer("assets/sounds/menu.wav")

btnclick = AudioPlayer("assets/sounds/click.wav")

playbtnsound = AudioPlayer("assets/sounds/playbtn.mp3")

slidesound = AudioPlayer("assets/sounds/slide.wav")

onsound = AudioPlayer("assets/sounds/on.mp3")
offsound = AudioPlayer("assets/sounds/off.mp3")

# TEXTE
pygame.font.init()
font = pygame.font.Font('assets/zorque.otf', 12)

maintext = font.render('', False, (0, 240, 0))

# DATA

f = open("data/data.txt", "r")
data = f.read()
f.close()
soption1 = True
print(str(data))
if str(data) == "True":
    soption1 = True
    print("Activation coord")
else:
    soption1 = False
soption2 = False
soption3 = False



f = open('map.txt')
map_data = [[colonne for colonne in rang] for rang in f.read().split('\n')]
f.close()

f = open('arena_1.txt')
arena_data = [[colonne for colonne in rang] for rang in f.read().split('\n')]
f.close()

nuages = [[random.randint(0, 900), random.randint(0, 400)] for _ in range(15)]


nuage = pygame.image.load('assets/images/ingame/ambient/cloud.png').convert_alpha()
nuage = pygame.transform.scale(nuage, (40, 28))






# Initialisation des variables
menuone = 1
menutwo = 0
menutwoclickable = 0
mouvement = 0
mnbtnhover = 0
stsbtnhover = 0
tttbtnhover = 0
plybtnhover = 0

settingspage = 0
settingspagebackgroundoff = 0


animone = 0
mnmnx = -10
mnmny = 600
mntwobtn = -110
animbtntwo = 0
animbtnone = 0
transitiony = -605
transitiondeady = -605
transparencelogo = 0
transpaanim = 0
transpaanimtwo = 0

mouseclicked = 0

settingsbgy = -605
set1x = 489
set2x = 400
set3x = 581
setxpos = set1x
optionssettings = 1
slidechanged = 1


ingame = 0
startinggame = 0
enteringgame = 0
enteringgamelspart = 0
couche=14
# PERSONNAGE
mouvx=0
mouvy=0
skill = 0

tppouvoir = 1
particles = []
cammouv = 0
jump = False
vely = 2


spinanim = 0
powerload = 0
current_img = 0
couleur = 1
# FONCTIONS ----------------
upbuttonattack = 0

nb_map = []
xp = 0
arene = 0
# LISTE MONSTRES

monstre_1 = [[10, 10, 25], [7,7, 25], [9, 12,25]]
for i in range(5):
    monstre_1.append([random.randint(10, 17), random.randint(7, 15), 25])
spawnmonstre = 0
attaquedispo = 1
attaquesimple = 0

newpos = 0

butinpage = 0
transitionbutiny = -605

cliquebutin = 0

boss = 0
boss_list = []
# JOUEUR
ldata = []
life = 100
joueurx = 0
joueury = 0
if soption1 == True:
    f = open("data/player.txt", "r")
    data = f.read()
    ldata = data.split(",")
    life = int(ldata[0])
    joueurx = int(ldata[1])
    joueury = int(ldata[2])
    cammouv = 1
    f.close()
# CHRONOMETRE

def chrono(s, pv):
    global temps
    global tempssecond
    global tppouvoir
    temps = float(time.time())
    tempssecond = time.time() + float(s)
    if pv == "pvtp":
        while temps < tempssecond:
            temps = float(time.time())
        print("Recharge téléportation OK")
        tppouvoir=1
        cammouv = 1


 # MAP
def map_jeu():
    global boss_list, touches, boss, xp, spawnmonstre,cliquebutin, butinpage, life, spinimg, current_img, spinanim, powerload, cammouv, mouvx, mouvy, xgmouse, ygmouse, joueurx, joueury, jump, tppouvoir
    global newpos, vely, playery, perso_spin, attaquesimple, position, couleur, maintext, upbuttonattack, nb_map, arene, attaquedispo, monstre_1, monstre_2
    pos = list(pygame.mouse.get_pos())


    # ENVIRONNEMENT

    for i in range(len(nuages)):
        display.blit(nuage, (nuages[i][0]+mouvx, nuages[i][1]+mouvy))
        nuages[i][0] = nuages[i][0]-0.1
        if nuages[i][0] < 0:
            nuages[i][0] = random.randint(0, 900)
    # PERSO
    
    ratiox = (screen_rect.width / display_rect.width)
    ratioy = (screen_rect.height / display_rect.height)
    xgmouse, ygmouse = (pos[0] / ratiox, pos[1] / ratioy)
    touches = pygame.key.get_pressed()
    if touches[pygame.K_RIGHT] == True:
        mouvx+=0.3
    if touches[pygame.K_LEFT] == True:
        mouvx-=0.3
    if touches[pygame.K_UP] == True:
        mouvy-=0.3
    if touches[pygame.K_DOWN] == True:
        mouvy+=0.3

    # JUMP MOUVEMENT
    if jump == False and touches[pygame.K_SPACE] == True and tppouvoir == 1:
        jump = True
        couleur = 1
        for i in range(20):
            particles.append([[150 + mouvx+joueurx*10 - joueury*10 + 15, 100 + joueurx * 5 + mouvy+joueury * 5 + 40], [random.randint(0, 10) / 10 - 1, -2], random.randint(2, 4)])

        print("JUMP")
    if jump == True:
        playery-=vely
        vely-=0.05
        if vely < -2:
            jump = False
            vely = 2
    for y, rang in enumerate(nb_map):
        for x, block in enumerate(rang):
            # PERSONNAGE
            if jump == False:
                playery = 100 + joueurx * 5 + mouvy+joueury * 5
        


            # GESTION CAMERA 
                 # CAMMOUV = 1 CAMERA SUIT LE PERSONNAGE
            if cammouv == 1:
                if (150 + mouvx+joueurx*10 - joueury*10) <= 130:
                    mouvx+=0.05
                elif (150 + mouvx+joueurx*10 - joueury*10) >= 165:
                    mouvx-=0.05
                elif (100 + joueurx * 5 + mouvy+joueury * 5) <= 80:
                    mouvy+=0.05
                elif (100 + joueurx * 5 + mouvy+joueury * 5) >= 120:
                    mouvy-=0.05
                else: cammouv = 0

            # BLOCKS

            if block == "1":
                # NE PAS AFFICHER LES BLOCKS QUI NE SONT PAS SUR LECRAN
                if (150 + mouvx+x*10 - y*10) >= 0 and (150 + mouvx+x*10 - y*10) <= 280 and (100 + x * 5 + mouvy+y * 5 + couche) >= 0 and (100 + x * 5 + mouvy+y * 5) <= 280: 
                    display.blit(broke_block_img, (150 + mouvx+x*10 - y*10, 100 + x * 5 + mouvy+y * 5))

            if block == "2":
                # NE PAS AFFICHER LES BLOCKS QUI NE SONT PAS SUR LECRAN
                if (150 + mouvx+x*10 - y*10) >= 0 and (150 + mouvx+x*10 - y*10) <= 280 and (100 + x * 5 + mouvy+y * 5 + couche) >= 0 and (100 + x * 5 + mouvy+y * 5) <= 280: 
                    display.blit(red_block_img, (150 + mouvx+x*10 - y*10, 100 + x * 5 + mouvy+y * 5))   
                    if joueurx+1 == x and joueury+1 == y:
                        life-=0.05

            if block == "3":
                # NE PAS AFFICHER LES BLOCKS QUI NE SONT PAS SUR LECRAN
                if (150 + mouvx+x*10 - y*10) >= 0 and (150 + mouvx+x*10 - y*10) <= 280 and (100 + x * 5 + mouvy+y * 5 + couche) >= 0 and (100 + x * 5 + mouvy+y * 5) <= 280: 
                    display.blit(blue_block_img, (150 + mouvx+x*10 - y*10, 100 + x * 5 + mouvy+y * 5))   

            if block == "4":
                # NE PAS AFFICHER LES BLOCKS QUI NE SONT PAS SUR LECRAN
                if (150 + mouvx+x*10 - y*10) >= 0 and (150 + mouvx+x*10 - y*10) <= 280 and (100 + x * 5 + mouvy+y * 5 + couche) >= 0 and (100 + x * 5 + mouvy+y * 5) <= 280: 
                    display.blit(blue_block_img, (150 + mouvx+x*10 - y*10, 100 + x * 5 + mouvy+y * 5)) 
                    display.blit(tresor_block_img, (150 + mouvx+x*10 - y*10, 100 + x * 5 + mouvy+y * 5 - couche))   
                    if joueurx+1 == x and joueury+1 == y and mouseclicked == 2 and powerload == 0:
                        couleur = 2
                        for i in range(100):
                            particles.append([[150 + mouvx+joueurx*10 - joueury*10 + 10, 100 + joueurx * 5 + mouvy+joueury * 5 + 5], [random.randint(0, 10) / 10 - 1, -2], random.randint(4, 6)])
                        print("BUTIN")
                        cliquebutin = 0
                        butinpage = 1
                        life+=10
                        # SUPPRIMER LE BUTIN
                        map_data[y][x] = '3'

            if block == "5":
                # NE PAS AFFICHER LES BLOCKS QUI NE SONT PAS SUR LECRAN
                if (150 + mouvx+x*10 - y*10) >= 0 and (150 + mouvx+x*10 - y*10) <= 280 and (100 + x * 5 + mouvy+y * 5 + couche) >= 0 and (100 + x * 5 + mouvy+y * 5) <= 280: 
                    display.blit(blue_block_img, (150 + mouvx+x*10 - y*10, 100 + x * 5 + mouvy+y * 5)) 
                    display.blit(portal_img, (150 + mouvx+x*10 - y*10, 100 + x * 5 + mouvy+y * 5 - couche))
                
                    if joueurx+1 == x and joueury+1 == y and mouseclicked == 2 and powerload == 0:
                        couleur = 3
                        for i in range(100):
                            particles.append([[150 + mouvx+joueurx*10 - joueury*10 + 10, 100 + joueurx * 5 + mouvy+joueury * 5 + 5], [random.randint(0, 10) / 10 - 1, -2], random.randint(4, 6)])
                        print("PORTAIL") 
                        # SUPPRIMER LE BUTIN
                        joueurx = 0
                        joueury= 0
                        nb_map = arena_data
                        cammouv = 1
                        arene = 1
                        

            # AFFICHER LE CHOIX DES BLOCKS PROCHES QUI NE SONT PAS VIDE
            if block != "0" and block != "" and xgmouse >= (150 + mouvx+x*10 - y*10) and xgmouse <= ((150 + mouvx+x*10 - y*10)+12) and ygmouse >= (100 + x * 5 + mouvy+y * 5) and ygmouse <= ((100 + x * 5 + mouvy+y * 5)+10):
                if jump == False:
                    if joueurx <= x+2 and joueurx >= x-4 and joueury <= y+2 and joueury >= y-4:
                        display.blit(direction, (150 + mouvx+x*10 - y*10, 100 + x * 5 + mouvy+y * 5))
                        if mouseclicked == 1 and tppouvoir == 1:
                            couleur = 1
                            for i in range(20):
                                particles.append([[150 + mouvx+joueurx*10 - joueury*10 + 15, 100 + joueurx * 5 + mouvy+joueury * 5 + 15], [random.randint(0, 10) / 10 - 1, -2], random.randint(4, 6)])
                            joueurx = x-1
                            joueury = y-1
                            func_tp = Thread(target=chrono, args=(0.1, "pvtp"))
                            func_tp.start()
                            tppouvoir = 0
                            cammouv = 1
                elif jump == True:
                    if joueurx <= x+4 and joueurx >= x-6 and joueury <= y+4 and joueury >= y-6:
                        display.blit(direction, (150 + mouvx+x*10 - y*10, 100 + x * 5 + mouvy+y * 5))
                        if mouseclicked == 1 and tppouvoir == 1:
                            couleur = 1
                            for i in range(20):
                                particles.append([[150 + mouvx+joueurx*10 - joueury*10 + 15, 100 + joueurx * 5 + mouvy+joueury * 5 + 15], [random.randint(0, 10) / 10 - 1, -2], random.randint(4, 6)])
                            joueurx = x-1
                            joueury = y-1
                            func_tp = Thread(target=chrono, args=(0.1, "pvtp"))
                            func_tp.start()
                            tppouvoir = 0
                            cammouv = 1

            if arene == 1:
                newpos+=1
                if newpos >= 10000: # CHAQUE SECONDE ENVIRON LE MONSTRE IRA VERS LE HALO DU JOUEUR
                    newpos = 0
                if spawnmonstre >= 300:
                    spawnmonstre = 0
                    for i in range(5):
                        monstre_1.append([random.randint(10, 17), random.randint(7, 15), 25])
                for i in range(len(monstre_1)):
                    mlist = monstre_1
                    monstrex = mlist[i][0]
                    monstrey = mlist[i][1]
                    monstrevie = mlist[i][2]
                    pygame.draw.rect(display, (153, 0, 20), ((150 + mouvx+monstrex*10 - monstrey*10)-5, (100 + monstrex * 5 + mouvy+monstrey * 5 - couche)-11, (int(monstrevie)*85/100), 4))
                    position = (150 + mouvx+monstrex*10 - monstrey*10, 100 + monstrex * 5 + mouvy+monstrey * 5 - couche) # POSITION DU MONSTRE
                    if newpos == 9999:
                        spawnmonstre+=1
                        if monstrex < joueurx+random.choice((1, 3, 4)):
                            monstrex+=1
                        elif monstrex > joueurx+random.choice((1, 3, 4)):
                            monstrex-=1
                        if monstrey < joueury+random.choice((1, 3, 4)):
                            monstrey+=1
                        elif monstrey > joueury+random.choice((1, 3, 4)):
                            monstrey-=1
                        if monstrex < joueurx+4 and monstrex > joueurx-2 and monstrey < joueury+4 and monstrey > joueury-2:
                            life-=0.5
                        mlist[i][0] = monstrex
                        mlist[i][1] = monstrey
                    if monstrevie <= 0:
                        mlist[i][0] = 100
                        mlist[i][1] = 100
                    else:
                        display.blit(monstre_1_right, position)
                    # SI LE JOUEUR EST PROCHE LORS DE LATAQUE
                    if attaquedispo == 1 and monstrex >= joueurx-5 and monstrex <= joueurx+3 and monstrey >= joueury-5 and monstrey <= joueury+3:
                        monstrevie -= 5 # UPDATE LE NIVEAU DE VIE DU MONSTRE
                        mlist[i][2] = monstrevie
                        couleur = 4
                        monstre_1 = mlist
                        for i in range(3):
                            particles.append([[150 + mouvx+monstrex*10 - monstrey*10 + 5, 100 + monstrex * 5 + mouvy+monstrey * 5 + 5], [random.randint(0, 10) / 10 - 1, -2], random.randint(2, 4)])
                    if attaquesimple == 1 and monstrex >= joueurx-5 and monstrex <= joueurx+3 and monstrey >= joueury-5 and monstrey <= joueury+3:
                        monstrevie -= 2 # UPDATE LE NIVEAU DE VIE DU MONSTRE
                        mlist[i][2] = monstrevie
                        couleur = 4
                        for i in range(3):
                            particles.append([[150 + mouvx+monstrex*10 - monstrey*10 + 5, 100 + monstrex * 5 + mouvy+monstrey * 5 + 5], [random.randint(0, 10) / 10 - 1, -2], random.randint(2, 4)])
                        monstre_1 = mlist
                    if i == len(monstre_1)-1 and attaquedispo == 1: # SI TOUT LES MONSTRES ON ETE TOUCHEE
                        attaquedispo = 0
                        
                    if i == len(monstre_1)-1 and attaquesimple == 1:
                        attaquesimple = 0
            if boss == 1:
                newpos+=1
                if newpos >= 10000: # CHAQUE SECONDE ENVIRON LE MONSTRE IRA VERS LE HALO DU JOUEUR
                    newpos = 0
                for i in range(len(boss_list)):
                    mlist = boss_list[i]
                    monstrex = mlist[0]
                    monstrey = mlist[1]
                    monstrevie = mlist[2]
                    image = mlist[3]
                    pygame.draw.rect(display, (153, 0, 20), ((150 + mouvx+monstrex*10 - monstrey*10)-5, (100 + monstrex * 5 + mouvy+monstrey * 5 - couche)-11, (int(monstrevie)*16/100), 4))
                    position = (150 + mouvx+monstrex*10 - monstrey*10, 100 + monstrex * 5 + mouvy+monstrey * 5 - couche) # POSITION DU MONSTRE
                    if newpos == 9999:
                        spawnmonstre+=1
                        if monstrex < joueurx+random.choice((1, 3, 4)):
                            monstrex+=1
                        elif monstrex > joueurx+random.choice((1, 3, 4)):
                            monstrex-=1
                        if monstrey < joueury+random.choice((1, 3, 4)):
                            monstrey+=1
                        elif monstrey > joueury+random.choice((1, 3, 4)):
                            monstrey-=1
                        if monstrex < joueurx+4 and monstrex > joueurx-2 and monstrey < joueury+4 and monstrey > joueury-2:
                            life-=0.5
                        mlist[0] = monstrex
                        mlist[1] = monstrey
                    if monstrevie <= 0:
                        mlist[0] = 100
                        mlist[1] = 100
                    else:
                        display.blit(image, position)
                    # SI LE JOUEUR EST PROCHE LORS DE LATAQUE
                    if attaquedispo == 1 and monstrex >= joueurx-5 and monstrex <= joueurx+3 and monstrey >= joueury-5 and monstrey <= joueury+3:
                        print("COLLISION SPIN ET MONSTRE")
                        monstrevie -= 10 # UPDATE LE NIVEAU DE VIE DU MONSTRE
                        mlist[2] = monstrevie
                        couleur = 4
                        attaquedispo = 0
                        for i in range(3):
                            particles.append([[150 + mouvx+monstrex*10 - monstrey*10 + 5, 100 + monstrex * 5 + mouvy+monstrey * 5 + 5], [random.randint(0, 10) / 10 - 1, -2], random.randint(2, 4)])

                    if attaquesimple == 1 and monstrex >= joueurx-5 and monstrex <= joueurx+3 and monstrey >= joueury-5 and monstrey <= joueury+3:
                        monstrevie -= 2 # UPDATE LE NIVEAU DE VIE DU MONSTRE
                        mlist[2] = monstrevie
                        couleur = 4
                        attaquesimple = 0
                        for i in range(3):
                            particles.append([[150 + mouvx+monstrex*10 - monstrey*10 + 5, 100 + monstrex * 5 + mouvy+monstrey * 5 + 5], [random.randint(0, 10) / 10 - 1, -2], random.randint(2, 4)])

                   



            # PERSONNAGE
            position = (150 + mouvx+joueurx*10 - joueury*10,playery)
            display.blit(perso_droite, position)


    # AFFICHAGE DU HUD
    display.blit(powerimg, (5, 5))
    
    pygame.draw.rect(display, (153, 0, 20), (11, 6, (int(life)*49/100), 12))
    pygame.draw.rect(display, (0, 102, 203), (11, 18, (powerload*49/100), 12))
    display.blit(maintext, (9, 30))

    # NIVEAU DE VIE DU JOUEUR
    if life < 0:
        life = 0

    elif life > 100: # TRANSFORMATION SURPLUS DE VIE EN XP
        print("XP - {}".format(int(life-100)))
        xp+=int(life-100)
        maintext = font.render('+{} XP'.format(int(life-100)), False, (0, 248, 0))
        life = 100

    # RECHARGE POUVOIR
    if upbuttonattack == 1 and powerload < 80:
        print("ATTACK SIMPLE") 
        couleur = 6
        for i in range(20):
            particles.append([[150 + mouvx+joueurx*10 - joueury*10 + 10, 100 + joueurx * 5 + mouvy+joueury * 5 + 5], [random.randint(0, 10) / 10 - 1, -2], random.randint(2, 4)])
        attaquesimple = 1
        upbuttonattack = 0
    if mouseclicked == 0 and powerload > 0:
        powerload-=0.5
    if mouseclicked == 2 and powerload < 100:
        powerload+=0.5
    elif powerload >99 and mouseclicked == 2 :
        print("ATTACK SPIN")
        powerload = 0
        spinanim = 1
        tppouvoir = 0

    if spinanim == 1:
        display.blit(perso_spin,(int(position[0])-20, int(position[1]-20)))
        perso_spin = spinimg[int(current_img)]
        perso_spin.set_colorkey((0, 0, 0))
        current_img+=0.3
        if current_img >= len(spinimg):
            current_img = 0
            spinanim = 0
            tppouvoir = 1
            attaquedispo = 1

    
    # PARTICULES / EFFETS SPECIAUX

    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] += 0.1
        if couleur == 1:
            pygame.draw.circle(display, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        elif couleur == 2:
            pygame.draw.circle(display, (255, 253, 175), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        elif couleur == 3:
            pygame.draw.circle(display, (171, 65, 217), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        elif couleur == 4:
            pygame.draw.circle(display, (255, 10, 10), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        elif couleur == 6:
            pygame.draw.circle(display, (255, 165, 0), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)
                
               




while running: 
    display.fill((0,0,0))
    xmouse, ymouse = pygame.mouse.get_pos()
    screen.blit(background, (1, 1))
    
    # ANIMATIONS ------------------------- MAIN MENU
    
        # MENU BUTTON
    dreamland.set_alpha(transparencelogo)
    if transpaanim == 0:
        if transparencelogo < 255:
            transparencelogo+=1.8
            
        else:
            transparencelogo = 255
            transpaanim = 1
    if animone!=2:
        if mnmnx <= 20:
            mnmnx+=0.2
        elif mnmnx > 20:
            mnmnx = 20
        if mnmny >= 550:
            mnmny-=0.26
        elif mnmny < 550:
            mnmny = 550
            animone=2
            # STARTING MENU SOUND
            mainmenusound.play()

    # MENU 2 BUTTONS ANIMATION


    #INTRO
    # Main menu partie 1

    if menuone == 1:
        screen.blit(dreamland, (410, 50))
        if mnbtnhover == 0:
            screen.blit(mainmenubutton, (mnmnx, mnmny))
        elif mnbtnhover == 1:
            screen.blit(mainmenubuttonhover, (mnmnx, 550))

    if animbtnone == 1:
        if mnmnx >= -110:
            mnmnx-=1
            mnbtnhover = 0
        else:
            animbtnone = 0
            menuone = 0
            menutwo = 1
            menutwoclickable = 1


    # MAIN Menu partie 2

    if menutwo == 1:
        screen.blit(dreamland, (410, 50))
        if animbtntwo == 0:
            if mntwobtn <= 20:
                mntwobtn+=1
            else:
                animbtntwo = 1

        if stsbtnhover == 0:
            screen.blit(settingsbutton, (mntwobtn, 500))
        elif stsbtnhover == 1:
            screen.blit(settingsbuttonhover, (mntwobtn, 500))
        
        if tttbtnhover == 0:
            screen.blit(tutorialbutton, (mntwobtn, 450))
        elif tttbtnhover == 1:
            screen.blit(tutorialbuttonhover, (mntwobtn, 450))

        if plybtnhover == 0:
            screen.blit(playbutton, (mntwobtn, 400))
        elif plybtnhover == 1:
            screen.blit(playbuttonhover, (mntwobtn, 400))


    screen.blit(settingsbg, (0, settingsbgy))

    # SETTINGS PAGE

    if settingspage == 1:
        if settingsbgy < -2:
            settingsbgy+=6
        elif settingsbgy >= -2:
            menutwoclickable = 0
            stsbtnhover = 0
            # SLIDE BAR DES OPTIONS SETTINGS
            screen.blit(sliderbar, (250, 45))
            if slidechanged != optionssettings:
                slidesound.play()
                slidechanged = optionssettings
            if ymouse >= 5 and ymouse <= 80:
                if xmouse >= 250 and xmouse <= 750:
                    if mouseclicked == 1:
                        screen.blit(sliderset, (xmouse-5, 5))
                    if xmouse >= 435 and xmouse <= 545:
                        if mouseclicked == 1:
                            screen.blit(sliderset, (xmouse-5, 5))
                            setxpos = set1x
                            optionssettings = 1
                            
                    if xmouse >= 250 and xmouse <= 435:
                        if mouseclicked == 1:
                            screen.blit(sliderset, (xmouse-5, 5))
                            setxpos = set2x
                            optionssettings = 2
                            
                    if xmouse >= 545 and xmouse <= 750:
                        if mouseclicked == 1:
                            screen.blit(sliderset, (xmouse-5, 5))
                            setxpos = set3x
                            optionssettings = 3
                            
                else:


                    # BORDS

                    if xmouse <= 250:
                        if mouseclicked == 1:
                            screen.blit(sliderset, (250, 5))
                            setxpos = set2x
                    elif xmouse >= 750:
                        if mouseclicked == 1:
                            screen.blit(sliderset, (735, 5))
                            setxpos = set3x

            if mouseclicked == 0:
                screen.blit(sliderset, (setxpos, 5))

            if optionssettings == 2:
                screen.blit(controlsettings, (250, 150))

            if optionssettings == 1:
                screen.blit(descsettings, (250, 150))
                if soption1 == True:
                    screen.blit(toggle_on, (680, 180))
                elif soption1 == False:
                    screen.blit(toggle_off, (680, 180))
                if soption2 == True:
                    screen.blit(toggle_on, (680, 290))
                elif soption2 == False:
                    screen.blit(toggle_off, (680, 290))
                if soption3 == True:
                    screen.blit(toggle_on, (680, 400))
                elif soption3 == False:
                    screen.blit(toggle_off, (680, 400))


                if xmouse >= 680 and xmouse <= 705:
                    if ymouse >= 180 and ymouse <= 180+42:
                        if mouseclicked == 1:
                            if soption1 == True:
                                soption1 = False
                                mouseclicked = 0
                                offsound.play()
                            elif soption1 == False:
                                soption1 = True
                                mouseclicked = 0
                                onsound.play()

                    elif ymouse >= 290 and ymouse <= 290+42:
                        if mouseclicked == 1:
                            if soption2 == True:
                                soption2 = False
                                mouseclicked = 0
                                offsound.play()
                            elif soption2 == False:
                                soption2 = True
                                mouseclicked = 0
                                onsound.play()

                    elif ymouse >= 400 and ymouse <= 400+42:
                        if mouseclicked == 1:
                            if soption3 == True:
                                soption3 = False
                                mouseclicked = 0
                                offsound.play()
                            elif soption3 == False:
                                soption3 = True
                                mouseclicked = 0
                                onsound.play()

    screen.blit(transition, (0, transitiony))


    if settingspagebackgroundoff == 1:
        if settingspage == 1:
            settingspage = 0
        if settingsbgy > -600:
            settingsbgy-=6
        elif settingsbgy <= -600:
            menutwoclickable = 1
            menutwo = 1
            settingspagebackgroundoff = 0

    # DÉBUT DU JEU

    if startinggame == 1:

        if transitiony < -2:
            transitiony+=5
        elif transitiony >= -2:
            mainmenusound.stop()
            startinggame = 0
            enteringgame = 1
            if soption1 == False:
                life = 100
                joueurx = 0
                joueury = 0
            transparencelogo = 0

        menuone = 0
        menutwo = 0

    if enteringgame == 1:
        dreamland.set_alpha(transparencelogo)
        screen.blit(dreamland, (119, 250))
        if transpaanimtwo == 0:
            if transparencelogo <= 255:
                transparencelogo+=0.3
            elif transparencelogo >= 255 and transparencelogo <= 255.3:
                transparencelogo+=0.3
            elif transparencelogo > 255.3 and transparencelogo <= 260:
                transparencelogo+=0.3
            elif transparencelogo >= 260:
                transparencelogo = 255
                transpaanimtwo = 1
                enteringgame = 0
                enteringgamelspart = 1
                nb_map = map_data



    # DEBUT DU JEU ---------------------


    if enteringgamelspart == 1:
        # DESSIN DE LA MAP
        map_jeu()
        screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))

    if butinpage == 1:
        screen.blit(transitionbutin, (0, transitionbutiny))
        if transitionbutiny < -2:
            transitionbutiny+=5
        if touches[pygame.K_SPACE] == True:     
            transitionbutiny = -605
            boss = 1

            boss_list.append([joueurx+2, joueury+2, 150, random.choice((boss_1_image, boss_2_image, boss_3_image))])
            print(boss_list)
            butinpage = 0


    if life == 0: # MORT
        screen.blit(transitiondead, (0, transitiondeady))
        if transitiondeady < -2:
            transitiondeady+=5




# QUITTER LE JEU
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            f = open("data/player.txt", "w")
            f.write("{}, {}, {}".format(int(life), joueurx, joueury))
            f.close()
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("ESCAPE")
                    f = open("data/data.txt", "w")
                    f.write(str(soption1))
                    f.close()
                    if settingspage == 1:
                        settingspagebackgroundoff = 1

        # MENU -----------------

            # MAIN MENU BUTTON
        if menuone == 1:
            if xmouse >= 20 and xmouse <= 150:
                if ymouse >= 550 and ymouse <= 570:
                    mnbtnhover = 1
            else:
                mnbtnhover = 0
        if menutwo == 1:
            if menutwoclickable == 1:
                if xmouse >= 20 and xmouse <= 150:
                    if ymouse >= 500 and ymouse <= 520:
                        stsbtnhover = 1
                    else:
                        stsbtnhover = 0
                    if ymouse >= 450 and ymouse <= 470:
                        tttbtnhover = 1
                    else:
                        tttbtnhover = 0
                    if ymouse >= 400 and ymouse <= 420:
                        plybtnhover = 1
                    else:
                        plybtnhover = 0

        if event.type == pygame.MOUSEBUTTONUP:
            if mouseclicked == 2:
                upbuttonattack = 1
            mouseclicked = 0
            # MENU ------------------
            if menuone == 1:
                if xmouse >= 20 and xmouse <= 150:
                    if ymouse >= 550 and ymouse <= 570:
                        btnclick.play()
                        animbtnone = 1
            if menutwo == 1:
                if menutwoclickable == 1:
                    if xmouse >= 20 and xmouse <= 150:
                        if ymouse >= 500 and ymouse <= 520:
                            btnclick.play()
                            print("SETTINGS")
                            settingspage = 1
                        elif ymouse >= 450 and ymouse <= 470:
                            btnclick.play()
                            print("TUTORIAL")
                        elif ymouse >= 400 and ymouse <= 420:
                            playbtnsound.play()
                            startinggame = 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseclicked = 1
            elif event.button == 3:
                mouseclicked = 2






