f=open("count","r")
dict={}
for i in f:
  word=i.split(" ")
  for j in word:
      if j not in dict:
          dict.update({j:1})
      else:
          val=int(dict[j])
          val+=1
          dict.update({j:val})
print(dict)

