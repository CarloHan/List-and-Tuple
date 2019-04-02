import random as r

coor_x = [0, 10]
coor_y = [0, 10]

class Turtle(object):
    def __init__(self):
        self.hp = 200 # 初始体力
        self.x = r.randint(coor_x[0], coor_x[1]) # 出生位置随机
        self.y = r.randint(coor_y[0], coor_y[1])

    def move(self):
        new_x = self.x + r.choice([1, 2, -1, -2]) # 计算随即移动后的新位置
        new_y = self.y + r.choice([1, 2, -1, -2])

        if new_x < coor_x[0]: # 检查是否超出x轴边界
            self.x = coor_x[0] - (new_x - coor_x[0])
        elif new_x > coor_x[1]:
            self.x = coor_x[1] - (new_x - coor_x[1])
        else:
            self.x = new_x

        if new_y < coor_y[0]: # 检查是否超出y轴边界
            self.y = coor_y[0] - (new_y - coor_y[0])
        elif new_y > coor_y[1]:
            self.y = coor_y[1] - (new_y - coor_y[1])
        else:
            self.y = new_y

        self.hp -= 1 # 每移动一次消耗1点hp

        return (self.x, self.y) # 返回移动后的新位置

    def eat(self):
        self.hp += 20
        if self.hp > 100:
            self.hp = 100

class Fish(object):
    def __init__(self):
        self.x = r.randint(coor_x[0], coor_x[1])
        self.y = r.randint(coor_y[0], coor_y[1])

    def move(self):
        new_x = self.x + r.choice([1, 2, -1, -2])
        new_y = self.y + r.choice([1, 2, -1, -2])

        if new_x < coor_x[0]:
            self.x = coor_x[0] - (new_x - coor_x[0])
        elif new_x > coor_x[1]:
            self.x = coor_x[1] - (new_x - coor_x[1])
        else:
            self.x = new_x

        if new_y < coor_y[0]:
            self.y = coor_y[0] - (new_y - coor_y[0])
        elif new_y > coor_y[1]:
            self.y = coor_y[1] - (new_y - coor_y[1])
        else:
            self.y = new_y

        return (self.x, self.y)

turtle = Turtle() # 生成一只乌龟
fish = []
for i in range(10): # 生成10条鱼
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print('鱼儿都被吃完了，游戏结束！')
        break
    if not turtle.hp:
        print('乌龟体力耗尽，挂掉了！')
        break

    coordinate = turtle.move() 
    for each_fish in fish[:]: # 直接在迭代器中删除列表元素是非常危险的
        if each_fish.move() == coordinate:
            turtle.eat()
            fish.remove(each_fish)
            print('有一条鱼儿被吃掉了...')
