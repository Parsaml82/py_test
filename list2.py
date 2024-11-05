p_list= [1,2,3,4,5,6,7,8,9,10,10,9,8,7,6,5,4,3,2,1]
new_list=[]
for i in p_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)