people = [
    {'name': 'David', 'age': 25},
    {'name': 'Ahmed', 'age': 45},
    {'name': 'Omar', 'age': 30},
    {'name': 'Yousef', 'age': 50}
]

age_limit = 40

result = []

for person in people:
    if person['age'] <= age_limit:
        result.append(person)

for p in result:
    print(p['name'], "-", p['age'], "years old")