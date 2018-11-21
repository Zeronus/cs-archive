# Assignment 5 Python Unit Testing

# TASK 2 UNIT TESTS

import bell

assert bell.pattern([1, 2]) == [2,3,5]
assert bell.pattern([3,7,9]) == [9,12,19,28]
assert bell.pattern([5,7,10,15]) == [15,20,27,37,52]
assert bell.pattern([2,4,6]) == [6,8,12,18]
assert bell.pattern([1,3,5,7,9]) == [9,10,13,18,25,34]

assert bell.loveTri(5) == [[1], [1, 2], [2, 3, 5], [5, 7, 10, 15], [15, 20, 27, 37, 52]]
assert bell.loveTri(10) == [[1],[1, 2],[2, 3, 5],[5, 7, 10, 15],[15, 20, 27, 37, 52],[52, 67, 87, 114, 151, 203],[203, 255, 322, 409, 523, 674, 877],[877, 1080, 1335, 1657, 2066, 2589, 3263, 4140],[4140, 5017, 6097, 7432, 9089, 11155, 13744, 17007, 21147],[21147, 25287, 30304, 36401, 43833, 52922, 64077, 77821, 94828, 115975]]
assert bell.loveTri(7) == [[1], [1, 2], [2, 3, 5], [5, 7, 10, 15], [15, 20, 27, 37, 52], [52, 67, 87, 114, 151, 203],[203, 255, 322, 409, 523, 674, 877]]
assert bell.loveTri(3) == [[1], [1, 2], [2, 3, 5]]
assert bell.loveTri(1) == [[1]]

# TASK 3 UNIT TESTS

import sleuth

matrix1 = [["r","a","w","b","i","t"],
          ["x","a","y","z","c","h"],
          ["p","q","b","e","i","e"], 
          ["t","r","s","b","o","g"],
          ["u","w","x","v","i","t"],
          ["n","m","r","w","o","t"]]

matrix2 = [['c','n','a','w','o','r','q','a'],
           ['h','u','l','u','q','v','n','a'],
           ['d','w','c','v','m','a','w','p'],
           ['g','c','h','u','n','q','h','p'],
           ['f','j','a','a','m','e','h','l'],
           ['i','w','b','i','h','b','m','e'],
           ['a','e','u','o','q','c','e','b'],
           ['s','q','u','a','r','e','e','r']]

matrix3 = [['y','g','v','f','b','q','b','h','u','d','e','q','o','g','h'],
           ['g','c','d','d','v','a','r','e','t','b','f','m','m','r','p'],
           ['c','w','r','m','w','f','o','k','n','d','i','a','l','e','q'],
           ['e','o','a','a','u','i','v','q','a','f','c','t','f','a','u'],
           ['f','k','g','m','b','l','q','f','h','t','a','j','k','s','w'],
           ['c','m','o','c','v','u','d','z','u','p','u','e','c','e','o'],
           ['j','f','n','j','p','p','i','q','p','x','g','g','v','n','x'],
           ['o','k','m','v','d','n','l','l','w','u','k','f','i','x','m'],
           ['j','n','h','v','w','j','l','p','d','g','t','y','e','w','n'],
           ['o','c','y','b','s','m','e','b','w','g','c','v','k','p','n'],
           ['b','o','d','a','s','l','x','e','l','n','j','w','f','n','r'],
           ['o','d','t','g','i','c','r','z','n','l','x','t','d','j','o'],
           ['k','y','k','z','h','u','m','l','q','e','v','q','x','g','g'],
           ['q','h','c','q','a','l','w','g','b','a','b','b','i','v','u'],
           ['e','t','h','v','p','e','t','a','g','g','z','c','o','h','e']]

matrix4 = [['y','w','y','g','e'],
           ['a','r','q','r','n'],
           ['y','a','i','e','v'],
           ['q','t','h','e','y'],
           ['t','h','i','d','e']]

matrix5 = [['f','d','r','n','b','l','u','e','w','v'],
           ['i','y','e','l','l','o','w','q','h','l'],
           ['v','h','i','n','t','v','i','j','v','y'],
           ['r','n','q','g','r','e','e','n','e','f'],
           ['a','e','f','e','c','b','p','q','z','p']]

