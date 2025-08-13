from game.environment import Environment
from game.homestead import Homestead
from game.robot import Robot


def main():
    """Initialize the game and run a simple simulation loop."""
    env = Environment()
    homestead = Homestead()

    # Example: create a single robot for demonstration
    robot = Robot(robot_id=1, role='planter')
    homestead.add_robot(robot)

    # Run a basic simulation loop for a few steps
    for step in range(10):
        env.update()
        homestead.update(env)
        print(f"Step {step + 1}: Time {env.time}, Robots {len(homestead.robots)}")


if __name__ == '__main__':
    main()
