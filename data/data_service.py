import random

from data.compression_service import CompressionService
from models.character import Character
from models.game_definition import GameDefinition
from models.state import GameState
from utils.singleton import Singleton

class DataService(metaclass=Singleton):

    def __init__(self):
        self.gameDefinition:GameDefinition = GameDefinition("", "", "", "", "")
        self.gameStarted:bool = False
        self.state:GameState = GameState("Welcome to the game", "prologue")
        self.characters:[Character] = []
        self.summaries:[str] = []

    def update_characters(self, characters_updates:[Character]) -> None:
        # Replace all characters with the same name with the new ones
        for character in characters_updates:
            self.characters = [character if c.name == character.name else c for c in self.characters]

        # Add new characters
        for character in characters_updates:
            if character not in self.characters:
                self.characters.append(character)

    def save_summary(self, summary:str) -> None:
        self.summaries.append(summary)

        if len(self.summaries) > 100:
            self.summaries = CompressionService.compress_summaries(self.summaries)

    def get_characters_of_location(self, location:str) -> [Character]:
        return [character for character in self.characters if character.location == location]

    randomGameDefinitions: [GameDefinition] = [
        GameDefinition(
            "Neanderthal hunter named Grok",
            "2021",
            "Prehistoric Survival",
            "Survive and establish a thriving tribe",
            "Face the elements and wild animals while discovering fire and basic tools"
        ),
        GameDefinition(
            "Space explorer named Nova",
            "2200",
            "Sci-fi Exploration",
            "Explore and colonize distant planets",
            "Navigate alien terrains, meet extraterrestrial beings, and gather resources"
        ),
        GameDefinition(
            "Medieval knight named Sir Galahad",
            "1250",
            "Medieval Fantasy",
            "Defend the kingdom from invaders and mythical creatures",
            "Complete quests, train squires, and participate in jousting tournaments"
        ),
        GameDefinition(
            "Cyberpunk hacker named Zero",
            "2077",
            "Cyberpunk",
            "Uncover corporate secrets and fight against digital oppression",
            "Upgrade your cybernetic implants and avoid law enforcement"
        ),
        GameDefinition(
            "Ancient Roman soldier named Maximus",
            "50 BC",
            "Historical Warfare",
            "Expand the Roman Empire and achieve military glory",
            "Engage in epic battles and political intrigue within the Roman Senate"
        ),
        GameDefinition(
            "Wild West outlaw named Black Jack",
            "1870",
            "Western Adventure",
            "Build your reputation as the most feared outlaw",
            "Rob trains, duel in shootouts, and evade the law"
        ),
        GameDefinition(
            "Renaissance artist named Leonardo",
            "1500",
            "Artistic Renaissance",
            "Create masterpieces and gain patronage from influential figures",
            "Navigate the politics of the art world and rival artists"
        ),
        GameDefinition(
            "Future stock trader named Aiden",
            "2050",
            "Financial Strategy",
            "Dominate the stock market and become a financial tycoon",
            "Use advanced algorithms and insider information to make strategic trades"
        ),
        GameDefinition(
            "Post-apocalyptic survivor named Raven",
            "2085",
            "Post-apocalyptic Survival",
            "Rebuild society after a catastrophic event",
            "Scavenge for resources, form alliances, and fend off hostile factions"
        ),
        GameDefinition(
            "Victorian detective named Sherlock",
            "1890",
            "Mystery Investigation",
            "Solve complex cases and bring criminals to justice",
            "Gather clues, interrogate suspects, and uncover hidden motives"
        ),
    ]

    game_definition_suggestion: GameDefinition = random.choice(randomGameDefinitions)

    def change_game_definition_suggestion(self):
        self.game_definition_suggestion = random.choice(self.randomGameDefinitions)