assert sleuth.makeUnique([1,2,3,1,4,5,2]) == [1,2,3,4,5]
assert sleuth.makeUnique(['frog','dog','man','frog','rabbit','rabbit']) == ['dog', 'man', 'frog', 'rabbit']
assert sleuth.makeUnique(['bog', 'rabbit', 'the', 'bit', 'bit', 'raw']) == ['rabbit', 'raw', 'the', 'bog', 'bit']
assert sleuth.makeUnique(['John','Johnny','Johnathan','Joestar','Joestar','Joseph']) == ['Joestar', 'John', 'Johnathan', 'Joseph', 'Johnny']
assert sleuth.makeUnique(['bacon','eggs','ham','milk','bacon','ham']) == ['bacon', 'eggs', 'milk', 'ham']
assert sleuth.makeUnique(['juice','soda','juice','milk']) == ['milk','soda','juice']

assert sleuth.inGridRange(matrix1,0,0) == True
assert sleuth.inGridRange(matrix1,2,3) == True
assert sleuth.inGridRange(matrix3,0,4) == True
assert sleuth.inGridRange(matrix4,7,0) == False
assert sleuth.inGridRange(matrix5,6,6) == False

assert sleuth.diag(matrix1,3,3) == ['bit'] 
assert sleuth.diag(matrix3,7,0) == ['onyaiuwa']
assert sleuth.diag(matrix1,0,5) == ['t']
assert sleuth.diag(matrix4,0,0) == ['yriee']
assert sleuth.diag(matrix5,0,3) == ['nlveq']

assert sleuth.diagReverse(matrix1,5,0) == ['nwsect']
assert sleuth.diagReverse(matrix5,3,0) == ['rhen']
assert sleuth.diagReverse(matrix3,14,0) == ['ehkgsmllppatlrh']
assert sleuth.diagReverse(matrix2,7,4) == ['rcml']
assert sleuth.diagReverse(matrix1,0,5) == ['t']

assert sleuth.checkDiagonal(matrix1) == [['rabbit'],['r'],['xqsvo'],['xa'],['prxw'],['paw'],['twr'],['tqyb'],['um'],['urbzi'],['n'],['nwsect'],['ayeot'],['mxbih'],['wzig'],['rvoe'],['bce'],['wig'],['ih'],['ot'],['t'],['t']]
assert sleuth.checkDiagonal(matrix2) == [['cucumber'],['c'],['hwhahce'],['hn'],['dcaiqe'],['dua'],['gjbor'],['gwlw'],['fwua'],['fccuo'],['ieu'],['ijhvqr'],['aq'],['awaumvq'],['s'],['sebanana'],['nlvnemb'],['quimqwa'],['aumqhe'],['uohehp'],['wqahl'],['aqbhp'],['ovwp'],['rcml'],['rnp'],['eee'],['qa'],['eb'],['a'],['r']]
assert sleuth.checkDiagonal(matrix3) == [['ycrabuildgjtxve'],['y'],['gwamvplpwnxqih'],['gg'],['cogcpnlbllvbo'],['ccv'],['ekojdjeenebc'],['ewdf'],['fmnvwmxzqaz'],['fordb'],['cfmvslrlbg'],['ckamvq'],['jkhbscmgg'],['jmgawab'],['onyaiuwa'],['ofomufrh'],['jcdghlt'],['jkncbioeu'],['ootzae'],['onmjvlvktd'],['bdkqp'],['bchvpuqqnbe'],['oycv'],['ooyvdpdfadfq'],['khh'],['kddbwnizhfimo'],['qt'],['qytasjlqutcamg'],['e'],['ehkgsmllppatlrh'],['gdmuldqwgcwdgu'],['tczilepwxujfep'],['vdwiqzputvfjg'],['hqhcxbdugekaq'],['fvfvfuxkykno'],['vaurewgkgcsu'],['baoqhpgfepr'],['plmzlgtfvew'],['qrkatugiwn'],['ewlnncyino'],['benfaevxn'],['tgqljvexx'],['htdcjcnm'],['abexwkwm'],['ubitkex'],['gavtfpn'],['dfafso'],['gbqdnn'],['emlaw'],['zbxjr'],['qmeu'],['cigo'],['orq'],['ovg'],['gp'],['hu'],['h'],['e']]
assert sleuth.checkDiagonal(matrix4) == [['yriee'],['y'],['aahd'],['aw'],['yti'],['yry'],['qh'],['qaqg'],['t'],['ttire'],['wqey'],['hhen'],['yrv'],['iev'],['gn'],['dy'],['e'],['e']]
assert sleuth.checkDiagonal(matrix5) == [['fyigc'],['f'],['ihqe'],['id'],['vnf'],['vyr'],['re'],['rhen'],['a'],['anilb'],['denrb'],['eqnll'],['rltep'],['fgtou'],['nlveq'],['ervwe'],['boinz'],['ceiqw']]

