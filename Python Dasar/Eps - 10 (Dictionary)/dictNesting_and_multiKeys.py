# sama seeperti list, dictionary juga ada nestingnya (dictionary yg berisi dict)

person1 = {
    'nama' : 'Grunge',
    'kulit' : 'Hitam',
    'umur' : '19'
}

person2 = {
    'nama' : 'Niggerpleo',
    'kulit' : 'Hitam',
    'umur' : '88'
}

person3 = {
    'nama' : 'Whiterusi',
    'kulit' : 'Putih',
    'umur' : '69'
}

persons = {
    'person1' : person1,
    'person2' : person2,
    'person3' : person3
}

print(persons)

# looping

for keys, values in persons.items():
    print(f"\n {keys}")
    for fixedkeys in values:
        print(f"{fixedkeys} : {values[fixedkeys]}")
