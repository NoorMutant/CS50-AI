# first = float(input("Input first number to add   "))
# second = float(input("Input second number to add   "))
# answer = first + second
# print ("answer : " + str(answer))

#weight converter
weight = float(input ("Input your weight  "))
meter = input("K for KG or L for LB : ")

if meter.upper() == "K":
    print("Weight in lb is : " + str(weight * 2.205))
elif meter.upper() == "L":
    print("Weight in kg is : " + str(weight / 2.205))