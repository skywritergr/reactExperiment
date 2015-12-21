import json
import os
import time
from urllib.request import Request, urlopen, URLError
from flask import Flask, Response, request
from requests_oauthlib import OAuth1Session

app = Flask(__name__, static_url_path='', static_folder='public')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

@app.route('/api/comments', methods=['GET', 'POST'])
def comments_handler():

    with open('comments.json', 'r') as file:
        comments = json.loads(file.read())

    if request.method == 'POST':
        newComment = request.form.to_dict()
        newComment['id'] = int(time.time() * 1000)
        comments.append(newComment)

        with open('comments.json', 'w') as file:
            file.write(json.dumps(comments, indent=4, separators=(',', ': ')))

    return Response(json.dumps(comments), mimetype='application/json', headers={'Cache-Control': 'no-cache'})
    
@app.route('/api/getTweets', methods=['GET'])
def get_tweets():        
    try:
        # Load keys from external file. Not checked in.
        with open('twitterKeys.json', 'r') as file:
            keys = json.loads(file.read())
        
        twitter = OAuth1Session(keys['client'],
                    client_secret=keys['client_secret'],
                    resource_owner_key=keys['resource_owner_key'],
                    resource_owner_secret=keys['resource_owner_secret'])
        url = 'https://api.twitter.com/1.1/statuses/retweets_of_me.json'
        res = twitter.get(url).json()

        return Response(json.dumps(res), mimetype='application/json', headers={'Cache-Control': 'no-cache'})
    except URLError as e:
       return Response(e)

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT",3000)))
