class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word + "("+self.meaning+")"
flash = []
print("welcome to the flashcard app")
while(True):
    word = input("enter the word that you want to add to the flashcard : ")
    meaning = input("enter the meaning of the word : ")
    flash.append(flashcard(word, meaning))
    option = int(input("enter 0 if you want to add another flashcard else enter 1 : "))
    if(option):
        break
print("your flashcards\n")
for i in flash:
    print(">", i)