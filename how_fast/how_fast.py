import time


start = "true"
print ("Instruction: type in 'asdfghjkl' when the game starts. That is the only rule!")
input ("Press enter to start")
name = input("What is your name? :\n")
name = name.split(' ')

while start == "true":
    #name stuff

    

    #start 
    print ("Game will start in: ")
    print ("3 ")
    time.sleep(1)
    print ("2 ")
    time.sleep(1)
    print ("1 ")
    time.sleep(1)

    startTime = time.time()

    #type in alphabet
    alphabet = input("GO! GO! GO! Type in the Alphabet: \n")
    alphabet = alphabet.lower()

    if alphabet == "asdfghjkl":
        endTime = time.time()
        
        score = endTime- startTime
        score = round(score, 1)#########
        print("Congratulations " + name[0] + "\n Your time is: " + str(score) + 's')
        restart = input("Type 'YES' if you want to be the fastest winner: \n")
        if(restart == "YES"):
            start = "true"
        else:
            start = "false"
        
    else:
        print ("you made a mistake! ")
        restart = input("input 'YES' to restart: \n")
        if(restart == "YES"):
            start == true
        else:
            start = "false"
    
    

#What you can learn as  a beginner: str(score), have to convert float into string
#round(score,1 ), input, name.split(' '),module time

