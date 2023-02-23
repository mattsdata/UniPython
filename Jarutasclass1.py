# name = "Friend" #input("What is your name :")
# print(f"hello {name}")
# age = 40 #input("What is your age :")
# print(f"Age: {age}")
# height = int(input("What is your height :"))
# print(f"height: {height} cms")
# weight = int(input("What is your weight :"))
# print(f"weight: {weight} kg")
#
# print(f"Your BMI: {weight / (height/100)**2:.2f}")
# def bmi_calc(a,b):
#     bmi = a / (b/100)**2
#     if bmi>=30:
#         print(f"Your {bmi} index is very high: Obesity")
#     elif bmi>=25.0:
#         print(f"Your {bmi} index is high: Overweight")
#     elif bmi >= 18.5:
#         print(f"Your {bmi} index is good: Healthy")
#     else:
#         print(f"Your {bmi} index is low: Underweight")
#
# bmi_calc(weight,height)

'''
Next Excercise
'''
# live = int(input("What is your Live level :"))
# Energy = input("What is your Energy level :")
# shield = input("What is your shield level :")
# print(f"Live level: {'♥' * int(live)} ")
'''
Next Excercise - Decision loops
'''
#cable_num=int(input("")

# total = 0
#
# number = int(input("Enter a number or just enter to quit: "))
#
# while number >= 0:
#     total = total+number
#     print(f"The summation is {total}")
#     number = int(input("Enter a number or just enter to quit: "))
#
# print(f"The summation is {total}")

'''
Next Excercise - Decision loops
'''
# num = int(input("Enter the number"))
# sum=0
# count=0
# while count <= num:
#     sum=sum+count
#     print(count)
#     count =count+1
#
# print(f"The total is {sum} and count {count}")

'''
Next Excercise - For loops
'''
def count_num():
    print(count)

num = int(input("Enter the number"))
count = 0
for i in range(num):
    count_num()
    count=count+i

count_num()
