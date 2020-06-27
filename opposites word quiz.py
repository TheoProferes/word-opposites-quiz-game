import random

def question(contents,counter,score):
    keyfind(contents)
    syn1=synpicker(contents,key1)
    ant1=antpicker(contents,key1)
    syn2=synpicker(contents,key2)
    possible=antpossible(contents,key2)
    answer=input("Q"+str(counter)+": "+str(syn1)+" is to "+str(ant1)+" as "+str(syn2)+" is to...").lower()
    if answer in possible:
        score=score+1
        print("Correct!")
    else:
        print("Wrong")
        print("You could have put",possible)
    
def synpicker(contents,key):
    synList = contents[key+2].split(",")
    picked=random.randint(1,len(synList)-1)
    syn= synList[picked]
    syn=syn.replace("\n","")
    syn=syn.replace(".","")
    syn=syn.replace(" ","")
    if syn[0]=="{":
        synpicker(contents,key)
    return syn
def antpicker(contents,key):
    antList = contents[key+4].split(",")
    picked=random.randint(1,len(antList)-1)
    ant= antList[picked]
    ant=ant.replace("\n","")
    ant=ant.replace(".","")
    ant=ant.replace(" ","")
    if ant[0]=="{":
        antpicker(contents,key)
    return ant
def antpossible(contents,key):
    ant=contents[key+4]
    ant=ant.replace("\n","")
    ant=ant.replace(".","")
    ant=ant.replace(" ","")
    ant=ant.replace("ANT:","")

    antList = ant.split(",")
    return antList

def keyfind(contents):   
    new=True
    line=random.randint(0,len(contents)-100)
    check(contents,line,new)
    new=False
    line2=random.randint(0,len(contents)-100)
    check(contents,line2,new)
    valid=False
    while valid==False:
        if "SYN" in contents[key1+2] and "ANT" in contents[key1+4]:
            if "SYN" in contents[key2+2] and "ANT" in contents[key2+4]:
                valid==True
                break
            else:
                new=False
                line=random.randint(0,len(contents)-1)
                check(contents,line,new)
        else:
            new=True
            line=random.randint(0,len(contents)-1)
            check(contents,line,new)
            
def check(contents,line,new):
    if "KEY" in contents[line]:
        if  new==True:
            global key1
            global key2

            key1=line
         
        else:
            key2=line
    
           
    else:
            line=line+1
            check(contents,line,new)
            


opposites= open("Opposites.txt","r")
contents= opposites.readlines()
opposites.close()
import random
global score
global counter             
score=0
counter=0
number=int(input("How many questions would you like"))
for count in range(number):
    counter=counter+1
    question(contents,counter,score)
print("You got",score,"out of",number,"correct")





            

    
    
    
