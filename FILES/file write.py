# f=open("readex.txt", "w")  #to open in write mode
# f.write("1234")

#if we open a text file we have not created a new file in that name will automatically be created

f=open("abc.txt", "w")
f.write("chikku")

#to append a file we use "a"
f=open("abc.txt","a")
f.write(" good")