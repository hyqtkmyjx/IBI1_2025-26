class food_item:
    def __init__(self, name, calories, carbs, protein, fat):
        self.name = name
        self.calories = calories
        self.carbs = carbs
        self.protein = protein
        self.fat = fat

def calculate_nutrition(food_list):
    total_calories = sum(food.calories for food in food_list)
    total_carbs = sum(food.carbs for food in food_list)
    total_protein = sum(food.protein for food in food_list)
    total_fat = sum(food.fat for food in food_list)

    if total_calories > 2500:
        print("Warning: High calorie intake!")
    if total_fat > 90:
        print("Warning: High fat intake!")

    print(f"Total Calories: {total_calories} kcal")
    print(f"Total Carbohydrates: {total_carbs} g")
    print(f"Total Protein: {total_protein} g")
    print(f"Total Fat: {total_fat} g\n")

if __name__ == "__main__":
    apple = food_item("apple", calories=60, protein=0.3, carbs=15, fat=0.5)
    chicken_breast = food_item("chicken_breast", calories=165, protein=31, carbs=0, fat=3.6)
    rice = food_item("rice", calories=130, protein=2.7, carbs=28, fat=0.3)
    burger = food_item("burger", calories=800, protein=25, carbs=45, fat=50)
    fried_chicken = food_item("fried_chicken", calories=1000, protein=20, carbs=20, fat=80)

    normal_foods = [apple, chicken_breast, rice]
    unhealthy_foods = [burger, fried_chicken]
    calculate_nutrition(normal_foods)
    calculate_nutrition(unhealthy_foods)