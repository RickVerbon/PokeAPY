
class Pokemon:
    def __init__(self, id, name, height, weight, types, moves, abilities, stats, sprites) -> None:
        self.id = id
        self.name = name
        self.height = height
        self.weight = weight
        self.types = types
        self.moves = moves
        self.abilities = abilities
        self.stats = stats
        self.sprites = sprites

    def __str__(self) -> str:
        return f"{self.name.capitalize()} (ID: {self.id})"


class Move:
    def __init__(self, name, accuracy, power, pp, priority, type, damage_class, learned_by) -> None:
        self.name = name
        self.accuracy = accuracy
        self.power = power
        self.pp = pp
        self.priority = priority
        self.type = type
        self.damage_class = damage_class
        self.learned_by = learned_by

    def __str__(self) -> str:
        return f"{self.name.capitalize()}"
