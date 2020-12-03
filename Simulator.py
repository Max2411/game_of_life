from World import *

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world = None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if world == None:
            self.world = World(20)
        else:
            self.world = world

    def non_zero(self, lst):
        lst1 = list(filter(lambda x: x != 0, lst))
        num = len(lst1)
        return num

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        self.generation += 1
        for x in range(self.world.width):

            for y in range(self.world.height):

                neighbors = self.non_zero(self.world.get_neighbours(x,y))
                # rule1
                if neighbors < 2:
                    self.world.set(x,y,0)
                # rule 2
                elif neighbors > 3:
                    self.world.set(x, y, 0)
                # rule 3
                else:
                    pass



        #TODO: Do something to evolve the generation

        return self.world

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world