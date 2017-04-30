# Write a Python program to simulate an ecosystem containing two types
# of creatures, bears and fish. The ecosystem consists of a river, which is
# modeled as a relatively large list. Each element of the list should be a
# Bear object, a Fish object, or None. In each time step, based on a random
# process, each animal either attempts to move into an adjacent list location
# or stay where it is. If two animals of the same type are about to collide in
# the same cell, then they stay where they are, but they create a new instance
# of that type of animal, which is placed in a random empty (i.e., previously
# None) location in the list. If a bear and a fish collide, however, then the
# fish dies (i.e., it disappears).
from random import shuffle
from random import randrange
from random import choice
from copy import copy
from time import sleep



class Animal:
    def __str__(self):
        return type(self).__name__[:1]
    def __repr__(self):
        return str(self)

class Bear(Animal):
    def fight(self, other):
        if isinstance(other, Fish):
            return self


class Fish(Animal):
    pass


class Ecosystem:
    ANIMALS = (Bear, Fish)

    class FightController:
        @staticmethod
        def fight(animal1, animal2):
            # find animal higher in hierarchy
            ANIMALS = Ecosystem.ANIMALS
            a1, a2 = ANIMALS.index(type(animal1)), ANIMALS.index(type(animal2))
            a1, a2 = min(a1, a2), max(a1, a2)
            if type(animal1) == ANIMALS[a1]:
                better = animal1
                worse = animal2
            else:
                better = animal2
                worse = animal1
            winner = better.fight(worse)
            return winner



    def __init__(self, length):
        self.river = [None] * length
        self._spawn_animals(10)

    def cycle(self):
        self._move_all_animals()

    def _spawn_animals(self, max):
        where_spawn = list(range(len(self)))
        shuffle(where_spawn)
        where_spawn = where_spawn[:max]
        for index in where_spawn:
            self.river[index] = choice(Ecosystem.ANIMALS)()

    def _move_all_animals(self):
        self.river = copy(self.river)
        forward = False
        for index1, cell in enumerate(self.river):
            if forward:
                # animal just went here
                forward = False
                continue

            if cell:
                index2 = index1 + choice([-1, 1])
                forward = True if index2 > 0 else False
                if index2 > len(self) - 1:
                    index2 = 0
                elif index2 < 0:
                    index2 = len(self) - 1
                animal1 = cell
                animal2 = self.river[index2]
                if animal2 is not None:
                    if type(animal1) == type(animal2):
                        # make new animal
                        # print('spawning', type(animal1))
                        self._spawn(type(animal1))
                        continue  # nothing more to do. Skip tour
                    else:
                        alive = Ecosystem.FightController.fight(animal1, animal2)
                        if alive is animal1:
                            # kill the loser
                            self.river[index2] = None
                            self.river[index1], self.river[index2] = None, animal1
                        else:
                            self.river[index1] = None
                else:
                    self.river[index1], self.river[index2] = None, animal1
                # Nothing to do. just move


    def _spawn(self, animal, times=1):
        where = list(range(len(self)))
        shuffle(where)
        for _ in range(times):
            for index in where:
                if self.river[index] is None:
                    self.river[index] = animal()
                    break

    def __len__(self):
        return len(self.river)

    def __str__(self):

        end = ''
        for x in self.river:
            if x is None:
                end += ' '
            else:
                end += str(x)

            end += '|'
        return end



if __name__ == '__main__':

    canada = Ecosystem(100)
    while True:
        print(canada)
        canada.cycle()
        sleep(1)
