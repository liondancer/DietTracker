import re, sys

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
	mealplan_dict = {}
	choose_macro = int(raw_input("Do you want a macronutrient diet plan(1) or simply a calorie restricting plan(2)? "))
	# macro choice
	if choose_macro == 1:
		calorie_deficit = int(raw_input("What is your calorie limit? "))
		macro_percentages = ask_macro_percentages()

		protein_limit = float(macro_percentages[0]/100.0) * calorie_deficit / 4
		carb_limit = float(macro_percentages[2]/100.0) * calorie_deficit / 4
		fat_limit = float(macro_percentages[1]/100.0) * calorie_deficit / 9

		print "Your meal plan consists of: " + str(protein_limit) + "g of protein, ",
		print str(fat_limit) + "g of fat, ",
		print "and " + str(carb_limit) + "g of carbohydrates"


		run = True
		ignore_limit = False

		while run:
			food = raw_input("Enter in food name: ")
			if findFood(food):
				print "Nutrition facts: " + findFood(food)
				add_or_skip = raw_input("Would you like to add? (y/n) ")
				if add_or_skip == 'y' or add_or_skip == 'yes':
					servings = int(raw_input("Number of servings: "))
					nutrients = {'protein' : food_db[food]['protein'], 'fat' : food_db[food]['fat'], 'carbohydrate' : food_db[food]['carb'], 'sodium' : food_db[food]['sodium'], 'fiber' : food_db[food]['fiber'], 'servings' : servings}
					nutrients.update((x, int(y) * servings) for x, y in nutrients.items())
					mealplan_dict.update({food : nutrients})
					protein_limit = protein_limit - mealplan_dict[food]['protein']
					carb_limit = carb_limit - mealplan_dict[food]['carbohydrate']
					fat_limit = fat_limit - mealplan_dict[food]['fat']
					calorie_deficit = calorie_deficit - (mealplan_dict[food]['fat'] * 9) - (mealplan_dict[food]['carbohydrate'] * 4) - (mealplan_dict[food]['protein'] * 4)
					negatvie_check_list = [carb_limit, calorie_deficit, fat_limit, protein_limit]
					print "Remaining:   " + str(calorie_deficit) + " calories |   " + str(protein_limit) + "g of protein |   " + str(carb_limit) + "g of carbohydrates |   " + str(fat_limit) + "g of fat."
					while not ignore_limit:
						for x in xrange(len(negatvie_check_list)):
							if negatvie_check_list[x] < 0:
								if x == 0:
									print "Carbohydrates ",
								elif x == 2:
									print "Calories ",
								elif x == 3:
									print "Fats ",
								elif x == 4:
									print "Protein ",
							print "limit surpassed! Remove food and try again (1), continue anyway (2), or exit program (3)? ",
							choice = int(raw_input())
							if choice == 1:
								del mealplan_dict[food]
								break
							elif choice == 2:
								ignore_limit = True
								break
							elif choice == 3:
								print "Here is your meal plan: "
								for x, y in mealplan_dict.iteritems():
									print str(y['servings']) + " servings of " + x + " : " + str(y['protein']) + "g of protein, " + str(y['carbohydrate']) + "g of carbohydrates, " + str(y['fat']) + "g of fat, " + str(y['fiber']) + "g of fiber, " + str(y['sodium']) + "mg of sodium."
								print "Have a good day!"
								sys.exit()
				else:
					continue

			else:
				print "Food not found! Try again? (y/n): ",
				choice = raw_input()
				if choice == 'y' or choice == "yes":
					print "done"
				else:
					return
	elif choose_macro == 2:
		# only count calories


def ask_macro_percentages():
	percent_protein = int(raw_input("Percent protein: "))
	percent_fat = int(raw_input("Percent fat: "))
	percent_carbohydrate = int(raw_input("Percent carbohydrate: "))
	percentages = [percent_protein, percent_fat, percent_carbohydrate]
	total = 0
	for x in percentages:
		total += x
	if total > 100 or total < 100:
		print "Total percentage does not add up 100. Please try again."
		ask_macro_percentages()
	return percentages

def calc_marcos(total_calories, percentages_of_macros):
	protein = total_calories * (percentages_of_macros[0] / 100)
	fat = total_calories * (percentages_of_macros[1] / 100)
	carbs = total_calories * (percentages_of_macros[2] / 100)

def calculate_calories(serving, proteins, carbs, fats, fiber, sodium):
	calories = servings * ((protiens + carbs) * 4 + (fats * 9))
	total_fiber = fiber * servings
	total_sodium = sodium * servings
	return calories

nutrition_facts = re.compile(r'(?P<name>\S+)\s\-\-\>\s[^\:]+\:\s(?P<serv_size>\d+)[^\:]+\:\s(?P<protein>\d+)[^\;]+\:\s(?P<carb>\d+)[^\:]+\:\s(?P<fat>\d+)[^\:]+\:\s(?P<fiber>\d+)[^\:]+\:\s(?P<sodium>\d+).*')

food_db = {}
f = open("foods.txt", "r+")
# populate dictionary
for line in f.readlines():
	name = re.search(nutrition_facts, line).group(1)
	nutrition = re.search(nutrition_facts, line).groupdict(1)
	nutrition.update({"full_facts" : line})
	food_db.update({name : nutrition})
main()
f.close()


