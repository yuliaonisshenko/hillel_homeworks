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
        """
        Get the name of the company
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Set the name of the company
        """
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    @property
    def industry(self) -> str:
        """
        Get the industry of the company
        """
        return self._industry

    @industry.setter
    def industry(self, value: str) -> None:
        """
        Set the industry of the company.
        """
        if not isinstance(value, str):
            raise ValueError("Industry must be a string.")
        self._industry = value

    @property
    def departures(self) -> str:
        """
        Get the departures of the company
        """
        return self._departures

    @departures.setter
    def departures(self, value: str) -> None:
        """
        Set the departures of the company
        """
        if not isinstance(value, str):
            raise ValueError("Departures must be a string.")
        self._departures = value

    @property
    def employees(self) -> list[Worker]:
        """
        Get the list of employees in the company
        """
        return self._employees

    def hire_employee(self, employee: Worker) -> None:
        """
        Hire an employee and add them to the company's employee list
        """
        self._employees.append(employee)

    def fire_employee(self, employee: Worker) -> None:
        """
        Fire an employee and remove them from the company's employee list
        """
        if employee in self._employees:
            self._employees.remove(employee)

    def get_total_employees(self) -> int:
        """
        Get the total number of employees in the company
        """
        return len(self._employees)

    @staticmethod
    def get_total_companies() -> int:
        """
        Get the total amount on companies
        """
        return len(Company.all_companies)

    @classmethod
    def get_all_companies(cls) -> list["Company"]:
        """
        Get all companies
        """
        return cls.all_companies
