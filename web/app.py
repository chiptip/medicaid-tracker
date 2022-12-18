from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})

from flask import Flask, request, render_template
from web import api

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/oauth-page")
def oauth_page():
    return "<p>Oauth page</p>"


@app.route("/create_link_token", methods=['GET', 'POST'])
def create_link_token():

    client = api.get_client()
    link_token = api.create_link_token(api_client=client)

    return {
        "link_token": link_token
    }


@app.route("/exchange_public_token", methods=['POST'])
def exchange_public_token():
    client = api.get_client()
    public_token = request.form.get('public_token')
    api.exchange_public_token(api_client=client,
                              public_token=public_token)

    return "<p>access token obtained</p>"
