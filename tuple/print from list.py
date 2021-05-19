# to print the details of employee having salary above 50k
# tuples inside a list
lst=[('anu',28,25000),('manju',32,30000),('sajeev',36,60000)]
for i in lst:
    if(i[2]>50000):
        print("details: ",i)
