# PROBLEM 1

def longIncSlice(L):
    length = 1
    answer = []
    for i in range(len(L)-1):
        if L[i+1] > L[i]:
            length += 1
        else:
            length = 1
        answer.append(length)
    return max(answer)

# Use 'for' loop to count the length of the list. If the next number is bigger
# than the current number, increase length. If the next number is <= current
# number, reset length back to one. Append lengths to a list and find max.


         
assert longIncSlice([1,2,3,2,4,5,10,2,3])== 4 
assert longIncSlice([1,-1,1,-1,1,-1])== 2 
assert longIncSlice([5,4,3,2,1])== 1 
assert longIncSlice([7,1,10,5,2,5,7])== 3
assert longIncSlice([7,1,10,5,2,5,7,1,1,1,2,3,4,1,2,3,4,5,6,7,8,9,10,11,12])== 12
    