test_list = [1, 4, 5, 18, 10] 
  
print ("Original list : " + str(test_list)) 
  
flag = 0
if(test_list == sorted(test_list)): 
    flag = 1
      
if (flag) : 
    print ("Yes, List is sorted.") 
else : 
    print ("No, List is not sorted.") 