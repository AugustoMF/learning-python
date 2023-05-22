weight = int(input("Insert your weight "))
unit = input ("insert the measurement unit (K fot kgs or L for lbs) ")

if unit.upper () == "K":
    converted = weight / 0.45
    print ("Weight in pounds " + str(converted))

else:
    converted = weight * 0.45
    print ("Weight in KGs " + str(converted))
    

print ("Done")
