import random
from typing import Optional

from data.compression_service import CompressionService
from models.character import Character
from models.game_definition import GameDefinition
from models.state import GameState
from utils.singleton import Singleton

class DataService(metaclass=Singleton):

    def __init__(self):
        self.gameDefinition:Optional[GameDefinition] = None
        self.gameStarted:bool = False
        self.state:GameState = GameState("Welcome to the game", "prologue")
        self.characters:[Character] = []
        self.summaries:[str] = []

    def update_characters(self, characters_updates:[Character]) -> None:
        # Replace all characters with the same name with the new ones
        for character in characters_updates:
            self.characters = [character if c.name() == character.name() else c for c in self.characters]

        # Add new characters
        for character in characters_updates:
            if character not in self.characters:
                self.characters.append(character)

    def save_summary(self, summary:str) -> None:
        self.summaries.append(summary)

        if len(self.summaries) > 100:
            self.summaries = CompressionService.compress_summaries(self.summaries)

    def get_characters_of_location(self, location:str) -> [Character]:
        return [character for character in self.characters if character.location() == location]

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
        GameDefinition(
            "Fantasy wizard named Merlin",
            "1200",
            "Magical Adventure",
            "Master the arcane arts and protect the realm from dark forces",
            "Learn spells, brew potions, and battle mythical creatures"
        ),
        GameDefinition(
            "Modern spy named Agent X",
            "2025",
            "Espionage Thriller",
            "Uncover international conspiracies and prevent global conflicts",
            "Infiltrate enemy organizations, gather intel, and eliminate threats"
        ),
        GameDefinition(
            "Pirate captain named Redbeard",
            "1700",
            "High Seas Adventure",
            "Plunder treasure and establish a pirate empire",
            "Sail the Caribbean, engage in naval battles, and search for buried loot"
        ),
        GameDefinition(
            "Space marine named Commander Vargas",
            "2500",
            "Sci-fi Warfare",
            "Defend humanity from alien invaders and rogue AI",
            "Pilot advanced spacecraft, lead ground assaults, and deploy orbital strikes"
        ),
        GameDefinition(
            "Mythical hero named Achilles",
            "1200 BC",
            "Ancient Mythology",
            "Embark on epic quests and face legendary monsters",
            "Seek the favor of the gods, wield enchanted weapons, and challenge fate"
        ),
        GameDefinition(
            "Modern firefighter named Blaze",
            "2020",
            "Emergency Response",
            "Save lives and protect the community from disasters",
            "Battle raging fires, rescue civilians, and provide medical aid"
        ),
        GameDefinition(
            "Steampunk inventor named Professor Gear",
            "1880",
            "Industrial Revolution",
            "Invent groundbreaking machines and revolutionize society",
            "Build steam-powered contraptions, compete in exhibitions, and outwit rivals"
        ),
        GameDefinition(
            "Zombie apocalypse survivor named Alice",
            "2035",
            "Survival Horror",
            "Escape the undead hordes and find sanctuary",
            "Scavenge for supplies, fortify shelters, and confront zombie mutations"
        ),
        GameDefinition(
            "Samurai warrior named Hanzo",
            "1600",
            "Feudal Japan",
            "Serve a noble lord and uphold the samurai code",
            "Train in martial arts, engage in duels, and defend honor"
        ),
        GameDefinition(
            "Modern archaeologist named Lara",
            "2020",
            "Adventure Exploration",
            "Discover lost civilizations and ancient artifacts",
            "Navigate treacherous ruins, decipher cryptic puzzles, and outwit rivals"
        ),
        GameDefinition(
            "Alien diplomat named Zara",
            "3000",
            "Intergalactic Diplomacy",
            "Negotiate peace treaties and forge alliances",
        "Mediate disputes between alien species, navigate political intrigue, and prevent wars",
        ),
        GameDefinition(
            "Fantasy bard named Lyra",
            "1400",
            "Musical Quest",
            "Travel the land and compose epic ballads",
            "Perform in royal courts, collect rare instruments, and uncover forgotten songs"
        ),
        GameDefinition(
            "Modern chef named Gordon",
            "2020",
            "Culinary Challenge",
            "Climb the ranks and earn Michelin stars",
            "Create signature dishes, manage restaurants, and compete in cooking competitions"
        ),
        GameDefinition(
            "Superhero vigilante named Shadow",
            "2025",
            "Crime Fighting",
            "Protect the city from supervillains and corruption",
            "Develop superpowers, build gadgets, and maintain a secret identity"
        ),
        GameDefinition(
            "Fantasy blacksmith named Forge",
            "1100",
            "Craftsmanship",
            "Forge legendary weapons and armor",
            "Mine rare ores, master ancient techniques, and fulfill epic commissions"
        ),
        GameDefinition(
            "Modern athlete named Ace",
            "2020",
            "Sports Competition",
            "Train hard and win championships",
            "Compete in tournaments, break records, and inspire fans"
        ),
        GameDefinition(
            "Time-traveling historian named Tempus",
            "3000",
            "Temporal Exploration",
            "Witness key events and preserve the timeline",
            "Interact with historical figures, prevent paradoxes, and explore alternate realities"
        ),
    ]

    game_definition_suggestion: GameDefinition = random.choice(randomGameDefinitions)

    def change_game_definition_suggestion(self):
        self.game_definition_suggestion = random.choice(self.randomGameDefinitions)

    def reset(self):
        self.gameDefinition = None
        self.gameStarted = False
        self.state = GameState("Welcome to the game", "prologue")
        self.characters = []
        self.summaries = []
