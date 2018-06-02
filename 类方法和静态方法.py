class mthd:
    @staticmethod #静态方法的装饰器
    def static_mthd():  #静态类定义
        print('调用静态方法！')
    @classmethod #类方法装饰器
    def class_mthd(cls):    #类方法定义，带默认方法cls
        print('调用类方法')
mthd.static_mthd()  #未实例化类，通过类名调用静态类
mthd.class_mthd()   #未实例化类，通过类名调用类方法
dm=mthd()   #实例化类
dm.static_mthd()
dm.class_mthd()
