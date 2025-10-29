class Greeter:
    async def __init__(self, name: str):
        self.name = name

    async def __call__(self):
        return("Hello, {}!".format(self.name))

greet = Greet("Samke")

print(greet())
