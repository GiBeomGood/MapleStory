import numpy as np
import pandas as pd

def generate_prob_chart(starcatch=True, event_15=False, dest_prevention=False) -> np.ndarray:
    prob_chart = np.zeros((25, 4))
    prob_chart[:, 0] = [
        0.95, 0.9, 0.85, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55,
        0.5, 0.45, 0.4, 0.35, 0.3,
        0.3, 0.3, 0.3, 0.3, 0.3,
        0.3, 0.3, 0.03, 0.02, 0.01
    ]

    # modification of success probability
    if starcatch is True:
        prob_chart[:, 0] *= 1.05
    if event_15 is True:
        prob_chart[[5, 10, 15], 0] = 1
    
    # modification of destruction probability
    prob_chart[:, -1] = (1-prob_chart[:, 0]) * np.array([
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0.03, 0.03, 0.03, 0.04, 0.04,
        0.1, 0.1, 0.2, 0.3, 0.4
    ])
    if dest_prevention is True:
        prob_chart[[15, 16], -1] = 0
    fail_or_remain = 1 - prob_chart[:, 0] - prob_chart[:, -1]
    prob_chart[:16, 1] = fail_or_remain[:16]  # 0->1 ~ 15->16
    prob_chart[16:20, 2] = fail_or_remain[16:20]  # 16->17 ~ 19->20
    prob_chart[20, 1] = fail_or_remain[20]  # 20->21
    prob_chart[21:, 2] = fail_or_remain[21:]  # 21->22 ~ 24->25

    return prob_chart

def generate_dest_prob_chart(starcatch=True, event_15=False, dest_prevention=False, pretty=False):
    prob = generate_prob_chart(starcatch, event_15, dest_prevention)
    dest_chart = pd.DataFrame(
        np.zeros((10, 10)),
        columns=range(15, 25),
        index=range(16, 26)
    )  # 15->16 ~ 24->25
    dest_chart = np.zeros((10, 10))  # 15->16 ~ 24->25
    dest_chart[-1, -1] = 1

    for end in range(10):
        start = end+15
        dest_chart[end, end] = prob[start, 0] / (
            1 - prob[start, 1] - prob[start, 2] * (
                    prob[start-1, 0] + prob[start-1, 1:3].sum()*dest_chart[end-1, end-1]
                )
        )

        for start in range(end):
            dest_chart[end, start] = dest_chart.diagonal()[start:end+1].prod()

    dest_chart = pd.DataFrame(
        dest_chart,
        columns=range(15, 25),
        index=range(16, 26),
    )

    if pretty is True:
        dest_chart = dest_chart.applymap(lambda x: '' if x==0 else f'{x:6.2%}')

    return dest_chart