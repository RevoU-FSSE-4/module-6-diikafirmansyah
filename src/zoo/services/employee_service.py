from zoo.repository.employee_repository import EmployeeRepository
from enum import Enum


class ListGender(Enum):
    MALE = "Male"
    FEMALE = "Female"


class EmployeeService:

    def __init__(self, employee_repository):
        self.employee_repository: EmployeeRepository = employee_repository

    def add_employee(self, employee):
        employee_name = employee.get("employee_name")
        age = employee.get("age")
        gender = employee.get("gender")

        if (
            not employee_name
            or not isinstance(employee_name, str)
            or len(employee_name) < 3
        ):
            raise ValueError(
                "Employee name must be a string and have 3 character minimun"
            )
        if not age or not isinstance(age, int):
            raise ValueError("Age of employee must be number and cannot be empty")
        if gender not in [gender.value for gender in ListGender]:
            raise ValueError("Gender must be on of : Male or Female")
        saved_employee = self.employee_repository.save(employee)

        return saved_employee

    def get_all(self):
        return self.employee_repository.get_all()

    def get_employee(self, id):
        return self.employee_repository.get_employee_by_id(int(id))

    def delete_employee(self, id):
        return self.employee_repository.delete_employee(int(id))

    def update_employee(self, employee, id):
        employee_name = employee.get("employee_name")
        age = employee.get("age")
        gender = employee.get("gender")
        species = employee.get("species")

        if (
            not employee_name
            or not isinstance(employee_name, str)
            or len(employee_name) < 3
        ):
            raise ValueError(
                "Employee name must be a string and have 3 character minimun"
            )
        if not age or not isinstance(age, int):
            raise ValueError("Age of employee must be number and cannot be empty")
        if gender not in [gender.value for gender in ListGender]:
            raise ValueError("Gender must be on of : Male or Female")

        updated_employee = self.employee_repository.update_employee(int(id), employee)

        return updated_employee
