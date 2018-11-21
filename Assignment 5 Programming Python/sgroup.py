# Assignment 5, Task 5
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: 
# Time Spent: 5 hours

lst = [71.4, 72.73, 74.36, 75.38, 76.15, 76.96, 79.51, 86.82, 87.81, 87.87, 146.38, 150.89,
151.16, 152.18, 152.36, 153.27, 155.7, 160.99, 161.36, 164.55]
lst2 = [1,1.2,4.5,4.7,9.1,9.8,9.9]
lst3 = [1,1,1,2,2,2,3,3,3,4,4,4]
lst4 = [4.5,4.7,5.2,8.7,9,10,14,15.3,17]
lst5 = [0.1,0.5,0.9,10,11,12.3,17,18.7,23.3]

def findGaps(lst): 
    diff = [] # gaps between each value
    index = [] # index of each value
    ans = [] # return list (will be indexes sorted in order of gaps)
    i = 1
    while i < len(lst):
        diff.append(lst[i]-lst[i-1])
        index.append(i)
        i += 1
    zipped = list(zip(diff,index)) # assign index values to gaps
    sortedzip = sorted(zipped,reverse=True) # sort the zip from biggest gap to smallest
    for i in range(len(sortedzip)):
        ans.append(sortedzip[i][1]) 
    return ans # list of only indexes (in order of gaps)
        
def separate(data,k):
    ans = []
    i = 1
    allgaps = sorted(findGaps(data)[:k-1]) # the first (k-1) gap indexes in order, easier to split the data
    while i < len(allgaps):
        ans.append(data[allgaps[i-1]:allgaps[i]]) # splits data at the gaps between first and last
        i += 1
    ans.append(data[:allgaps[0]]) # splits data at the first gap
    ans.append(data[allgaps[-1]:]) # splits data at the last gap
    return sorted(ans)
        
        
        
        
    



    
    