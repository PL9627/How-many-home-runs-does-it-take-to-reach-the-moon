"""attempting to find who is the best pitcher and batter combo needed to reach 
the moon in the fewest amount of home runs"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pybaseball as pyb
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

hr_lead_df = pd.read_csv("C:/Users/Paul/how-many-hr-to-moon/csv/stats.csv")
hr_dist_df = pd.read_csv(
    "C:/Users/Paul/how-many-hr-to-moon/csv/exit_velocity.csv")
