import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_table = pd.read_fwf('data/data.txt')

print(data_table.head())