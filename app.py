
import os
from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask_pymongo import PyMongo, pymongo
from werkzeug.security import check_password_hash, generate_password_hash
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import math
import json


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'tandev'
app.config['MONGO_URI'] = os.environ.get("MONGO_URI")

# Assign a randomized secret key
app.secret_key = os.urandom(24)

mongo = PyMongo(app)

client = MongoClient(app.config['MONGO_URI'])
db = client.tandev

#Helper Lists
skills = list(["CSS", "JavaScript", "React", "Vue", "Angular",
               "UX", "Web Design", "SQL", "Python", "PHP", "Ruby", "C++", "C#",
               "Java", "Rust", "Go", "Swift", "Kotlin", "Perl"])

commstyles = list(["text", "video", "inperson"])

other = list(["availableForProjects", "availableForHire", "lookingforCoFounder"])

page_number = 1



# Begin creating routes
# Index page
@app.route('/', methods=['GET'])
def index():
    """ Create a list of 6 random profiles whose display key is set to 'True' to be used in the
    index.html carousel. """

    loggedIn = True if 'username' in session else False


    carousel = db.profile.aggregate([{"$match" : {"display" : True}},
                                     {"$sample": {"size": 6}}])
    carousel = list(carousel)
    return render_template("pages/index.html", active="index", carousel=carousel, loggedIn=loggedIn)



#About page
@app.route('/about', methods=['GET'])
def about():
    """ Checks if the user is logged in in order to show the correct navbar items.
    Render the About page. """

    loggedIn = True if 'username' in session else False

    return render_template("pages/about.html", active="about", loggedIn=loggedIn)



# Search page
@app.route('/search/<page_number>', methods=['GET', 'POST'])
def search(page_number):
    """ Checks if the user is logged in in order to show the correct navbar items.
    Collect user feedback in arguments. Display all profiles by default.
    Check which fields the user selected, and assign the appropriate MongoDB
    search arguments to the 'profiles' variable.
    Render the Search page. """

    loggedIn = True if 'username' in session else False

    # Set form variables
    # Checks if the variables already exist in the session cookies.

    if 'skill_arg' in session:
        skill_arg = session['skill_arg']

    elif 'skill_arg' not in session:
        skill_arg = str(request.form.getlist("skill"))

    if 'district_arg' in session:
        district_arg = session['district_arg']

    elif 'district_arg' not in session:
        district_arg = request.form.get("district") 

    if 'comm_arg' in session:
        comm_arg = session['comm_arg']

    elif 'comm_arg' not in session:
        comm_arg = request.form.getlist("commstyle")

