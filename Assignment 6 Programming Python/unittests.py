# Unit Testing Assignment 6

import passwd
import findme
import eto
import diet
import t2048

###################################################

assert passwd.passwordOK('Abbc1$f') == False
assert passwd.passwordOK('f#9') == False
assert passwd.passwordOK('ABd1234@1') == True
assert passwd.passwordOK('@#$abcd') == False
assert passwd.passwordOK('@ABCdeff') == False
assert passwd.passwordOK('123456Abcdefgh#') == False
assert passwd.passwordOK('1aBcdEf#$') == True

assert findme.findMe(5,[1,2,5,5,4,3]) == 2
assert findme.findMe('hello',[1,3,5,'hi','hello','hello']) == 4
assert findme.findMe(5,[2,4,6,8,10]) == None
assert findme.findMe(7,[1,7,7,7,2,3,4,7]) == 1
assert findme.findMe('one',['two','three','four',1,'ones','one']) == 5

assert eto.eto([3,1,2]) == [2,1,3]
assert eto.eto([4,5,6,2,1,3,8]) == [4,6,2,8,3,1,5]
assert eto.eto([8,-2,3,-3,-1,5,8,-1,5]) == [8,-2,8,5,-1,5,-1,-3,3]
assert eto.eto([-2,-3,-5,-8,-2,4,27,48]) == [-2,-8,-2,4,48,27,-5,-3]
assert eto.eto([1,3,5,7,9,11,13,15]) == [15,13,11,9,7,5,3,1]

recipe1 = ["Pork Stew:Cabbage*5,Carrot*1,Fatty Pork*10","Green Salad1:Cabbage*10,Carrot*2,Pineapple*5","T-Bone:Carrot*2,Steak Meat*1"]
recipe2 = ['Pizza:Cheese*2,Tomato Sauce*3,Pepperoni*5','Fruit Salad:Lettuce*5,Pineapple*5,Apple*5','Omlette:Eggs*2,Pork*5,Shrimp*3']
recipe3 = ['Khao Mun Gai:Chicken*5,Rice*3','Tom Yum Kung:Shrimp*3,Herbs*5,Vegetables*2,Mushroom*5']
recipe4 = ['Sushi:Rice*5,Salmon*3,Tuna*3','Ramen:Noodles*3,Soup*1,Egg*1,Pork*3']
recipe5 = ['Fish and Chips:Fish*3,Chips*3','Tea:Tea*2,Sugar*2,Milk*2','Cottage Pie:Beef*5,Tomatoes*2,Vegetables*1,Pastry*5']
assert diet.recipe_dict(recipe1) == {'Pork Stew': ['Cabbage', '5', 'Carrot', '1', 'Fatty Pork', '10'],'Green Salad1': ['Cabbage', '10', 'Carrot', '2', 'Pineapple', '5'],'T-Bone': ['Carrot', '2', 'Steak Meat', '1']}
assert diet.recipe_dict(recipe2) == {'Pizza':['Cheese','2','Tomato Sauce','3','Pepperoni','5'],'Fruit Salad':['Lettuce','5','Pineapple','5','Apple','5'],'Omlette':['Eggs','2','Pork','5','Shrimp','3']}
assert diet.recipe_dict(recipe3) == {'Khao Mun Gai':['Chicken','5','Rice','3'],'Tom Yum Kung':['Shrimp','3','Herbs','5','Vegetables','2','Mushroom','5']}
assert diet.recipe_dict(recipe4) == {'Sushi':['Rice','5','Salmon','3','Tuna','3'],'Ramen':['Noodles','3','Soup','1','Egg','1','Pork','3']}
assert diet.recipe_dict(recipe5) == {'Fish and Chips':['Fish','3','Chips','3'],'Tea':['Tea','2','Sugar','2','Milk','2'],'Cottage Pie':['Beef','5','Tomatoes','2','Vegetables','1','Pastry','5']}

