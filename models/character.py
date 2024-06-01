class Character:

    def __init__(self, name:str, description:str, location:str, inventory:[str]):
        self.name:str = name
        self.description:str = description
        self.location:str = location
        self.inventory:[str] = inventory

    def __str__(self):
        return f"""
        Name: {self.name}
        \nDescription: {self.description}
        \nLocation: {self.location}
        \nInventory: {self.inventory}"""
