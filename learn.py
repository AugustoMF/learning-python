age = input ("How old are you? ")
price = input ("What's the ticket price? ")

if int(age) <12:
    print ("You are ", age, "Years, entrance is ", int (price)*0)

elif int(age) <18:
    print ("You are ", age, "Years, pay half price, the purchase is ", int (price)/2, "dollars")
    
else:
 print ("You are ", age, "Years, pay full price, the purchase is", int (price), "dollars")
