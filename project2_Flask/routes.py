from project2_Flask import app, forms
from flask import request, render_template

@app.route('/')
def helloWeb():
    first_name = "Welcome to Project 2"
    last_name = "Please type /search next to url to get to the form page"
    return "{0} {1}".format(first_name,last_name)

@app.route('/page1')
def page1():
    return "page1"


@app.route('/search',methods=['GET','POST'])
def search():
    my_form = forms.NewsForm(request.form)

    if request.method == "POST":
        full_name = request.form["full_name"]
        source = request.form["source"]
        section = request.form["section"]

        #get values provided by the user
        #call the API
        #generate requested data
        api_results= forms.generateDataFromAPI(source,section)
        #response = [full_name, year, month]

        return render_template('results.html', response=api_results, form=my_form)

    return render_template('search.html', form=my_form)

