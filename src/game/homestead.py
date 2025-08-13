"""
Homestead module for the Robotic Homestead Tycoon game.
Defines the Homestead class that manages the farm, robots, and resources.
"""

from typing import List, Dict

from .robot import Robot

class Homestead:
    """Represents the player's homestead including fields, robots, resources, and finances."""

    def __init__(self) -> None:
        # List of fields (for future expansion; could store crop types, growth stages, etc.)
        self.fields: List[Dict] = []
        # Active robots on the homestead
        self.robots: List[Robot] = []
        # Financial resources available to the player
        self.funds: float = 1000.0
        # Energy reserve for charging robots
        self.energy_reserve: float = 500.0
        # Storage for harvested goods
        self.storage: Dict[str, float] = {}

    def add_robot(self, robot: Robot) -> None:
        """Add a robot to the homestead."""
        self.robots.append(robot)

    def remove_robot(self, robot: Robot) -> None:
        """Remove a robot from the homestead."""
        if robot in self.robots:
            self.robots.remove(robot)

    def update(self, environment) -> None:
        """Update all robots and manage resources each simulation step."""
        # Recharge robots if energy reserve available
        for robot in self.robots:
            if robot.energy < 20.0 and self.energy_reserve > 0:
                charge_amount = min(20.0, self.energy_reserve)
                robot.recharge(charge_amount)
                self.energy_reserve -= charge_amount
            # Let the robot perform its role-specific action
            robot.perform_action(environment, self)

        # Simple placeholder: gradually accumulate funds based on number of robots
        self.funds += len(self.robots) * 0.5

    def harvest_crop(self, crop_type: str, quantity: float) -> None:
        """Store harvested crops in storage."""
        self.storage[crop_type] = self.storage.get(crop_type, 0) + quantity

    def consume_energy(self, amount: float) -> None:
        """Consume energy from the reserve (for other operations)."""
        self.energy_reserve = max(0.0, self.energy_reserve - amount)
