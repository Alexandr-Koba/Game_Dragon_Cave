import random
import time

def displayIntro():
    print('''
    --ТЫ НАХОДИШСЯ В ДРАКОН-ВОРЛД--
     
    --и этот мир заселён ДРАКОНАМИ!!!--
    --Перед собой Ты видишь ДВЕ пещеры-- 
    --в одной из них Добрый дракон-- 
    --который поделится своими сокровищами-- 
          
    --Во второй Злой и голодный-- 
    --который проглотит тебя мигом--''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print("В какую пещеру Ты войдешь (нажми клавишу 1 или 2)")
        cave = input()
    return cave

def checkCave(chosenCave):
    print("Вы приближаетесь к пещере...")
    time.sleep(2)
    print("В темноте страшно...")
    time.sleep(2)
    print("Огромный дракон выпрыгивает перед тобой! он раскрывает пасть и...")
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print("Йоу человек держи кучку золота и чемодан $$$$$$")
    else:
        print("...Моментально тебя СЖИРАЕТ...")
        time.sleep(2)
        print("ты даже не успел почувствовать боль... бедняга.")

playAgain = "да"
while playAgain == 'да' or playAgain == 'д':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Попытайте удачу еще раз 'да' или 'нет'")
    playAgain = input()


displayIntro()
chooseCave()