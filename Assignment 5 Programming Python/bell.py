# Assignment 5, Task 2
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: 
# Time Spent: 00:42 hours

def pattern(previous):
    current = []
    current.append(previous[-1]) # list starts with last item of prev list
    while len(current) < len(previous) + 1:
        for i in range(0,len(previous)):
            current.append(current[i] + previous[i]) # list pattern = list[index] + prevlist[index]
    return current


def loveTri(n):
    ans = [[1]]
    while len(ans[-1]) < n:
        ans.append(pattern(ans[-1]))      
    return ans
        
            
        