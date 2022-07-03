#This python project can make you spell out the numbers as you may
#define. This python code will help you support than a million
#inputs along with the non-positive integers like zero, negative integers
# or floating numbers


#basic 1-10 first 

integers = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6, 
    "seven" : 7, 
    "eight" : 8,
    "nine" : 9,
    "zero" : 0,
    "hundred" : 00,
    "thousand" : 000, 
    "million" : 000000, 
    "billion" : 000000000,
    "and" : " "
}

numbers_spoken = input("what's the integer string: ").split()

#if 'one is detected' 
#print 1 
# then look for the trailing number whether it's hundred, thousand 
#million, etc 

# if integers["one"] == True:
#     print("found one")
#works above but too long in time to program out

#FOR LOOPS!
#for each word found in the string, print it's respected key 
#value
#for instance If I found one thousand 3 hundred two five one
#look at each word and see if it's in the dictionary, if it's not
#then move on. 
#add and to the dictionary.

for x in numbers_spoken:
    print(integers[x])
    #how do we switch from one directory to another one? JUST ADD
    #THEM TOGETHER DUMBASS
    #for some reason when I ask it to print hundred or thousand it's only
    #printing out one zero
    #Okay I'm done I'm checking the answers....
    #This dude! He's like made it so it prints an image of the 
    #number the user has spoken in words....smh 
    #couple of ways to do this, inflect, num2words (pkg),
    
    #https://stackoverflow.com/questions/19504350/how-to-convert-numbers-to-words-without-using-num2word-library

#examples:
#one hundred
# two thousand
# five million

