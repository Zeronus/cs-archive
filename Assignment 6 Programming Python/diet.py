# Assignment 6, Task 4
# Name: Naran Kongpithaksilp (Tan)
# Collaborators:
# Time Spent: 2:17 hours

def recipe_dict(lst):
    ingredients = []
    dish = []
    d = {} # Dictionary of dishes to ingredients
    for item in lst:
        splitColon = item.split(':') # Separate the ingredients from the dish name
        dish.append(splitColon[0]) # Make a list of meals
        splitValue = splitColon[1].replace('*','.').replace(',','.').split('.') # Separate the ingredient name and ingredient values
        ingredients.append(splitValue) # Make a list of ingredients
    for index in range(len(dish)):
        d[dish[index]] = ingredients[index]
    return d # Returns a dictionary with meals as a key and ingredients as value

def ing_values(dct,dish): # Input is a dish (Pizza, Pork Stew, etc.) and dct is the output of recipe_dict
    d = {}
    index = 0
    while index < len(dct[dish])-1:
        d[dct[dish][index]] = dct[dish][index+1]
        index += 2       
    return d # Function returns a dict with ingredient as key and amount needed as values for the input dish

def db_dict(lst):
    calories = [4,4,9] # carbs, protein, fat
    d = {} # Dictionary of ingredients to nutrients
    temp_value = 0 # temp variable used for second loop
    nutrients = []
    ingredients = []
    for item in lst:
        splitColon = item.split(':') # Separate ingredients from nutrients
        ingredients.append(splitColon[0])
        nutrients.append(splitColon[1].split(','))
    for index in range(len(nutrients)): # Loop through nutrients
        for value in range(3): # Loop through each item in nutrients
            temp_value += float(nutrients[index][value]) * calories[value] # Multiply each value with calories
        d[ingredients[index]] = temp_value # Add the total calories for each ingredient to dict
        temp_value = 0 # Reset temp value
    return d
                
def mealCal(meal,recipes,db): # Final function
    ans = []
    temp_cal = 0 # Temporary variable to store total calories
    recipePerDish = recipe_dict(recipes) # Dict with meals to ingredients
    caloriesPerIng = db_dict(db) # dict with total calories for each ingredient
    for dish in meal:
        ingredients = ing_values(recipePerDish,dish) # Dict with amount needed per ingredient
        for key in ingredients: # Loop through ingredients
            temp_cal += float(ingredients[key])*caloriesPerIng[key] # Times calories per ingredient by amount
        ans.append(temp_cal) # Append total calories for dish to list
        temp_cal = 0 # Reset variable
    return sum(ans) # Return sum of all calories in list == total calories for meal
        