# Author: hawkerpl
# https://gist.github.com/hawkerpl/b20439f449d607cfd8b5

# fork from http://code.activestate.com/recipes/577519-a-star-shortest-path-algorithm/

from heapq import heappush, heappop  # for priority queue
from node import Node
import numpy as np


class Pathfinder(object):
    def __init__(self, the_map, number_of_possible_directions, start, finish):
        self.the_map = the_map
        self.number_of_possible_directions = number_of_possible_directions
        self.start = start
        self.finish = finish
        self.y_range = len(the_map)
        self.x_range = len(the_map[0])
        self.directions = Pathfinder.get_possible_directions_of_movement(number_of_possible_directions)


    def run(self):
        """
        :return: list of tuples with coordinates
        """
        self.route = self.pathFind()
        self.route_coordinates = self.route_as_coordinates()
        return self.route_coordinates

    #@TODO
    #This is outrageus and CRAVES for refactorisation
    # A-star algorithm.
    # The path returned will be a string of digits of directions.
    def pathFind(self):
        number_possible_directions = self.number_of_possible_directions
        dx, dy = self.directions
        xA, yA = self.start
        if type(xA) is not int and type(yA) is not int:
            raise ValueError
        xB, yB = self.finish
        if type(xB) is not int and type(yB) is not int:
            raise ValueError
        closed_nodes_map = []  # map of closed (tried-out) nodes
        open_nodes_map = []  # map of open (not-yet-tried) nodes
        dir_map = []  # map of directions
        row = [0] * self.x_range
        for i in range(self.y_range):  # create 2d arrays
            closed_nodes_map.append(list(row))
            open_nodes_map.append(list(row))
            dir_map.append(list(row))

        pq = [[], []]  # priority queues of open (not-yet-tried) nodes
        pqi = 0  # priority queue index
        # create the start node and push into list of open nodes
        n0 = Node(xA, yA, 0, 0)
        n0.updatePriority(xB, yB)
        heappush(pq[pqi], n0)
        open_nodes_map[yA][xA] = n0.priority  # mark it on the open nodes map

        # A* search
        while len(pq[pqi]) > 0:
            # get the current node w/ the highest priority
            # from the list of open nodes
            n1 = pq[pqi][0]  # top node
            n0 = Node(n1.xPos, n1.yPos, n1.distance, n1.priority)
            x = n0.xPos
            y = n0.yPos
            heappop(pq[pqi])  # remove the node from the open list
            open_nodes_map[y][x] = 0
            closed_nodes_map[y][x] = 1  # mark it on the closed nodes map
            # quit searching when the goal is reached
            # if n0.estimate(xB, yB) == 0:
            if x == xB and y == yB:
                # generate the path from finish to start
                # by following the directions
                path = ''
                while not (x == xA and y == yA):
                    j = dir_map[y][x]
                    c = str((j + number_possible_directions / 2) % number_possible_directions)
                    path = c + path
                    x += dx[j]
                    y += dy[j]
                return path

            # generate moves (child nodes) in all possible directions
            for i in range(number_possible_directions):
                xdx = x + dx[i]
                ydy = y + dy[i]
                if not (xdx < 0 or xdx > self.x_range - 1 or ydy < 0 or ydy > self.y_range - 1
                        or self.the_map[ydy][xdx] == 1 or closed_nodes_map[ydy][xdx] == 1):
                    # generate a child node
                    m0 = Node(xdx, ydy, n0.distance, n0.priority)
                    m0.nextMove(number_possible_directions, i)
                    m0.updatePriority(xB, yB)
                    # if it is not in the open list then add into that
                    if open_nodes_map[ydy][xdx] == 0:
                        open_nodes_map[ydy][xdx] = m0.priority
                        heappush(pq[pqi], m0)
                        # mark its parent node direction
                        dir_map[ydy][xdx] = (i + number_possible_directions / 2) % number_possible_directions
                    elif open_nodes_map[ydy][xdx] > m0.priority:
                        # update the priority
                        open_nodes_map[ydy][xdx] = m0.priority
                        # update the parent direction
                        dir_map[ydy][xdx] = (i + number_possible_directions / 2) % number_possible_directions
                        # replace the node
                        # by emptying one pq to the other one
                        # except the node to be replaced will be ignored
                        # and the new node will be pushed in instead
                        while not (pq[pqi][0].xPos == xdx and pq[pqi][0].yPos == ydy):
                            heappush(pq[1 - pqi], pq[pqi][0])
                            heappop(pq[pqi])
                        heappop(pq[pqi])  # remove the target node
                        # empty the larger size priority queue to the smaller one
                        if len(pq[pqi]) > len(pq[1 - pqi]):
                            pqi = 1 - pqi
                        while len(pq[pqi]) > 0:
                            heappush(pq[1 - pqi], pq[pqi][0])
                            heappop(pq[pqi])
                        pqi = 1 - pqi
                        heappush(pq[pqi], m0)  # add the better node instead
        return ''  # if no route found

    def print_map(self):
        print 'Map:'
        for y in range(self.y_range):
            for x in range(self.x_range):
                xy = self.the_map[y][x]
                if xy == 0:
                    print '.',  # space
                elif xy == 1:
                    print 'O',  # obstacle
                elif xy == 2:
                    print 'S',  # start
                elif xy == 3:
                    print 'R',  # route
                elif xy == 4:
                    print 'F',  # finish
            print

    @staticmethod
    def get_possible_directions_of_movement(directions):
        if directions == 4:
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
        elif directions == 8:
            dx = [1, 1, 0, -1, -1, -1, 0, 1]
            dy = [0, 1, 1, 1, 0, -1, -1, -1]
        return dx, dy

    def route_as_coordinates(self):
        if self.route == None:
            raise ValueError
        coordinates = []
        x, y = self.start
        dx, dy = self.directions
        for i in range(len(self.route)):
            j = int(self.route[i])
            x += dx[j]
            y += dy[j]
            coordinates.append((x, y))
        return coordinates

    def mark_route_on_map(self):
        x, y = self.start
        self.the_map[y][x] = 2
        for (x, y) in self.route_coordinates:
            self.the_map[y][x] = 3
        self.the_map[y][x] = 4


    def create_obstacles(self):
        for x in range(x_range / 8, x_range * 7 / 8):
            self.the_map[y_range / 2][x] = 1
        for y in range(y_range / 8, y_range * 7 / 8):
            self.the_map[y][x_range / 2] = 1

    @staticmethod
    def create_empty_map(m, n):
        the_map = []
        row = [0] * n
        for i in range(m):  # create empty map
            the_map.append(list(row))
        return the_map

    @staticmethod
    def map_from_binary_image(binary_image):
        inverted_image = np.logical_not(binary_image)
        the_new_map = inverted_image + np.zeros(inverted_image.shape)
        return the_new_map


if __name__ == "__main__":
    y_range = 30
    x_range = 30
    the_map = Pathfinder.create_empty_map(y_range, x_range)
    number_of_possible_directions = 8
    start, finish = (0, 0), (29, 29)
    pathfinder = Pathfinder(the_map, number_of_possible_directions, start, finish)
    pathfinder.create_obstacles()
    pathfinder.run()
    pathfinder.mark_route_on_map()
    pathfinder.print_map()
