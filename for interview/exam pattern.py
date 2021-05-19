# 1
# 11
# 111
# 1111
# 11111
# 111111
# 222222
# 22222
# 2222
# 222
# 22
# 2
# 3
# 33
# 333
# 3333
# 33333
# 333333
# 444444
# 44444
# 4444
# 444
# 44
# 4
# 5
# 55
# 555
# 5555
# 55555
# 555555
# 666666
# 66666
# 6666
# 666
# 66
# 6
# 7
# 77
# 777
# 7777
# 77777
# 777777
# enter initial range 1
# enter final range 8

ini=int(input("enter initial range"))    #1
fin=int(input("enter final range"))      #8
for i in range(ini,fin):                 #(1,8)
    if(i%2==0):                          #2%2==0
        for k in range(0,fin):           #(0,8) 0   1
            for j in range(fin-k,ini,-1):#(8,0,-1)  6 times   5times    4times 3times  2times  1times
                print(i,end=" ")         #22222222   222222   22222     2222      222     22     2
            print()
    else:                                #1
        for k in range(0,fin):           #(0,8) k=0  1   2    3   4      5       6         7
            for j in range(0,k+1):       #(0,1)
                print(i,end=" ")         #1          11  111 1111 11111  111111  1111111   11111111
            print()
