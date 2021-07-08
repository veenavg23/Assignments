#list_num=[]
#count=1

#x=int(input("How many numbers do you want to insert: "))
#for i in range(0,x):
 #   num=int(input("Enter the number: "))
#    if num in list_num:
#        count+=1
#    list_num.append(num)
    
#print("In"+str(list_num)+", The equal numbers are : "+str(count))
count=1
def equal(n1,n2,n3):
    global count
    list_num=[n1,n2,n3]
    list_equal=[]
    for i in list_num:
        if  i in list_equal:
            count+=1
            if count==1:
                count=0
        list_equal.append(i)
        
    print("In"+" "+str(list_num)+", The equal numbers are : "+str(count))
        
equal(200,200,100)
