MoneyStr = input("请输入带符号RMB或USD的钱:")
if MoneyStr[-1] in ["B","b"]:
  USD = (eval(MoneyStr[0:-3]))/6.78
  print("转换后的金额是{:2f}USD".format(USD))
elif MoneyStr[-1] in ["D","d"]:
  RMB = (eval(MoneyStr[0:-3]))*6.78
  print("转换后的金额是{:2f}RMD".format(RMB))
else:
  print("输入格式错误")
