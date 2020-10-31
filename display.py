import matplotlib.pyplot as plt
import sys
import json

import plotly.express as px
import pandas as pd
import numpy as np


def _prepare(data):
    data = data.active_cases_info
    data = map(lambda x: (x.date, x.amount_new), data)
    x, y = zip(*data)
    return x,y

def plot_plotly(data, args):
    x, y = _prepare(data)
    df = pd.DataFrame(np.array((x, y)).T, columns=['Datum', 'Nakazeni za den'])
    fig = px.line(data, x=x, y=y, title='Progress of COVID-19 in Czechia')
    fig.show()

def plot_matplotlib(data, args):
    title = data.source
    x, y = _prepare(data)

    fig, axs = plt.subplots(tight_layout=True)
    fig.autofmt_xdate()
    axs.set_title(title)
    axs.plot(x, y)
    plt.show()

def display(data, args):
    if args.plotly:
        plot_plotly(data, args)
    else:
        plot_matplotlib(data, args)
