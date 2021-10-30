import random

wins = 0        
energy = 10
power = 10
alive = True


def input_value():
    while True:
        a = input()
        if a == "1":
            return True
        elif a == "2":
            return False
        else:
            print("Введите 1 или 2")


def rand(x: int, y: int):
    return random.randint(x, y)


if __name__ == '__main__':

    while wins < 10:
        print("Рыцарь: жизни = " + str(energy) + " ,сила удара = " + str(power) + ", побед = " + str(wins))
        step = rand(0, 2)
        if step == 0:
            apple = rand(5, 10)
            print("Повезло ты нашёл яблоко! + " + str(apple) + " к жизни")
            energy = energy + apple
        elif step == 1:
            sword = rand(10, 20)
            print("Ты нашёл меч, сила удара его: " + str(sword))
            print("Если хочешь взять новый меч нажми: 1, если идёшь дальше со своим нажми: 2")
            if input_value():
                power = sword
        else:
            monster_energy = rand(5, 20)
            monster_power = rand(5, 12)
            print("Вы встретили чудовище с " + str(monster_energy) + " жизнями и с силой удара " + str(monster_power))
            print("Если хочешь атаковать чудовище нажми: 1, если позорно бежать нажми: 2")
            if input_value():
                energy = energy - monster_power
                if energy <= 0:
                    print("Game Over")
                    alive = False
                    break
                if monster_energy <= power:
                    wins = wins + 1
                    print("В этот раз тебе повезло!")
    if alive:
        print("Ура ты достиг " + str(wins) + " побед!!")
