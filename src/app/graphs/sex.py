from re import template
from utils.functions import count_freq_simple_answer
import plotly.graph_objects as go
from dash import dcc
from .config import config
import plotly.express as px


def get_sex_graphs(df):
    s = count_freq_simple_answer(df, 'Sex')
    s_fig =  go.Pie(values=s['frequency'], labels=s['response'])
    #sex_fig = dcc.Graph(figure=s_fig, config=config, className="desc-graph-u")
    return s_fig


def get_sex_graphs_c(df):
    s = count_freq_simple_answer(df, 'Sex')
    s_fig =  px.pie(s, values='frequency', names='response', title='Respondent genders',
    hole=.3, 
    color='response',
             color_discrete_map={'Male':'royalblue',
                                 'Female':'darkblue'})
    sex_fig = dcc.Graph(figure=s_fig, 
    config=config,
    className="desc-graph-u")
    return sex_fig