# if 'all' was selected for district, remove the district argument from the search variables.
    if district_arg == 'all':
        district_arg = None

    # Upon hitting search, save the arguments in sessions. 
    if request.method == "POST":
        session['skill_arg'] = str(request.form.getlist('skill'))
        session['district_arg'] = request.form.get("district")
        session['comm_arg'] = request.form.getlist('commstyle')
        return redirect(url_for('search', page_number=1))

    # Clear the search arguments upon hitting the 'clear' button.
    if request.method == "POST" and request.form['btn'] == 'clear':
        session.pop('skill_arg', None)
        session.pop('district_arg', None)
        session.pop('comm_arg', None)
        return redirect(url_for('search', page_number=1))

    # Set pagination variables
    page_number = int(page_number)  
    limit = 4
    skips = limit * (page_number - 1)

    # Create text search index
    db.profile.create_index([('skills', 'text')])

    # By default, display all published profiles.
    profiles = db.profile.find({"display": True})

    # Go through all the possible combinations of variable entry.
    # if all possible variables have been selected.   
    if skill_arg != "[]" and district_arg is not None and comm_arg != []:
        profiles = db.profile.find({"$and": [{"display": True}, {"$text":{"$search": skill_arg}},
                                              {"district": district_arg}, {"communicationStyle": {"$all": comm_arg}}]})

    # if district and communication style is selected.  
    if skill_arg == "[]" and district_arg is not None and comm_arg != []:
        profiles = db.profile.find({"$and": [{"display": True }, {"district": district_arg}, {"communicationStyle": {"$all": comm_arg}}]})

    # if skills and communication style is selected.
    if skill_arg != "[]" and district_arg is None and comm_arg != []:
        print("skill and comm selected")
        profiles = db.profile.find( { "$and": [  {"$text": {"$search": skill_arg }}, { "display": True},  {"communicationStyle": {"$all": comm_arg}} ] } )

    # if only skills are selected   
    if skill_arg != "[]" and district_arg is None and comm_arg == []:
        profiles = db.profile.find( { "$and": [ { "display": True }, {"$text": {"$search": skill_arg }} ] } )
    
    # if skills and district were selected.
    if skill_arg != "[]" and district_arg is not None and comm_arg == []:
        profiles = db.profile.find( { "$and": [ { "display": True }, {"$text": {"$search": skill_arg }}, {"district": district_arg} ] } )

    # if district and communication style were selected.    
    if skill_arg == "[]" and district_arg is not None and comm_arg != []:
        profiles = db.profile.find( { "$and": [ { "display": True }, {"district": district_arg}, {"communicationStyle": {"$all": comm_arg}} ] } )

    # if only district was selected.
    if district_arg is not None and skill_arg == "[]" and comm_arg == []:
        profiles = db.profile.find( { "$and": [ { "display": True }, {"district": district_arg} ] } )

    # if only communication style was selected.
    if skill_arg == "[]" and district_arg is None and comm_arg != []:
        profiles = db.profile.find( { "$and": [ { "display": True }, {"communicationStyle": {"$all": comm_arg}} ] } )



    # Profile Counts

    all_profiles = db.profile.find( {  "display": True } )
    all_profile_count = all_profiles.count()
    profile_count = profiles.count() if profiles else ""

    print(profile_count)

    # Calculate the number of total pages per search result.
    total_pages = math.ceil(profile_count / limit)

    # Calculate the numbers of the first and last profile on each page.

    if page_number == total_pages:
        last_profile = profile_count

    else:
        last_profile = (page_number * limit)

    first_profile = (page_number * limit) - (limit - 1)


    # Assign profiles with skip and limit
    profiles = profiles.sort("_id", pymongo.ASCENDING).skip(skips).limit(limit)

    # Set previous and next buttons 

    next_url = url_for('search', page_number=page_number + 1)
    prev_url = url_for('search', page_number=page_number - 1)

    print(skill_arg)
    print(comm_arg)

    return render_template("pages/search.html", active="search", loggedIn=loggedIn, skills=skills, 
                            profiles=profiles, last_profile=last_profile, first_profile=first_profile, total_pages=total_pages, page_number=page_number, next_url=next_url, prev_url=prev_url, commstyles=commstyles, profile_count=profile_count, all_profile_count=all_profile_count)



# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Checks if the user already exists in the database. If they don't exist, the user is notified of this. 
    If the username does exist, the password is matched against it. If it matches, the user is logged in.
    Otherwise, the user is notified that his username and password combination didn't match. """

    loggedIn = True if 'username' in session else False

    if request.method == 'POST' and request.form['btn'] == 'login':
        existing_user = db.profile.find_one({'username': request.form.get('username')})
        if not existing_user:
            flash("Hmm... this username doesn't seem to exist.", "error")
            return redirect(url_for('login'))

        if check_password_hash(existing_user["password"], 
        request.form.get("password")):
            session['username'] = request.form.get('username')
            return redirect(url_for('profile', username = session['username']))
        else:
            flash("Uh-oh! Username and password combo doesn't match.", "error")
            return redirect(url_for('login'))

    else:
        return render_template("pages/logreg.html", active="logreg", loggedIn=loggedIn)


# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Check if the username already exists in the database. Return warning to the user if it exists.
    If it doesn't exist, add user to the database and create a new document in the database.
    This function was written with the help of Tim Nelson who helped me get the hang of Python backend coding, so I could do
    the remaining functions on my own. """

    loggedIn = True if 'username' in session else False

    if request.method == 'POST' and request.form['btn'] == 'register':
        exists = db.profile.find_one({'username': request.form.get('username')})
        if exists:
            flash("Sorry, this username already exists", "error")
            return redirect(url_for('register', _anchor = 'register-tab'))
        register = {
            "username": request.form.get('username'),
            "email": request.form.get('email'),
            "password": generate_password_hash(request.form.get('password')),
            "imgURL": "",
            "district": "",
            "shortDescription": "",
            "description": "",
            "experience": "",
            "communicationStyle": [],
            "skills": [],
            "desiredSkills": [],
            "otherDetails": [],
            "github": "",
            "registered": datetime.now().strftime("%d-%M-%Y"),
            "published": "",
            "display": False
        }
        db.profile.insert_one(register)
        session['username'] = request.form.get('username')
        return redirect(url_for('newprofile', username = session['username']))

    return render_template("pages/logreg.html", active="logreg", loggedIn=loggedIn)


# New profile
@app.route('/newprofile/<username>', methods = ['GET', 'POST'])
def newprofile(username):
    """ Check if the user selected at least skill and one desired skill.
    If they haven't, display an error message.
    Else, if all requirements are met, add the new data to the user's database document """

    loggedIn = True if 'username' in session else False

    if loggedIn == False:
        return redirect(url_for('forbidden'))


    if request.method == 'POST':
        
        if request.form.getlist("skills") and request.form.getlist("desiredSkills") != "":

            db.profile.update_many( {'username': username},
            { "$set": {
                'shortDescription': request.form.get('shortDescription'),
                "imgURL": request.form.get('imgURL'),
                "district": request.form.get('district'),
                "skills": request.form.getlist("skills"),
                "desiredSkills": request.form.getlist("desiredSkills"),
                "communicationStyle": request.form.getlist("communicationStyle"),
                "otherDetails": request.form.getlist("other"),
                "published": datetime.now().strftime("%d-%M-%Y"),
                "github": request.form.get('github'),

            }})

            flash("Changes saved successfully. Scroll down to preview or edit.", "success")

            return redirect(url_for('profile', username = session['username']))

        else:
            flash("Please select at least one acquired and one desired skill", "error")
            return redirect(url_for('newprofile', username = session['username'])) 

    return render_template("pages/newprofile.html", username=username, active="profile", loggedIn=loggedIn, skills=skills,
    commstyles=commstyles, other=other)


# Profile page
@app.route('/myprofile/<username>', methods = ['GET', 'POST'])
def profile(username):
    """ Checks in if the user is logged in. If they are not, redirect to custom forbidden page.
    If they are, continue. If the 'preview' button was clicked, redirect to the 'preview' function.
    If the 'edit' button was clicked, redirect to the 'edit' function.
    If the 'unpublish', find the user in the database, and set 'display' to False, and reload the page.    
    """
    loggedIn = True if 'username' in session else False

    if loggedIn == False:
        return redirect(url_for('forbidden'))

    username = db.profile.find_one({"username": username})

    if request.method == 'POST' and request.form['btn'] == 'preview':

        username=session['username']
        return redirect(url_for('preview', loggedIn=loggedIn, username=username))

    if request.method == 'POST' and request.form['btn'] == 'edit':
        username=session['username']
        return redirect(url_for('edit', loggedIn=loggedIn, username=username))

    if request.method == 'POST' and request.form['btn'] == 'unpublish':

        db.profile.find_one_and_update({"username": session['username']}, {"$set": {"display": False}})
        username = session['username']
        return redirect(url_for('profile', loggedIn=loggedIn, username=username))


    return render_template("pages/profile.html", username=username, active="profile", loggedIn=loggedIn, commstyles=commstyles, other=other)


# Preview
@app.route('/preview/<username>', methods = ['GET', 'POST'])
def preview(username):
    """ Grab the details of the user and display them in the user_details template.
    If the user pushes the 'publish' button, the display variable is set to True, so
    that the user can now be found in searches or show up on the carousel on index.html. """

    loggedIn = True if 'username' in session else False

    if loggedIn == False:
        return redirect(url_for('forbidden'))

    user = db.profile.find_one({"username": username})

    if request.method == 'POST' and request.form['btn'] == 'publish':
        db.profile.find_one_and_update({"username": username}, {"$set": {"display": True}})

        flash("You have been published on tanDev. You will now show up in search results.", "success")

        return redirect(url_for('user_details', username=session['username'] ))


    if request.method == 'POST' and request.form['btn'] == 'discard':
        db.profile.update_many( {'username': username},
        { "$set": {
                'shortDescription': "",
                "imgURL": "",
                "district": "",
                "skills": [],
                "desiredSkills": [],
                "communicationStyle": [],
                "otherDetails": [],
                "published": "",
                "github": "",

        }})
        username = session['username']
        flash("Your changes have been discarded.", "success")
        return redirect(url_for('newprofile', username = username, discarded=True, skills=skills,
        commstyles=commstyles, other=other))


    return render_template("pages/user_details.html", active="profile", user=user, loggedIn = loggedIn, preview=True)


