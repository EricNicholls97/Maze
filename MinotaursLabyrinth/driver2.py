from matrix import Matrix
from maze import Maze
from painter import Painter

import datetime
import time


def score_maze(weights, scores):
    total_score = 0
    if len(weights) != len(scores):
        raise Exception("Arrays are different length")
    for i in range(len(weights)):
        w = weights[i]
        s = scores[i]
        total_score += w*s

    return total_score



# perc_progress = 50%
# sex elapsed = 30
# sex_left = 30

# perc_progress = 25% = 1/4
# sex elapsed = 50
# sex_left = 150

# perc_progress = 75% = 3/4
# sex elapsed = 100
# sex_left = 270


def get_eta(sex_elapsed, progress):
    if progress==0:
        return "undefined"

    now = datetime.datetime.now()
    sex_left = sex_elapsed * (1/progress - 1)

    eta = now + datetime.timedelta(seconds=sex_left)

    return eta.strftime("%H:%M (%m-%d)")

def main():

    # Part 1: single maze

    # m = Maze(18, 18)


    # print('building maze')
    # m.build_maze(1.0)
    # p.draw_foundation()
    # p.draw_maze_lines(m.get_vert_walls(), m.get_horz_walls())
    #
    # print('writing metrics')
    #
    # metric_1 = m.get_k_metric(6)
    # metric_1_value = metric_1[0]
    # metric_1_score = metric_1[1]
    #
    # p.write_metric("all basic loops", metric_1_value, metric_1_score)
    #
    # # metric 2: wall sparsity
    # metric_2 = m.get_wall_sparsity_metric()
    # metric_2_value = metric_2[0]
    # metric_2_score = metric_2[1]
    # p.write_metric("Wall Sparsity", metric_2_value, metric_2_score)
    #
    # # metric 3: all shortest loops
    # metric_3 = m.get_all_shortest_loops_metric()
    # metric_3_value = metric_3[0]
    # metric_3_score = metric_3[1]
    # p.write_metric("All shortest loops", metric_3_value, metric_3_score)
    #
    # print('printing outputs')
    # # output 1: num horiz walls
    # print("\tnum horiz walls: ", m.num_horz_walls())
    # print("\tnum verti walls: ", m.num_vert_walls())

    # PART 2: optimizing single metric

    print("Part II")

    n = int(6.5 * 60 * 15)

    best_maze = None
    best_score = -1

    t1 = time.time()

    # optimize for one metric
    for i in range(n):
        m = Maze(30, 30)
        m.build_maze(1.0)

        elapsed_sex = int(time.time() - t1)
        progress = i/n
        eta = get_eta(elapsed_sex, progress)
        print("i={}, {}%, t= {}min,   eta= {}".format(i, round(100*progress, 2), elapsed_sex//60, eta))

        score_3 = m.get_all_shortest_loops_metric()[1]
        if score_3 > best_score:
            best_score = score_3
            best_maze = m

    p = Painter(1800, 1100, 800)
    p.draw_foundation()
    p.draw_maze_lines(best_maze.get_vert_walls(), best_maze.get_horz_walls())

    time.sleep(1000000)




main()