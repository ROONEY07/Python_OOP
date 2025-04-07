car = {
    'brand' : 'Toyota',
    'model' : 'Corolla',
    'year' : 2020
}

car['color'] = 'red'
# print(car)
# for key,val in car.items():
#     print(f"{key} : {val}")


car.update({'price' : 203040})
print(car)