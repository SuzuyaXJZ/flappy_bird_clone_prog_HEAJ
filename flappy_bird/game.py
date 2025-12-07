# Importation des librairies
import pygame
import random
import os
import json
import unicodedata
import math
import time


pygame.init()
pygame.mixer.init()

# Initialisation des variables in-game
linesThickness = 5
spaceBtwStats = 50
lengthScreen = 800
heightScreen = 600
listScore = []
marginSign = 25
lifeRect1 = pygame.Rect(lengthScreen - (marginSign + 2*linesThickness), linesThickness, marginSign, marginSign)
lifeRect2 = lifeRect1.move(-(marginSign + linesThickness), 0)
lifeRect3 = lifeRect2.move(-(marginSign + linesThickness), 0)
lifeRect4 = lifeRect3.move(-(marginSign + linesThickness), 0)
lifeRect5 = lifeRect4.move(-(marginSign + linesThickness), 0)
lifeRect6 = lifeRect5.move(-(marginSign + linesThickness), 0)
listLifeRect = [lifeRect3, lifeRect2, lifeRect1]
lastScore = 0
defaultDiff = 0
speed = 0
fps = 60
listScore = []
clickNum = 0
lengthGameInSec = 0
coinsNum = 0


# Création de la fenêtre
pygame.display.set_caption("Flappy Bird")
screen = pygame.display.set_mode((lengthScreen, heightScreen))


# Initialisation des couleurs
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
grey = (60, 60, 60)
brighterGrey = (120, 120, 120)
red = (255, 0, 0)
gold = (255, 223, 0)
silver = (70, 130, 180)
bronze = (110, 77, 37)

# Initialisation des variables pour la fenêtre d'entrées utilisateur

screen = pygame.display.set_mode((lengthScreen, heightScreen))
inputRect = pygame.Rect(lengthScreen * (30/100), heightScreen * (45/100), lengthScreen * (40/100), heightScreen * (10/100))
inputRectInside = inputRect.inflate(-(linesThickness), -(linesThickness))
smallFont = pygame.font.Font("./typo/Minecraft.ttf", 20)
username = ""
age = ""
error = ""
padding = 5
active = False
mediumFont = pygame.font.Font("./typo/Minecraft.ttf", 30)
selector = 0
bigFont = pygame.font.Font("./typo/Minecraft.ttf", 40)

# Initalisation des zones cliquables dans le menu

startRect = pygame.Rect(0, heightScreen*(10/100), lengthScreen/2, (heightScreen - (heightScreen*(10/100))) / 2)
startRectInside = startRect.inflate(-(linesThickness), -(linesThickness))

LBRect = pygame.Rect(lengthScreen/2, heightScreen*(10/100), lengthScreen/2, (heightScreen - (heightScreen*(10/100))) / 2)
LBRectInside = LBRect.inflate(-(linesThickness), -(linesThickness))

colorRect = pygame.Rect(0, (heightScreen/2)+(heightScreen*(10/100))/2, lengthScreen/2, (heightScreen - (heightScreen*(10/100))) / 2)
colorRectInside = colorRect.inflate(-(linesThickness), -(linesThickness))

bonusRect = pygame.Rect(lengthScreen/2, (heightScreen/2)+(heightScreen*(10/100))/2, lengthScreen/2, (heightScreen - (heightScreen*(10/100))) / 2)
bonusRectInside = bonusRect.inflate(-(linesThickness), -(linesThickness))

listRectMenu = [startRect, startRectInside, LBRect, LBRectInside, colorRect, colorRectInside, bonusRect, bonusRectInside]
listSectionText = ["Start !", "Leaderboard", "Select the color", "Bonus"]


widthclosingSign = 50
closingSign = pygame.Rect(lengthScreen - widthclosingSign, 0, widthclosingSign + 1, heightScreen*(10/100))
closingSignInside = closingSign.inflate(-(linesThickness), -(linesThickness))







                    ### _________________________________________________________________ ###

                    ###                             Code final                            ###

                    ### _________________________________________________________________ ###






# Boucle principale du jeu contenant les différentes boucles de menu et celle du jeu
firstScreenRect = pygame.Rect(lengthScreen*(25/100), heightScreen*(40/100), lengthScreen*(50/100), heightScreen*(20/100))
firstScreenRectInside = firstScreenRect.inflate(-10, -10)
firstText = mediumFont.render("Press 'SPACE' to start !", True, red)
targetRect = firstText.get_rect(center=(lengthScreen/2, heightScreen/2))
firstScreen = True
while firstScreen:
    screen.fill(black)
    pygame.draw.rect(screen, red, firstScreenRect, 0, 13)
    pygame.draw.rect(screen, black, firstScreenRectInside, 0, 10)
    screen.blit(firstText, targetRect)

 
    for event in pygame.event.get():
        key_pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
        if key_pressed[pygame.K_SPACE]:
            firstScreen = False

    pygame.time.Clock().tick(fps)
    pygame.display.flip()


