#!/usr/bin/python3
import sys
import sqlite3
from random import randint
from time import sleep, localtime
from datetime import datetime
from sys import platform
from os import system

answer_yes = """
   YY      YY   EEEEEE    SSSS
   YY      YY   EEEEEE   SSSSSS
    YY    YY    EE       SS
     YY  YY     EE       SS
       YY       EEEEE    SSSSS
       YY       EEEEE     SSSSS
       YY       EE           SS
       YY       EE           SS
       YY       EEEEEE   SSSSSS
       YY       EEEEEE    SSSS
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

def save_stat(data_to_save):
    t = localtime()
    connection = sqlite3.connect(sys.path[0]+'/statc.db')
    cursor = connection.cursor()
    d_date = "{:%d.%m.%Y}".format(datetime(t.tm_year, t.tm_mon, t.tm_mday))
    d_time = "{:%H:%M:%S}".format(datetime(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec))
    cursor.execute("INSERT INTO statistic (result, date, time) VALUES ({0}, '{1}', '{2}')".format(data_to_save, d_date, d_time))
    connection.commit()
    cursor.close()
    connection.close()

def read_stat():
    connection = sqlite3.connect(sys.path[0]+'/statc.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM statistic")
    summ = 0
    sz = 0
    for i in cursor.fetchall():
        summ+=i[1]
        sz+=1
    if sz!=0:
        rez=summ/sz

    print('Current statistics: '+str(rez))
    cursor.close()
    connection.close()
    return rez

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
    save_stat(arg)

def main():
    if platform == "linux":
        system("clear")
    elif platform == "win32":
        system("cls")
    else:
        print(platform)
    print_answer(choice())


if __name__ == "__main__":
    if len(sys.argv)>1:
        if "-s" in sys.argv[1:]:
            read_stat()
    else:
        main()
