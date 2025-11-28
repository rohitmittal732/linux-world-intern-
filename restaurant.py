print("welcome to our restaurant")

cart=0
amount=0
print("""
      choose the menu
      1.pav bhaji
      2.masala dosa
      3.chicken biryani
      4.dhokla
      5.pizza 
      6 burger
      7.egg chat
      8.water
      """
)
item= int(input("enter your choice"))
if item==1:
    price1=90
    print("the pav bhaji price is:",price1)
    ask=int(input("can i order this for yes 1 and for no 0"))
    if ask==1:
        cart=int(input("enter the plates"))
        print("order is placed 10 minutes wait")
        amount+=price1*cart
        print("your total amount is:",amount)
    else:
        print("new order you can order")

elif item==2:
    price2=190
    print("the masala dosa price is:",price2)
    ask=int(input("can i order this for yes 1 and for no 0"))
    if ask==1:
        cart=int(input("enter the plates"))
        print("order is placed 10 minutes wait")
        amount+=price2*cart
        print("your total amount is:",amount)
    else:
        print("new order you can order")
    
elif item==3:
    price3=100
    print("the chicken biryani price is :",price3)
    ask=int(input("can i order this for yes 1 and for no 0"))
    if ask==1:
        cart=int(input("enter the plates"))
        print("order is placed 10 minutes wait")
        amount+=price3*cart
        print("your total amount is:",amount)
    else:
        print("new order you can order")

elif item==4:
    price4=50
    print("the dhokla price is:",price4)
    ask=int(input("can i order this for yes 1 and for no 0"))
    if ask==1:
        cart=int(input("enter the plates"))
        print("order is placed 10 minutes wait")
        amount+=price4*cart
        print("your total amount is:",amount)
    else:
        print("new order you can order")

elif item==5:
    price5=290
    print("the pizza price is:",price5)
    ask=int(input("can i order this for yes 1 and for no 0"))
    if ask==1:
        cart=int(input("enter the plates"))
        print("order is placed 10 minutes wait")
        amount+=price5*cart
        print("your total amount is:",amount)
    else:
        print("new order you can order")
    
elif item==6:
    price6=30
    print("the burger price is:",price6)
    ask=int(input("can i order this for yes 1 and for no 0"))
    if ask==1:
        cart=int(input("enter the plates"))
        print("order is placed 10 minutes wait")
        amount+=price6*cart
        print("your total amount is:",amount)
    else:
        print("new order you can order")
        
elif item==7:
    price7=70
    print("the egg chat price is :",price7)
    ask=int(input("can i order this for yes 1 and for no 0"))
    if ask==1:
        cart=int(input("enter the plates"))
        print("order is placed 10 minutes wait")
        amount+=price7*cart
        print("your total amount is:",amount)
    else:
        print("new order you can order")
        
elif item==8:
    price8=10
    print("the water price is",price8)
    ask=int(input("can i order this for yes 1 and for no 0"))
    if ask==1:
        cart=int(input("enter the plates"))
        print("order is placed 10 minutes wait")
        amount+=price8*cart
        print("your total amount is:",amount)
    else:
        print("new order you can order")

else:
    random=int(input("have you eat the order if yes press 1 and no press 2:"))
    if random==1:
        val=str(input("plz enter the feedback"))
    else:
        print("plz wait")