assert sleuth.checkHorizontal(matrix1) == ['rawbit', 'xayzch', 'pqbeie', 'trsbog', 'uwxvit', 'nmrwot']
assert sleuth.checkHorizontal(matrix2) == ['cnaworqa','huluqvna','dwcvmawp','gchunqhp','fjaamehl','iwbihbme','aeuoqceb','squareer']
assert sleuth.checkHorizontal(matrix3) == ['ygvfbqbhudeqogh','gcddvaretbfmmrp','cwrmwfokndialeq','eoaauivqafctfau','fkgmblqfhtajksw','cmocvudzupueceo','jfnjppiqpxggvnx','okmvdnllwukfixm','jnhvwjlpdgtyewn','ocybsmebwgcvkpn','bodaslxelnjwfnr','odtgicrznlxtdjo','kykzhumlqevqxgg','qhcqalwgbabbivu','ethvpetaggzcohe']
assert sleuth.checkHorizontal(matrix4) == ['ywyge', 'arqrn', 'yaiev', 'qthey', 'thide']                        
assert sleuth.checkHorizontal(matrix5) == ['fdrnbluewv', 'iyellowqhl', 'vhintvijvy', 'rnqgreenef', 'aefecbpqzp']

assert sleuth.checkVertical(matrix1) == ['rxptun', 'aaqrwm', 'wybsxr', 'bzebvw', 'icioio', 'thegtt']
assert sleuth.checkVertical(matrix2) == ['chdgfias','nuwcjweq','alchabuu','wuvuaioa','oqmnmhqr','rvaqebce','qnwhhmee','aapplebr']
assert sleuth.checkVertical(matrix3) == ['ygcefcjojobokqe','gcwokmfkncodyht','vdragonmhydtkch','fdmamcjvvbagzqv','bvwubvpdwssihap','qafilupnjmlcule','brovqdillexrmwt','hekqfzqlpbezlga','utnahupwdwlnqbg','dbdftpxuggnleag','eficaugktcjxvbz','qmatjegfyvwtqbc','omlfkcviekfdxio','greasenxwpnjgvh','hpquwoxmnnrogue']
assert sleuth.checkVertical(matrix4) == ['yayqt', 'wrath', 'yqihi', 'greed', 'envye']
assert sleuth.checkVertical(matrix5) == ['fivra','dyhne','reiqf','nlnge','bltrc','loveb','uwiep','eqjnq','whvez','vlyfp']

assert sleuth.wordSleuth(matrix1,["bog", "moon", "rabbit", "the", "bit","raw"]) == ['rabbit', 'raw', 'the', 'bog', 'bit']
assert sleuth.wordSleuth(matrix2,['apple','banana','cucumber','square','pear','pineapple'])  == ['banana', 'apple', 'square', 'cucumber']
assert sleuth.wordSleuth(matrix3,['build','dragon','rogue','grease','evolve','funky']) == ['dragon', 'build', 'rogue', 'grease']
assert sleuth.wordSleuth(matrix4,['greed','lust','wrath','envy','gluttony','sloth','pride']) == ['greed', 'envy', 'wrath']
assert sleuth.wordSleuth(matrix5,['blue','green','yellow','orange','red']) == ['blue', 'green', 'yellow']

# TASK 4 UNIT TESTS

import karma

