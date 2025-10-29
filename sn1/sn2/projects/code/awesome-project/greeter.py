class Greeter:
    def __init__(self, name: str):
        self.name = name

    def __call__(self):
        return("Hello, {}!".format(self.name))

greet = Greeter("Samke")

print(greet())
