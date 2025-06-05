# sigil_kin/kin.py

class SigilKin:
    def __init__(self, name, sin_affinity):
        self.name = name
        self.sin_affinity = sin_affinity
        self.trust_level = 0
        self.skills = []
        self.mood = "neutral"

    def feed(self, item):
        if item == "relic":
            self.trust_level += 10
            self.mood = "content"
        elif item == "sin_token":
            self.trust_level += 5
            self.mood = "energized"
        else:
            self.trust_level -= 2
            self.mood = "unsettled"

    def train(self, skill):
        if self.trust_level >= 10:
            self.skills.append(skill)
            self.trust_level -= 5
            return f"{self.name} learned {skill}!"
        return f"{self.name} needs more trust to learn that."

    def mood_status(self):
        return f"{self.name} feels {self.mood}."

    def get_summary(self):
        return {
            "Name": self.name,
            "Affinity": self.sin_affinity,
            "Trust Level": self.trust_level,
            "Mood": self.mood,
            "Skills": self.skills
        }
