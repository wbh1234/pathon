EengryStr = input("请输入热量值和热量标签:")
if(EengryStr[-1] in ["J","j"]):
    cal = (eval(EengryStr[0:-1]))/4.186
    print("{:.3f}cal".format(cal))
elif(EengryStr[-1] in ["L","l"]):
    J = (eval(EengryStr[0:-3]))*4.186
    print("{:.3f}J".format(J))
else:
    print("输入格式错误")
