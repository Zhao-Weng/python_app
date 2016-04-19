import os

f1 = open("read.txt","r")
f2 = open("write.txt", "w")


#read(5) and read()
#print(f1.read()) and print (f1)
rtf = f1.read(5)
print(f1.read())
print (f1)
print(f1.readlines(2))
f2.write("\n i love you" + rtf)


#mode, closed, name attributes.
print(f1.mode)

if f1.closed == bool(0):
    print ("File status: Open")
else:
    print ("File status: closed")


#rename
os.rename("HelloWorld","read.txt")


#remove file.
os.remove("Helloworld")

#create dif(can't make repeatedly
os.mkdir("new folder")

#changing current directory
os.chdir("new folder")

#pwd
os.getcwd()

#delete a dir
os.rmdir("new folder")




