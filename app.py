#!flask/bin/python
from flask import Flask, jsonify, request, json

import filteromatic.main
from filteromatic.settings import app_name, licensed, docs, copy_r, lic_loc
from filteromatic.main import Filter_o_matic
from werkzeug.contrib.atom import AtomFeed
from filteromatic.utils import word_lists
from datetime import datetime
app = Flask(__name__)


    
@app.route('/word_lists/')
def serialize_lists():
    feed_content = []
    all_words = []
    ltypes = ('all', 'silly', 'profanity')
    if 'feed' not in request.args:
        list_type = 'all'
    elif request.args['feed'] not in ltypes:
        list_type = 'all'
    else:
        list_type = request.args['feed']
    if list_type != 'all':
        for item in word_lists(list_type):
            word_cat = item[0]
            word = item[1]
            rating = item[2]
            list_category = item[3]
            
            item_list = {'word':word,
                       'word_type':word_cat,
                       'rating':rating
                       }
            feed_content.append(item_list)
            
        content = {list_category:{'the words':feed_content}
            }
    else:
        lists = ('silly', 'profanity')
        for l in lists:
            for item in word_lists(l):
                word_cat = item[0]
                word = item[1]
                rating = item[2]
                list_category = item[3]
                
                item_list = {'word':word,
                           'word_type':word_cat,
                           'rating':rating
                           }
                feed_content.append(item_list)
                
            content = {list_category:{'the words':feed_content}
                }
            all_words.append(content)
        
    content_list = all_words if list_type == 'all' else content
    
    word_feed = {'filter-o-matic':'',
                 'request':list_type,
                 'link':request.url,
                 'content_type':'json',
                 'attribution':'officeish.com',
                 'app':app_name,
                 'copyright':copy_r,
                 'licensed':licensed,
                 'license':lic_loc,
                 'docs':docs,
                 'updated':datetime.now(),
                 'content':content_list
                    }

    return_feed = json.dumps(word_feed)
        
    return return_feed

@app.route('/evaluate/')
def apply_filter():
    if 'eval_string' not in request.args:
        return 'invalid request'

    elif request.args['eval_string'] == '':
        return 'invalid request'
    else:
        eval_string  = request.args['eval_string']
    
    if len(eval_string) > 1024:
        return 'invalid request: string too long'
    
    cleaned_string = Filter_o_matic(eval_string).cleanit()
    
    return cleaned_string

@app.route('/')
def hello_world():
    # return "home"
    raise InvalidUsage('This view is gone', status_code=410)

@app.errorhandler(404)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

if __name__ == '__main__':
    app.run(debug=True)
    
class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv