# check negative positiove and zero

# num = int(input("enter sny number:"))
# if num >0:
#                print("positive number")
# elif num <0:
#         print("negative number")
# else:
#         print("the number is zero")

#  1 se 20 tak even numbers with modulu operator
# for i in range(1,21):
#                if i % 2==0:
#                        print(i)



# sum of 10 natural numbers using while loop
# i = 1
# sum = 0
# while i <= 10:
#                sum += i
#                i +=1
# print("sum:", sum)


# 4 
# while True:
#                num = int(input("enter a number (0 to exit):"))
#                if num == 0:
#                        print("exiting loop....")
#                        break      # stop the iteration ......5


# student grade program
# marks = int(input("enter your marks:"))
# if marks >= 90:
#                print("grade A")    # excellent
# elif marks >= 80:
#         print("grade B")     # very good
# elif marks >= 70:
#         print("grade C")        # good

# else:
#         print("Grade: Fail")      # needs improvments

# simple calculator

num1 = float(input("enter first number:"))
num2 = float(input("enter secong number:"))
op = input("enter operator(+,-,*,/):")
if op == "+":
               print("result:",num1+num2)
elif op == "-":
        print("result:", num1 - num2)
elif op == "*":
        print("result :",num1*num2)
elif op == "/":
        print("result :", num1/num2)
else:
        print("cannot divide by zero")


