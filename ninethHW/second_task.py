"""Create a class with a description of the worker. Any worker. employees."""


class Worker:
    def __init__(self, name: str, age: int, job_position: str, salary: float):
        self._name = name
        self._age = age
        self._job_position = job_position
        self._salary = salary

    @property
    def name(self) -> str:
        """
        Get the name of worker
        """
        return self._name

    @property
    def age(self) -> int:
        """
        Get the age of worker
        """
        return self._age

    @property
    def position(self) -> str:
        """
        Get the job position of worker
        """
        return self._job_position

    @property
    def salary(self) -> float:
        """
        Get the salary of worker
        """
        return self._salary

    @salary.setter
    def salary(self, new_salary: float) -> None:
        """
        Set the salary of worker
        """
        self._salary = new_salary

    def promote(self, new_job_position: str, new_salary: float) -> None:
        """
        Promote the worker to new job position with new salary
        """
        self._job_position = new_job_position
        self._salary = new_salary
