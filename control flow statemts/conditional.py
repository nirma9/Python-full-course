#if statements 

age = 22
if age >=18:
               print("you are adult...")


#if - else

number = 9
if number%2 == 0:
        print("even number")
else:
        print("odd numbers")

#if elif else 
marks = 78
if marks>= 90:
        print("Grade A")
elif marks >= 75:
        print("Grade B")
elif marks >= 60:
        print("Grade C")
else:
        print("fail...")

#nested if 
user_type = "student"
age = 19
if user_type == "student":
        if age < 25:
                print("student discount allowed..")
               