# Luis Arroyo
# PSID: 2037081
# CIS 2348

class FoodItem: # TODO: Define constructor with parameters to initialize instance # attributes (name, fat, carbs, protein)
    def __init__(self, foodname='None', gramsfat = 0.0, gramscarbs =0.0, gramsprotein = 0.0):
        self.name = foodname
        self.fat = gramsfat
        self.carbs = gramscarbs
        self.protein = gramsprotein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))

if __name__ == '__main__':
    food_item1 = FoodItem()
    food_name = input()
    grams_fat = float(input())
    grams_carbs = float(input())
    grams_protein = float(input())
    grams_servings = float(input())

    food_item2 = FoodItem(food_name, grams_fat, grams_carbs, grams_protein)

    food_item1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(grams_servings, food_item1.get_calories(grams_servings)))
    print()

    food_item2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(grams_servings, food_item2.get_calories(grams_servings)))