db1 = ["Cabbage:4,2,0", "Carrot:9,1,5", "Fatty Pork:431,1,5","Pineapple:7,1,0", "Steak Meat:5,20,10", "Rabbit Meat:7,2,20"]
db2 = ['Lettuce:4,2,0','Pineapple:7,1,0','Apple:7,1,0','Cheese:2,10,5','Tomato Sauce:5,2,1','Pepperoni:1,15,4']
db3 = ['Chicken:3,10,5','Rice:10,1,0','Shrimp:3,10,3','Herbs:3,1,0','Vegetables:3,1,0','Mushroom:2,5,1']
db4 = ['Rice:10,1,0','Salmon:1,15,5','Tuna:0,10,10','Noodles:15,1,0','Soup:1,1,1','Egg:1,10,2','Pork:1,15,8']
db5 = ['Fish:1,15,5','Chips:10,1,5','Tea:1,1,1','Sugar:5,2,1','Milk:3,10,1','Beef:3,20,10','Tomatoes:10,3,2','Vegetables:1,1,1','Pastry:20,3,5']
assert diet.db_dict(db1) ==  {'Cabbage': 24, 'Carrot': 85, 'Fatty Pork': 1773, 'Pineapple': 32, 'Steak Meat': 190, 'Rabbit Meat': 216}   
assert diet.db_dict(db2) == {'Lettuce':24,'Pineapple':32,'Apple':32,'Cheese':93,'Tomato Sauce':37,'Pepperoni':100}
assert diet.db_dict(db3) == {'Chicken':97,'Rice':44,'Shrimp':79,'Herbs':16,'Vegetables':16,'Mushroom':37}
assert diet.db_dict(db4) == {'Rice':44,'Salmon':109,'Tuna':130,'Noodles':64,'Soup':17,'Egg':62,'Pork':136}
assert diet.db_dict(db5) == {'Fish':109,'Chips':89,'Tea':17,'Sugar':37,'Milk':61,'Beef':182,'Tomatoes':70,'Vegetables':17,'Pastry':137}

meal1 = ['T-Bone','T-Bone','Green Salad1']
meal2 = ['Pork Stew','T-Bone']
meal3 = ['Pizza','Fruit Salad']
meal4 = ['Khao Mun Gai','Tom Yum Kung']
meal5 = ['Fish and Chips','Tea','Cottage Pie']
assert diet.mealCal(meal1,recipe1,db1) == 1290
assert diet.mealCal(meal2,recipe1,db1) == 18295
assert diet.mealCal(meal3,recipe2,db2) == 1237
assert diet.mealCal(meal4,recipe3,db3) == 1151
assert diet.mealCal(meal5,recipe5,db5) == 2576

dct1 = {'Pork Stew': ['Cabbage', '5', 'Carrot', '1', 'Fatty Pork', '10'],'Green Salad1': ['Cabbage', '10', 'Carrot', '2', 'Pineapple', '5'],'T-Bone': ['Carrot', '2', 'Steak Meat', '1']}
dct2 = {'Pizza':['Cheese','2','Tomato Sauce','3','Pepperoni','5'],'Fruit Salad':['Lettuce','5','Pineapple','5','Apple','5'],'Omlette':['Eggs','2','Pork','5','Shrimp','3']}
dct3 = {'Khao Mun Gai':['Chicken','5','Rice','3'],'Tom Yum Kung':['Shrimp','3','Herbs','5','Vegetables','2','Mushroom','5']}
dct4 = {'Sushi':['Rice','5','Salmon','3','Tuna','3'],'Ramen':['Noodles','3','Soup','1','Egg','1','Pork','3']}
dct5 = {'Fish and Chips':['Fish','3','Chips','3'],'Tea':['Tea','2','Sugar','2','Milk','2'],'Cottage Pie':['Beef','5','Tomatoes','2','Vegetables','1','Pastry','5']}

assert diet.ing_values(dct1,'Pork Stew') == {'Cabbage':'5','Carrot':'1','Fatty Pork':'10'}
assert diet.ing_values(dct5,'Cottage Pie') == {'Beef':'5', 'Tomatoes':'2','Vegetables':'1','Pastry':'5'}
assert diet.ing_values(dct3,'Tom Yum Kung') == {'Shrimp':'3','Herbs':'5','Vegetables':'2','Mushroom':'5'}
assert diet.ing_values(dct4,'Sushi') == {'Rice':'5','Salmon':'3','Tuna':'3'}
assert diet.ing_values(dct2,'Omlette') == {'Eggs':'2','Pork':'5','Shrimp':'3'}

a = [[' ',' ','2',' '],
     ['4','2',' ',' '],
     ['2','4','16','8']]

b = [[' ',' ',' ',' '],
     ['2',' ','4',' '],
     [' ','2',' ','2']]

c = [[' ','4','2','4'],
     [' ','8','4','2'],
     [' ','4','16','8'],
     ['8','2','4','32']]

d = [['8','16',' ',' '],
     ['2','16','4','4'],
     [' ',' ','2','2']]

e = [['2','16','4','2'],
     ['32','8','128','8'],
     ['2','32','8','2'],
     ['4','8','2','16']]

