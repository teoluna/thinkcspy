class Hero:
    def __init__(self):
        self.health = 30
        self.armor = 0
    
    def decrease_health(self, x):
        if x < 0:
            raise ValueError("Can be only positive integer") 
        
        self.health = self.health - x
        
        if self.health < 0:
            self.health = 0

        return self
    
    def atack(self, enemy):
        enemy.decrease_health(-300)
        return self
        
warlock = Hero()
uter = Hero()

warlock.atack(uter)
print(uter.health)