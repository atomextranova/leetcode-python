# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
class Solution:
    """
    :type robot: Robot
    :rtype: None
    """
    def cleanRoom(self, robot):
        #write your code here
        visited = set()
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = 0
        y = 0
        self.face = 0
        self.dfs(robot, visited, x, y)

    def dfs(self, robot, visited, x, y):
        if (x, y) in visited:
            return
        visited.add((x, y))
        robot.clean()

        for i in range(4):
            dx, dy = self.directions[self.face]
            new_pos = (x + dx, y + dy)
            if robot.move():
                self.dfs(robot, visited, new_pos[0], new_pos[1])
                self.back_by_one_step(robot)
            self.turn_right(robot)

    def back_by_one_step(self, robot):
        robot.turnLeft()
        robot.turnLeft()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    def turn_left(self, robot):
        robot.turnLeft()
        self.face = (self.face - 1) % 4

    def turn_right(self, robot):
        robot.turnRight()
        self.face = (self.face + 1) % 4