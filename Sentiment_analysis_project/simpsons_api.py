from flask import Flask, request 
import markdown.extensions.fenced_code
import json
import pandas as pd
import tools.getdata as get
import tools.postdata as pos
import dotenv
dotenv.load_dotenv()


app = Flask(__name__)

@app.route("/")
def index():
    readme_file = open("Readme.md", "r")
    md_template = markdown.markdown( 
        readme_file.read(), extensions=["fenced_code"]
    )
    return md_template

@app.route("/names")
def character_names():
    characters = get.all_names()
    return json.dumps(characters)

@app.route("/names/<name>")
def one_name(name):
    char = get.get_name(name)
    print(char)
    return json.dumps(char)

@app.route("/phrases")
def all_phrases():
    pr = get.get__all_phrases()
    return json.dumps(pr)

@app.route("/phrases/<name>")
def phrases(name):
    phrase = get.get_phrase(name)
    return json.dumps(phrase)

@app.route("/episodes")
def episode_numbers():
    epi = get.all_episodes()
    return json.dumps(epi)
    
@app.route("/episode/<num>")
def episode(num):
    episode = get.get_episode(num)
    return json.dumps(episode)

@app.route("/last_id")
def last_id():
    id = get.last_id()
    return json.dumps(id)

@app.route("/sentiments/<name>")
def get_sentiment(name):
    n = get.get_phrase(name)
    get.tokenize(n)
    get.sentimentAnalysis(n)
    return 


@app.route("/new_character/<name>", methods=["POST"])
def insert_character(name):
    pos.insert_character(name)
    print(name)
    return json.dumps(name)

@app.route("/new_phrase", methods=["POST"])
def insert_phrase():
    episode_id = request.args.get("episode_id", None)
    character_id = request.args.get("character_id", None)
    phrase = request.args.get("phrase", None)
    return pos.insert_phrase(episode_id, character_id, phrase)

@app.route("/delete_character/<name>", methods=["POST"])
def del_character(name):
    delete = pos.delete_character(name)
    return delete

@app.route("/delete_phrase", methods=["POST"])
def del_phrase():
    phrase = request.args.get("phrase", None)
    return pos.delete_phrase(phrase)


#@app.route("/insert_all_characters")
#def insert_characters():
    #for n, line in characters_grouped.iterrows():
        #pos.insert_characters():
    #return    
            

app.run("0.0.0.0", 5000, debug=True)