actions = ["Jim++", "John--", "Jeff++", "Jim++", "John--", "John->Jeff", "Jeff--","June++", "Home->House"]
actions2 = ["Naruto--", "Sasuke--", "Naruto->Luffy", "Ichigo++"]
actions3 = ["Obama--","Trump++","Clinton->Bush","Bush++","Clinton--","Trump->Kim Jong"]
actions4 = ['Razor--','Riki--','Ember Spirit++','Storm Spirit--','Templar Assassin->Shadow Fiend']
actions5 = ['Kobe++','Kevin--','Lebron++','Curry++','Kyrie++','Kyrie->Curry']

assert karma.namesToDict(actions) == {'Jim': 0, 'John': 0, 'Jeff': 0, 'June': 0, 'Home': 0, 'House': 0}
assert karma.namesToDict(actions2) == {'Naruto': 0, 'Sasuke': 0, 'Luffy': 0, 'Ichigo': 0}
assert karma.namesToDict(actions3) == {'Obama': 0, 'Trump': 0, 'Clinton': 0, 'Bush': 0, 'Kim Jong': 0}
assert karma.namesToDict(actions4) == {'Razor': 0,'Riki': 0,'Ember Spirit': 0,'Storm Spirit': 0,'Templar Assassin': 0,'Shadow Fiend': 0}
assert karma.namesToDict(actions5) == {'Kobe': 0, 'Kevin': 0, 'Lebron': 0, 'Kyrie': 0, 'Curry': 0}

assert karma.keepTabs(actions) == {'Jim': 2, 'Jeff': -2, 'June': 1}
assert karma.keepTabs(actions2) == {'Sasuke': -1, 'Luffy': -1, 'Ichigo': 1}
assert karma.keepTabs(actions3) == {'Obama': -1, 'Clinton': -1, 'Bush': 1, 'Kim Jong': 1}
assert karma.keepTabs(actions4) == {'Razor': -1, 'Riki': -1, 'Ember Spirit': 1, 'Storm Spirit': -1}
assert karma.keepTabs(actions5) == {'Kobe': 1, 'Kevin': -1, 'Lebron': 1, 'Curry': 2}

# TASK 5 UNIT TESTS

import sgroup

lst = [71.4, 72.73, 74.36, 75.38, 76.15, 76.96, 79.51, 86.82, 87.81, 87.87, 146.38, 150.89,
151.16, 152.18, 152.36, 153.27, 155.7, 160.99, 161.36, 164.55]
lst2 = [1,1.2,4.5,4.7,9.1,9.8,9.9]
lst3 = [1,1,1,2,2,2,3,3,3,4,4,4]
lst4 = [4.5,4.7,5.2,8.7,9,10,14,15.3,17]
lst5 = [0.1,0.5,0.9,10,11,12.3,17,18.7,23.3]

assert sgroup.findGaps(lst) == [10, 7, 17, 11, 19, 6, 16, 2, 1, 13, 3, 8, 15, 5, 4, 18, 12, 14, 9]
assert sgroup.findGaps(lst2) == [4, 2, 5, 3, 1, 6]
assert sgroup.findGaps(lst3) == [9, 6, 3, 11, 10, 8, 7, 5, 4, 2, 1]
assert sgroup.findGaps(lst4) == [6, 3, 8, 7, 5, 2, 4, 1]
assert sgroup.findGaps(lst5) == [3, 6, 8, 7, 5, 4, 2, 1]

assert sgroup.separate(lst,2) == [[71.4, 72.73, 74.36, 75.38, 76.15, 76.96, 79.51, 86.82, 87.81, 87.87],[146.38, 150.89, 151.16, 152.18, 152.36, 153.27, 155.7, 160.99, 161.36, 164.55]]
assert sgroup.separate(lst2,3) == [[1, 1.2], [4.5, 4.7], [9.1, 9.8, 9.9]]
assert sgroup.separate(lst,4) == [[71.4, 72.73, 74.36, 75.38, 76.15, 76.96, 79.51],[86.82, 87.81, 87.87],[146.38, 150.89, 151.16, 152.18, 152.36, 153.27, 155.7],[160.99, 161.36, 164.55]]
assert sgroup.separate(lst5,3) == [[0.1, 0.5, 0.9], [10, 11, 12.3], [17, 18.7, 23.3]]
assert sgroup.separate(lst4,7) == [[4.5, 4.7], [5.2], [8.7, 9], [10], [14], [15.3], [17]]
assert sgroup.separate(lst3,4) == [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]] 





