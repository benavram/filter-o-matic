#!flask/bin/python
"""filter-o-matic flas app
    Copyright (c) 2016 office(ish).com

    https://github.com/benavram/filter-o-matic

    This file is part of filter-o-matic.

    filter-o-matic is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Foobar is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with [app name].  If not, see <http://www.gnu.org/licenses/> or
    <https://github.com/benavram/filter-o-matic/blob/master/LICENSE>

  # Configuration variables

API docs at https://github.com/benavram/filter-o-matic
# Authors:

"""
from flask import Flask, jsonify, request, json, render_template

import filteromatic.main
from filteromatic.settings import app_name, licensed, docs, copy_r, lic_loc
from filteromatic.main import Filter_o_matic
from filteromatic.utils import word_lists, word_check
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

    return_feed = jsonify(word_feed)
        
    return return_feed

@app.route('/evaluate/')
def apply_filter():
    """evaluate and return edited sring
       request objects:
           eval_string: string to be evaluated, mandatory
           replacement_type:  type of replacement to insert (default = None)
    """    
    r = None
    if 'eval_string' not in request.args:
        return jsonify({'exception':'invalid request'})
    elif request.args['eval_string'] == '':
        return jsonify({'exception':'invalid request'})
    else:
        eval_string  = request.args['eval_string']
    
    if len(eval_string) > 1024:
        return json.dumps({'exception':'invalid request: string too long'})
    
    if 'replacement_type' in request.args:
        r = request.args['replacement_type']
        
    cleaned_string = Filter_o_matic(eval_string).cleanit(r)
    return_string = {'clean_string':cleaned_string}
    return jsonify(return_string)


@app.route('/check_word/')
def check_word():
    """check word against profanity list and return true in json
    object if exists word: string
    """
    if 's_word' not in request.args:
        return jsonify({'exception':'invalid request'})
    else:
        s = request.args['s_word']
        if word_check(s):
            return jsonify(result='true')
        else:
            # return jsonify({'profanity':'false'})
            return jsonify(result='false')


@app.route('/')
def hello_world():
    return render_template('test.html', items="filter-o-matic")
    # return "\25AE"
    # return jsonify({'exception':'invalid request'})


if __name__ == '__main__':
    #app.run(host='192.168.1.3', debug=True)
    app.run(debug=True)    
    
