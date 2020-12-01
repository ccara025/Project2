from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SelectField, RadioField
import requests
from project2_Flask import main_functions
from nltk import sent_tokenize



class NewsForm(FlaskForm):
    full_name = StringField("Full name")
    source = RadioField("Source", choices=[ ('nyt','NYT - New York Times'),
                                            ('inyt','INYT - International New York Times'),
                                            ('all','All - Both NYT and INYT')
                                            ])
    section = SelectField("Section",
                          choices = [('sports','Sports'),
                                     ('arts','Arts'),
                                     ('automobiles','Automobiles'),
                                     ('books','Books'),
                                     ('u.s.','United States'),
                                     ('business','Business'),
                                     ('climate','Climate'),
                                     ('style','Style'),
                                     ('education','Education'),
                                     ('fashion','Fashion'),
                                     ('food','Food'),
                                     ('movies','Movies')])

def generateDataFromAPI(source,section):

    api_key_dict = main_functions.read_from_file("project2_Flask/JSON_Files/api_key.json")
    api_key = api_key_dict["my_key"]
    url = "https://api.nytimes.com/svc/news/v3/content/"

    final_url = url + source + "/" + section + ".json?api-key=" + api_key

# https://api.nytimes.com/svc/news/v3/content/{source}/{section}.json


    response = requests.get(final_url).json()
    main_functions.save_to_file(response, "project2_Flask/JSON_Files/response.json")

    # """From the response dictionary, filter the data"""
    # # import json
    # # response = json.loads(response)
    my_response = main_functions.read_from_file("project2_Flask/JSON_Files/response.json")
    str1 = ""
    sentences = [""]
    for i in my_response["results"]:
        str1 = i["title"]
        sentences += sent_tokenize(str1)
        sentences +=  " "
        str1 = " "



    return sentences
