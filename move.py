def move(n,f,buffer,to):
    if n==1:
        print("Move",n,"from",f,"to",to)
    else:
        move(n-1,f,to,buffer)
        move(1,f,buffer,to)
        move(n-1,buffer,f,to)
        
