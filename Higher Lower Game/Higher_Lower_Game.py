from game_data import data
from logo import vs
from os import system, name
from logo import main_logo
from random import randint
from os import system
import time
##################IMPORT#######################
dict1 = {'A':{},'B':{}}
score = 0
should_continue = True
##################Public var###################
# define our clear function
# The screen clear function
def clear():
    system('cls')
    



def gen_num():
    rnd = randint(0,49)
    return rnd
dict1['A'] = data[gen_num()]
dict1['B'] = data[gen_num()]
if dict1['A'] == dict1['B'] :
    dict1['B'] = data[gen_num()]

def show(dic):
    name = dic['name']
    des = dic['description']
    country = dic['country']
    return name +' , ' + 'a '+ des +', ' + 'from ' + country+'.' 
###Generetaing random number between 0 till 49
def ext_fl(dic):
    count = dic['follower_count']
    return count
##################################
def compare(dic):
    global dict1
    final=''
    flw_A = ext_fl(dic['A'])
    flw_B = ext_fl(dic['B'])
    if flw_A > flw_B :
        dict1['B'] = data[gen_num()]
        final = 'A'
        return final
    elif flw_A < flw_B :
        final = 'B'
        dict1['A'] = dict1['B']
        dict1['B'] = data[gen_num()]
        return final


###############################ASK USER#####################
def guess():
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    return guess

def play():
    clear()
    global score
    global dict1
    global should_continue
    stringA = "Compare A: "
    stringB = "Against B: "
    print(main_logo)
    stringA+= show(dict1['A'])
    stringB+= show(dict1['B'])
    print(stringA)
    print(vs)
    print(stringB)
    if guess() == compare(dict1):
        score +=2
        print (f"You're right! Current score: {score}.")
        
        
    else:
        should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")






#######################Main program###########
#initial()
while should_continue:
    play()
    clear()

