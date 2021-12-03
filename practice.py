import random
Num=random.randint(1,100)
for i in range(0,5):
  n=int(input("Enter a number between 1 and 100\n"))
  if(n<Num):
        print("Think a little high 😄\n")
        print("Guesses left=",5-i-1)
  elif(n>Num):
        print("Think a little less 😄\n")
        print("Guesses left=",5-i-1)
  else:
        print("Congratulations you made the right guess 🍫 😄 🍫")
        break;
else:
  print("Sorry 😄, your guesses are over. Better luck next time")