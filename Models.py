class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def to_dict(self):
        return self.__dict__
    def __str__(self):
        return f"{self.name} -> {self.password}"

    @classmethod
    def dict_to(cls, data):
        return cls(data["name"], data["password"])