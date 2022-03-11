from maze import Maze

import datetime
import time


def get_eta(sex_elapsed, progress):
    if progress==0:
        return "undefined"

    now = datetime.datetime.now()
    sex_left = sex_elapsed * (1/progress - 1)

    eta = now + datetime.timedelta(seconds=sex_left)

    return eta.strftime("%H:%M (%m-%d)")


def score_maze(weights, scores):
    total_score = 0
    if len(weights) != len(scores):
        raise Exception("Arrays are different length")
    for i in range(len(weights)):
        w = weights[i]
        s = scores[i]
        total_score += w*s

    return total_score



# create a maze using a list of Metric objects and corresponding weights.
# num of trials = n
def create_maze(n, rows, cols):
    t1 = time.time()

    best_score = -1
    best_m = None

    for i in range(n):
        m = Maze(rows, cols)

        m.build_maze(1.0)

        metric_1 = m.get_k_metric(6)
        metric_2 = m.get_wall_sparsity_metric()
        metric_3 = m.get_all_shortest_loops_metric()

        metric_values = [metric_1[1], metric_2[1], metric_3[1]]
        weights = [0.15, .05, 0.8]

        score = score_maze(metric_values, weights)

        if score > best_score:
            best_score = score
            best_m = m

        # TIME KEEPING (deletable)
        elapsed_sex = int(time.time() - t1)
        progress = (i+1)/n
        eta = get_eta(elapsed_sex, progress)
        print("maze # {}  (n={}) \t|  {}% \t|  t= {} m \t|  eta= {}".format(i+1, n, round(100*progress, 2), elapsed_sex//60, eta))

    return best_m