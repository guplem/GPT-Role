class Character:

    def __init__(self, name:str, description:str, location:str, inventory:[str]):
        self._name:str = name
        self._description:str = description
        self._location:str = location
        self._inventory:[str] = inventory

    def __str__(self):
        return f"""
        Name: {self._name}
        \nDescription: {self._description}
        \nLocation: {self._location}
        \nInventory: {self._inventory}"""


    def name(self) -> str:
        return self._name

    def description(self) -> str:
        return self._description

    def location(self) -> str:
        return self._location

    def inventory(self) -> [str]:
        return self._inventory

    def set_location(self, location:str) -> None:
        self._location = location

    def add_to_inventory(self, item:str) -> None:
        self._inventory.append(item)

    def remove_from_inventory(self, item:str) -> None:
        self._inventory.remove(item)


    def to_json(self):
        return {
            "name": self._name,
            "description": self._description,
            "location": self._location,
            "inventory": self._inventory
        }