from matrix import Matrix
from maze import Maze
from painter import Painter

from game import Game
import maze_factory

import datetime
import time


# TODO: is player its own class or part of game

def main():

    width, height = 30, 30

    m = maze_factory.create_maze(1, width, height)

    print("\n-- maze created --\n")

    g = Game(m)
    g.create_game()


    # Painter
    p = Painter(1800, 1100, 800)
    p.draw_foundation()
    p.draw_maze_lines(m.get_vert_walls(), m.get_horz_walls())

    # draw game
    game_obj_list = g.get_paintable_list()
    player_loc = g.get_player_loc()
    p.draw_game(player_loc, game_obj_list, width, height)

    # pass

    time.sleep(1000000)


main()

