import time
import os 

# Função de limpar o terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

list_monster = []

# Herói principal
link = {
    'nome': 'Link',
    'level': 1,
    'exp': 0,
    'exp_max': 10,
    'HP': 5,
    'mana': 10,
    'atk': 3
}

# Função para criar inimigos
def create_monster(level):
    new_monster = {
        'nome': f"Goblin #{level}",
        'HP': 2 + level,
        'atk': 2 + level,
        'level': level,
        'exp': 5 * level
    }
    return new_monster

# Função para gerar lista de monstros
def gen_monster(n_monster):
    for x in range(n_monster):
        monster = create_monster(x + 1)
        list_monster.append(monster)

# Função para ganhar exp e upar
def give_experience(monster):
    link['exp'] += monster['exp']
    print(f"{link['nome']} ganhou {monster['exp']} pontos de experiencia!")
    up_level()

# Função para upar
def up_level():
    if link['exp'] >= link['exp_max']:
        link['level'] += 1
        link['exp'] = 0
        link['exp_max'] *= 2
        link['HP'] += 2
        link['atk'] += 2
        print(f"{link['nome']} upou de level!")

# Função de atacar inimigo
def atack_npc(monster):
    monster['HP'] -= link['atk']
    print(f"{link['nome']} atacou {monster['nome']} e causou {link['atk']} de dano.")

# Função de ser atacado
def atack_link(monster):
    link['HP'] -= monster['atk']
    print(f"{monster['nome']} atacou {link['nome']} e causou {monster['atk']} de dano.")

# Função de morte de npc
def death_npc(monster):
    if monster['HP'] <= 0:
        print(f"{monster['nome']} foi derrotado!")
        give_experience(monster)
        return True
    return False

# Função para game over
def death_link():
    if link['HP'] <= 0:
        print('GAME OVER!!')
        return True
    return False

# Função para mostrar herói
def show_link():
    print(f"Nome: {link['nome']} // Vida: {link['HP']} // Level: {link['level']} // Experiencia: {link['exp']}")

# Função para mostrar monstro
def show_monster(monster):
    print(f"Nome: {monster['nome']} // Vida: {monster['HP']} // Ataque: {monster['atk']} // Experiencia: {monster['exp']}")

# Fluxo principal do jogo
gen_monster(5)  # Gerar 5 monstros

while True:
    clear_screen()
    print('--------------')
    show_link()
    if list_monster:
        current_monster = list_monster[0]
        show_monster(current_monster)
    else:
        print('Não há mais monstros.')
        break
    print('--------------')

    action = input('O que quer fazer?  (1) Atacar inimigo  //  (2) Sair ')

    if action == '1':
        atack_npc(current_monster)
        if death_npc(current_monster):
            list_monster.pop(0)
            if not list_monster:
                print('Todos os monstros foram derrotados! Você venceu!')
                break
        else:
            atack_link(current_monster)
            if death_link():
                break
    elif action == '2':
        break
    else:
        print('AÇÃO INVALIDA')

show_link()

time.sleep(8)

clear_screen()

print('Jogo Terminado')

time.sleep(5)
clear_screen()
