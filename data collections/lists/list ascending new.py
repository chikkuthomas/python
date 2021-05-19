a=[111,-15,-26,15,1,0,8,876,100,54,23,-64,23,76]
print(a)
b=[]

while a:
    min=a[0]
    for i in a:
        if i<min:
            min=i
    b.append(min)
    a.remove(min)
print(b)

#EXPLANATION
# min=111
# 1)111<111 - not true
# 2)-26<111 - true ,min=-26
# 3) 15<-26, not true
# 4) 1<-26, not true
# 5) 0<-26, not true
# 6) 8<-26,not true
# 7) 876<-26,not true
# 8) 100<-26, not true
# 9)54/-26,not true
# 10) 23>26,not true
# 10) -64<-26 ,true ,min=-64
# 12) 23<-64,not true
# 13) 76<-64, not true

# the min id added to empty set b[]
# the min is removed from the orginal set a
#to sort using sort method
a.sort()
print(a)


