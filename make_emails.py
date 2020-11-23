import time 
import random
from collections import OrderedDict


#List with names to generate the email 
names = ['james', 'john', 'robert', 'michael', 'william', 'david', 'richard', 'joseph','thomas', 'charles', 'christopher', 
        'daniel', 'matthew', 'anthony', 'donald', 'mark', 'paul', 'steven', 'andrew','kenneth', 'joshua', 'kevin', 'brian', 'george', 'edward', 'ronald', 'timothy', 'jason', 'rebecca', 'laura',
        'emily', 'kimberly', 'betty', 'margaret', 'lisa', 'karen', 'jessica', 'susan','linda','jennifer',' patricia', 'mary', 'charlotte', 'kayla', 'isabelle', 'rose', 'natalie','diana']

#Extensions 
extension = ["@gmail.com", "@yahoo.com", "@live.com", "@live.nl", "@kpn.nl", "@ziggo.nl"]

#List with generated emails 
generated = [] 


#Creates the email emails 
def create_emails(): 
    while(len(generated) < 10000):
        name_char = random.choice(names)
        extension_char = random.choice(extension)
        generated.append((str(name_char) + str(create_random_num(100)) + str(extension_char)))
    
    print("There were " + str(len(generated)) + " words generated!")
    show_email_list()
    remove_duplicates(generated)

#Shows the emails from the generated list 
def show_email_list(): 
    for i in generated: 
        print(i)

#Removes duplicates from the list 
def remove_duplicates(listOfElems): 
    list(OrderedDict.fromkeys(listOfElems))


#Returns a random number between 1 and 100
def create_random_num(leng): 
    n = random.randint(1,leng)
    return n 



#Runs first 
if __name__ == "__main__":
    print(create_emails())