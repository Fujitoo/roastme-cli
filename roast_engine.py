"""
Roast generator engine for RoastMe CLI.
Handles randomization and roast generation.
"""

import random
from roast_data import (
    ROAST_TEMPLATES,
    COMEBACK_JUDGMENTS,
    GREETINGS,
    FAREWELLS,
)


class RoastEngine:
    """Engine for generating roasts based on user input."""

    def __init__(self, name: str, hobby: str, major: str, confidence: int, level: str = "medium"):
        self.name = name or "Anonymous"
        self.hobby = hobby or "scrolling"
        self.major = major or "Undeclared"
        self.confidence = max(1, min(10, confidence or 5))
        self.level = level.lower() if level else "medium"

        if self.level not in ["easy", "medium", "savage"]:
            self.level = "medium"

    def generate_roast(self, style: str = None) -> str:
        """Generate a single roast, optionally from a specific style."""
        if style and style in ROAST_TEMPLATES:
            templates = ROAST_TEMPLATES[style][self.level]
        else:
            # Random style
            style = random.choice(list(ROAST_TEMPLATES.keys()))
            templates = ROAST_TEMPLATES[style][self.level]

        template = random.choice(templates)
        return template.format(
            name=self.name,
            hobby=self.hobby,
            major=self.major,
            confidence=self.confidence,
        )

    def generate_roasts(self, count: int = 5, style: str = None) -> list[str]:
        """Generate multiple roasts with varied styles."""
        roasts = []
        
        if style:
            # Use specific style
            for i in range(count):
                roast = self.generate_roast(style)
                # Avoid duplicates
                attempts = 0
                while roast in roasts and attempts < 5:
                    roast = self.generate_roast(style)
                    attempts += 1
                roasts.append(roast)
        else:
            # Cycle through all styles for variety
            styles = list(ROAST_TEMPLATES.keys())
            for i in range(count):
                style = styles[i % len(styles)]
                roast = self.generate_roast(style)
                # Avoid duplicates
                attempts = 0
                while roast in roasts and attempts < 5:
                    roast = self.generate_roast(style)
                    attempts += 1
                roasts.append(roast)

        return roasts

    def rate_comeback(self, comeback: str) -> tuple[int, str]:
        """Rate a comeback and return a judgment."""
        # Simple rating based on length and keywords
        base_score = min(10, max(1, len(comeback) // 5))

        # Bonus points for certain words
        bonus_words = ["you", "your", "at least", "says", "called"]
        comeback_lower = comeback.lower()
        for word in bonus_words:
            if word in comeback_lower:
                base_score = min(10, base_score + 1)

        # Add some randomness
        rating = max(1, min(10, base_score + random.randint(-2, 2)))

        # Get judgment based on rating
        for (low, high), judgments in COMEBACK_JUDGMENTS.items():
            if low <= rating <= high:
                judgment = random.choice(judgments)
                break
        else:
            judgment = "Interesting choice of words."

        # Personalize judgment
        judgment = judgment.format(
            name=self.name,
            hobby=self.hobby,
            major=self.major,
        )

        return rating, judgment

    def get_greeting(self) -> str:
        """Get a random greeting message."""
        greeting = random.choice(GREETINGS)
        return greeting.format(name=self.name)

    def get_farewell(self) -> str:
        """Get a random farewell message."""
        farewell = random.choice(FAREWELLS)
        return farewell.format(name=self.name)

    def get_style_description(self, style: str) -> str:
        """Get a description of a roast style."""
        descriptions = {
            "academic": "📚 Academic Roast - For the academically challenged",
            "nerd": "🤓 Nerd Roast - For the tech-obsessed",
            "overconfident": "💪 Overconfident Roast - For the boldly delusional",
            "existential": "🌌 Existential Roast - For the spiritually lost",
            "lifestyle": "🏠 Lifestyle Roast - For the domestically challenged",
        }
        return descriptions.get(style, "🎯 Generic Roast")

    def get_level_description(self) -> str:
        """Get a description of the current difficulty level."""
        descriptions = {
            "easy": "🧸 Easy - Playful teasing, gentle jabs",
            "medium": "🌶️ Medium - Sharp sarcasm, actual burns",
            "savage": "🔥 Savage - Brutal honesty, maximum damage",
        }
        return descriptions.get(self.level, "🌶️ Medium - Sharp sarcasm, actual burns")
