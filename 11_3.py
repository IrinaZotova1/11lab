import random


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Кухня: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

    def open_restaurant(self):
        res = random.randint(0, 1)
        if res == 1:
            res1 = "открыт"
        else:
            res1 = "закрыт"
        print(f"Ресторан {self.restaurant_name} {res1}")

    def update_rating(self, new_rating):
        self.rating = new_rating


restaurant1 = Restaurant("Метрополь", "русская", 5)
restaurant2 = Restaurant("Паульсен", "французская", 4)
restaurant3 = Restaurant("Альпенхаус", "немецкая", 5)

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

otvet = input("Хотите ли вы поменять рейтинг у ресторана?(нет/да) ")
if otvet.lower() == "да":

    print("1-Метрополь")
    print("2-Паульсен")
    print("3-Альпенхаус")

    otvet1 = int(input("У какого ресторана вы хотите поменять рейтинг? "))
    new_rating = input("Ваш рейтинг: ")

    if otvet1 == 1:
        restaurant1.update_rating(new_rating)
        restaurant1.describe_restaurant()
    elif otvet1 == 2:
        restaurant2.update_rating(new_rating)
        restaurant2.describe_restaurant()
    elif otvet1 == 3:
        restaurant3.update_rating(new_rating)
        restaurant3.describe_restaurant()

else:
    print("До свидания!")