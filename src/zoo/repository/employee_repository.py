class EmployeeRepository:
    def __init__(self):
        self.employees = {}
        self.id = 1

    def save(self, employee):
        employee["id"] = self.id
        self.employees[self.id] = employee
        self.id += 1
        return employee

    def get_all(self):
        return list(self.employees.values())

    def get_employee_by_id(self, id):
        print(self.employees)
        return self.employees.get(id)

    def delete_employee(self, id):
        print(id)
        return self.employees.pop(id, None)

    def update_employee(self, id, updated_info):
        if id not in self.employees:
            raise ValueError("Animal with given ID does not exist")
        self.employees[id].update(updated_info)
        return self.employees[id]
