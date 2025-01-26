class EmotionalModel:
    def __init__(self):
        self.parameters = {
            "valence": 4,  # Default: neutral
            "arousal": 4,  # Default: neutral
            "selection_threshold": 4,  # Default: neutral
            "resolution_level": 4,  # Default: neutral
            "goal_directedness": 4,  # Default: neutral
            "securing_rate": 4,  # Default: neutral
        }

    def update_parameters(self, new_parameters):
        self.parameters.update(new_parameters)

    def calculate_anger(self):
        # Anger formula: high arousal + negative valence + high selection threshold
        arousal = self.parameters["arousal"]
        valence = self.parameters["valence"]
        selection_threshold = self.parameters["selection_threshold"]
        anger = (arousal + (7 - valence) + selection_threshold) / 3
        return min(max(anger, 1), 5)  # Clamp between 1 and 5

    def calculate_sadness(self):
        # Sadness formula: low arousal + negative valence + low goal-directedness
        arousal = self.parameters["arousal"]
        valence = self.parameters["valence"]
        goal_directedness = self.parameters["goal_directedness"]
        sadness = ((7 - arousal) + (7 - valence) + (7 - goal_directedness)) / 3
        return min(max(sadness, 1), 5)  # Clamp between 1 and 5

# Initialize emotional model
emotional_model = EmotionalModel()