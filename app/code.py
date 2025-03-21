# Class Person:
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, city={self.city})"


# Create a list of dictionaries
data_list = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
]

# Create a list of Person objects
people = []
for data in data_list:
    person = Person(name=data['name'], age=data['age'], city=data['city'])
    people.append(person)

# Print the list of Person objects
for person in people:
    print(person)
