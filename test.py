import time
import os 

#função de limpar o terminal
def clear_screan():
    os.system('cls')

#heroi principal
link = {
    'nome': 'Link',
    'level': 1,
    'exp': 0,
    'exp_max': 20,
    'HP': 5,
    'mana': 10,
    'atk': 3
}

#atual inimigo principal
monster = {
    'nome': 'Goblin',
    'HP': 2,
    'atk': 2,
    'exp': 5
}

#função para ganhar exp e upar
def give_experience():
    link['exp'] += monster['exp']
    print(f"{link['nome']} ganhou {monster['exp']} pontos de experiencia!")
    up_level()

#função para upar
def up_level():
    if link['exp'] >= link['exp_max']:
        link['level'] += 1
        link['exp'] = 0
        link['exp_max'] *= 2
        link['HP'] += 2
        link['atk'] += 2
        print(f"{link['nome']} upou de level!")

#função de atacar inimigo
def atack_npc():
    monster['HP'] = monster['HP'] - link['atk']

#função de ser atacado
def atack_link():
    link['HP'] -= monster['atk']
#função de luta
def fight():
    atack_npc()
    atack_link()

#função de morte de npc
def death_npc():
    if monster['HP'] <= 0:
        print('você venceu!!')
        give_experience()
        return True
    return False

#função para game over
def death_link():
    if link['HP'] <= 0:
        print('GAME OVER!!')
        return True
    return False

#função para mostrar heroi
def show_link():
    print(
        f"Nome: {link['nome']} // Vida: {link['HP']} // Level: {link['level']} // Experiencia: {link['exp']}"
    )

def show_monster():
    print(
        f"Nome: {monster['nome']} // Vida: {monster['HP']}// Ataque: {monster['atk']} // Experiencia: {monster['exp']}"
   )

#fluxo principal do jogo
while True:
    clear_screan()
    print('--------------')
    show_link()
    show_monster()
    print('--------------')

    action = input('O que quer fazer?  (1)atacar inimigo  //  (2)Sair ')

    if action == '1':
        atack_npc()
        if death_npc():
            break
        atack_link()
        if death_link():
            break
    elif action == '2':
        break
    else:
        print('AÇÃO INVALIDA')
    
show_link()

time.sleep(8)

clear_screan()

print('Jogo Terminado')

time.sleep(5)
clear_screan()
