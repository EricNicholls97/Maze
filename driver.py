
from game import Game


# either the game can paint
# or the driver has to have a loop

def main():

    g = Game()
    g.new_game()

    # width, height = 7, 7
    #
    # print("\nstarting...")
    # print("\n--------------------\n")
    #
    # for i in range(1, 11):
    #     print("creating maze", i)
    #     m = maze_factory.create_maze(1, width, height)
    #
    #     g = Game(m)
    #     g.create_game()
    #
    #     # Painter
    #     p = Painter(1800, 1100, 800)
    #     p.draw_foundation()
    #     p.draw_maze_lines(m.get_vert_walls(), m.get_horz_walls())
    #
    #     # draw game
    #     game_obj_list = g.get_paintable_list()
    #     if len(game_obj_list) != 8:
    #         print("MAYDAY")
    #     player_loc = g.get_player_loc()
    #     p.draw_game(player_loc, game_obj_list, width, height)
    #
    #     print("\n--------------------\n")
    #     time.sleep(6)

    # end


main()

