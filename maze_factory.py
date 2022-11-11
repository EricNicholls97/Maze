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
    best_vales = -1

    for i in range(n):
        m = Maze(rows, cols)

        m.build_maze(1.0)

        metric_1 = m.get_k_metric(6)
        metric_2 = m.get_wall_sparsity_metric()
        metric_3 = m.get_all_shortest_loops_metric()

        metric_values = [metric_1[1], metric_2[1], metric_3[1]]
        weights = [0.18, .12, 0.7]

        score = score_maze(metric_values, weights)
        print(f"Score: {score}   | {metric_values}")

        if score > best_score:
            best_score = score
            best_m = m
            best_values = metric_values

        # TIME KEEPING (deletable)
        elapsed_sex = int(time.time() - t1)
        progress = (i+1)/n
        eta = get_eta(elapsed_sex, progress)
        print(f"maze # {i+1}  ({100.0*i/n}) \t|  {round(100*progress, 2)}% \t|  t= {elapsed_sex//60} m \t|  eta= {eta}")
        print(f"[{'#'*i + '|'*(n-i)}]")
        print()

    print(f"Best Score:\t{best_score}\t{best_values}\n")

    return best_m

# O(n)*
# TODO: spacing of output