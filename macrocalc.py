import re

def main():
	print "Welcome!"
	print "!hat would you like to do?"
	options = ["1 - create a meal plan","2 - add food","3 - search food"]
	for choice in options:
		print choice
	selection = int(raw_input())
	if selection > 3:
		print "Incorrect selection. Please try again."
		self.display_options()
	else: 
		print "You chose: ",
		if selection == 1:
			print "\'create a meal plan\'"
			build_meal_plan()
		elif selection == 2:
			print "\"add food\""
			addfood()
		else: 
			print "\"search food\""			
			searchFood()


def addfood():
	print "Name of the food: ",
	food = raw_input()
	exists = findFood(food)
	if exists:
		print "Food already exists!"
		add_different_food_or_restart()
	print "Serving size(grams): ",
	serving_size = int(raw_input())
	print "Grams of protein per serving: ",
	protein = int(raw_input())
	print "Grams of carbohydrate per serving: ",
	carbohydrate = int(raw_input())
	print "Grams of fat per serving: ",
	fat = int(raw_input())
	print "Grams of fiber per serving: ",
	fiber = int(raw_input())
	print "Milligrams of sodium per serving: ",
	sodium = int(raw_input())
	food_db_format = food + " --> " + "Serving size: " + str(serving_size) + "g, Protein: " + str(protein) + "g" + ", Carbs: " + str(carbohydrate) + "g, Fats: " + str(fat) + "g, Fiber: " + str(fiber) + "g, Sodium: " + str(sodium) + "mg\n" 
	f.write(food_db_format)


def add_different_food_or_restart():
	choice = int(raw_input("Would you like to try again(1) or restart program(2) ?"))
	if choice == 1:
		f.close()
		addfood()
	elif choice == 2:
		f.close()
		main()
	else:
		print "Bad input. Please try again."
		add_different_food_or_restart()

def findFood(food):
	try: 
		return food_db[food]['full_facts']
	except KeyError:
		return False


def searchFood():
	food = raw_input("Enter the name of the food: ")
	exists = findFood(food)
	if exists:
		print exists
		again_option = raw_input("Search again? (y/n) ")
		if again_option == 'y' or again_option =="yes":
			searchFood()
		else:
			print "Have a nice day!"
			return
	else:
		print "Food does not exist! Try again? (y/n): ",
		choice = raw_input()
		if choice == 'y' or choice == "yes":
			searchFood()
		else:
			return


# not done yet!!
def build_meal_plan():
	# used to keep track of current diet plan
	food_dict = {}
	choose_macro = int(raw_input("Do you want a macronutrient diet plan(1) or simply a calorie restricting plan(2)? "))
	# macro choice
	if choose_macro == 1:
		calorie_deficit = int(raw_input("What is your calorie limit? "))
		macro_percentages = ask_macro_percentages()
		while calorie_deficit > 0:
			food = raw_input("Enter in food name: ")
			if findFood(food):
				print "Nutrition facts: " + findFood(food)
				add_or_skip = raw_input("Would you like to add? (y/n)")
				if add_or_skip == 'y' or add_or_skip == 'yes':
					servings = int(raw_input("Number of servings: "))
					food_dict.update({food : servings})

				#else:


			else:
				print "Food not found! Try again? (y/n): ",
				choice = raw_input()
				if choice == 'y' or choice == "yes":
					
				else:
					return


def ask_macro_percentages():
	percent_protein = int(raw_input("Percent protein "))
	percent_fat = int(raw_input("Percent fat "))
	percent_carbohydrate = int(raw_input("Percent carbohydrate "))
	percentages = [percent_protein, percent_fat, percent_carbohydrate]
	total = 0
	for x in percentages:
		total += x
	if total > 100 or total < 100:
		print "Total percentage does not add up 100. Please try again."
		ask_macro_percentages()
	return percentages

#def add_to_diet(servings):




def calculate_calories(serving, proteins, carbs, fats, ):
	calories = servings * ((protiens + carbs) * 4 + (fats * 9))

	return calories

nutrition_facts = re.compile(r'(?P<name>\S+)\s\-\-\>\s[^\:]+\:\s(?P<serv_size>\d+)[^\:]+\:\s(?P<protein>\d+)[^\;]+\:\s(?P<carb>\d+)[^\:]+\:\s(?P<fat>\d+)[^\:]+\:\s(?P<fiber>\d+)[^\:]+\:\s(?P<sodium>\d+).*')

#def extract_data(filename):
#	with open(filename) as f:

food_db = {}
f = open("foods.txt", "r+")
# populate dictionary
for line in f.readlines():
	name = re.search(nutrition_facts, line).group(1)
	nutrition = re.search(nutrition_facts, line).groupdict(1)
	nutrition.update({"full_facts" : line})
	print nutrition
	food_db.update({name : nutrition})
main()
f.close()


