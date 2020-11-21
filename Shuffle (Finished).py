# Imports [] - This is the are that all of the imports must be inserted into.
import os
import sys
import time
import uuid
import random
import datetime
import itertools
# Variables [1] - This region is where all of the basic variables stay
1 == int('1')
2 == int('2')
3 == int('3')
4 == int('4')
5 == int('5')
6 == int('6')
7 == int('7')
8 == int('8')
9 == int('9')
10 == int('10')
11 == int('11')
12 == int('12')
13 == int('13')
14 == int('14')
15 == int('15')
16 == int('16')
17 == int('17')
18 == int('18')
19 == int('19')
20 == int('20')
21 == str('alpha')
22 == str('beta')
23 == str('gamma')
24 == str('delta')
25 == str('zeta')
27 == str('theta')
28 == str('iota')
29 == str('kappa')
30 == str('lambda')
31 == str('mu')
L = ''
N = ''
a0 = False
a1 = False
a2 = False
a3 = False
a4 = False
a5 = False
a6 = False
a7 = False
a8 = False
a9 = False
a10 = False
# Variables [2]
newline = str('\n')
speech_gratitude = str('Thank you \n')
speech_blank = str('... \n')
speech_error = str('Sorry, this was not supposed to happen.. \n')
speech1 = str('How many times should the list be shuffled?\n')
speech2 = str('Please input one of the following\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n')
speech3 = str('Done\n')
card_max = int('52')
suit_max = int('13')
blackcards_max = int('26')
redcards_max = int('26')
blacksuit1_name = str('Spades')
blacksuit1_max = int('13')
blacksuit2_name = str('Clubs')
blacksuit2_max = int('13')
redsuit1_name = str('Diamonds')
redsuit_max = int('13')
blacksuit2_name = str('Hearts')
redsuit2_max = int('13')
set = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
L_ = list(itertools.product(range(1,20), ['alpha','beta','gamma','delta','epsilon','zeta','eta','theta','iota','kappa','lambda','mu']))
# Program []
def riffle_once(L):
    number = 0
    while number < 20:
        time.sleep(1)
        random.shuffle(L_)
        number += 1
        for i in range(10):
            if i == 1:
                print(L_[i][0])
                print(L_[i][1])
                if i == 2:
                    print(L_[i][0])
                    print(L_[i][1])
                    if i == 3:
                        print(L_[i][0])
                        print(L_[i][1])
                        if i == 4:
                            print(L_[i][0])
                            print(L_[i][1])
                            if i == 5:
                                print(L_[i][0])
                                print(L_[i][1])
                                if i == 6:
                                    print(L_[i][0])
                                    print(L_[i][1])
                                    if i == 7:
                                        print(L_[i][0])
                                        print(L_[i][1])
                                        if i == 8:
                                            print(L_[i][0])
                                            print(L_[i][1])
                                            if i == 9:
                                                print(L_[i][0])
                                                print(L_[i][1])
                                                if i == 10:
                                                    print(L_[i][0])
                                                    print(L_[i][1])
                                                    if i == 11:
                                                        print(L_[i][0])
                                                        print(L_[i][1])
                                                        if i == 12:
                                                            print(L_[i][0])
                                                            print(L_[i][1])
                                                            if i == 13:
                                                                print(L_[i][0])
                                                                print(L_[i][1])
                                                                if i == 14:
                                                                    print(L_[i][0])
                                                                    print(L_[i][1])
                                                                    if i == 15:
                                                                        print(L_[i][0])
                                                                        print(L_[i][1])
                                                                        if i == 16:
                                                                            print(L_[i][0])
                                                                            print(L_[i][1])
                                                                            if i == 17:
                                                                                print(L_[i][0])
                                                                                print(L_[i][1])
                                                                                if i == 18:
                                                                                    print(L_[i][0])
                                                                                    print(L_[i][1])
                                                                                    if i == 19:
                                                                                        print(L_[i][0])
                                                                                        print(L_[i][1])
                                                                                        if i == 20:
                                                                                            print(L_[i][0])
                                                                                            print(L_[i][1])
                                                                                            return();
def riffle(L, N):
    a0 = False
    a1 = False
    a2 = False
    a3 = False
    a4 = False
    a5 = False
    a6 = False
    a7 = False
    a8 = False
    a9 = False
    a10 = False
    print(newline)
    print(speech1)
    time.sleep(1)
    input_1 = input(speech2)
    while a0 == False:
        if input_1 == 1:
            a0 = True
            a1 = True
            random.shuffle(L_) #1
        elif input_1 == 2:
            a0 = True
            a2 = True
            random.shuffle(L_) #1
            random.shuffle(L_) #2
        elif input_1 == 3:
            a0 = True
            a3 = True
            random.shuffle(L_) #1
            random.shuffle(L_) #2
            random.shuffle(L_) #3
        elif input_1 == 4:
            a0 = True
            a4 = True
            random.shuffle(L_) #1
            random.shuffle(L_) #2
            random.shuffle(L_) #3
            random.shuffle(L_) #4
        elif input_1 == 5:
            a0 = True
            a5 = True
            random.shuffle(L_) #1
            random.shuffle(L_) #2
            random.shuffle(L_) #3
            random.shuffle(L_) #4
            random.shuffle(L_) #5
        elif input_1 == 6:
            a0 = True
            a6 = True
            random.shuffle(L_) #1
            random.shuffle(L_) #2
            random.shuffle(L_) #3
            random.shuffle(L_) #4
            random.shuffle(L_) #5
            random.shuffle(L_) #6
        elif input_1 == 7:
            a0 = True
            a7 = True
            random.shuffle(L_) #1
            random.shuffle(L_) #2
            random.shuffle(L_) #3
            random.shuffle(L_) #4
            random.shuffle(L_) #5
            random.shuffle(L_) #6
            random.shuffle(L_) #7
        elif input_1 == 8:
            a0 = True
            a8 = True
            random.shuffle(L_) #1
            random.shuffle(L_) #2
            random.shuffle(L_) #3
            random.shuffle(L_) #4
            random.shuffle(L_) #5
            random.shuffle(L_) #6
            random.shuffle(L_) #7
            random.shuffle(L_) #8
        elif input_1 == 9:
            a0 = True
            a9 = True
            random.shuffle(L_) #1
            random.shuffle(L_) #2
            random.shuffle(L_) #3
            random.shuffle(L_) #4
            random.shuffle(L_) #5
            random.shuffle(L_) #6
            random.shuffle(L_) #7
            random.shuffle(L_) #8
            random.shuffle(L_) #9
        elif input_1 == 10:
            a0 = True
            a10 = True
            random.shuffle(L_) #1
            random.shuffle(L_) #2
            random.shuffle(L_) #3
            random.shuffle(L_) #4
            random.shuffle(L_) #5
            random.shuffle(L_) #6
            random.shuffle(L_) #7
            random.shuffle(L_) #8
            random.shuffle(L_) #9
            random.shuffle(L_) #10
        else:
            return();
riffle_once(L)
#This is the first thing that shows up when the program runs
riffle(L, N)
#This is after the numbers have been
print(speech3)
riffle_once(L)
sys.exit('closing')
