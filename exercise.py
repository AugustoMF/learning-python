weight =  int (input ("How much do you weight? "))
question = input ("Type L por lbs or K to kilos ")

if question.upper () == "K":
    converted = weight / 0.45
    print ("Weight in kilos " + str(converted))

else:
     converted = weight * 0.45
     print ("Weight in pounds " + str(converted))

print ("Done")
