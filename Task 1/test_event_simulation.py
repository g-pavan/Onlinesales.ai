import unittest
from event_simulation import EventSimulation  

class TestEventSimulation(unittest.TestCase):
    def test_valid_integer_probabilities(self):
        input_data = {1: 10, 2: 30, 3: 15, 4: 15, 5: 30, 6: 0}
        event_simulator = EventSimulation(input_data)
        outcome_counts = event_simulator.simulate_multiple_occurrences(1000)
        self.assertTrue(all(count >= 0 for count in outcome_counts.values()))
        self.assertAlmostEqual(sum(outcome_counts.values()), 1000, delta=10)

    def test_valid_float_probabilities(self):
        input_data = {1: 0.1, 2: 0.3, 3: 0.15, 4: 0.15, 5: 0.3, 6: 0.0}
        event_simulator = EventSimulation(input_data)
        outcome_counts = event_simulator.simulate_multiple_occurrences(1000)
        self.assertTrue(all(count >= 0 for count in outcome_counts.values()))
        self.assertAlmostEqual(sum(outcome_counts.values()), 1000, delta=10)

    def test_negative_num_occurrences(self):
        input_data = {1: 10, 2: 30, 3: 15, 4: 15, 5: 30, 6: 0}
        event_simulator = EventSimulation(input_data)
        with self.assertRaises(ValueError):
            event_simulator.simulate_multiple_occurrences(-5)

    def test_zero_num_occurrences(self):
        input_data = {1: 10, 2: 30, 3: 15, 4: 15, 5: 30, 6: 0}
        event_simulator = EventSimulation(input_data)
        outcome_counts = event_simulator.simulate_multiple_occurrences(0)
        self.assertEqual(sum(outcome_counts.values()), 0)

    def test_outcome_counts_sum(self):
        input_data = {1: 10, 2: 30, 3: 15, 4: 15, 5: 30, 6: 0}
        event_simulator = EventSimulation(input_data)
        outcome_counts = event_simulator.simulate_multiple_occurrences(1000)
        self.assertAlmostEqual(sum(outcome_counts.values()), 1000, delta=10)

    def test_negative_probabilities(self):
        input_data = {1: 10, 2: 30, 3: 15, 4: -5, 5: 30, 6: 0}
        with self.assertRaises(ValueError):
            EventSimulation(input_data)

    def test_higher_normalized_values(self):
        input_data = {1: 0.9, 2: 0.2}
        event_simulator = EventSimulation(input_data)
        outcome_counts = event_simulator.simulate_multiple_occurrences(1000)
        self.assertTrue(all(count >= 0 for count in outcome_counts.values()))
        self.assertAlmostEqual(sum(outcome_counts.values()), 1000, delta=10)

if __name__ == '__main__':
    unittest.main()
