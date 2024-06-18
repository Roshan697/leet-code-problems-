rows = 5 

for i in range(rows):
    if i % 2 == 0:
    #print 5 stars if the row number is even
     for j in range(5):
        print('*',end='')

    else:
        #print two asterisks if the row number is odd
        for j in range(2):
            print('*',end='')

    print() # move to next line after print ing a row            
