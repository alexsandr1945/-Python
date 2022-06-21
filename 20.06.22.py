# 22.06.22 Лекция 7
# Модули и пакеты
class Dragon:
    def __init__(self,name):
        self.name=name
        self.health = 100

    def is_alive(self):
        return self.health > 0

    def get_gamage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def talk(self):
        print(self.name,' health ', self.health, '. Hit me!')

    def final_cry(self):
        print (self.name, 'is dead...')
def main():
    enemy_list =[Dragon('Smog'),Dragon('Hidra')]
    finish = False
    while not finish:
        enemy=enemy_list[0]
        enemy.talk()
        damage = int(input())
        enemy.get_gamage(damage)
        if not enemy.is_alive(): # Удаляем из списка убитого дракона
            enemy_list.pop(0)
            enemy.final_cry()
        if not enemy_list: # Проверяем пуст ли список врагов
            finish=True

    print('You win!')


main()
