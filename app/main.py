class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    person_objs = [Person(p['name'], p['age']) for p in people]

    for p in people:
        person_obj = Person.people[p['name']]
        if p.get('wife'):
            person_obj.wife = Person.people[p['wife']]
        if p.get('husband'):
            person_obj.husband = Person.people[p['husband']]

    return person_objs
