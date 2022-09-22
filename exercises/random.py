notas ={
    "Sera": 7.8,
    "Rey": 9.0,
    "Damu": 9.0,
    "Liam": 6.1,
    "Julio": 5.3,
    "Samuel": 9.1,
    "Victor": 9.1,
    "Thomás": 9.1
}

notas_points = list(notas.values())
max_num = max(notas_points)

first_place_quantity = notas_points.count(max_num)
coincidences = 0

print(f"The first places are next: ")
for key, value in notas.items():
    if coincidences == first_place_quantity:
        break
    else:
        if value == max_num:
            print(f"{key}: {value}")
            coincidences += 1