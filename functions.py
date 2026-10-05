#=====================Functions======================
#--Named function without input and without return---------


#1. Find the sum of three numbers
# def sumOfNumbers():
#     a=30
#     b=60
#     c=90
#     sum = a+b+c
#     print(sum)
# sumOfNumbers()



#2. Find the average of three numbers
# def average():
#     n1=10
#     n2=20
#     n3=30
#     avg = (n1+n2+n3)/3
#     print(avg)
# average()




#3. Find the profit percentage using selling price and cost price

# def profitPercent():
#     sp=1000
#     cp=800
#     profit = sp-cp
#     profitPercentage = (profit/cp)*100
#     print(profitPercentage, "%")
# profitPercent()




#4. Find the missing angle in triangle by taking 2 angles
# def missingAngle():
#     a1=60
#     a2=90
#     sum = a1+a2
#     thirdAngle = 180-sum
#     print(thirdAngle)
# missingAngle()




#5. Find the gross salary
# def grossSalary():
#     basic_sal=20000
#     bonus_percent = 20
#     incentive_percent = 5

#     bonus = (bonus_percent/100)*basic_sal
#     incentive = (incentive_percent/100)*basic_sal

#     gross = basic_sal + bonus + incentive
#     print(gross)
# grossSalary()





#6. Write a program to check given number is alphabet or not
# def checkAlphabet():
#     text = "a"
#     if text>="A" and text<="Z" or text>="a" and text<="z":
#         print(text, " is a alphabet")
#     else:
#         print(text, " is not a alphabet")
# checkAlphabet()




#7. Write a Python program to check whether the given year is a leap year or not.
# def leapYear():
#     n = int(input("Enter a year : "))

#     if (n%4==0 and n%100!=0):
#         print("Leap year")
#     elif (n%400==0 and n%100!=0):
#         print("Leap year")
#     else:
#         print("Not leap year")
# leapYear()






#8. find the factorial of given number
# def factorial():
#     fact = 1
#     n= int(input("Enter a number :"))
#     for i in range(n,0,-1):
#         fact= fact*i
#     print(fact)
# factorial()





#9. Find the factors of given number
# def factors():
#     n= int(input("Enter a number: "))
#     print(f"Factors of {n} are :")
#     for i in range (1,n+1,1):
#         if(n%i==0):
#             print(i)
# factors()






#10. check whether the given number is prime number or not
# def checkPrime():
#     count = 0
#     n= int(input("Enter a number: "))
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             count+=1
#     # print(f"Count of factors of {n} are :",count)
#     if(count==2):
#         print(n," is prime number")
#     else:
#         print(n, " is not prime")
# checkPrime()









#--Named function with input and without return---------


#1. sum of first n natural numbers

# def naturalNums(n):
#     sum=0
#     for i in range(1,n+1,1):
#         sum = sum+i
#     print(sum)
# naturalNums(int(input("Enter a number :")))






#2. Find the avg of first n natural numbers using for-loop

# def averageOfNaturalNums(n):
#     sum = 0
#     for i in range(1,n+1,1):
#         sum = sum+i
#     average = sum/n
#     print(f"Average of first {n} natural numbers are {average}")
# averageOfNaturalNums(int(input("Enter a number :")))





#3. Display even numbers in the given range
# def evenNums(n1,n2):
#     for i in range(n1,n2+1,1):
#         if(i%2==0):
#             print(i)
# evenNums(int(input("Enter starting range :")) , int(input("Enter ending range :")))




#4. Display odd numbers in the given range
# def oddNums(n1,n2):
#     for i in range (n1,n2+1,1):
#         if(i%2!=0):
#             print(i)
# oddNums(int(input("Enter starting range :")) , int(input("Enter ending range :")))






#5. Write the code to display divisibles of 5 in the given range
# def divisibilities(n1,n2):
#     for i in range(n1,n2+1,1):
#         if(i%5==0):
#             print(i)
# divisibilities(int(input("Enter starting range :")) , int(input("Enter ending range :")))






