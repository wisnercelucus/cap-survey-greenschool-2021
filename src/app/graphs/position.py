from utils.functions import count_freq_simple_answer
import plotly.graph_objects as go
from .config import config
from dash import dcc
import plotly.express as px

def get_position_graphs(df):
    s = count_freq_simple_answer(df, 'Position')
    s_fig =  go.Bar(x=s["response"], y=s['frequency'], name="Role")
    #p_fig = dcc.Graph(figure=s_fig,  className="desc-graph-u", config=config)
    return s_fig


def get_position_graphs_c(df):
    s = count_freq_simple_answer(df, 'Position').rename(columns={"response": "Category", "frequency": "Total"})
    p_fig =  px.bar(s, x="Category", y='Total',  text_auto='.s', title='Respondent categories')
    p_fig = dcc.Graph(figure=p_fig,  className="desc-graph-u", config=config)
    return p_fig
