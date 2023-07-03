class Worker:
    def __init__(self, name: str, position: str):
        self._name = None
        self._position = None
        self.name = name
        self.position = position

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    @property
    def position(self) -> str:
        return self._position

    @position.setter
    def position(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Position must be a string.")
        self._position = value
