from zoo.repository.animal_repository import AnimalRepository
from enum import Enum
class ListSpecies(Enum):
    CARNIVORA = "Carnivora"
    OMNIVORA = "Omnivora"
    HERBIVORA = "Herbivora"
class AnimalService:
    def __init__(self, animal_repository):
        self.post_repository: AnimalRepository = animal_repository
    def add_animal(self, animal):
        animal_name = animal.get("animal_name")
        age = animal.get("age")
        gender = animal.get("gender")
        species = animal.get("species")
        if not animal_name or not isinstance(animal_name, str) or len(animal_name) < 3:
            raise ValueError("Animal name must be a string and have 3 character minimun")
        if not age or not isinstance(age, int):
            raise ValueError("Age of animal must be number and cannot be empty")
        if not gender or not isinstance(gender, str):
            raise ValueError("Gender of animal must be a string")
        if species not in [species.value for species in ListSpecies]:
            raise ValueError("Animal species must be on of : Carnivora, Omnivora or Herbivora")
        saved_animal = self.animal_repository.save(animal)
        return saved_animal
    def get_all(self):
        return self.animal_repository.get_all()
    def get_animal(self, id):
        return self.animal_repository.get_animal_by_id(int(id))
    def delete_post(self, id):
        return self.animal_repository.delete_animal(int(id))
    def update_animal (self, animal, id):
        animal_name = animal.get("animal_name")
        age = animal.get("age")
        gender = animal.get("gender")
        species = animal.get("species")
        if not animal_name or not isinstance(animal_name, str) or len(animal_name) < 3:
            raise ValueError("Animal name must be a string and have 3 character minimun")
        if not age or not isinstance(age, int):
            raise ValueError("Age of animal must be number and cannot be empty")
        if not gender or not isinstance(gender, str):
            raise ValueError("Gender of animal must be a string")
        if species not in [species.value for species in ListSpecies]:
            raise ValueError("Animal species must be on of : Carnivora, Omnivora or Herbivora")
        updated_animal = self.animal_repository.update_animal(int(id), animal)
        return updated_animal