#6. Count the factors of given number
# def countFactors(n):
#     count = 0
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             count+=1
#     print(f"Count of factors of {n} are :",count)
# countFactors(int(input("Enter a number: ")))




#7. check whether the number is perfect number or not
# def checkPerfectNum(n):
#     sum=0
#     for i in range(1,n,1):
#         if(n%i==0):
#             sum+=i
#     print(f"sum of factors of {n} excluding itself is ",sum)
#     if(sum==n):
#         print(n, " is a Perfect number")
#     else:
#         print(n, " is not a perfect number")
# checkPerfectNum(int(input("Enter a number: ")))





#8. check the number is palindrome or not

# def checkPallindrome(n):
#     newNum = n
#     rev =0
#     while (n!=0):
#         ld = n%10
#         rev = rev*10+ld
#         n=n//10
#     if(newNum==rev):
#         print("Palindrome")
#     else:
#         (print("Not a palindrome"))
# checkPallindrome(int(input("Enter a number : ")))







#9. write the code to display odd digits from given number
# def oddDigits(n):
#     while (n!=0):
#         ld = n%10
#         if(ld%2!=0):
#             print(ld)
#         n=n//10
# oddDigits(int(input("Enter a number : ")))






#10. skip all the odd numbers from the given number
# def skipOdd(n):
#     while n!=0:
#         ld=n%10
#         if(ld%2!=0):
#             n=n//10
#             continue
#         print(ld)
#         n=n//10
# skipOdd(63841)













#-----------Named function without input and with return-----------------

#1. sum of first n natural numbers

# def naturalNums():
#     sum=0
#     n=int(input("Enter a number :"))
#     for i in range(1,n+1,1):
#         sum = sum+i
#     return sum
# print(naturalNums())






#2. Find the avg of first n natural numbers using for-loop

# def averageOfNaturalNums():
#     sum = 0
#     n=int(input("Enter a number :"))
#     for i in range(1,n+1,1):
#         sum = sum+i
#     average = sum/n
#     return (f"Average of first {n} natural numbers are {average}")
# print(averageOfNaturalNums())





#3. Display even numbers in the given range
# def evenNums():
#     n1=int(input("Enter starting range :"))
#     n2=int(input("Enter ending range :"))
#     for i in range(n1,n2+1,1):
#         if(i%2==0):
#             print(i)
#     return i
# evenNums()




#4. Display odd numbers in the given range
# def oddNums():
#     n1=int(input("Enter starting range :"))
#     n2=int(input("Enter ending range :"))
#     for i in range (n1,n2+1,1):
#         if(i%2!=0):
#             print(i)
#     return i
# oddNums()






#5. Write the code to display divisibles of 5 in the given range
# def divisibilities():
#     n1=int(input("Enter starting range :"))
#     n2=int(input("Enter ending range :"))
#     for i in range(n1,n2+1,1):
#         if(i%5==0):
#             print(i)
#     return i
# print(divisibilities())






#6. Count the factors of given number
# def countFactors():
#     count = 0
#     n=int(input("Enter a number: "))
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             count+=1
#     return (f"Count of factors of {n} are :",count)
# print(countFactors())




#7. check whether the number is perfect number or not
# def checkPerfectNum():
#     sum=0
#     n=int(input("Enter a number: "))
#     for i in range(1,n,1):
#         if(n%i==0):
#             sum+=i
#     print(f"sum of factors of {n} excluding itself is ",sum)
#     if(sum==n):
#         return (n, 'is a Perfect number')
#     else:
#         return (n, ' is not a perfect number')
# print(checkPerfectNum())





#8. check the number is palindrome or not

# def checkPallindrome():
#     n=int(input("Enter a number : "))
#     newNum = n
#     rev =0
#     while (n!=0):
#         ld = n%10
#         rev = rev*10+ld
#         n=n//10
#     if(newNum==rev):
#         return ("Palindrome")
#     else:
#         return ("Not a palindrome")
# print(checkPallindrome())







#9. write the code to display odd digits from given number
# def oddDigits():
#     n=int(input("Enter a number : "))
#     while (n!=0):
#         ld = n%10
#         if(ld%2!=0):
#             print(ld)
#         n=n//10
#     return
# oddDigits()






