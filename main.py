num=float(input("Enter your number :"));
if(num<0):
    print("number is negative");
elif(num>0):
    if(num<=10):
        print("number is betwen 1-10");
    elif(num<=20):
        print("number is betwen 11-20");
    else:
        print("number is grewter than 20");
else:
    print("number is zero");