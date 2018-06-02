class ant:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def crawl(self,x,y):
        self.x=x
        self.y=y
        print('爬行')
        self.info()
    def info(self):
        print('当前位置:(%d,%d)'%(self.x,self.y))
    def attack(self):
        print("用嘴咬")
class flyant(ant):
    def attack(self):
        print("用尾针")
    def fly(self,x,y):
        print('飞行')
        self.x=x
        self.y=y
        self.info()
fa=flyant()
fa.crawl(3,5)
fa.fly(10,14)
fa.attack()
