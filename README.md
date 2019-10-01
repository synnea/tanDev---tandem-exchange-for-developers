# tanDev

### Milestone Project 3: Data-Centric Development

![indexpage](https://github.com/synnea/tanDev--tandem-for-devs/blob/master/static/img/amiresponsive_index.PNG)

[tanDev](https://tandev.herokuapp.com/index) is a skill exchange platform created by Carina Pöll to connect developers and designers with each other who wish to exchange their skills.

The term 'tandem' is taken from the language learning community, in which it means:

"*Tandem language learning is a method of language learning based on mutual language exchange between tandem partners, where ideally each learner is a native speaker in the language the other party wants to learn...*"

The tandem exchange concept is taken to connect developers and designers skilled in some languages or areas of development who wish to improve their skills in others.

## Table of Contents

1. [UX](#UX)
    - [Logo Design](#logo)
    - [User Stories](#userstories)
    - [Wireframes](#wireframes)

2. [Data](#data)

3. [Features](#features)
    - [Current Features](#current-features)
    - [Features Left to Implement](#future-features)

4. [Technologies Used](#technologies)
    - [Programming Languages](#languages)
    - [Frameworks](#frameworks)
    - [Libraries](#libraries)
    - [Other Technologies](#other)

5. [Testing](#testing)
    - [Responsiveness Testing](#responsiveness-testing)
    - [Code Testing](#code-testing)
    - [User Story Testing](#user-stories-testing)

6. [Known Bugs](#bugs)

7. [Deployment](#deployment)
    - [Deployment Writeup](#deployment-writeup)
    - [Differences between local and deployed versions](#deployment-differences)

8. [Credits](#credits)

## UX <a name="UX"></a>

The website's target audience are developers and designers. For developers based in Berlin, the option to search for users by district is useful; for all others, tanDev also seeks to connect individuals who wish to exchange their skills via text or video.

To appeal to the target audience, tanDev features a modern design. A blue color scheme was chosen, as blue is a color closely associatied with technology.

The main hero image featured on tanDev is one of two puzzle pieces being put together. This symbolizes the main mission of the website: to bring together people whose skills complement one another.

The website features a multi-page design. Three pages - index, about, and search - are accessible to non-members. For registered users, there is also a user area, where users may write, edit, publish and delete their profiles.

The design features a static navbar which is transparent and appears upon scroll for desktop users on some pages (mainly index and search). The navbar is fixed for mobile users and inside the user area of the tanDev.

FontAwesome icons are provided throughout the website to aid intuitive information input.

### Logo Design  <a name="logo"></a>

The logo was designed to invoke a tech-y feel. The letter 'a' in tanDev was manipulated to look like a speech bubble, to symbolize the exchange of technical skills. The original design was made in Adobe Illustrator. 

Several versions of the logo in different brand colors were created. Here is one example:

![tandevlogo](https://github.com/synnea/tanDev--tandem-for-devs/blob/master/static/img/logos/tandev_v1_brightmidblue.svg)


### User Stories <a name="userstories"></a>

The following user stories were used to design the website:

- I am a developer or designer. I heard about tanDev and have an idea what it's about. I am interested in finding out if there are other developers in the city with whom I could exchange my skills with.
- I am a developer or designer. I stumble upon tanDev without knowing what it is. 
- I am a tech recruiter interested in contacting available talent.
- I am a startup entrepreneur interested in finding a co-founder. I am a designer and need a programmer with strong backend skills to bring my product to life.


### Wireframes <a name="wireframes"></a>

Extensive wireframes with Balsamiq were created for the project. As an example, here is a wireframe for the index page:

![index-wire](https://github.com/synnea/tanDev--tandem-for-devs/blob/master/static/img/wireframe_index.jpg)


The wireframes for every page on the website are available in .pdf format on this github respository: [DESKTOP VERSION](https://github.com/synnea/tanDev--tandem-for-devs/blob/master/schemas/wireframes/wireframes%20desktop.pdf) and [MOBILE VERSION](https://github.com/synnea/tanDev--tandem-for-devs/blob/master/schemas/wireframes/wireframes%20for%20mobile.pdf).

A color palette was created early on, using the colors found in the background image as the basic point of reference. The palette was created using https://coolors.co/. The decision was taken early on that the website would feature a blue color scheme.

For the most part, the wireframes are similar to the finished product. However, some features were taken out due to time restraints: originally, the skill levels were supposed to be illustrated in a star rating on the search page, user details page as well as the profile page. However due to complexity of the dataset, this was later taken out.

An initially envisioned option to favorite other users was also removed, and has been added to the 'future features' wishlist.

## Data <a name="data"></a>

tanDev is backed by a MongoDB database. Only one collection is in use, the 'profile' collection. Here is the data schema used for individual documents in this collection:

| Key               | Value           |
| -------------     |:-------------:| 
| _id               | < integer > | 
| username          | < string >  |  
| imgUrl            |  < string > | 
| district          | < string >  |  
| shortDescription  | < string >  | 
| communicationStyle| < array >   |  
| skills            | < array >   | 
| desiredSkills     | < array >   |  
| otherDetails      | < array >   | 
| github            | < string >  |
| published         | < datetime >| 
| display           | < boolean > |  

The database was populated early on with 13 original profiles. 


## Features <a name="features"></a>

### Current Features <a name="current-features"></a>

#### Feature 1 - Carousel
The index page features a carousel of user profiles who have been published on tanDev.

#### Feature 2 - Animation on Scroll
The 'about' page features animation on scroll achieved through the [AOS library](https://michalsnik.github.io/aos/).

#### Feature 3 - Search function
The search page of tanDev allows the users to search the database for other users who have published their profiles. Searches can be executed according to desired skills, location (Berlin districts), communication styles, and other details. The search page also features pagination.

#### Feature 4 - Toggleable Sidebar
The search page also features a sidebar, which is fixed on desktop view, but toggleable on mobile, with a smooth transition animation.

#### Feature 5 - Eye-Catching Animated Usernames
In the user details view, the username is animated with an infinite text shadow keyframe.

#### Feature 6 - Preview Option
After successfully saving his or her details, the user may preview what their information would look like in a profile view.

#### Feature 7 - Flexible Navbar design
On the search and about pages, the navbar is transparent and pops into view upon scroll. On the other pages, and on mobile view, the navbar is dark and fixed.



### Features Left to Implement <a name="future-features"></a>

#### Messaging 
Currently, there is no way for users to connect with other users on tanDev. A messaging function of some sort is needed.

#### Favoriting
The option to favorite users and save them in a 'my favorites' tab of the my account dropdown is also a feature that is missing and which would add a lot of value to the website's UX.

## Technologies Used <a name="technologies"></a>

### Programming Languages  <a name="languages"></a>

 [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses **HTML5** to build the structure of the content.
    
 [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
    - The project uses **CSS3** to style the content.

 [JavaScript](https://developer.mozilla.org/de/docs/Web/JavaScript)
    - The project uses **JavaScript** for add additional frontend functionality.  

[Python](https://docs.python.org/3/)
    - The project uses **Python** to manage its database backend.
    
### Frameworks <a name="frameworks"></a>
[Bootstrap](https://getbootstrap.com/)
    - The project uses **Bootstrap**, a CSS3 and JavaScript framework.

[Flask](https://flask.palletsprojects.com/en/1.0.x/)
    - The project uses *Flask**, a Python framework.

### Libraries <a name="libraries"></a>

[jQuery.js, version 3.4.1](https://jquery.com/)
    - The project uses **jQuery.js**, a JavaScript library used for event handling.

[AOS](https://michalsnik.github.io/aos/)
    - The project uses **Animate on Scroll**.

### Other Technologies <a name="other"></a>

[Pymongo](https://api.mongodb.com/python/current/)
    - The project uses **Pymongo** to manipulate the data using Python.

[Font Awesome](https://fontawesome.com/)
    - The project uses **Font Awesome**, free icons for improved UI.

[Google Fonts](https://developers.google.com/fonts/)
     - The project uses **Google Fonts** for its typography.  

 
## Testing <a name="testing"></a>

### Responsiveness Testing <a name="responsiveness-testing"></a>

The responsiveness of the website was tested on Responsinator.

* iPhone eXpensive portrait
* iPhone eXpensive landscape
* Android portrait
* Android landscape
* iPhone 6-8 portrait
* iPhone 6-8 landscape
* iPhone 6-8 Plump landscape
* iPhone 6-8 Plump landscape
* iPad portrait
* iPad landscape

I collected the results in a responsiveness matrix:

![responsiveness matrix](https://github.com/synnea/tanDev--tandem-for-devs/blob/master/static/img/responsiveness_screenshot.JPG)

The complete .xls file has been uploaded [here](https://github.com/synnea/tanDev--tandem-for-devs/blob/master/tests/responsiveness_test_matrix.xls).

### Code Testing <a name="code-testing"></a>

**HTML** 
* [HTML Validator](https://www.freeformatter.com/html-validator.html).
    - The project contains a total of 16 html files. Throughout all of them, the HTML Validator did not recognize templating language, such as printing variables in double curly braces, as valid HTML, and threw errors. This was ignored throughout all files. Apart from Jinja-specific errors, the following anomalies remain:
        - in the 'forbidden.html' file, the HTML Validator throws an error that inline style CSS is not allowed in this context. However, moving the CSS to a separate file leads to the CSS not being rendered at all. Thus, I chose to keep the inline styling.
        - in the 'logreg.html' file, the HTML Validator throws the error that tabpanels must be part of a tablist. However, adding a div with the role of tablist disabled the functionality. Thus, the semantic problem remains uncorrected.
        - similarly, the profile pages also throw the tabpanel and tablist error. Not wanting to break the functionality, I chose to leave it alone.
        - for the 'base.html' file, the HTML Validator throws the error that the "|" character is not allowed in a query. However, it has been copied as part of a query to Google Fonts to import several different custom fonts, and was left in.

**CSS**  
* [CSS Validator](https://jigsaw.w3.org/css-validator/).
    - The project contains 1 CSS file (along with several SCSS ones). The file passes validation without any errors.

**JavaScript** 
* [JSHint.com](https://jshint.com/). 
    - The project contains 7 JavaScript files. All of them are semantically correct. The files contain a total of 27 functions, and the most complex function has a cyclomatic complexity value of 2.

**Python**
* [PEP8Online](http://pep8online.com/).
    - The project contains a total of 1 Python file. At the time of writing this readme, the Python code in this project contains a total of 10 lines which exceed the recommended max length of 79 characters. I chose to leave them in because breaking them up resulted in less readability. The PEP8 guide states that its guidelines could be bent on an individual basis when doing so raised readability, hence I chose to do so here. Apart from those 10 lines, the code is fully PEP8-compliant.

### User Story Testing <a name="user-stories-testing"></a>

Here are the results for the user story tests:

**Story 1**

- I am a developer or designer. I heard about tanDev and have an idea what it's about. I am interested in finding out if there are other developers in the city with whom I could exchange my skills with.

Solution: upon landing on the main page, the background picture of the puzzle pieces and the slogan 'exchange your skills with other developers and designers' confirms that I've come to the right place. I click on 'sign up' and am taken to the registration route.


**Story 2**

- I am a developer or designer. I stumble upon tanDev without knowing what it is.

Solution: upon landing on the main page, the imagry and slogan give me an idea about what tanDev is about. Scrolling down the page and seeing the profiles in the carousel gives a further idea. Finally, clicking on the 'about' page clarifies all doubts. Navigating back to the main page, I click on the 'sign up' button and follow the same journey as user story 1 from there on out.

**Story 3**

- I am a tech recruiter interested in contacting available talent.

Solution: upon landing on the main page, the imagry and slogan quickly give me an idea that I've come to a place where I can find relevant tech talent. The 'search' button seems most relevant to me, so I click on it. There, among the search options, I find the 'available for Hire' checkbox. I select it, and search the database for developers and designers who are open to new opportunities.

**Story 4**

- I am a startup entrepreneur interested in finding a co-founder. I am a designer and need a programmer with strong backend skills to bring my product to life.

Solution: upon landing on the main page, the imagry and slogan quickly give me an idea that I've come to a place where I can find someone to help me. The 'search' button seems most relevant to me, so I click on it. There, among the search options, I find the 'looking for Co-Founder' checkbox. I select it, and then select several backend languages in the skills menu. This gives me a list of people who have the skills I need, and who are open to being approached about co-founding opportunities. I decide to send one or several of them a message. The last point is not achieved yet, as tanDev at present does not feature a messaging function.


## Known Bugs <a name="bugs"></a>

On iPhones, the carousel on the index page overlaps with the indicators below. I was not able to find a good fix for it before it was time to submit, but I would like to fix this eventually.

## Deployment <a name="deployment"></a>

### Deployment Writeup <a name="deployment-writeup"></a>
 
To deploy tanDev on heroku, I took the following steps:

1. I created a requirements.txt file using the terminal command pip freeze > requirements.txt.

2. I created a Procfile with the terminal command echo web: python app.py > Procfile.

3. I staged and committed the requirements.txt and Procfile to my project repository. 

4. I went to heroku.com, logged in, and clicked on the "New" button in the dashboard to create a new app. I named it 'tanDev' and set its region to Europe.

5. In the heroku dashboard for the application, I clicked on "Settings" > "Reveal Config Vars". Then, I set the Port, IP, MongoURI and Secret Key variables.

6. From my terminal window, I logged into heroku using "heroku login --interactive." After entering my credentials, I registered heroku as a remote destination for my project with "heroku git remote." I then pushed my project to heroku with "git push heroku."

7. To get the app to run and scale the dynos, I used the command "heroku ps:scale web=1" in my terminal.

8. The app is now successfully deployed!

### Differences between local and deployed versions <a name="deployment-differences"></a>

The project was developed locally with Visual Studio Code. Environment variables, including secret key and Mongo URI, were saved in a settings.json file which was added to .gitignore. For the deployed version, as mentioned in the deployment writeup above, environemnt variables were set in the Config Variables.

## Credits <a name="credits"></a>

Credit for the logo goes to he-who-prefers-to-go-uncredited. You're awesome.

Many thanks to [Tim Nelson](https://github.com/TravelTimN), whose patience helped me to get started on the sever-side development.

Most of the images used on tanDev have been sourced from [Adobe Stock](https://stock.adobe.com/).