#10. skip all the odd numbers from the given number
# def skipOdd():
#     n=63841
#     while n!=0:
#         ld=n%10
#         if(ld%2!=0):
#             n=n//10
#             continue
#         print(ld)
#         n=n//10
#     return
# skipOdd()









#-----------Named function with input and with return-----------------


# def displayName(myName):
#     return myName
# name = displayName("Hero")
# print(name)



#1. check the number is palindrome or not

# def checkPallindrome(n):
#     newNum = n
#     rev =0
#     while (n!=0):
#         ld = n%10
#         rev = rev*10+ld
#         n=n//10
#     if(newNum==rev):
#         return ("Palindrome")
#     else:
#         return ("Not a palindrome")
# pallindrome= checkPallindrome(int(input("Enter a number : ")))
# print(pallindrome)






#2. check whether the given number is prime number or not
# def checkPrime(n):
#     count = 0
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             count+=1
#     if(count==2):
#         return(n," is prime number")
#     else:
#         return(n, " is not prime")
# prime=checkPrime(int(input("Enter a number: ")))
# print(prime)








#3. check whether the number is perfect number or not
# def checkPerfectNum(n):
#     sum=0
#     for i in range(1,n,1):
#         if(n%i==0):
#             sum+=i
#     print(f"sum of factors of {n} excluding itself is ",sum)
#     if(sum==n):
#         return (n, 'is a Perfect number')
#     else:
#         return (n, ' is not a perfect number')
# perfect=checkPerfectNum(int(input("Enter a number: ")))
# print(perfect)



#4. Check the age whether eligible to vote or not
# def checkVote(age):
#     if age>=18:
#         return ("Eligible to vote")
#     else:
#         return ("Not eligible to vote")
# checkEligibility = checkVote(19)
# print(checkEligibility)




#5. Write a Python program to check whether the given year is a leap year or not.

# def checkLeapYear(n):
#     if (n%4==0 and n%100!=0):
#         return("Leap year")
#     elif (n%400==0 and n%100!=0):
#         return("Leap year")
#     else:
#         return("Not leap year")
# leapYear = checkLeapYear(int(input("Enter a year : ")))
# print(leapYear)



#6. Display the grade based on given marks
#above 90 : O
#71 to 90 : A
#50 to 70 : B
#35 to 50 : C
#below 35 : Fail

# def displayGrade(marks):
#     if (marks>90):
#         return("Outstanding")
#     elif(marks>=71 and marks<=90):
#         return("Grade A")
#     elif(marks>=50 and marks<=70):
#         return("Grade B")
#     elif(marks<=50 and marks>=35):
#         return("Grade C")
#     else:
#         return("Fail")
# grade = displayGrade(int(input("Enter your marks: ")))
# print(grade)




#7. check the given character is alphabet, digit or symbol

# def checkCharacter(ch):

#     if(ch>="A" and ch<="Z" or ch>="a" and ch<="z"):
#         return("Alphabet")
#     elif(ch>"0" and ch<="9"):
#         return("digit")
#     else:
#         return("Symbol")
# character = checkCharacter(str(input("Enter a character: ")))
# print(character)






#8. check whether a number is positive, negative or zero
# def checkPositive(n):
#     if(n>0):
#         return("Positive Number")
#     elif(n<0):
#         return("Negative Number")
#     else:
#         return("Zero")
# number = checkPositive(int(input("Enter a number : ")))
# print(number)




#9.Count the factors of given number
# def countFactors(n):
#     count = 0
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             count+=1
#     return(f"Count of factors of {n} are :",count)
# fact = countFactors(int(input("Enter a number: ")))
# print(fact)




#10. Find the largest digit from given number
# def findLargestNum(n):
#     lar = 0
#     while (n!=0):
#         ld = n%10
#         if(ld>lar):
#             lar = ld
#         n=n//10
#     return(lar)
# largest = findLargestNum(int(input("Enter a number : ")))
# print(largest)













































