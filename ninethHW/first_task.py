"""Create a class describing any company. For example, Toshiba or Apple"""


class Company:
    def __init__(self, name: str, industry: str, departures: str, founded_year: int):
        self._name = name
        self._industry = industry
        self._departures = departures
        self._founded_year = founded_year
        self._employees = []

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
        self._departures = value

    @property
    def founded_year(self) -> int:
        """
        Get the year in which the company was founded
        """
        return self._founded_year

    @founded_year.setter
    def founded_year(self, value: int) -> None:
        """
        Set the year in which the company was founded
        """
        self._founded_year = value

    @property
    def employees(self) -> list:
        """
        Get the list of employees in the company
        """
        return self._employees

    def hire_employee(self, employee: "Worker") -> None:
        """
        Hire an employee and add them to the company's employee list
        """
        self._employees.append(employee)

    def fire_employee(self, employee: "Worker") -> None:
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
