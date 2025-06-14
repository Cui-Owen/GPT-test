class Player:
    def __init__(self, hp=100, attack=10, defense=5):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.keys = 0
        self.x = 2
        self.y = 2

    def is_alive(self):
        return self.hp > 0

class Enemy:
    def __init__(self, hp=50, attack=8, defense=2):
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

def display(map_data, player):
    for y, row in enumerate(map_data):
        line = ''
        for x, cell in enumerate(row):
            if x == player.x and y == player.y:
                line += '@'
            else:
                line += cell
        print(line)
    print(f"HP: {player.hp}  ATK: {player.attack}  DEF: {player.defense}  Keys: {player.keys}")

def battle(player, enemy):
    print("A battle begins!")
    while player.is_alive() and enemy.is_alive():
        damage_to_enemy = max(player.attack - enemy.defense, 1)
        damage_to_player = max(enemy.attack - player.defense, 1)
        enemy.hp -= damage_to_enemy
        if enemy.is_alive():
            player.hp -= damage_to_player
        print(f"You deal {damage_to_enemy} to the enemy. Enemy HP: {max(enemy.hp,0)}")
        if enemy.is_alive():
            print(f"The enemy hits back for {damage_to_player}! Your HP: {max(player.hp,0)}")
    if player.is_alive():
        print("You defeated the enemy!")
        return True
    else:
        print("You were defeated...")
        return False


def main():
    map_data = [
        list("#####"),
        list("#P E#"),
        list("# @D#"),
        list("#K S#"),
        list("#####")
    ]
    player = Player()

    while True:
        display(map_data, player)
        if not player.is_alive():
            print("Game Over!")
            break
        cmd = input("Move (w/a/s/d) or q to quit: ")
        if cmd == 'q':
            print("Thanks for playing!")
            break
        dx, dy = 0, 0
        if cmd == 'w':
            dy = -1
        elif cmd == 's':
            dy = 1
        elif cmd == 'a':
            dx = -1
        elif cmd == 'd':
            dx = 1
        else:
            continue
        new_x = player.x + dx
        new_y = player.y + dy
        if new_x < 0 or new_x >= len(map_data[0]) or new_y < 0 or new_y >= len(map_data):
            continue
        cell = map_data[new_y][new_x]
        if cell == '#':
            continue
        if cell == 'K':
            player.keys += 1
            print("You picked up a key!")
            map_data[new_y][new_x] = ' '
        elif cell == 'P':
            player.hp += 20
            print("You drank a potion. +20 HP!")
            map_data[new_y][new_x] = ' '
        elif cell == 'E':
            enemy = Enemy()
            if not battle(player, enemy):
                continue
            map_data[new_y][new_x] = ' '
        elif cell == 'D':
            if player.keys > 0:
                player.keys -= 1
                print("You used a key to open the door.")
                map_data[new_y][new_x] = ' '
            else:
                print("The door is locked. You need a key!")
                continue
        elif cell == 'S':
            print("You reached the stairs and won the game!")
            break
        player.x = new_x
        player.y = new_y

if __name__ == '__main__':
    main()
