import random
class fruitquiz:
    def __init__(self):
        self.fruits = {"apple":"sweet", "lemon":"sour", "watermelon":"sweet", "orange":"sour"}
    def quiz(self):
        while(True):
            fruit, taste = random.choice(list(self.fruits.items()))
            print("what does {} taste like".format(fruit))
            userans = input()
            if(userans.lower==taste):
                print("correct")
            else:
                print("wrong")
            option = int(input("0 to play again otherwise 1: "))
            if(option):
                break
print("welcome to the fruit quiz")
fq = fruitquiz
fq.quiz