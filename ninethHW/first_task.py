"""Create a class describing any company. For example, Toshiba or Apple"""


from worker import Worker

class Company:
    # Class attribute
    all_companies = []

    def __init__(self, name: str, industry: str, departures: str):
        self._name = name
        self._industry = industry
        self._departures = departures
        self._employees = []
        self.__class__.all_companies.append(self)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    @property
    def industry(self) -> str:
        return self._industry

    @industry.setter
    def industry(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Industry must be a string.")
        self._industry = value

    @property
    def departures(self) -> str:
        return self._departures

    @departures.setter
    def departures(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Departures must be a string.")
        self._departures = value

    @property
    def employees(self) -> list[Worker]:
        return self._employees

    def hire_employee(self, employee: Worker) -> None:
        self._employees.append(employee)

    def fire_employee(self, employee: Worker) -> None:
        if employee in self._employees:
            self._employees.remove(employee)

    def get_total_employees(self) -> int:
        return len(self._employees)

    @staticmethod
    def get_total_companies() -> int:
        return len(Company.all_companies)

    @classmethod
    def get_all_companies(cls) -> list["Company"]:
        return cls.all_companies
