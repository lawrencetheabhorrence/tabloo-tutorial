import tabloo
import pandas as pd
import sys

filename = sys.argv[1]

with open(filename) as f:
    i=0
    while True:
        if ('Attendee Details,' in f.readline()):
            i = i + 1
            break
        i = i + 1

    df = pd.read_csv(f, index_col=False, skiprows=i)
    tabloo.show(df)
