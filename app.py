import os.path
from os import path
import parserA as parserA
import Tree
from keywords import *
from backEnd import SQLBackEnd
import testCommands
from testCommands import SQLBackEnd
from flask import Flask
from flask import Blueprint, render_template, request
import threading


global app
app = Flask(__name__)







@app.route('/', methods=['POST', 'GET'])
def index():
    errors = []
    data = []
    runaround = 0


    # if (path.exists("./server.mdf")):
    #     os.remove("./
    if runaround == 0:
        testCommands.virtualServer = SQLBackEnd('server.mdf')
        print('Please upload Top50SpotifySongs.csv')
        testCommands.virtualServer.uploadCSV('TOP50', './Top50SpotifySongs2019.csv')
        print('Please upload Top50SpotifyArtists.csv')
        testCommands.virtualServer.uploadCSV('TOP50ARTISTS', './Top50SpotifyArtists2019.csv')
        runaround += 1

    if request.method == "POST":
        try:
            queryfromPOST = request.form['submission']
            errors.append(queryfromPOST)
            errors.append(type(queryfromPOST))
            tree = parserA.parse(queryfromPOST)
            errors.append(str(tree))
            errors.append(type(tree))

            try:
                output = []
                errors.append(tree.evaluate())
                data.append(tree.evaluate())

            except:
                errors.append("Broken Output Function")
                errors.append(str(output))
                pass

            try:
                data.append(output)
            except:
                errors.append("Cannot Append Output when Broken")
                return render_template("index.html", helpWords=HELP_WORDS_LIST, query=errors)

            #return render_template("index.html", helpWords=HELP_WORDS_LIST, query="In Parsing Thread")



            go = True
            loaded = True

            if queryfromPOST == "help":

                return render_template("index.html", helpWords=HELP_WORDS_LIST, query=queryfromPOST)

            elif queryfromPOST == "load":
                if loaded:
                    pass
                    return "<h1>Hello world4</h1>"
                else:
                    virtualServer = SQLBackEnd('server.mdf')
                    virtualServer.uploadCSV()
                    loaded = True

            elif not loaded:
                return render_template("index.html", data="CSV needs to be loaded. Type 'Load'", helpWords=HELP_WORDS_LIST, query=queryfromPOST)

            elif go:
                return render_template("index.html", data=data, helpWords=HELP_WORDS_LIST, query=queryfromPOST)

            else:
                return render_template("index.html", data=data, helpWords=HELP_WORDS_LIST, query=queryfromPOST)

        except:
            errors.append("Unable to process your request.")
            return render_template("index.html", helpWords=HELP_WORDS_LIST, query=errors)
    return render_template("index.html", helpWords=HELP_WORDS_LIST)







if __name__ == '__main__':

    app.run()


