import random
n=random.randint(0,30)

for count in range(1,7):   # 1,2,3,4,5,6
    user = int(input("Enter the number:- "))
    if user < n:
        print("Number is Low,please select high number:-")
    elif user > n:
        print("Number is high,please select low:-")
    else:
        score = 60 - 10 * (count-1)
        print("Congratulation! you guessed it the number is "+ str(n) +",in "+ str(count)+" attempt and your score is "+ str(score)+".")
        break
else:
    print(" Sorry! You ran out of guesses, better luck next time.")
