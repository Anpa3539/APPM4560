import numpy as np
import plotly.graph_objects as go
import math

def poisson(l,k): 
    return np.exp(-l)*l**k/(math.factorial(k))


def plot_2d(y:list,x:list = None, xlabel:str = None, ylabel:str = None,title:str = None,line_name:list[str] = None)-> None:
    """ 
    Do a simple 2D line chart (list of lines or other)
    """
    fig = go.Figure()
    

    if type(y[0]) == list or type(y[0]) == np.ndarray:
        for i in range(len(y)):
            if x is not None:
                fig.add_trace(go.Scatter(
                    x=x[i],
                    y=y[i],
                    mode='lines',
                    name=line_name[i]
                ))
            else:
                fig.add_trace(go.Scatter(
                    y=y[i],
                    mode='lines',
                    name=line_name[i]
                ))
    else:
        if x is not None:
            fig.add_trace(go.Scatter(
                x=x,
                y=y,
                mode='lines',
                name=line_name
            ))
        else:
            fig.add_trace(go.Scatter(
                y=y,
                mode='lines',
                name=line_name
            ))

    if title:
        fig.update_layout(
        title=title)
    if xlabel:
        fig.update_layout(
            xaxis_title = xlabel
        )
    if ylabel:
        fig.update_layout(
            yaxis_title = ylabel
        )

    # 4. Display the figure
    fig.show()

def plot_event_timeline(t_red,t_blue,xmin=None,xmax=None,title="Event Timeline",xlabel="Time",red_label="Team A",blue_label="Team B",tick_height=0.4,):
    """
    Plot a single horizontal timeline with red and blue event ticks.

    Args:
        t_red : array-like
            Times of red events
        t_blue : array-like
            Times of blue events
        xmin, xmax : float, optional
            Axis limits (auto if None)
        title : str
        xlabel : str
        red_label : str
        blue_label : str
        tick_height : float
            Vertical size of ticks
    """

    fig = go.Figure()

    # Baseline
    if xmin is None:
        xmin = min(min(t_red, default=0), min(t_blue, default=0))
    if xmax is None:
        xmax = max(max(t_red, default=1), max(t_blue, default=1))

    fig.add_trace(go.Scatter(
        x=[xmin, xmax],
        y=[0, 0],
        mode='lines',
        line=dict(width=2,color='black'),
        showlegend=False
    ))

    # Red ticks
    fig.add_trace(go.Scatter(
        x=t_red,
        y=[0]*len(t_red),
        mode='markers',
        marker=dict(
            symbol='line-ns',  # vertical tick
            size=20,
            color='red',
            line=dict(width=2,color='red')
        ),
        name=red_label
    ))

    # Blue ticks
    fig.add_trace(go.Scatter(
        x=t_blue,
        y=[0]*len(t_blue),
        mode='markers',
        marker=dict(
            symbol='line-ns',
            size=20,
            color='blue',
            line=dict(width=2,color='blue')
        ),
        name=blue_label
    ))

    # Layout tweaks
    fig.update_layout(
        title=title,
        xaxis_title=xlabel,
        yaxis=dict(
            visible=False,
            range=[-1, 1]  # gives space for ticks
        ),
        margin=dict(l=20, r=20, t=50, b=40),
        height=200
    )

    fig.update_xaxes(showgrid=True)

    fig.show()