f = [['4','2','32','2'],
     ['8','4','8','4'],
     ['16','64','4','128'],
     ['2','4','2','16']]

assert t2048.hist(a) == {16: 1, 2: 3, 4: 2, 8: 1}
assert t2048.hist(b) == {2:3,4:1}
assert t2048.hist(c) == {2:3,4:5,8:3,16:1,32:1}
assert t2048.hist(d) == {16: 2, 8: 1, 4: 2, 2: 3}
assert t2048.hist(e) == {2:5,4:2,8:4,16:2,32:2,128:1}

assert t2048.emptyPos(a) == [(0,0),(0,1),(0,3),(1,2),(1,3)]
assert t2048.emptyPos(b) == [(0,0),(0,1),(0,2),(0,3),(1,1),(1,3),(2,0),(2,2)]
assert t2048.emptyPos(c) == [(0,0),(1,0),(2,0)]
assert t2048.emptyPos(d) == [(0, 2), (0, 3), (2, 0), (2, 1)]
assert t2048.emptyPos(e) == []

assert t2048.doKeyUp(a) == (True, [['4', '2', '2', '8'], ['2', '4', '16', ' '], [' ', ' ', ' ', ' ']])
assert t2048.doKeyUp(b) == (True, [['2', '2', '4', '2'], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']])
assert t2048.doKeyUp(c) == (True,[['8', '4', '2', '4'],[' ', '8', '4', '2'],[' ', '4', '16', '8'],[' ', '2', '4', '32']])
assert t2048.doKeyUp(d) == (True, [['8', '32', '4', '4'], ['2', ' ', '2', '2'], [' ', ' ', ' ', ' ']])
assert t2048.doKeyUp(e) == (False,[['2', '16', '4', '2'],['32', '8', '128', '8'],['2', '32', '8', '2'],['4', '8', '2', '16']])

assert t2048.doKeyDown(a) == (True, [[' ', ' ', ' ', ' '], ['4', '2', '2', ' '], ['2', '4', '16', '8']])
assert t2048.doKeyDown(b) == (True, [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], ['2', '2', '4', '2']])
assert t2048.doKeyDown(c) == (False,[[' ', '4', '2', '4'],[' ', '8', '4', '2'],[' ', '4', '16', '8'],['8', '2', '4', '32']])
assert t2048.doKeyDown(d) == (True, [[' ', ' ', ' ', ' '], ['8', ' ', '4', '4'], ['2', '32', '2', '2']])
assert t2048.doKeyDown(e) == (False,[['2', '16', '4', '2'],['32', '8', '128', '8'],['2', '32', '8', '2'],['4', '8', '2', '16']])

assert t2048.doKeyLeft(a) == (True, [['2', ' ', ' ', ' '], ['4', '2', ' ', ' '], ['2', '4', '16', '8']])
assert t2048.doKeyLeft(b) == (True, [[' ', ' ', ' ', ' '], ['2', '4', ' ', ' '], ['4', ' ', ' ', ' ']])
assert t2048.doKeyLeft(c) == (True,[['4', '2', '4', ' '],['8', '4', '2', ' '],['4', '16', '8', ' '],['8', '2', '4', '32']])
assert t2048.doKeyLeft(d) == (True, [['8', '16', ' ', ' '], ['2', '16', '8', ' '], ['4', ' ', ' ', ' ']])
assert t2048.doKeyLeft(e) == (False,[['2', '16', '4', '2'],['32', '8', '128', '8'],['2', '32', '8', '2'],['4', '8', '2', '16']])

assert t2048.doKeyRight(a) == (True, [[' ', ' ', ' ', '2'], [' ', ' ', '4', '2'], ['2', '4', '16', '8']])
assert t2048.doKeyRight(b) == (True, [[' ', ' ', ' ', ' '], [' ', ' ', '2', '4'], [' ', ' ', ' ', '4']])
assert t2048.doKeyRight(c) == (False,[[' ', '4', '2', '4'],[' ', '8', '4', '2'],[' ', '4', '16', '8'],['8', '2', '4', '32']])
assert t2048.doKeyRight(d) == (True, [[' ', ' ', '8', '16'], [' ', '2', '16', '8'], [' ', ' ', ' ', '4']])
assert t2048.doKeyRight(e) == (False,[['2', '16', '4', '2'],['32', '8', '128', '8'],['2', '32', '8', '2'],['4', '8', '2', '16']])

assert t2048.isGameOver(a) == False
assert t2048.isGameOver(b) == False
assert t2048.isGameOver(e) == True
assert t2048.isGameOver(f) == True
assert t2048.isGameOver(c) == False