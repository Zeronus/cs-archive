# Assignment 5, Task 4
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: 
# Time Spent: 00:45 hours

actions = ["Jim++", "John--", "Jeff++", "Jim++", "John--", "John->Jeff", "Jeff--",
"June++", "Home->House"]

actions2 = ["Naruto--", "Sasuke--", "Naruto->Luffy", "Ichigo++"]

actions3 = ["Obama--","Trump++","Clinton->Bush","Bush++","Clinton--","Trump->Kim Jong"]

def namesToDict(lst): # uses lst (actions) and turns it into dict with names
    d = dict()
    names = []
    for i in lst:
        strip = i.strip('++')
        strip = strip.strip('--')
        names.extend(strip.split('->'))
    for n in names:
        d[n] = 0
    return d
        
def keepTabs(actions):
    d = namesToDict(actions)
    karma = dict()
    for i in actions:
        if '++' in i:
            d[(i.strip('++'))] += 1
        elif '--' in i:
            d[(i.strip('--'))] -= 1
        elif '->' in i:
            s = i.split('->')
            d[s[1]] += d[s[0]]
            d[s[0]] = 0
    for n in d:
        if d[n] != 0:
            karma[n] = d[n]
    return karma


