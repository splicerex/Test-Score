def score():
    num1=float(input("Your score"))
    num2=float(input("Your score"))
    num3=float(input("Your score"))
    num4=float(input("Your score"))
    num5=float(input("Your score"))
    num6=float(input("Your score"))
    num7=float(input("Your score"))
    num8=float(input("Your score"))
    num9=float(input("Your score"))
    num10=float(input("Your score"))
    add_all=num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10
                
    average=add_all/10
    print(average)
    
    if average >=90:
        print("you got an A")
    elif average >=80:
        print("you got an B")
    elif average >=70:
        print("you got an C")
    elif average >=60:
        print("you got an D")
    elif average >=50:
        print("you got an F")

score()



    
