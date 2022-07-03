#first project from interviewbit 
#email slicer 
#url https://www.interviewbit.com/blog/python-projects/

import re

email = input("What is your email address: ")

split_it = re.split('@', email)

print("Your username is " + split_it[0])
print("Your domain is " + split_it[1])

#compared to the code that the website lists for the project,
#I think this is more lines of code knowing that I have to load 
#a module....