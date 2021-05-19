count={}                       #creating an empty dictionary
data=input("enter")            # entering the string "hello hi hello"
words=data.split(" ")          # splitting the string with spaces,i.e hello, hi, hello
for word in words:             # iterating each element in a words
    if word not in count:      #comparing each element with the empty dictionary, if the element entered is not present
        count.update({word:1}) #update the dictionary with the key(element) and value(count)
    else:                      #if the word is present,[in cases where same elements are repeating]
        val=int(count[word])   # val=the value of the key in dictionary,i.e here value of word=1
        val+=1                 # if present increment the value by 1
        count.update({word:val}) # updating/adding new key and value to the dictionary
print(count)                     #printing new ditionary

