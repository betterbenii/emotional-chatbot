class EmotionalModel:
    def __init__(self):
        
        """
        Initializes the EmotionalModel with default parameters.

        The default parameters are set to a neutral state (4/7) for all six parameters:
        valence, arousal, selection threshold, resolution level, goal-directedness, and
        securing rate. These parameters are used to calculate the chatbot's emotional states
        (anger and sadness) and influence its responses. The parameters can be adjusted
        through the `update_parameters` method.
        """
        self.parameters = {
            "valence": 4,  # Default: neutral
            "arousal": 4,  # Default: neutral
            "selection_threshold": 4,  # Default: neutral
            "resolution_level": 4,  # Default: neutral
            "goal_directedness": 4,  # Default: neutral
            "securing_rate": 4,  # Default: neutral
        }

    def update_parameters(self, new_parameters):
        """
        Updates the emotional parameters of the chatbot.

        Parameters:
            new_parameters (dict): A dictionary with the new values for any of the six parameters:
                valence, arousal, selection threshold, resolution level, goal-directedness, and
                securing rate. Existing parameters will be updated with the new values.
        """
        
        self.parameters.update(new_parameters)

    def calculate_anger(self):
        # Anger formula: high arousal + negative valence + high selection threshold
        """
        Calculates the chatbot's current anger level based on its emotional parameters.

        The anger formula is a simple average of the arousal, negative valence, and
        selection threshold parameters. The result is clamped between 1 and 5.

        Returns:
            int: The current anger level of the chatbot (between 1 and 5).
        """
        arousal = self.parameters["arousal"]
        valence = self.parameters["valence"]
        selection_threshold = self.parameters["selection_threshold"]
        anger = (arousal + (7 - valence) + selection_threshold) / 3
        return min(max(anger, 1), 5)  # Clamp between 1 and 5

    def calculate_sadness(self):
        # Sadness formula: low arousal + negative valence + low goal-directedness
        """
        Calculates the chatbot's current sadness level based on its emotional parameters.

        The sadness formula is a simple average of the low arousal, negative valence, and
        low goal-directedness parameters. The result is clamped between 1 and 5.

        Returns:
            int: The current sadness level of the chatbot (between 1 and 5).
        """
        arousal = self.parameters["arousal"]
        valence = self.parameters["valence"]
        goal_directedness = self.parameters["goal_directedness"]
        sadness = ((7 - arousal) + (7 - valence) + (7 - goal_directedness)) / 3
        return min(max(sadness, 1), 5)  # Clamp between 1 and 5


emotional_model = EmotionalModel()