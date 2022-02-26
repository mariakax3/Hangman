#Author: Maria Karaszewska
#Date: 07-2021

import pygame
import sys
import os
import random
import time

pygame.init()

width = 800
height = 493
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (113, 165, 24)
lime = (147, 217, 28)
font = pygame.font.SysFont('consolas', 30)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Wisielec')

basePath = os.path.dirname(__file__)
dudePath = os.path.join(basePath, 'sounds\Two Finger Johnny.mp3')
bgMusic = pygame.mixer.Sound(dudePath)
bgMusic.play(-1)
bgMusic.set_volume(0.3)


def startScreen():
    titlefont = pygame.font.SysFont('sitkasmallsitkatextboldsitkasubheadingboldsitkaheadingboldsitkadisplayboldsitkabannerbold', 120)

    basePath = os.path.dirname(__file__)
    dudePath = os.path.join(basePath, 'images\loop.png')
    img = pygame.image.load(dudePath)
    screen.blit(img, (width - img.get_width() - 20, 0))

    title = titlefont.render('Wisi_l_c', True, white)
    screen.blit(title, (width // 2 - title.get_width() // 2, 30))

    cat = font.render('Wybierz kategorię:', True, white)
    phrases = font.render('1 - przysłowia', True, white)
    songs = font.render('2 - muzyka i film', True, white)
    physics = font.render('3 - fizyka', True, white)
    various = font.render('4 - inne', True, white)
    screen.blit(cat, (width // 3 - cat.get_width() // 2, 200))
    screen.blit(phrases, (width // 3 - phrases.get_width() // 2, 250))
    screen.blit(songs, (width // 3 - songs.get_width() // 2, 300))
    screen.blit(physics, (width // 3 - physics.get_width() // 2, 350))
    screen.blit(various, (width // 3 - various.get_width() // 2, 400))

    #print('1: x: {} - {}; y: 250 - {}'.format(width // 3 - phrases.get_width() // 2, width // 3 + phrases.get_width() // 2, 250 + phrases.get_height()))
    #print('2: x: {} - {}; y: 300 - {}'.format(width // 3 - songs.get_width() // 2, width // 3 + songs.get_width() // 2, 300 + songs.get_height()))
    #print('3: x: {} - {}; y: 350 - {}'.format(width // 3 - physics.get_width() // 2, width // 3 + physics.get_width() // 2, 350 + physics.get_height()))
    #print('4: x: {} - {}; y: 400 - {}'.format(width // 3 - various.get_width() // 2, width // 3 + various.get_width() // 2, 400 + various.get_height()))

def loadLetters(letOk, letNotOk):
    alphabet = ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó', 'P', 'Q', 'R', 'S', 'Ś', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ź', 'Ż']
    c = 0
    for i in range(189, 414, 45):
        for j in range(470, 785, 45):

            if alphabet[c].lower() in letOk or alphabet[c].upper() in letOk:
                color = lime
            elif alphabet[c].lower() in letNotOk or alphabet[c].upper() in letNotOk:
                color = red
            else:
                color = white

            pygame.draw.rect(screen, color, (j, i, 38, 38), 2, border_radius = 5)
            screen.blit(font.render(alphabet[c], True, color), (j + 11, i + 5))
            c += 1

def play(clue):
    fails = 0
    winV = 0
    t = 0
    let = []
    letOk = []
    correct = True
    clue = clue.upper()
    #print(clue)

    endFontD = pygame.font.SysFont('verdana', 38, bold=True)
    endFontC = pygame.font.SysFont('verdana', 25, bold=True)
    
    screen.fill(black)
    basePath = os.path.dirname(__file__)
    dudePath = os.path.join(basePath, 'images\s{}.jpg'.format(fails))
    img = pygame.image.load(dudePath)
    screen.blit(img, (0, height // 3 - 30))

    hidden = []
    for i in range(len(clue)):
        if clue[i] == ' ':
            hidden.append(' ')
        else:
            hidden.append('-')

    hiddenT = font.render(''.join(hidden), True, white)
    screen.blit(hiddenT, (width // 2 - hiddenT.get_width() // 2, 60))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif winV and event.type == pygame.MOUSEMOTION:
                m = pygame.mouse.get_pos()

                if m[0] > 525 and m[0] < 581 and m[1] > 370 and m[1] < 401:
                    yesT = endFontC.render('TAK', True, red)
                    screen.blit(yesT, (3 * width // 4 - restart.get_width() // 4, 370))
                
                elif m[0] > 649 and m[0] < 701 and m[1] > 370 and m[1] < 401:
                    noT = endFontC.render('NIE', True, red)
                    screen.blit(noT, (3 * width // 4 + restart.get_width() // 4 - noT.get_width() // 2, 370))
                
                else:
                    yesT = endFontC.render('TAK', True, white)
                    screen.blit(yesT, (3 * width // 4 - restart.get_width() // 4, 370))
                    noT = endFontC.render('NIE', True, white)
                    screen.blit(noT, (3 * width // 4 + restart.get_width() // 4 - noT.get_width() // 2, 370))

                pygame.display.update()

            elif winV and event.type == pygame.MOUSEBUTTONDOWN:
                m = pygame.mouse.get_pos()

                if m[0] > 525 and m[0] < 581 and m[1] > 370 and m[1] < 401:
                    return True
                
                elif m[0] > 649 and m[0] < 701 and m[1] > 370 and m[1] < 401:
                    return False


            elif event.type == pygame.KEYDOWN:
                correct = False
                x = event.unicode
                if len(x) != 1:
                    correct = True

                for i in range(len(clue)):
                    if (x == clue.lower()[i] or x == clue[i]) and x not in letOk:
                        t = 1
                        hidden[i] = clue[i]
                        correct = True
                        basePath = os.path.dirname(__file__)
                        dudePath = os.path.join(basePath, 'sounds\yes.wav')
                        yes = pygame.mixer.Sound(dudePath)
                        yes.play()
                
                if t:
                    letOk.append(x)
                    t = 0

                if not correct and x not in let and x not in letOk:
                    fails += 1
                    let.append(x)
                    basePath = os.path.dirname(__file__)
                    dudePath = os.path.join(basePath, 'sounds\ghf.wav')
                    no = pygame.mixer.Sound(dudePath)
                    no.play()

                if '-' not in hidden:
                    winV = 1
                    
                    screen.fill(black)
                    basePath = os.path.dirname(__file__)
                    dudePath = os.path.join(basePath, 'images\s{}.jpg'.format(fails))
                    img = pygame.image.load(dudePath)
                    screen.blit(img, (0, height // 3 - 30))
                    clueT = font.render(clue, True, white)
                    screen.blit(clueT, (width // 2 - clueT.get_width() // 2, 60))

                    win1 = endFontC.render('Tak jest! Wygrywasz talon', True, white)
                    win2 = endFontC.render('na kurwę i balon!', True, white)
                    restart = endFontD.render('JESZCZE RAZ?', True, green)
                    screen.blit(win1, (3 * width // 4 - win1.get_width() // 2, 180))
                    screen.blit(win2, (3 * width // 4 - win2.get_width() // 2, 210))
                    screen.blit(restart, (3 * width // 4 - restart.get_width() // 2, 300))
                    pygame.display.update()
                    
                    yesT = endFontC.render('TAK', True, white)
                    noT = endFontC.render('NIE', True, white)
                    screen.blit(yesT, (3 * width // 4 - restart.get_width() // 4, 370))
                    screen.blit(noT, (3 * width // 4 + restart.get_width() // 4 - noT.get_width() // 2, 370))

                    basePath = os.path.dirname(__file__)
                    dudePath = os.path.join(basePath, 'sounds\win.wav')
                    win = pygame.mixer.Sound(dudePath)
                    bgMusic.stop()
                    win.play()
                    time.sleep(2)
                    bgMusic.play()
                    

                if fails < 9 and winV == 0:
                    screen.fill(black)
                    basePath = os.path.dirname(__file__)
                    dudePath = os.path.join(basePath, 'images\s{}.jpg'.format(fails))
                    img = pygame.image.load(dudePath)
                    screen.blit(img, (0, height // 3 - 30))
                    hiddenT = font.render(''.join(hidden), True, white)
                    screen.blit(hiddenT, (width // 2 - hiddenT.get_width() // 2, 60))

                elif fails == 9 and winV == 0:
                    basePath = os.path.dirname(__file__)
                    dudePath = os.path.join(basePath, 'sounds\gameover.wav')
                    gameOverSound = pygame.mixer.Sound(dudePath)

                    screen.fill(black)
                    basePath = os.path.dirname(__file__)
                    dudePath = os.path.join(basePath, 'images\s{}.jpg'.format(fails))
                    img = pygame.image.load(dudePath)
                    screen.blit(img, (0, height // 3 - 30))
                    hiddenT = font.render(''.join(hidden), True, white)
                    youDied = endFontD.render('YOU DIED!', True, red)
                    correctClueText = endFontC.render('Prawidłowe hasło:', True, white)
                    correctClue = endFontC.render(clue, True, white)
                    screen.blit(youDied, (3 * width // 4 - youDied.get_width() // 2, 180))
                    screen.blit(correctClueText, (3 * width // 4 - correctClueText.get_width() // 2, 280))
                    screen.blit(correctClue, (width // 2 - correctClue.get_width() // 2, height - 2 * correctClue.get_height()))
                    screen.blit(hiddenT, (width // 2 - hiddenT.get_width() // 2, 60))

                    pygame.display.update()

                    bgMusic.stop()
                    gameOverSound.play()
                    time.sleep(5)
                    bgMusic.play()
                    return True
                
        if not winV:
            loadLetters(letOk, let)

        pygame.display.update()

def main():
    startScreen()
    firstRun = True
    while firstRun:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                m = pygame.mouse.get_pos()

                if m[0] > 147 and m[0] < 385 and m[1] > 250 and m[1] < 280:
                    basePath = os.path.dirname(__file__)
                    dudePath = os.path.join(basePath, 'clues\przyslowia.txt')
                    f = open(dudePath, 'r', encoding='utf-8')
                    clues = f.read().split('\n')
                    f.close()
                    clue = clues[random.randint(0, len(clues) - 1)]
                    firstRun = False
                elif m[0] > 122 and m[0] < 410 and m[1] > 300 and m[1] < 330:
                    basePath = os.path.dirname(__file__)
                    dudePath = os.path.join(basePath, 'clues\muzykaifilm.txt')
                    f = open(dudePath, 'r', encoding='utf-8')
                    clues = f.read().split('\n')
                    f.close()
                    clue = clues[random.randint(0, len(clues) - 1)]
                    firstRun = False
                elif m[0] > 181 and m[0] < 351 and m[1] > 350 and m[1] < 380:
                    basePath = os.path.dirname(__file__)
                    dudePath = os.path.join(basePath, 'clues\gfizyka.txt')
                    f = open(dudePath, 'r', encoding='utf-8')
                    clues = f.read().split('\n')
                    f.close()
                    clue = clues[random.randint(0, len(clues) - 1)]
                    firstRun = False
                elif m[0] > 198 and m[0] < 334 and m[1] > 400 and m[1] < 430:
                    basePath = os.path.dirname(__file__)
                    dudePath = os.path.join(basePath, 'clues\inne.txt')
                    f = open(dudePath, 'r', encoding='utf-8')
                    clues = f.read().split('\n')
                    f.close()
                    clue = clues[random.randint(0, len(clues) - 1)]
                    firstRun = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    basePath = os.path.dirname(__file__)
                    dudePath = os.path.join(basePath, 'clues\przyslowia.txt')
                    f = open(dudePath, 'r', encoding='utf-8')
                    clues = f.read().split('\n')
                    f.close()
                    clue = clues[random.randint(0, len(clues) - 1)]
                    firstRun = False
                elif event.key == pygame.K_2:
                    basePath = os.path.dirname(__file__)
                    dudePath = os.path.join(basePath, 'clues\muzykaifilm.txt')
                    f = open(dudePath, 'r', encoding='utf-8')
                    clues = f.read().split('\n')
                    f.close()
                    clue = clues[random.randint(0, len(clues) - 1)]
                    firstRun = False
                elif event.key == pygame.K_3:
                    basePath = os.path.dirname(__file__)
                    dudePath = os.path.join(basePath, 'clues\gfizyka.txt')
                    f = open(dudePath, 'r', encoding='utf-8')
                    clues = f.read().split('\n')
                    f.close()
                    clue = clues[random.randint(0, len(clues) - 1)]
                    firstRun = False
                elif event.key == pygame.K_4:
                    basePath = os.path.dirname(__file__)
                    dudePath = os.path.join(basePath, 'clues\inne.txt')
                    f = open(dudePath, 'r', encoding='utf-8')
                    clues = f.read().split('\n')
                    f.close()
                    clue = clues[random.randint(0, len(clues) - 1)]
                    firstRun = False
        pygame.display.update()

    gameOn = True
    while gameOn:
        gameOn = play(clue)
        if gameOn:
            screen.fill(black)
            main()
        else:
            pygame.quit()
            sys.exit()


main()