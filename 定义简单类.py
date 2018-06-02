class Myclass:
    def info(self):
        print("定义我的类")
    def add(self,x,y):
        return x+y
sc=Myclass()
print('调用info方法的结果')
sc.info()
print('调用info方法的结果')
print(sc.add(2,3))
