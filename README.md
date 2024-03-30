# zQuiz
#### Video Demo: https://youtu.be/0CsNPLA6f0k
#### Description:
This is a web application that is a quiz that has 6 quesitons with 4 options each to chose the correct one.
Then at the end it will show if you chosed the correct one or the wrong one.
It will propt a log in page asking for a name and a Go button that will get user to main page
It has a nav bar at the top of the page with logo built using bootstrap, home button, and on the right has a div with logged in user name taken from session name, and a log out button.
On the first page, index.html there is a set of rules explaining how the application works, and a start button that will go to first question
All questions are a part of a form that via post submits the selected options to app.py.
The main section in the center of the page includes 1 question at the time that will change with next question when clicked "Next question" button, or will change to previous question when "Previous button" is clicked.
Also at the top of this main section is a progress bar that will fill depending on how far in to the quiz user is, also built using bootstrap.
Each selected option by user is saved in to a list after form is submited, also i have created a database to keep track of users, and results that each user has selected.
In app.py i used next libraries: session, random, helpers that has the login function, flask, and cs50`s SQL
Also in app.py i have "/" main route, that renders index.html after user logged in, log_in route that handles loggin in, by adding some information to database and saving name to session, log_out that deletes all information from session, and submit which takes the options selected by user and adds them to database.
The index file has some javascript functions, one changes the divs displayed that contains each question, other updates the progress bar at the top.
The results page prints a list of answers the current user has selected, an icon next to it that show is the answer selected was correct or wrong, this is done with a javascript function that displayes one image or another deoending what is the answer, and next to it the correct answer. the answers selected by the user are taken from app.py using jinja and placeholders.

It is a very simple application but with no guidence or any help it was a challenge still, i also tried to show a chart at the end with most popular selected answers for each question using pandas and other data analysis libraries but i failed and decided to stop here as it already took me lot of time.
