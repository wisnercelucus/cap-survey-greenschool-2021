from plotly.subplots import make_subplots
from .sex import get_sex_graphs, get_sex_graphs_c
from .position import get_position_graphs, get_position_graphs_c
from .config import config
from dash import dcc

def get_desc_fig(df):
    fig = make_subplots(
        rows=1, cols=2,
        shared_xaxes=False,vertical_spacing=0.009,horizontal_spacing=0.5,
        subplot_titles=('Gender',  'Role'),
        specs=[[{"type": "pie"}, {"type": "bar"}],
            ],
    )

    fig.append_trace(get_sex_graphs(df),
                row=1, col=1)

    fig.append_trace(get_position_graphs(df),
                row=1, col=2)

    g = dcc.Graph(figure=fig,  className="desc-graph-u", config=config)
    return g


def get_desc_fig_c(df):
    return [get_sex_graphs_c(df), get_position_graphs_c(df)]
