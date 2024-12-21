crusts = {'thin', 'deepdish', 'hand_tossed', 'stuffed'}
toppings = {'cheese', 'sausage', 'black_olive', 'pepperoni'}
meats = {'sausage', 'pepperoni'}

prices = {'thin': 8.0,
          'deepdish': 8.0,
          'hand_tossed': 8.0,
          'stuffed': 10.0,
          'cheese': 1.0,
          'pepperoni': 2.0,
          'sausage': 1.5,
          'black_olive': 1.0}

def make_pizza(crust):
    if crust not in crusts:
        raise AttributeError('Invalid crust: ' + str(crust))
    return( {'crust': crust, 'toppings': []})

def get_crust(pizza):
    return(pizza['crust'])

def get_toppings(pizza):
    return(pizza['toppings'])

def add_topping(pizza, topping):
    if topping not in toppings:
        raise AttributeError('Invalid topping: ' + str(topping))
    get_toppings(pizza).append(topping)

def is_veggetarian(pizza):
    non_veg_toppings = ['pepperoni', 'sausage']
    for topping in pizza['toppings']:
        if topping in non_veg_toppings:
            return False
    return True

def calculate_price(pizza):
    price = prices.get(pizza['crust'], 0)
    for topping in pizza['toppings']:
        price += prices.get(topping, 0)
    return price

def remove_topping(pizza, topping):
    if topping in pizza['toppings']:
        pizza['toppings'].remove(topping)

def is_dairy_free(pizza):
    return 'cheese' not in pizza['toppings']