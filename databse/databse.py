

live = 1
while live == 1:
    dataRead = open("db.txt","r")
    if dataRead.read() != "" and dataRead.read() != "[]":
        dataRead.close()
        #close for to start reading the first line rather than
        #at the start of the cursor
        dataRead = open("db.txt","r")
        people = eval(dataRead.read())
        dataRead.close()
        
        
        do = input("What do you wish to do?(search, add, change,del): \n")
    else:
        do = input("What do you wish to do?(search, add, change,del): \n")
        
        people = []
        


    if do == "search":
       c_name = input("Input the Name of the Person you are search : \n")
       def search(n):
           
           for p in people:
               if p['Name'] == n:
                   print("Name: " + p['Name'])
                   
                   print("Address: " + p['Address'])
                   print("Date of Birth: " + p['DoB'])
                   print("Phone Number: " + str(p['Phone Number']))
               else:
                    print("Nobody with the name was found")
                
       search(c_name)
       live = 0

    if do =="add":
        print("#--------------------------Adding User-----------------#")
        newName = input("Input the new name:\n")
        newAddress = input("Input the new address:\n")
        newDoB = input("Input the date of birth:\n")
        newPhone = input("Input the new phone number:\n")
        tempDict = {"Name":newName, "Address":"newAddress","DoB":newDoB,"newPhone":newPhone}
        people.append(tempDict)
        print(people )
        print("hello")
        
        print(dataRead.mode)
        print(dataRead.closed)
        dataWrite = open("db.txt","w")
        dataWrite.write(str(people))
        live = 0
        dataWrite.close()
        
        
    else:
        
        live = 0

###bug_log
#write is rewrite, not append
#remember to close the file, otherwise, other process can't access it. 
#can't convert int into str implicitly.
#can only write string to file.

#there will be a cursor!!!!, so once opened, read() will read at the beginning
#cursor not always at the start of the program.

#append to list
