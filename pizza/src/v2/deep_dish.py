from src.v2.pizza import Pizza

class DeepDishCrust(Pizza):
    def is_veggetarian(self):
        return True

    def calculate_price(self):
        return 11.0