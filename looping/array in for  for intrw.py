# for i in range(1,5): # first read 1 in i then shift to 1 in j ,
#                      # then again shift to 2 in j....untill 4, then again it shift to 2 in i
#     for j in range(1,5):
#         print(i,end=' ')      # each time we print it goes to a new line
#     print()   #so in print(i) add end='' so it will be in same line
                                    # so one more print we lead to a new line for each print
                                    # u can use/n for space

for i in range(1,5):
    for j in range(1,5):
         print(j,end=' ')
    print()
