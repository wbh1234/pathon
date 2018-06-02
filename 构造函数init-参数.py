class csinit:
    def __init__(self,x,y=0):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
a=csinit(3)
print(a.add())
b=csinit(2.4)
print(b.add())
