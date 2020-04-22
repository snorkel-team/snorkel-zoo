from typing import Dict
from snorkel.labeling import LabelingFunction

ABSTAIN = -1

# Construct a worker_dict that contains lookup table for for each WorkerId
WorkerId = str
WorkerLabelDict = Dict[int, int]
worker_dicts: Dict[WorkerId, WorkerLabelDict] = {}


def make_worker_lf(worker_id, x_id_field: str = "tweet_id") -> LabelingFunction:
    def worker_lf(x, worker_dict):
        return worker_dict.get(x[x_id_field], ABSTAIN)


    worker_dict = worker_dicts[worker_id]
    name = f"worker_{worker_id}"
    return LabelingFunction(name, f=worker_lf, resources={"worker_dict": worker_dict})


worker_lfs = [make_worker_lf(worker_id) for worker_id in worker_dicts]