ready = False
instruction = bigFont.render("Write your name : ", True, white)
instructionRect = instruction.get_rect(center=(lengthScreen/2, heightScreen * (20/100)))
activeError = False
# Pre-game loop
while not(ready):
    errorMessage = mediumFont.render(error, True, red)
    errorRect = errorMessage.get_rect(center=(lengthScreen/2, heightScreen * (75/100)))

    screen.fill(black)
    screen.blit(instruction, instructionRect)
    pygame.draw.rect(screen, white, inputRect, 0, 13)
    pygame.draw.rect(screen, black, inputRectInside, 0, 10)
    textSurface = mediumFont.render(username, True, brighterGrey)
    targetRectInput = textSurface.get_rect(center=(inputRectInside.center))
    screen.blit(textSurface, targetRectInput)
    
    if activeError:
        screen.blit(errorMessage, errorRect)

    for event in pygame.event.get():
        key_pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()

        if key_pressed[pygame.K_RETURN]:
            if len(username) >= 3 and username[0].isalpha() and len(username) <= 11:
                error = ""
                ready = True
            else:
                if len(username) < 3:
                    error = "Your username should contain at least 3 characters."
                elif not(username[0].isalpha()):
                    error = "Your username should start with a letter."
                activeError = True


        if event.type == pygame.KEYDOWN and not(key_pressed[pygame.K_RETURN]):
            if key_pressed[pygame.K_BACKSPACE]:
                username = username[:-1]
            else:
                username += event.unicode
                username = unicodedata.normalize('NFD', username).encode('ascii', 'ignore').decode("utf-8")
                activeError = False
        

    pygame.time.Clock().tick(fps)
    pygame.display.flip()


readyAge = False
instruction = bigFont.render("Indicate your age : ", True, white)
instructionRect = instruction.get_rect(center=(lengthScreen/2, heightScreen * (20/100)))
activeError = False
# Pre-game loop
while not(readyAge):
    errorMessage = mediumFont.render(error, True, red)
    errorRect = errorMessage.get_rect(center=(lengthScreen/2, heightScreen * (75/100)))

    screen.fill(black)
    screen.blit(instruction, instructionRect)
    pygame.draw.rect(screen, white, inputRect, 0, 13)
    pygame.draw.rect(screen, black, inputRectInside, 0, 10)
    ageSurface = mediumFont.render(age, True, brighterGrey)
    targetRectInput = ageSurface.get_rect(center=(inputRectInside.center))
    screen.blit(ageSurface, targetRectInput)

    if activeError:
        screen.blit(errorMessage, errorRect)

    for event in pygame.event.get():
        key_pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()

        if key_pressed[pygame.K_RETURN]:
            try:
                age_for_diff = int(age)
                if age_for_diff <= 0:
                    error = "You can't be 0 or younger..."
                    activeError = True
                else:
                    if age_for_diff >= 12:
                        defaultDiff = 6
                        speed = 4
                    elif age_for_diff > 10:
                        defaultDiff = 6
                        speed = 3
                    elif age_for_diff > 8:
                        defaultDiff = 5
                        speed = 3
                        listLifeRect.insert(0, lifeRect4)
                    elif age_for_diff > 5:
                        defaultDiff = 5
                        speed = 3
                        listLifeRect.insert(0, lifeRect4)
                        listLifeRect.insert(0, lifeRect5)
                    else:
                        defaultDiff = 4
                        speed = 2
                        listLifeRect.insert(0, lifeRect4)
                        listLifeRect.insert(0, lifeRect5)
                        listLifeRect.insert(0, lifeRect6)
                    readyAge = True
            except ValueError:
                error = "Your age should be an integer."
                activeError = True


        if event.type == pygame.KEYDOWN and not(key_pressed[pygame.K_RETURN]):
            if key_pressed[pygame.K_BACKSPACE]:
                age = age[:-1]
            else:
                age += event.unicode
        
    pygame.time.Clock().tick(fps)
    pygame.display.flip()



