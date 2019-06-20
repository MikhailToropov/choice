#!/usr/bin/python3
from random import randint
from time import sleep
from sys import platform
from os import system

answer_yes = """
    YY    YY   EEEEEE    SSSS
    YY    YY   EEEEEE   SSSSSS
     YY  YY    EE       SS
     YY  YY    EE       SS
       YY      EEEEE    SSSSS
       YY      EEEEE     SSSSS
       YY      EE           SS 
       YY      EE           SS
       YY      EEEEEE   SSSSSS
       YY      EEEEEE    SSSS 
    """
answer_no = """
    NNNN       NN      OOOOO
    NNNN       NN    OO     OO
    NN NN      NN   OO       OO
    NN  NN     NN  OO         OO
    NN   NN    NN  OO         OO
    NN    NN   NN  OO         OO
    NN     NN  NN  OO         OO
    NN      NN NN   OO       OO
    NN       NNNN    OO     OO
    NN        NNN      OOOOO  
    """

def choice():
    count = [i for i in range(randint(1, 13))]
    while count:
        answer = randint(0, 10)
        print(count.pop())
        sleep(1)
    if answer >= 5:
        return 1
    else:
        return 0

def print_answer(arg):
    if arg:
        print(answer_yes)
    else:
        print(answer_no)

def main():
    if platform == "linux":
        system("clear")
    elif platform == "win32":
        system("cls")
    else:
        print(platform)
    print_answer(choice())


if __name__ == "__main__":
    print("Start")
    main()
