import random

class EventSimulation:
    def __init__(self, probabilities):
        """
        Initialize the EventSimulation with probabilities and normalize them.

        Args:
            probabilities (dict): A dictionary of outcome probabilities.

        Raises:
            ValueError: If probabilities are invalid, i.e., not in [0, 1] or don't sum up to approximately 1.
        """
        self.normalized_probabilities = self.normalize_probabilities(probabilities)
        if not self.validate_normalized_probabilities(self.normalized_probabilities):
            raise ValueError("Invalid probabilities")

        self.outcomes = list(self.normalized_probabilities.keys())

    def validate_normalized_probabilities(self, normalized_probabilities):
        """
        Validate the normalized probabilities to ensure they are in the valid range and sum to approximately 1.

        Args:
            normalized_probabilities (dict): A dictionary of normalized outcome probabilities.

        Returns:
            bool: True if the normalized probabilities are valid, False otherwise.
        """
        if not all(0 <= prob <= 1 for prob in normalized_probabilities.values()):
            return False
        if abs(sum(normalized_probabilities.values()) - 1) > 1e-6:
            return False
        return True

    def normalize_probabilities(self, probabilities):
        """
        Normalize probabilities to ensure they sum up to 1.

        Args:
            probabilities (dict): A dictionary of outcome probabilities.

        Returns:
            dict: A dictionary of normalized outcome probabilities.
        """
        total = sum(probabilities.values())
        return {outcome: probability / total for outcome, probability in probabilities.items()}

    def simulate_event(self):
        """
        Simulate a single event outcome based on the normalized probabilities.

        Returns:
            Any: The simulated event outcome.
        """
        random_num = random.uniform(0, 1)
        current_prob_sum = 0
        for outcome, probability in self.normalized_probabilities.items():
            current_prob_sum += probability
            if random_num <= current_prob_sum:
                return outcome

    def simulate_multiple_occurrences(self, num_occurrences):
        """
        Simulate multiple event occurrences.

        Args:
            num_occurrences (int): The number of event occurrences to simulate.

        Returns:
            dict: A dictionary of outcome counts based on the simulations.
        """
        if num_occurrences < 0:
            raise ValueError("num_occurrences must be a positive integer")

        outcome_counts = {outcome: 0 for outcome in self.normalized_probabilities}
        for _ in range(num_occurrences):
            outcome = self.simulate_event()
            outcome_counts[outcome] += 1
        return outcome_counts

    def print_outcome_counts(self, outcome_counts):
        """
        Print the counts of each outcome after simulation.

        Args:
            outcome_counts (dict): A dictionary of outcome counts.
        """
        for outcome, count in outcome_counts.items():
            print(f"{outcome} appeared {count} times")

if __name__ == "__main__":
    input_data = {1: 10, 2: 30, 3: 15, 4: 15, 5: 30, 6: 0}
    print("====================================================")
    num_occurrences = 0
    event_simulator = EventSimulation(input_data)
    outcome_counts = event_simulator.simulate_multiple_occurrences(num_occurrences)
    event_simulator.print_outcome_counts(outcome_counts)

    print("====================================================")

    num_occurrences = 600
    event_simulator = EventSimulation(input_data)
    outcome_counts = event_simulator.simulate_multiple_occurrences(num_occurrences)
    event_simulator.print_outcome_counts(outcome_counts)

    print("====================================================")
    input_data = {"Head": 0.35, "Tail": 0.65}
    num_occurrences = 1000

    event_simulator = EventSimulation(input_data)
    outcome_counts = event_simulator.simulate_multiple_occurrences(num_occurrences)
    event_simulator.print_outcome_counts(outcome_counts)
