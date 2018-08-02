###################################
# Welcome to the                  #
# fake electronic genre generator #
# by AKJM                         #
###################################

# import libraries for use
import random

# write list of prefixes and suffixes based off of the wikipedia list of electronic subgenres
# https://en.wikipedia.org/wiki/List_of_electronic_music_genres
prefixes = "ambient,dark,drone,big,breakbeat,broken,nu,jersey,euro,space,acid,chill,trip,liquid,neuro,dark,drum,funk,hard,tech,dance,dub,electro,acoustic,cold,crunk,minimal,new,post,folk,live,hard,speed,psy,alternative,indie,lo-fi,hip,melodic,bigroom,fidget,jungle,cyber,future,power,industrial,glitch,synth,vapor,future,dream,chip,break,bit,harsh,sine,pure"
suffixes = "dub,industrial,ambient,club,beat,core,breaks,bass,disco,jazz,hop,funk,step,wave,clash,punk,noise,gaze,pop,electro,trance,beat,techno,style,hiphop,house,hop,bounce,tune"

# setup running variable
running = True

# split into arrays
start = prefixes.split(",")
end = suffixes.split(",")

# generate function
def generate(number):

    # loop for inputted amount of times
    for x in range(number):

        # take on random entry from both prefixes and suffixes and concat them
        output = start[random.randint(0,len(start)-1)] + " " + end[random.randint(0,len(end)-1)]

        # print output
        print(output)

# run loop
while(running):

    # take user input
    number = int(input("How many genres am I generating?: "))

    # run function
    generate(number)
    
    # continue confirmation
    yesno = input("Would you like to make more? y/n: ")

    # terminate
    if yesno == "n":
        running = False
