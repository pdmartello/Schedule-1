class Ingredient:
    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        attrs = ", ".join(f"{k}={v}" for k, v in self.__dict__.items() if k != 'name')
        return f"Ingredient('{self.name}', {attrs})"