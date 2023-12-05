import random
#import time

class Snjokorn:
    def __init__(self):
        self.shape=random.choice(["*","+","-"])
        self.position=" "*random.choice(range(1,100))

    def __str__(self):
        return "Ég er snjókorn"

    def print(self):
        print(self.position,end="")
        print(self.shape)

def main():
    while True:
        temp = Snjokorn()
        temp.print()
        #time.sleep(0.015)

main()