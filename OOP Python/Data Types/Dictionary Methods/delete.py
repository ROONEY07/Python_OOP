car = {
    'brand' : 'Toyota',
    'model' : 'Corolla',
    'year' : 2020,
    'price' : 24532
}

# print(car.clear())
# print(car.pop('year'))
# for key,val in car.items():
#     print(f"{key} : {val}")
# print(car.popitem({'model':2020}))
print(car.popitem())

print()





for key,val in car.items():
    print(f"{key} : {val}")