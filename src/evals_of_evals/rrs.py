"""
Generates a representative random sample ("rrs") of an eval.
The input format is a path to an eval file, or anything supported as input to 
inspect_ai.analysis.samples_df.
The output format is a pandas DataFrame that is returned, without printing.
"""

import inspect_ai
from inspect_ai.analysis import samples_df
import numpy as np
import pandas as pd

def rrs(logs, #must be type compatible with the input to samples_df! Exact types hard to import
        seed: int = 42,
        n_elems: int = 10) -> pd.DataFrame:
    samples_dataframe = samples_df(logs = logs)
    rng = np.random.default_rng(seed=seed)
    permuted_dataframe = pd.DataFrame(
        rng.choice(
            samples_dataframe,
            size = n_elems,
            replace=False,
            )
        )
    return permuted_dataframe
