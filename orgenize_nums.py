"""
we create 2 array, 1 full, 1 empty
our goal is to fill the empty arry and order by the numbers
1- we open a while loop (while the arry exist)
2- we set up a minimum value- the [0] position in the data_list,
 in oredr to check one by one from the numbers and to start from the begginer
3- we open a for loop inside the while loop,
for exch value we check if he is smallest than the min, if he is we set him like the min.
we pass by all the numbers in the list
when we found the smallest value (after the for loop run above all the numbers in the data list)-
we add it to the empty list (now is in [0] position- the first)
and remove this value from the data_list
now we combeback
right now in tha data list we had a new min value (bec we remove the last) and we need to find him.
we set again the minimum value is the [0] position in data list (in order to check every num)- 
its may be differnt value due to the list (if the last min value was the first than he was deleted)
- but the most importent is the location [0]
we pass by all the numbers in the data list - for the next minimum value 
we do all this progress again
add this value to the new list (now he will be the [1] postion) and remove from the data_list

in this way- at every round of while we check who is the smallest (with for) and print it.
than the list become orgenize from the smallest to the biggest
"""
data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)

print (new_list)

