print('Добро пожаловать в игру по вселенной Erehat! \n\nС чего начнём? (-? список команд)\n')
import random
import time
#карта: номер изображения, уровень, мораль, раса

card1 = ('Воин - странник', 1, 5, 0, 'hum')
card2 = ('Орк - охотник', 2, 4, 0, 'orc')
card3 = ('Гном Харима', 3, 3, 0, 'gnm')
card4 = ('Глубинная тварь', 1, 5, 0, 'dem')
card5 = ('Страж лесов', 2, 4, 0, 'elf')


#работа

def play(
    que,
    card1,
    card2,
    card3,
    card4,
    card5,
    ):
    battle_console(
        que,
        card1,
        card2,
        card3,
        card4,
        card5,
        )
        


    #вызов списка армии игрока:    
    if que == 'mv':
        k = 0
        for i in player_army:
            if k < int(len(player_army)):
                i = player_army[k]
                i = str(i[1])
                print('{}: {}'.format(str(k), i))
            else:
                break
    



def console_menu():
    while True:
        que = input('Menu >')
        if que == 'ex':
            print('---Выход---')
            exit()
        elif que == '-play':
            console_battle(
                    card1,
                    card2,
                    card3,
                    card4,
                    card5,
                    )
            break
        elif que == '-?':
            print('-----\nКоманды:'
                  '\n-? список команд'
                  '\n-play начать игру'
                  '\nex выход из игры\n'
                  )
        else:
            print('Непонятная команда...')

def console_battle(
    card1,
    card2,
    card3,
    card4,
    card5,
    ):
    print('Начать новую игру?\n    y - да         n - нет')
    while True:
        ans = input('Answer >')
        if ans == 'n':
            print('Вернуться в меню?\n    y - да         n - нет')
            ans = input('Answer >')
            if ans == 'y':
                console_menu()
            elif ans == 'n':
                break
            else:
                print('Выберите либо yes, либо no')
                exit()
                
        elif ans == 'y':     
            while True:
                a = False

                if a == 0: #генерируем армию если нет    
                    player_army = []
                    bad_army = []

                    all_cards = [card1, card2, card3, card4, card5]

                    k1 = 0
                    if True:
                        for i in all_cards:
                            if not(k1 == 2):
                                i = random.choice(all_cards)
                                player_army.append(i)
                                print('генерация вашего войска...')
                                time.sleep(1/2)
                                k1 + 1
                            else:
                                break

                    k2 = 0
                    if True:
                        for i in all_cards:
                            if not(k2 == 2):
                                i = random.choice(all_cards)
                                bad_army.append(i)
                                print('генерация войска противника...')
                                time.sleep(1/2)
                                k2 + 1
                            else:
                                break

                    print('\nВаших воинов:'+(str(len(player_army))+'\nУ противника:'+str(len(bad_army))))
                    if True:
                        print('\nНачнём битву!\n\nКоманды: mv, vv, ')

                    a = True #сгенерировали
                else:
                    print('\n'+str(a)+'\n')



                que = input('Battle >')
                if que == 'ex':
                    print('---Выход---')
                    exit()
                elif que == '-menu':
                    console_menu()
                    break
                elif que == '-?':
                    print('-----\nКоманды:'
                          '\n-? список команд'
                          '\n-menu выйти в меню игры'
                          '\nex выход из игры\n'
                          )
                    
                elif que == 'mv': #вызов списка армии игрока:
                    k1 = 0
                    print('Ваше войско:')
                    for i in player_army:
                        if k1 < int(len(player_army)):
                            i = player_army[k1] #вызываем карту
                            i_name = str(i[0]) #название карты
                            i_lvl = str(i[2])
                            print('{}: {}    ур.{}'.format(str(k1), i_name, i_lvl))
                            k1 + 1
                        else:
                            break

                elif que == 'vv': #вызов списка армии противника:
                    k2 = 0
                    print('Войско противника:')
                    for i in bad_army:
                        if k2 < int(len(bad_army)):
                            i = bad_army[k2] #вызываем карту
                            i_name = str(i[0]) #название карты
                            i_lvl = str(i[2])
                            print('{}: {}    ур.{}'.format(str(k1), i_name, i_lvl))
                            k2 + 1
                        else:
                            break
#____________________________________________________________режим боя




                else:
                    print('Непонятная команда...')
                

        else:
            print('Непонятный ответ')
            





#активация консоли
console_menu()
        
#интерфейс
