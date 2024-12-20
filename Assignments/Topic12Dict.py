
di1 = {"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}
di2 = {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}
di3 = {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}
di4 = {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}


dict_list = [di1, di2, di3, di4]


accumulated = {}


try:
    
    for dictionary in dict_list:
        for key, value in dictionary.items():
            
            if key in accumulated:
                accumulated[key] += value
            else:
                accumulated[key] = value

    
    print("Accumulated sum of values:")
    for key, value in accumulated.items():
        print(f"{key}: {value}")

except Exception as e:
    print(f"An error occurred: {e}")
