from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.express as px

df = px.data.gapminder()

templates = [
    "bootstrap",
    "minty",
    "pulse",
    "flatly",
    "quartz",
    "cyborg",
    "darkly",
    "vapor",
]

load_figure_template(templates)

figures = [
    px.scatter(
        df.query("year==2007"),
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        log_x=True,
        size_max=60,
        template=template,
        title="Gapminder 2007: '%s' theme" % template,
    )
    for template in templates
]

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

graphs = [dcc.Graph(figure=fig, className="m-4") for fig in figures]
core_activities = ['Improve access to water.', 
'Rehabilitation/construction of sanitary facilities.',
'Hygiene Promotion in schools. Using the hygiene-friendly schools’ approach.',
]


logos = ['assets/lwf_logo.png', 'assets/dkh_logo.png', 'assets/nca_logo.png',]


document_title = html.Div(
    [
        html.Div(
            [html.Img(src=image_path, className="logo") for image_path in logos],
            className="logo-container"
        ),
        html.Div(
            html.Div(
            [
                html.H1(
                "CAP SURVEY REPORT",
                className="document-title"
            ),
                html.P("Reported on: October 2022", className="text-center report-date"),
            ]
        )
        ),
    ],

    className="document-title-wrapper"
)

header = html.Div([
    html.Div(
        [
            html.H2(
            "Project",
            className='title'
            ),

            html.P(
            'Sustainable access to safe drinking water, sanitation, and hygiene for schools in southern Haiti',
            className="p-title"
            ),

            html.Div(
                html.Span("Project timeline: 2020-2021"),
                 className="report-year"
            )
        ],
        
    )
],
className="project-title mb-4"
)

report_narrative = html.Div(
    [
        #dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
        dbc.CardBody(
            [
                html.H4("Background", className="card-title"),
                html.P(
                    "To help to reduce the incidence of water-borne diseases in Haiti, Non-Governmental Organizations (NGO) and, International Organization and Agencies for development are working alongside government actors to strengthen the enabling environment for sustainable WASH services. These efforts had helped to control the epidemic of cholera that killed a lot of people after the earthquake of 2010. The Joint Office LWF/NCA has been involved in these efforts for years through their long-term partnership. Thus, through the green school project, the Joint Office helped schools to have access to sustainable and safe drinking water, sanitation, and hygiene in southern Haiti. The project has succeeded over the years in developing and delivering training and hygiene friendly and inclusive sanitary infrastructures that are expected to result in lasting skills and knowledge uptake, behavior change and wellbeing in schools for the students and school staff.",
                    className="card-text",
                ),
                html.P(
                    "The project approach is based on hygiene friendly school. This approach aims to prevent and reduce diseases related to water and sanitation, and to improve the academic performance of students by increasing school attendance, the development of children's 'life skills' over the long term in hygiene practices and promoting gender equality. It is an approach based on the child to child adapted to the Haitian context and his mandatory by the Ministry of Education.  The Green school package during 2021 was implemented at The Public School of Saut Mathurine and Public School of Mersan, Camp Perrin, Haiti, focusing on three (3) core activities:",
                    className="card-text",
                ),

                html.Ul(
                    id='activities', children=[html.Li(i) for i in core_activities]
                ),

                html.P(
                    "The public Schools of Saut Mathurine and Mersan are primary and secondary schools and provide learnings to boys and girls from 6 to 20 years old in their respective communities.",
                    className="card-text",
                ),
                
                html.P(
                    "The project was executed by a collaboration between LWF/NCA and one of his long-term local partners in the South, AHAAMES who has gained expertise implementing WASH projects particularly from the 3 years WASH project in the big south with NFMA financing.",
                    className="card-text",
                ),

                html.P(
                    "The target population for this project is girls’ and boys’ schoolchildren of the 2 selected schools (aged 6 to 14 years old), teachers and school principals of the schools. The project will also impact the families of the students, as well as the communities surrounding the targeted schools.",
                    className="card-text",
                ),

                

            ]
        ),
    ],
    style={"width": "100%"},
)


app.layout = dbc.Container(
    [
        document_title,
        header,
        report_narrative,
        *graphs
    ]
    ,
    className="p-5 wrapper"
    )

if __name__ == "__main__":
    app.run_server(debug=True)