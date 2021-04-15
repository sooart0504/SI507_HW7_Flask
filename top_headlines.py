#########################################
##### Name: Soo Ji Choi             #####
##### Uniqname: soojc               #####
#########################################

from flask import Flask, render_template
app = Flask(__name__)

import requests
import json
import secrets # secrets.API_KEY

def retrieve_top_news():
    """Requests an API search of Top news in Technology section of NYTimes API,
    and returns a JSON-friendly list of dictionaries.

    Parameters:
        none

    Returns:
        list of dictionaries: list of dictionary representations of the decoded JSON document
    """
    # TOP 5 news from Technology section of NYTimes API
    BASE_URL = "https://api.nytimes.com/svc/topstories/v2/technology.json"
    API_KEY = f"?api-key={secrets.API_KEY}"

    request_url = BASE_URL + API_KEY

    retrieved_json = requests.get(request_url).json()

    return retrieved_json



@app.route('/')
def index():
    return '<h1>Welcome!</h1>'


@app.route('/name/<nm>')
def name(nm):
    #nm = "Buffy"
    return render_template('name.html',
        name=nm)

@app.route('/headlines/<nm>')
def headlines(nm):
    top_news_dict = retrieve_top_news()
    top_news_results = top_news_dict['results']
    top_5 = []

    for each_result in top_news_results[:5]:
        top_5.append(each_result['title'])

    return render_template('headlines.html', name=nm, news=top_5)





if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)