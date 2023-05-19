weight = input ("How much do you wieght? ")
question = input ("Type L por lbs or K to kilos ")

if question.upper == "L":
 print ("Your weight in KG is: ", int (weight)*0.4535, "KG")

else:
 print ("Your weight in LBS is: ",  int (weight)//0.4535, "LBS")

print ("Done")