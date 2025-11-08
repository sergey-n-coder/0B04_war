from abc import ABC , abstractmethod

class Weapon(ABC):
    def __init__(self,damage,name):
        self.damage = damage
        self.name = name
    @abstractmethod
    def attack(self,per):
        #print (f'Взял '{self.name})
        pass

class Sword (Weapon):
    def attack(self,per):
        print ('Боец наносит удар мечом')


#------
#@abstractclass
class Perc(ABC):
    def __init__(self,life,damage,name):
        self.life = life
        self.damage = damage
        self.name = name
        self.weapon = None # Weapon(0,'Без оружия')
    @abstractmethod
    def change_weapon(self,weapon:Weapon):
        pass

    @abstractmethod
    def attack(self,perc):
       pass

    @abstractmethod
    def attacked (self,damage):
        print ('Принт из абстрактного метода')


class Fighter(Perc):
    def __init__(self, life, damage, name,weapon :Weapon):
        super().__init__(life, damage, name)
        #self.weapon = Weapon(0,'Без оружия')
        self.weapon = weapon
    def change_weapon(self,weapon:Weapon):
        #self.damage = self.damage + weapon.damage - self.weapon.damage
        self.weapon = weapon
        print (f'Воин выбирает {self.weapon.name}')

    def attack(self,perc):
        print(f'Воин {self.name} атакует!'  )
        self.weapon.attack(perc)
    def attacked (self, damage):
        self.life = self.life - damage
        print (f' Воин {self.name} получает {damage} урона')


#-----
sword = Sword(10,'Меч кладенец')


ivan = Fighter(35,0,'Иван',sword)
monstr1 = Monster(20,0,'Кащей')

#ivan.attack(monstr1)
#ivan.change_weapon(knaif2)