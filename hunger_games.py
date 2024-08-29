import maze_factory as MF
from maze import Maze
from player import Player

def main():
    g = HungerGames()
    g.create_mazes()
    g.create_game()


class HungerGames:

    def __init__(self) -> None:
        self.rows = 30
        self.cols = 30

        self.num_mazes = 1


    def create_mazes(self):
        # creates maze from factory, items, starts looping each player
        print(f"\ncreating mazes ({self.num_mazes})\n")

        self.current_maze = MF.create_maze(self.num_mazes, self.rows, self.cols)
        
    def create_game(self):
        self.setup_player()

        self.setup_AI()

    def setup_player(self):
        # TODO: uncomment
        # p = Player(self.current_maze, self.rows, self.cols)
        # p.game_loop()
        pass    

    def setup_environment(self):
        pass


    def set_environmental_varibles():
        # environmental logic should be done here. 
        # how to interface with maze
        #   - sets locations for "hazards"
            #   - when a hazard is hit (in game class), ask gamemode class what the effect is
        pass
        # figure out how variables like frequency



if __name__ == '__main__':
    main()