# Edit Profile
@app.route('/edit/<username>', methods = ['GET', 'POST'])
def edit(username):
    """ Checks if the user is logged in, if they are not, redirect to custom forbidden page.
    If the 'save' button was clicked, update the corresponding database fields with their
    new values before redirecting to the profile page.
    """

    loggedIn = True if 'username' in session else False

    if loggedIn == False:
        return redirect(url_for('forbidden'))

    if request.method == 'POST' and request.form['btn'] == 'save':
        db.profile.update_many( {'username': session['username']},
        { "$set": {
        'shortDescription': request.form.get('shortDescription'),
        "imgURL": request.form.get('imgURL'),
        "district": request.form.get('district'),
        "skills": request.form.getlist("skills"),
        "desiredSkills": request.form.getlist("desiredSkills"),
        "communicationStyle": request.form.getlist("communicationStyle"),
        "otherDetails": request.form.getlist("other"),
        "github": request.form.get('github'),

        }})

        flash("Edits saved successfully. Scroll down to preview and publish.", "success")

        return redirect(url_for('profile', loggedIn=loggedIn, username=session['username']))


    username = db.profile.find_one({"username": username})

    return render_template('pages/editprofile.html', loggedIn=loggedIn, username=username, active="profile", skills=skills,
    commstyles=commstyles, other=other)


# Settings
@app.route('/settings/', methods = ['GET', 'POST'])
def settings(): 
    """ Checks if the user is logged in, if they are not, redirect to custom forbidden page.
    If the user clicked the 'edit' button, redirect them to the 'edit_settings' route.
    If they clicked the 'delete account' button, find the user in the database and remove them,
    clear the session, and redirect to the index page.
    """

    loggedIn = True if 'username' in session else False

    if loggedIn == False:
        return redirect(url_for('forbidden'))

    if request.method == 'POST' and request.form['btn'] == 'edit':
        return redirect(url_for('edit_settings'))

    if request.method == 'POST' and request.form['btn'] == 'delete':
        db.profile.delete_one({'username': session['username']})
        session.clear()
        return redirect(url_for('index'))

    username = db.profile.find_one({"username": session['username']})

    return render_template('/pages/settings.html', loggedIn=loggedIn, username=username, active="profile")


# Edit Settings
@app.route('/settings/edit', methods = ['GET', 'POST'])
def edit_settings():
    """ Checks if the user is logged in, if they are not, redirect to custom forbidden page.
    If the user clicked on the 'save changes' button, update the relevant fields, and redirect to 
    the settings route.
    """

    loggedIn = True if 'username' in session else False

    if loggedIn == False:
        return redirect(url_for('forbidden'))

    if request.method == 'POST' and request.form['btn'] == 'save':
        db.profile.update_many( {'username': session['username']},
        { "$set": {
        'email': request.form.get('email'),
        "password": generate_password_hash(request.form.get('password')),
        }})

        flash("Your settings have been updated.", "success")

        return redirect(url_for('settings'))
        

    username = db.profile.find_one({"username": session['username']})

    return render_template('/pages/settings.html', loggedIn=loggedIn, username=username, active="profile", edit=True)


# Logout
@app.route('/logout', methods = ['GET'])
def logout():
    """ Logs the user out of their session. """

    session.clear()

    return redirect(url_for('index'))


# User details page
@app.route('/user/<username>', methods = ['GET', 'POST'])
def user_details(username):
    """ Checks if the user is logged in to display the correct navbar configuation.
    Accepts the username variable, looks it up in the database, and passes it on to
    the html page with full user details. """

    loggedIn = True if 'username' in session else False

    user = db.profile.find_one({"username": username})

    return render_template("pages/user_details.html", user=user, active="profile", loggedIn=loggedIn)


# Custom 403 page
@app.route('/denied')
def forbidden():
    """ If a user tries to access a part of the website that for which they need
    need to be logged in, but aren't, they get redirected to the custom permission denied page. """

    return render_template("pages/forbidden.html")

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=(os.getenv('PORT')), debug="True")
