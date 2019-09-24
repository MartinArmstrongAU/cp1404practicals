
class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection="", year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return ""

    def is_dynamic(self):
        return self.typing == "Dynamic"

