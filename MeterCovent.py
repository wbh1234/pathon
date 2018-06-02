MeterChange = input("请输入带有符号m或in的长度")
if MeterChange[-1] in ["M","m"]:
    IN = (eval(MeterChange[0:-1])) *39.37
    print("转换后的长度是{:.2f}IN".format(IN))
elif MeterChange[-1] in ["N","n"]:
    M = (eval(MeterChange[0:-2])/39.37)
    print("转换后的长度是{:.2f}M".format(M))
else:
    print("输入格式错误")

    
