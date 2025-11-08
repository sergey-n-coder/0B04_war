from abc import ABC , abstractmethod

class Weapon(ABC):
    def __init__(self,damage,name):
        self.damage = damage
        self.name = name
    @abstractmethod
    def attack(self):
        #print (f'Взял '{self.name})
        pass

class Sword (Weapon):
    def attack(self):
        print ('Боец наносит удар мечом')


class Pica (Weapon):
    '''Удар пикой'''
    def attack(self):
        print ('Боец наносит удар пикой')

class Knaif (Weapon):
    def attack(self):
        print ('Боец наносит удар ножом')
#------
# @abstractclass
class Perc(ABC):
    def __init__(self,life,name,weapon:Weapon):
        self.life = life
        self.name = name
        self.weapon = weapon
    @abstractmethod
    def change_weapon(self,weapon:Weapon):
        pass

    @abstractmethod
    def attack(self,per):
       pass

    #@abstractmethod
    #def attacked (self,damage):
    #    print ('Принт из абстрактного метода')

class Fighter(Perc):
    #def __init__(self, life, name,weapon :Weapon):
    #   super().__init__(life,name ,weapon)

    def change_weapon(self,weapon:Weapon):
        #self.damage = self.damage + weapon.damage - self.weapon.damage
        self.weapon = weapon
        print (f'Воин выбирает {self.weapon.name}')

    def attack(self,per: Perc):
        print(f'Воин {self.name} атакует {per.name}!' )
        self.weapon.attack()

    #def attacked (self, damage):
    #    self.life = self.life - damage
    #    print (f' Воин {self.name} получает {damage} урона')

class Monster(Perc):
    def change_weapon(self,weapon:Weapon):
        #self.damage = self.damage + weapon.damage - self.weapon.damage
        self.weapon = weapon
        print (f'Монстр выбирает {self.weapon.name}')

    def attack(self,per):
        print(f'Монстр {self.name} атакует {per.name}!' )
        self.weapon.attack()
    #def attacked (self, damage):
    #    self.life = self.life - damage
    #    print (f'Монстр {self.name} полу чает {damage} урона')
#-----
sword = Sword(10,'Меч кладенец')
knaif1 = Knaif(5,'Штык-нож')
knaif2 = Knaif(8,'Лопата')

kogti = Knaif(8,'Когти')


ivan = Fighter(35,'Иван',sword)
monstr1 = Monster(20,'Кащей',kogti)

ivan.attack(monstr1)
ivan.change_weapon(knaif1)
ivan.attack(monstr1)
#ivan.change_weapon(knaif2)