#read the text file to python file

#define a variable

f=open("readex.txt", "r")  # f is the variable, to open the file we use open keyword, " file to be opened"," which mode u want to open the file"

# to read we need to iterate
# if we just use print(f), only the location of the file will be printed

for i in f:      # to iterate
    print(i)