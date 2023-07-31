import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

# Inicializar a aplicação Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Dados fixos para o gráfico de barras
x_data = ['Categoria A', 'Categoria B', 'Categoria C', 'Categoria D', 'Categoria E']
y_data = [40, 25, 30, 15, 50]

# Criar o gráfico de barras
fig = go.Figure(data=[go.Bar(x=x_data, y=y_data, marker_color='rgb(26, 118, 255)')])
fig.update_layout(title="Gráfico de Barras Fixo", xaxis_title="Categoria", yaxis_title="Valores")

# Layout do container do dashboard
dashboard_layout = dbc.Container([
    html.H1("Dashboard"),
    dcc.Graph(figure=fig)
], className="mt-4")

# Layout da aplicação Dash
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Formulário de login
login_form = dbc.Container([
    html.H1("Página de Login"),
    dbc.Input(id="input-username", type="text", placeholder="Nome de usuário"),
    dbc.Input(id="input-password", type="password", placeholder="Senha"),
    dbc.Button("Login", id="login-button", n_clicks=0, color="primary", className="mt-2")
], className="mt-4")

# Callback para exibir a página do dashboard ou o formulário de login (rota padrão)
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/dashboard':
        return dashboard_layout
    else:
        return login_form

if __name__ == '__main__':
    app.run_server(debug=True)
