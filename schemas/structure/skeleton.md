## Skeleton structure


### Index.html

*A function is required that picks 6 profiles from the databases and displays them in a carousel of 2*

def display_profiles:
    indexprofiles = db.profiles.aggregate({'$sample': {'size': 6}}])
    indexprofiles = list(indexprofiles)

return render_template


### Search.html

*Receive user input into filters and return results from db*


 loggedIn = True if 'user' in session else False

if request.method == *POST*:


    for skill in skills:
        if skill.* != none:
            skill = post_request['skill']

        else:
         return 'Please select at least one skill that you're willing to offer.'

    for desiredSkill in desiredSkill:

        if desiredSkill.* != none:
            desiredSkill = post_request['desiredSkill']

        else:
         return 'Please select at least one skill that you'd like to learn.'    



        district = post_request['district']
        

        if len(communication) >= 1:
            for communication_style in communication_style:
                 if selected: add to filter
                return list of selected filters
        

        if len(other) >= 1:
            for other in other:
                if selected: add to filter
                return list of selected filters

        display matching database entries where display=true;

    
### Profile(user xzy)

*this is the enlarged view of a user's profile. The main functionality is adding the user to the favorites list.*
*checks if user is logged in to show correct view*

loggedIn = True if 'user' in session else False

profile = db.profile.find_one({"_id": ObjectId(profile_id)})

favorites = []

if heart is clicked:
    favorites = favorites.append[username]



### Register.html


create new document in 'users'


newdoc.user = request.get(username)
newdoc.email = request.get(email)
newdoc.password = request.get(password)



### Login.html

*checks if user is already logged in, if they are redirects them to 'my profile*

     loggedIn = True if 'user' in session else False

    if loggedIn == True:
        return redirect(my profile)

    else:
        wait for data entry
        when entered: check against data base
            username correct?
            password correct?
                if yes: return redirect(my profile)
                else: return("Sorry, there seems to be something wrong with your information")


    return render_template("login.html")


## Logout page

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home_page'))


### My Profile - filling it out and clicking on Preview


    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))


    def preview:
        profile = mongo.db.profile
        profile.insert_one(request.form.to_dict())
        render_template("profile/<username>")


### MyProfile - Changes Rejected

def delete_profile(username):
    mongo.db.profile.remove({'username': username})
    return redirect(url_for(myprofile))



### MyProfile - Publishing


db.profile.insert_one("display":"true");


## My Profile - Editing

def edit_myprofile(username):
    profile.update( {'username': username},
    {
.... replace all fields with request.form.get
    })
    return redirect(url_for('myprofile'))


    

