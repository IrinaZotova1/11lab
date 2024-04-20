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

# Создание трех экземпляров класса Restaurant
restaurant1 = Restaurant("Метрополь", "русская")
restaurant2 = Restaurant("Паульсен", "французская")
restaurant3 = Restaurant("Альпенхаус", "немецкая")

# Вызов метода describe_restaurant() для каждого экземпляра
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
restaurant3.describe_restaurant()
restaurant3.open_restaurant()