inMenu = False
inGame = False
inColorSelect = False
inLB = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
    match selector:

        # On regarde si selector == 0, dans ce cas on affiche le menu
        case 0:
            inMenu = True
            while inMenu:
                mousePos = pygame.mouse.get_pos()
                screen.fill(black)
                pygame.draw.line(screen, white, (0, heightScreen * (10/100)), (lengthScreen, heightScreen * (10/100)), linesThickness)
                menuTitle = mediumFont.render("Le Menu", True, white)
                menuTitleRect = menuTitle.get_rect(center=(lengthScreen/2, (heightScreen*(10/100))/2))
                screen.blit(menuTitle, menuTitleRect)
                coinNumber = mediumFont.render(f"Coin(s): {coinsNum}", True, gold)
                coinNumberRect = coinNumber.get_rect(right=(lengthScreen - 10), centery=((heightScreen*(10/100))/2))
                screen.blit(coinNumber, coinNumberRect)

                for i in listRectMenu:
                    if listRectMenu.index(i) % 2 == 0:
                        pygame.draw.rect(screen, yellow, i)
                    else:
                        for n in range(len(listRectMenu)//2):
                            if listRectMenu[n*2 + 1].collidepoint(mousePos):
                                pygame.draw.rect(screen, grey, listRectMenu[n*2 + 1])
                            else:
                                pygame.draw.rect(screen, black, i)

                for i in listSectionText:
                    index = listSectionText.index(i) * 2 + 1
                    text = mediumFont.render(i, True, yellow)
                    targetRect = text.get_rect(center=(listRectMenu[index]).center)
                    screen.blit(text, targetRect)


                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if startRectInside.collidepoint(mousePos):
                            selector = 1
                            inMenu = False
                        elif LBRectInside.collidepoint(mousePos):
                            selector = 2
                            inMenu = False


                pygame.time.Clock().tick(fps)
                pygame.display.flip()

        # Si selector == 1, startGame
        case 1:
            with open("leaderboard.json", 'r', encoding="ascii") as f:
                leaderboard = json.load(f)

            # Personnage
            CHARACTER_DIMENSION = (40, 40)
            characterRect = pygame.Rect(lengthScreen * (15/100), heightScreen/2, CHARACTER_DIMENSION[0], CHARACTER_DIMENSION[1])
           
            running = True
            damage = 0
            score = 0
            alreadyInserted = False
            runningDiff = 35
            PxBtwPipe = heightScreen * (runningDiff/100)
            heightPipe = (heightScreen - PxBtwPipe)//2 + PxBtwPipe 
            lengthPipe = 50
            posXPipe = lengthScreen * (40/100)
            spaceNextPipe = (lengthScreen + (30/100)) // 3
            listPipe = []
            hasCollided = False
            died = False
            firstIter = True
            maxSpeed = (5 / 3) * defaultDiff
            speed = 1
            speedCount = 0
            upperLimit = pygame.Rect(0, -(maxSpeed), lengthScreen, maxSpeed)
            listRectParallax = []
            animationState = 0
            actualDiff = defaultDiff
            actualDownSpeed = 1
            clickNum = 0
            lengthGameInSec = 0
            listCoinSprite = []
            listCoinRect = []
            stateAnimCoin = 0
            DIM_COIN = (20, 20)
            counterAnim = 0
            # Le flag existe pour dire à la dernière pièce quand elle peut être calculée pour éviter les doublons
            flagCoin = False
            lastGameCoinNum = 0
            baseAngle = 0
            angle = baseAngle
            print(lengthPipe, heightPipe)

            
            

            for i in range(5):
                posY = random.uniform(heightScreen * (15/100), heightScreen * (85 / 100) - PxBtwPipe) 
                listPipe.append([pygame.Rect(posXPipe, posY - heightPipe, lengthPipe, heightPipe), pygame.Rect(posXPipe, posY + PxBtwPipe, lengthPipe, heightPipe)])
                posXPipe += spaceNextPipe 

            for i in range(5):
                posYMiddle= listPipe[i][0].bottom + PxBtwPipe // 2
                randomPosY = random.uniform(posYMiddle - 60, posYMiddle + 60)
                (targetX, targetY) = (listPipe[i][0].centerx + spaceNextPipe//2, randomPosY) 
                listCoinRect.append(pygame.Rect(targetX, targetY, DIM_COIN[0], DIM_COIN[1]))

            listParallax = []
            # Cette section permet d'adapter les images au format de ma fenêtre.
            # On opère dans un second temps un changement du format pixel sur les images .png qui possèdent un alpha.
            for i in range(4):
                image = pygame.transform.scale(pygame.image.load(os.path.join("images/parallax", f"{i+1}.png")), (lengthScreen, heightScreen))
                image = pygame.Surface.convert_alpha(image)
                listParallax.append(image)
                listRectParallax.append(screen.get_rect(center=(lengthScreen//2, heightScreen//2)))

            listSprite = []
            for i in range(4):
                image = pygame.transform.scale(pygame.image.load(os.path.join("images/sprite", f"{i+1}.png")), CHARACTER_DIMENSION)
                image = pygame.Surface.convert_alpha(image)
                listSprite.append(image)


            # On utilise .copy() ici pour que listSpriteIG ne contiennent pas des références vers les valeurs de listSprite mais 
            # soit bel et bien une copie de la liste originale.
            # Sans ça, à chaque modification apportée à une valeurs de listSpriteIG, les valeurs de listSprite sont modifiées également
            listSpriteIG = listSprite.copy()

            counterRot = 0

            pointRect = pygame.Rect(listPipe[0][0].left, listPipe[0][0].bottom, lengthPipe, PxBtwPipe)
            
            listSpritePipe = []
            for i in range(len(listPipe)):
                image = pygame.transform.scale(pygame.image.load(os.path.join("images/tuyaux", f"{random.randint(0, 14)}.png")), (lengthPipe, heightPipe))
                image = pygame.Surface.convert(image)
                image2 = pygame.transform.scale(pygame.image.load(os.path.join("images/tuyaux", f"{random.randint(0, 14)}.png")), (lengthPipe, heightPipe))
                image2 = pygame.Surface.convert(image2)
                listSpritePipe.append([image, image2])

            for i in range(8):
                image = pygame.transform.scale(pygame.image.load(os.path.join("images/coins", f"{i}.png")), DIM_COIN)
                image = pygame.Surface.convert_alpha(image)
                listCoinSprite.append(image)
        
            # Lancement de la musique
            pygame.mixer.music.load("./sons/JetpacK_Theme.wav")
            pygame.mixer.music.play(loops=-1)
            pygame.mixer.music.set_volume(0.3)
            coinSound = pygame.mixer.Sound("./sons/coin_collect.mp3")
            coinSound.set_volume(0.5)
            pipeHitSound = pygame.mixer.Sound("./sons/pipe_hit_sound.wav")


            while running:

                # Pour éviter un effet de pénétration des tuyaux par le corps du character, on set la valeur
                # de son right au left du tuyau (idem pour le top ou bottom selon le contexte)
                # Ici on vient donc rétablir le x, car c'est la seule valeur à être toujours impactée après la remise en place
                if characterRect.x < lengthScreen * (15/100):
                    characterRect.move_ip(1, 0)

                PxBtwPipe = heightScreen * (runningDiff/100)
                
                if died:
                    pygame.time.wait(1500)
                    selector = 5
                    lastScore = score
                    listScore.append(score)
                    endTime = time.time()
                    lengthGameInSec = endTime - startTime
                    running = False

                # Dessin et initialisation
                key_pressed = pygame.key.get_pressed()

                screen.fill(white)

                for i in range(len(listParallax)):
                    screen.blit(listParallax[i], (listRectParallax[i]))
                    screen.blit(listParallax[i], (listRectParallax[i].left + lengthScreen, listRectParallax[i].y))


            # Affichage du sprite player
                screen.blit(listSpriteIG[animationState], listSpriteIG[animationState].get_rect(center=(characterRect.center)))
                print(listSpriteIG[animationState].get_size())

                for i in range(len(listPipe)):
                    screen.blit(listSpritePipe[i][0], listPipe[i][0])
                    screen.blit(listSpritePipe[i][1], listPipe[i][1])

                
                scoreSurface = bigFont.render(f"{score}", True, silver)
                scoreRect = scoreSurface.get_rect(left=(10), top=(10))
                speedStatSurface = mediumFont.render(f"Speed : {actualDiff}", True, silver)
                speedRect = speedStatSurface.get_rect(left=(10), top=(spaceBtwStats))
                screen.blit(speedStatSurface, speedRect)
                screen.blit(scoreSurface, scoreRect)


                for coin in listCoinRect:
                    screen.blit(listCoinSprite[stateAnimCoin], coin)

                coinsCollected = mediumFont.render(f"Coin(s) : {coinsNum}", True, gold)
                coinsCollectedRect = coinsCollected.get_rect(left=(10), bottom=(heightScreen - 10))
                screen.blit(coinsCollected, coinsCollectedRect)

                if damage == 0:
                    for i in listLifeRect:
                        pygame.draw.rect(screen, red, i)
                elif damage == len(listLifeRect):
                    for i in listLifeRect:
                        pygame.draw.rect(screen, grey, i)
                elif (damage - 1) in range(0, len(listLifeRect)) and not(damage > len(listLifeRect)):
                    for i in listLifeRect[0:damage]:
                        pygame.draw.rect(screen, grey, i)
                    for i in listLifeRect[damage:]:
                        pygame.draw.rect(screen, red, i)

                if damage == len(listLifeRect) and not(alreadyInserted):
                    data = [username, score]
                    screen.blit(listSpriteIG[2], characterRect)

                    for i in range(len(leaderboard)):
                        if score > leaderboard[i][1]:
                            leaderboard.insert(i, data)
                            break
                        elif (score == leaderboard[i][1]) and (len(leaderboard) < 10):
                            leaderboard.insert(i + 1, data)
                            break
                    else:
                        if len(leaderboard) < 10:
                            leaderboard.append(data)

                    with open("leaderboard.json", 'w', encoding="ascii") as f:
                        json.dump(leaderboard[0:10], f, indent=4, ensure_ascii=False)
                    alreadyInserted = True
                    continue

                elif damage == len(listLifeRect):
                    gameOver = mediumFont.render("You died.", True, red)
                    gameOverRect = gameOver.get_rect(center=(lengthScreen/2, heightScreen/2))
                    # On redessine l'écran pour éviter les superpositions de sprite
                    screen.fill(white)
                    for i in range(len(listParallax)):
                        screen.blit(listParallax[i], (listRectParallax[i]))
                        screen.blit(listParallax[i], (listRectParallax[i].left + lengthScreen, listRectParallax[i].y))
                    screen.blit(listSpriteIG[2], characterRect)
                    for i in range(len(listPipe)):
                        screen.blit(listSpritePipe[i][0], listPipe[i][0])
                        screen.blit(listSpritePipe[i][1], listPipe[i][1])
                    
                    screen.blit(gameOver, gameOverRect)
                    died = True
                    pygame.display.flip()
                    continue


                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYUP:
                        clickNum += 1



                if listPipe[0][0].right <= 0: 
                    posY = random.uniform(heightScreen * (15/100), heightScreen * (85 / 100) - PxBtwPipe)
                    del listPipe[0]
                    del listSpritePipe[0]
                    listPipe.append([pygame.Rect(listPipe[-1][0].left + spaceNextPipe, posY - heightPipe, lengthPipe, heightPipe), pygame.Rect(listPipe[-1][1].left + spaceNextPipe, posY + PxBtwPipe, lengthPipe, heightPipe)])
                    image = pygame.transform.scale(pygame.image.load(os.path.join("images/tuyaux", f"{random.randint(0, 14)}.png")), (lengthPipe, heightPipe))
                    image = pygame.Surface.convert(image)
                    image2 = pygame.transform.scale(pygame.image.load(os.path.join("images/tuyaux", f"{random.randint(0, 14)}.png")), (lengthPipe, heightPipe))
                    image2 = pygame.Surface.convert(image2)
                    listSpritePipe.append([image, image2])
                    flagCoin = True

                if hasCollided:
                    pygame.time.wait(1500)
                    hasCollided = False
                    spacePressed = False
                    goodPos = (listPipe[0][0].bottom + (PxBtwPipe//2))
                    countColor = 0
                    if characterRect.centery < goodPos:
                        speedForCenter =  math.ceil((goodPos - characterRect.centery) / ((10/100) * heightScreen))
                        upCenter = True
                    else:
                        speedForCenter = -math.ceil((characterRect.centery - goodPos) / ((10/100) * heightScreen))
                        upCenter = False

                    while not(spacePressed):
                        screen.fill(white)
                        for i in range(len(listParallax)):
                            screen.blit(listParallax[i], (listRectParallax[i]))
                            screen.blit(listParallax[i], (listRectParallax[i].left + lengthScreen, listRectParallax[i].y))
                        if countColor % 60 == 0:
                            colorCharacterDamage = 2
                        elif countColor % 30 == 0:
                            colorCharacterDamage = 3

                        for i in range(len(listPipe)):
                            screen.blit(listSpritePipe[i][0], listPipe[i][0])
                            screen.blit(listSpritePipe[i][1], listPipe[i][1])

                        screen.blit(listSprite[colorCharacterDamage], characterRect)

                        for coin in listCoinRect:
                            screen.blit(listCoinSprite[stateAnimCoin], coin)

                        coinsCollected = mediumFont.render(f"Coin(s) : {coinsNum}", True, gold)
                        coinsCollectedRect = coinsCollected.get_rect(left=(10), bottom=(heightScreen - 10))
                        screen.blit(coinsCollected, coinsCollectedRect)

                        if damage == 0:
                            for i in listLifeRect:
                                pygame.draw.rect(screen, red, i)
                        elif damage == len(listLifeRect):
                            for i in listLifeRect:
                                pygame.draw.rect(screen, grey, i)
                        elif (damage - 1) in range(0, len(listLifeRect)) and not(damage > len(listLifeRect)):
                            for i in listLifeRect[0:damage]:
                                pygame.draw.rect(screen, grey, i)
                            for i in listLifeRect[damage:]:
                                pygame.draw.rect(screen, red, i)
                        key_pressedCollision = pygame.key.get_pressed()
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()

                        if characterRect.centery == goodPos:
                            continueText = mediumFont.render("Press 'SPACE' to continue", True, red)
                            continueTextRect = continueText.get_rect(center=(lengthScreen/2, heightScreen/2))
                            screen.blit(continueText, continueTextRect)
                            if key_pressedCollision[pygame.K_SPACE]:
                                spacePressed = True
                        elif upCenter and characterRect.centery > goodPos:
                            characterRect.centery = goodPos
                        elif not(upCenter) and characterRect.centery < goodPos:
                            characterRect.centery = goodPos
                        else:
                            characterRect.move_ip(0, speedForCenter)

                        if counterAnim == 6:
                            counterAnim = 0
                            stateAnimCoin += 1
                            if stateAnimCoin > len(listCoinSprite) - 1:
                                stateAnimCoin = 0
                        counterAnim += 1
                        countColor += 1
                        pygame.display.flip()
                        pygame.time.Clock().tick(fps)
                    
                
                if firstIter:
                    continueText = mediumFont.render("Press 'SPACE' to start", True, red)
                    continueTextRect = continueText.get_rect(center=(lengthScreen/2, heightScreen/2))
                    screen.blit(continueText, continueTextRect)
                    if key_pressed[pygame.K_SPACE]:
                        firstIter = False
                        startTime = time.time()
                    pygame.display.flip()
                    pygame.time.Clock().tick(fps)
                    continue

                if characterRect.colliderect(listCoinRect[0]):
                    coinSound.play()
                    listCoinRect[0].right = 0
                    coinsNum += 1
                    lastGameCoinNum += 1

                    
                


                # Calcul des mouvements


                if characterRect.colliderect(listPipe[0][0]) or characterRect.colliderect(listPipe[0][1]):
                    pipeHitSound.play()
                    damage += 1
                    if characterRect.left >= listPipe[0][0].left:
                        if characterRect.top <= listPipe[0][0].bottom:
                            characterRect.top = listPipe[0][0].bottom
                        else:
                            characterRect.bottom = listPipe[0][1].top
                    else:
                        characterRect.right = listPipe[0][0].left
                    if damage < len(listLifeRect):
                        # On redessine l'écran pour éviter les superpositions de sprite
                        screen.fill(white)
                        for i in range(len(listParallax)):
                            screen.blit(listParallax[i], (listRectParallax[i]))
                            screen.blit(listParallax[i], (listRectParallax[i].left + lengthScreen, listRectParallax[i].y))
                        screen.blit(listSpriteIG[2], characterRect)
                        for i in range(len(listPipe)):
                            screen.blit(listSpritePipe[i][0], listPipe[i][0])
                            screen.blit(listSpritePipe[i][1], listPipe[i][1])


                        hasCollided = True
                        damageText = mediumFont.render("Too bad, you hit a pipe...", True, red)
                        damageTextRect = damageText.get_rect(center=(lengthScreen/2, heightScreen/2))
                        screen.blit(damageText, damageTextRect)
                    else:
                        continue

                if characterRect.bottom >= heightScreen:
                    characterRect.bottom = heightScreen
                    damage += 1
                    if damage < len(listLifeRect):
                        # On redessine l'écran pour éviter les superpositions de sprite
                        screen.fill(white)
                        for i in range(len(listParallax)):
                            screen.blit(listParallax[i], (listRectParallax[i]))
                            screen.blit(listParallax[i], (listRectParallax[i].left + lengthScreen, listRectParallax[i].y))
                        screen.blit(listSpriteIG[2], characterRect)
                        for i in range(len(listPipe)):
                            screen.blit(listSpritePipe[i][0], listPipe[i][0])
                            screen.blit(listSpritePipe[i][1], listPipe[i][1])
                        hasCollided = True
                        damageText = mediumFont.render("No, you can't pass through the ground...", True, red)
                        damageTextRect = damageText.get_rect(center=(lengthScreen/2, heightScreen/2))
                        screen.blit(damageText, damageTextRect)
                    else:
                        continue

                if listCoinRect[0].right < 0 and flagCoin:
                    flagCoin = False
                    del listCoinRect[0]
                    posYMiddle= listPipe[-1][0].bottom + PxBtwPipe // 2
                    randomPosY = random.uniform(posYMiddle - 60, posYMiddle + 60)
                    (targetX, targetY) = (listPipe[-1][0].centerx + spaceNextPipe//2, randomPosY) 
                    listCoinRect.append(pygame.Rect(targetX, targetY, DIM_COIN[0], DIM_COIN[1]))

                if not(hasCollided):
                
                    if key_pressed[pygame.K_SPACE]:
                        animationState = 1
                        characterRect.y -= maxSpeed
                        animationState = 1
                        speed = 1
                        
                        if counterRot < 10:
                            for i in range(len(listSprite)):
                                listSpriteIG[i] = pygame.transform.rotate(listSprite[i], counterRot)
                            counterRot += 1

                        if characterRect.colliderect(upperLimit):
                            characterRect.top = upperLimit.bottom
                    else: 
                        characterRect.y += speed
                        animationState = 0
                        speedCount += 1
                        if counterRot > -10:
                            for i in range(len(listSprite)):
                                listSpriteIG[i] = pygame.transform.rotate(listSprite[i], counterRot)
                            counterRot -= 1
                        if (speed < maxSpeed) and speedCount % 5 == 0:
                            speed += actualDownSpeed
                            speedCount = 0


                    for pipes in listPipe:
                        pipes[0].move_ip(-(actualDiff), 0)
                        pipes[1].move_ip(-(actualDiff), 0)

                    for coin in listCoinRect:
                        coin.move_ip(-(actualDiff), 0)
                        
                    pointRect.move_ip(-(actualDiff), 0)

                    if characterRect.colliderect(pointRect):
                        pointRect = pygame.Rect(listPipe[1][0].left, listPipe[1][0].bottom, lengthPipe, PxBtwPipe)
                        score+=1
                        if score == 50:
                            actualDownSpeed += 1
                        if score % 25 == 0 and not(actualDiff > (defaultDiff + 3)) and score > 1:
                            actualDiff += 1
                            maxSpeed += 1
                        if score % 5 == 0 and runningDiff > 23:
                            runningDiff -= 1
                            
                    

                    for i in range(len(listRectParallax)):
                        listRectParallax[i].move_ip(-(actualDiff - len(listRectParallax) + i), 0)
                        if listRectParallax[i].right <= 0:
                            listRectParallax[i].left = 0

                    
                    if counterAnim == 6:
                        counterAnim = 0
                        stateAnimCoin += 1
                        if stateAnimCoin > len(listCoinSprite) - 1:
                            stateAnimCoin = 0

                    counterAnim += 1

                pygame.display.flip()
                pygame.time.Clock().tick(fps)
                # Si selector == 2, afficher le LB
        case 2:
            gapBwScore = (heightScreen * (90/100))/10 
            inLB = True
            while inLB:
                mousePos = pygame.mouse.get_pos()
                screen.fill(black)
                pygame.draw.rect(screen, brighterGrey, closingSign)
                if closingSignInside.collidepoint(mousePos):
                    pygame.draw.rect(screen, red, closingSignInside)
                    XSign = bigFont.render("X", True, white)
                    
                else: 
                    pygame.draw.rect(screen, black, closingSignInside)
                    XSign = bigFont.render("X", True, brighterGrey)       

                XSignRect = XSign.get_rect(center=(closingSign.centerx + 2, closingSign.centery + 5))
                screen.blit(XSign, XSignRect)
                # tracer les lignes pour séparer les scores
                for i in range(10):
                    new_pos = heightScreen * (10/100) + (gapBwScore)*(i+1)
                    pygame.draw.line(screen, brighterGrey, (0, new_pos), (lengthScreen, new_pos), linesThickness)
                
                pygame.draw.line(screen, white, (0, heightScreen * (10/100)), (lengthScreen, heightScreen * (10/100)), linesThickness)
                scoreTable = mediumFont.render("Score", True, white)
                scoreTableRect = scoreTable.get_rect(center=((lengthScreen*(75/100)/2 + lengthScreen * (25/100)), (heightScreen*(10/100))/2))
                screen.blit(scoreTable, scoreTableRect)

                pygame.draw.line(screen, white, (lengthScreen * (25/100), 0), (lengthScreen * (25/100), heightScreen), linesThickness)
                nameTable = mediumFont.render("Player", True, white)
                nameTableRect = nameTable.get_rect(center=(lengthScreen*(25/100)/2, heightScreen*(10/100)/2))
                screen.blit(nameTable, nameTableRect)


                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if closingSignInside.collidepoint(mousePos):
                            selector = 0
                            inLB = False


                with open("leaderboard.json", 'r', encoding="utf-8") as f:
                    leaderboard = json.load(f)
                    for i in range(len(leaderboard)):
                        gap = (10/100) * heightScreen * (90/100)
                        centerXPlayer = (lengthScreen*(25/100))/2
                        centerXScore = (lengthScreen*(75/100)/2 + lengthScreen * (25/100))
                        centerY = (gap*i) + gap/2 + heightScreen*(10/100)
                        if i == 0:
                            player = mediumFont.render(leaderboard[i][0], True, gold)
                            scoreLB = mediumFont.render(str(leaderboard[i][1]), True, gold)
                        elif i == 1:
                            player = mediumFont.render(leaderboard[i][0], True, silver)
                            scoreLB = mediumFont.render(str(leaderboard[i][1]), True, silver)
                        elif i == 2:
                            player = mediumFont.render(leaderboard[i][0], True, bronze)
                            scoreLB = mediumFont.render(str(leaderboard[i][1]), True, bronze)
                        else:
                            player = mediumFont.render(leaderboard[i][0], True, brighterGrey)   
                            scoreLB = mediumFont.render(str(leaderboard[i][1]), True, brighterGrey)    
                        playerRect = player.get_rect(center=(centerXPlayer, centerY)) 
                        scoreRect = scoreLB.get_rect(center=(centerXScore, centerY))         
                        screen.blit(player, playerRect)
                        screen.blit(scoreLB, scoreRect)


                pygame.time.Clock().tick(fps)
                pygame.display.flip()

            
        # Si selector == 3, sélection des couleurs pour l'oiseau
        case 3:
            '''TODO'''

        # Si selector == 4, section bonus
        case 4:      
            '''TODO'''
            
        case 5:
            # Si selector == 5, écran de fin/récapitulatif de la partie + demander si l'utilisateur veut rejouer
            # Si oui, selector == 1
            # Si non, Afficher le nombre de try + le meilleur score de toutes les parties
            endScreenRect = pygame.Rect(lengthScreen*(25/100), heightScreen*(40/100), lengthScreen*(50/100), heightScreen*(20/100))
            endScreenRectInside = firstScreenRect.inflate(-10, -10)
            endText = ""
            endTextFinal = f"Well done {username}!"
            endScreen = True
            targetIndex = 0
            counter = 0
            averageScore = 0
            for score in listScore:
                averageScore += score
            averageScore /= len(listScore)
            pygame.mixer.music.load("./sons/keyboard_sound.mp3")

            while endScreen:
                endSurface = mediumFont.render(endText, True, red)
                targetRect = endSurface.get_rect(center=(lengthScreen/2, heightScreen/2))
                screen.fill(black)
                pygame.draw.rect(screen, red, endScreenRect, 0, 13)
                pygame.draw.rect(screen, black, endScreenRectInside, 0, 10)
                screen.blit(endSurface, targetRect)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                if endText == endTextFinal:
                    endScreen = False
                
                if counter % 8 == 0 and targetIndex < len(endTextFinal):
                    pygame.mixer.music.play()
                    endText += endTextFinal[targetIndex]
                    targetIndex += 1
                

                counter += 1
                pygame.display.flip()
                pygame.time.Clock().tick(fps)
            
            pygame.time.wait(1000)

            # Ecran pour les statistiques, possibilités de recommencer ou de revenir au menu
            inStats = True
            spaceBtwText = heightScreen * (10/100)
            subtitleMargin = (lengthScreen//2) * (20/100)
            headerScore = bigFont.render("Scores:", True, yellow)
            headerScoreRect  = headerScore.get_rect(left=((lengthScreen//2) * (10/100)), top=(heightScreen * (5/100)))
            headerStats = bigFont.render("Stats (last game):", True, yellow)
            headerStatsRect  = headerStats.get_rect(left=((lengthScreen//2) + (lengthScreen//2) * (10/100)), top=(heightScreen * (5/100)))


            gotoMenu = pygame.Rect(lengthScreen * (5/100), heightScreen * (80/100), (lengthScreen / 2) - lengthScreen * (5/100) * 2, heightScreen * (15/100))
            gotoMenuInside = gotoMenu.inflate(-(linesThickness*2), -(linesThickness*2))
            startAgain = gotoMenu.move(lengthScreen//2, 0)
            startAgainInside = startAgain.inflate(-(linesThickness*2), -(linesThickness*2))
            listButtons = [gotoMenu, gotoMenuInside, startAgain, startAgainInside]
            
            startAgainText = mediumFont.render("Start again !", True, yellow)
            gotoMenuText = mediumFont.render("Go to Menu", True, yellow)

            # Subtitles for score section
            lastScore = smallFont.render(f"You just did : {lastScore}", True, yellow)
            worstScore = smallFont.render(f"Worst score : {min(listScore)}", True, yellow)
            bestScore = smallFont.render(f"Best score : {max(listScore)}", True, yellow)
            averageScoreSurf = smallFont.render(f"Average score : {round(averageScore, 1)}", True, yellow)
            # Subtitles for stats section
            totalClicks = smallFont.render(f"Total of clicks : {clickNum}", True, yellow)
            clicksPerSecsAverage = smallFont.render(f"Average clicks per second : {round(clickNum / lengthGameInSec, 1)}", True, yellow)
            lastGameCoinsCollected = smallFont.render(f"Coins collected : {lastGameCoinNum}", True, yellow)

            scoreListData = [lastScore, worstScore, bestScore, averageScoreSurf]
            statsList = [totalClicks, clicksPerSecsAverage, lastGameCoinsCollected]

            while inStats:
                mousePos = pygame.mouse.get_pos()
                screen.fill(black)
                pygame.draw.line(screen, brighterGrey, (lengthScreen // 2, heightScreen * (5/100)), (lengthScreen // 2, heightScreen * (75/100)), linesThickness)
            
                screen.blit(headerScore, headerScoreRect)        
                screen.blit(headerStats, headerStatsRect)

                for score in scoreListData:
                    screen.blit(score, score.get_rect(left=(lengthScreen * (8/100)), top=(heightScreen*(15/100) + spaceBtwText)))
                    spaceBtwText += heightScreen * (10/100)

                spaceBtwText = heightScreen * (10/100)
                
                for stat in statsList:
                    screen.blit(stat, stat.get_rect(left=((lengthScreen//2) + lengthScreen * (8/100)), top=(heightScreen*(15/100) + spaceBtwText)))
                    spaceBtwText += heightScreen * (10/100)

                spaceBtwText = heightScreen*(10/100)

                for i in listButtons:
                    if listButtons.index(i) % 2 == 0:
                        pygame.draw.rect(screen, yellow, i)
                    else:
                        for n in range(len(listButtons)//2):
                            if listButtons[n*2 + 1].collidepoint(mousePos):
                                pygame.draw.rect(screen, grey, listButtons[n*2 + 1])
                            else:
                                pygame.draw.rect(screen, black, i)
                
                screen.blit(startAgainText, startAgainText.get_rect(center=(startAgainInside.center)))
                screen.blit(gotoMenuText, gotoMenuText.get_rect(center=(gotoMenuInside.center)))



            # Affichage des statistiques 



                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if startAgainInside.collidepoint(mousePos):
                            selector = 1
                            inStats = False
                        elif gotoMenuInside.collidepoint(mousePos):
                            selector = 0
                            inStats = False

                pygame.display.flip()
                pygame.time.Clock().tick(fps)


        case _:
            print(f"DEBUG: ERROR SOMEWHERE, SELECTOR SHOULD NOT TAKE THIS VALUE")

