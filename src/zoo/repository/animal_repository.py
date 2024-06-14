class AnimalRepository:
    def __init__(self):
        self.animals = {}
        self.id = 1

    def save(self, animal):
        animal["id"] = self.id
        self.animals[self.id] = animal
        self.id += 1
        return animal

    def get_all(self):
        return list(self.animals.values())

    def get_animal_by_id(self, id):
        print(self.animals)
        return self.animals.get(id)

    def delete_animal(self, id):
        print(id)
        return self.animals.pop(id, None)

    def update_animal(self, id, updated_info):
        if id not in self.animals:
            raise ValueError("Animal with given ID does not exist")
        self.animals[id].update(updated_info)
        return self.animals[id]
