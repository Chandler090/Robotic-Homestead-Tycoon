"""
Robot module for the Robotic Homestead Tycoon game.
Defines the Robot class responsible for performing tasks in the environment.
"""

class Robot:
    """A simple robot actor that can move, perform actions and manage its own energy."""

    def __init__(self, robot_id: int, role: str = "harvester", energy: float = 100.0, location: tuple = (0, 0)) -> None:
        self.id = robot_id
        self.role = role
        self.energy = energy
        self.location = location
        self.cargo = None  # can hold harvested crops or building materials

    def move(self, new_location: tuple) -> None:
        """Move the robot to a new location and reduce energy."""
        # Compute energy cost based on distance (simple Manhattan distance)
        distance = abs(new_location[0] - self.location[0]) + abs(location[1] - self.location[1])
        self.energy = max(0.0, self.energy - distance * 0.5)
        self.location = new_location

    def perform_action(self, environment, homestead) -> None:
        """Perform an action based on the robot's role. Placeholder for now."""
        if self.energy <= 0:
            return  # robot is out of energy

        if self.role == "harvester":
            # Harvest crops (placeholder logic)
            # In a full implementation, interact with homestead fields and environment
            self.energy = max(0.0, self.energy - 5.0)
        elif self.role == "builder":
            # Build or upgrade structures (placeholder)
            self.energy = max(0.0, self.energy - 10.0)
        elif self.role == "maintenance":
            # Perform maintenance tasks (placeholder)
            self.energy = max(0.0, self.energy - 2.0)
        else:
            # Unknown role; idle
            self.energy = max(0.0, self.energy - 1.0)

    def recharge(self, amount: float) -> None:
        """Recharge the robot's battery by a given amount (bounded)."""
        self.energy = min(100.0, self.energy + amount)
