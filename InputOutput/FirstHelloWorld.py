homework = {
    "Rus": 2,
    "Math": 3,
    "Eng": 2
}

print(f"Нужно выполнить {", ".join(homework.keys())}. По {", ".join(map(str, homework.values()))} номеров", end=".")