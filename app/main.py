class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    person_objs = [Person(person_data["name"], person_data["age"]) for person_data in people]

    for person_data in people:
        person_obj = Person.people[person_data["name"]]
        if person_data.get("wife"):
            person_obj.wife = Person.people[person_data["wife"]]
        if person_data.get("husband"):
            person_obj.husband = Person.people[person_data["husband"]]

    return person_objs
