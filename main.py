import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc


data = pd.read_csv("fastfood.csv")
avg_calories = data.groupby('restaurant')['calories'].mean().reset_index()
fig_avg_calories = px.bar(avg_calories, x="restaurant", y="calories", color="restaurant", title="Average Calories by Restaurant")

fig_avg_calories.update_layout(
    plot_bgcolor="#f9f9f9",
    paper_bgcolor="#f9f9f9"
)

avg_sugar = data.groupby('restaurant')['sugar'].mean().reset_index()
fig_avg_sugar = px.bar(avg_sugar, x="restaurant", y="sugar",color="restaurant", title="Average Sugar (g) by Restaurant")

avg_fat = data.groupby('restaurant')['total_fat'].mean().reset_index()
fig_avg_fat =  px.pie(avg_fat, names="restaurant", values ="total_fat", title="Average Total Fat Distribution by Restaurant")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# app.layout = html.Div(children=[
#     html.H1(children="Hello"),
#     dcc.Graph(
#         figure=fig_avg_calories,
#     )
# ])
app.layout = dbc.Container([
    dbc.Navbar(
        dbc.Container(
            [
                dbc.NavbarBrand("Fastfood Dashboard", className="mx-auto",style={"font-size":"27px","color":"orange"})
            ]
        ),
        color="black",
        dark=True,
    ),
    dbc.Row(
        [
            dbc.Col(
                dcc.Graph(
                    figure=fig_avg_calories
                ),
                width = 6
            ),
            dbc.Col(
                dcc.Graph(
                    figure=fig_avg_sugar
                ),
                width = 6
            ),
            dbc.Col(
                dcc.Graph(
                    figure=fig_avg_fat
                ),
                width = 6
            )
        ]
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)