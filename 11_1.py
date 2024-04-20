import random


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Кухня: {self.cuisine_type}")

    def open_restaurant(self):
        res = random.randint(0, 1)
        if res == 1:
            res1 = "открыт"
        else:
            res1 = "закрыт"
        print(f"Ресторан {self.restaurant_name} {res1}")


# Создание экземпляра класса Restaurant
newRestaurant = Restaurant("Метрополь", "русская")
# Вызов методов
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
