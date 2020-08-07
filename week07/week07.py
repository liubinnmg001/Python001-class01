from abc import ABCMeta, abstractmethod
class Zoo:
    #属性：名字
    def __init__(self, name=''):
        self.name = name
        self.animal_list = []
    #添加动物方法：同一个动物实例不能被重复添加
    def add_animal(self, animal_name):
        if animal_name not in self.animal_list:
            self.animal_list.append(animal_name)
        else:
            print('动物园已存在该实例')    

#不允许被实例化
class Animal(metaclass=ABCMeta):
    #属性：体型，类型，性格
    #体型分值从0到100分，50分为中等体型，>50 偏胖，<50 偏瘦
    @abstractmethod
    def __init__(self, somatotype=50, genre='raptatorial', personality='ferocity',ferocious='False'):
        self.somatotype = somatotype
        self.genre = genre
        self.personality = personality
    #是否属于凶猛动物：同时满足  “体型 >= 中等” “食肉类型”  “性格凶猛”
        if  self.somatotype >= 50 and self.genre == 'raptatorial' and self.personality == 'ferocity':
            self.ferocious = 'True'
        else:
            self.ferocious = 'False'

class Cat(Animal):
    #属性：名字，叫声，是否适合作为宠物
    def __init__(self, name='', yell='True', pet='True',somatotype=40, genre='raptatorial', personality='ferocity'):
        self.name = name
        self.yell = yell
        self.pet = pet
        super().__init__(somatotype=somatotype, genre=genre, personality=personality)

if __name__ == '__main__':
    # a = Animal() 不能实例化，否则报错"TypeError: Can't instantiate abstract class Animal with abstract methods __init__"
    z = Zoo('beijing')
    c = Cat('苏拉','True','True')
    d = Cat('丁丁','True','True') 
    e = Cat('花花','True','True',somatotype=90, genre='Rhombozoa', personality='docile')
    print(f'猫的名字：{c.name}，是否属于凶猛动物：{c.ferocious}') 
    print(f'猫的体型分值：{c.somatotype}') 
    z.add_animal(c)
    z.add_animal(d)
    z.add_animal(d) #重复添加报"动物园已存在该实例"