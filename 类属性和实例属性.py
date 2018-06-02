class shuxing():
    classname="shuxing"
    def __init__(self,x=5):
        self.x=x
    def info(self):
        print("类变量值:",shuxing.classname)
        print("实例变量值",self.x)
    def b(self,x):
        self.x=x
    def c(self,name):
        shuxing.classname=name
t1=shuxing()
t2=shuxing()
print('初始化两个实例')
t1.info()
t2.info()
print('修改实例变量')
t1.b(3)
t1.info()
t2.info()
print('修改类变量')
t1.c('jack')
t1.info()
t2.info()
