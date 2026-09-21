# Webcode-center
Webcode Center is an online learning website for to learn web development.
The website allows users to view different coding courses and read information about each course. Each course has a title, description, price and lessons.

Users can create an account, log in and buy a course using Stripe. After the payment is successful, the purchased course will be added to the My Courses page. The user can then open 
the course and view its lessons.

Users can also add a review and give a rating from 1 to 10. They can edit or delete their own reviews.
The website also has features for staff users. Staff users can add new courses and edit or delete existing courses.

the main purpose of Webcode Center is to create a simple place where users can find coding courses, buy them and access their course content from their account.
The website was created using Django, python, HTML, CSS and JavaScript. Bootstrap is used for the website layout and stripe is used to process course payments.

# User Experience (UX)
## User Story 1: Create an account
- As a user I want to create an account so that I can buy courses and access my purchased courses.
- Acceptance Criteria
1. The sign up page is available.
2. The user can create a new account.
3. The user can enter username, email and password.
4. The user can confirm the email adress.
5. The user can login after creating the account.

## User Story 2: Login and Logout
- As a user I want to login and logout so that I can access my account safetly.

- Acceptance Criteria
1. The login page is available.
2. The user can login with the correct account details.
3. The user can logout from the website.
4. My courses is available after login.
5. Login and register are only displayed hwne the user is logged out.

## User Story 3: View Courses
- As a user I want to view the available courses so that I can find a course Iwant to learn 

- Acceptance Criteria

1. Courses are displayed on the main page.
2. Each course shows its title and description.
3. A view Course button is available.
4. The user can open the course details page.

## User Story 4: Search Courses 

- As a user I want to search for courses so that i can find a course more easily.

- Acceptance Criteria

1. A search field is displayed on the courses page.
2. The user can type a course name.
3. Courses that match the search are displayed.
4. Courses that do not match the search are hidden.

## User Story 5: View Course Details

- As a user I want to view the course detais so that I can know
more about the course before buying it.

- Acceptance criteria

1. The course title is diplayed.
2. The course description is displayed.
3. The course price displayed.
4. What the user learn is displayed.
5.  Buy button is available.


## User Story 6: Buy Course

- As a registered user I want to buy a course so that I can access its lessons.

- Acceptance Criteria
1. The user must be logged in to buy a course.
2. The checkout page displays the course and price.
3. The user can enter payment details.
4. Stripe is used to process the payment.
5. A successful payment gives the user access to the course.
6. A purchased course is added to My Courses.

## User Story 7: View Purchased Courses

- As a user I want to view my purchased courses so that i can easily access them again.

- Acceptance Criteria
1. A My Courses link is available for logged in users.
2. Purchased courses are displayed on the My Courses page.
3. The course title and description are displayed.
4. The user can open a purchased course.

## User Story 8: Access Course Lessons

- As a user I want to view the lessons of a course I purchased so that I can learn from the courses.

- Acceptance Criteria
1. Lessons are displayed after the course is purchased.
2. The lesson title is displayed.
3. The lesson content is displayed.
4. Users who have not purchased the course cannot view the lessons.

## User Story 9: Add a Review

- As a logged in user I want to add a review and rating so that i can share my opinion about a course.

- Acceptance Criteria
1. An add review button is available.
2. The user can write a review.
3. The user can select a rating from 1 to 10.
4. The review is displayed on the course page after it is added.


## User story 10: Edit and Delete Review

- As a user I want to edit or delete my review so that i can
manage the reviews i created.

- Acceptance Criteria
1. An Edit Review button is available for the review owner.
2. The user can update thier review.
3. The user can delete their review.
4. A user cannot edit or delete another user's review.

## User Story 11: Manage Courses as Staff

- As a staff user I want to manage courses so that i can keep
the courses content udpated.

- User Story 11: Manage Courses as Staff

As a staff user I want to manage courses so that I can keep the course content updated.

- Acceptance Criteria

1. Staff users can see the add courses link.
2. Staff users can add a new course.
3. staff users can edit an existing course.
4. staff users can delete a course.
5. Normal users cannot access the course management features.

# Features

- Existing Features
- Navigation Bar 

the navigation bar helps users move between the main pages of the website. 

1. Users can go back to the Courses page.
2. Logged out users can see Login and Register 
3. Logged in users can also see Add Course.
4. Staff users can also see Add Course.
5. The navigation bar works on smaller screen sizes using the Bootstrap menu.

- Course List 
the main page displays the available courses.

1. Each course has a title and description.
2. Each course has a View Course button.
3. The button opens the details page.

- Course Search 
A search field is available on the main courses page.

1. Users can type text into the searh field.
2. JavaScript checks the course cards.
3. Courses that match the search stay visible.
4. Courses that do not match are hidden.

- Course Details
The details page gives more information about a course.

The page display:

1. Course title.
2. Course description.
3. What the user will learn.
4. Course price.
5. Course lessons.
6. Course reviews.
the lessons are protected and are only displayed when the user has purchased the course.

- User Accounts
the website uses Django Alluath for user account.
User can:

1. Register a new account.
2. Confrim their email address.
3. Login.
4. Logout.

- Stripe Payment 
Stripe is used to process course payments.

1. The checkout page shows the selected course and its price. 
2. The user can enter card details.
3. The payment is processed using Stripe.
4. After a successful payment the course is added to the user's purchased courses. 
5. The website checks if the course was already purchased to stop duplicate purchased. 

- My courses 
Logged in users have a My Courses page.

1. The page display courses purchased by the user.
2. the user can open a purchased course.
3. Purchased course lessons are available to the user.

- Reviews and Ratings 
Logged in users can add reviews to courses.

1. A review contains text and a rating.
2. the rating is from 1 to 10.
3. JavaScript is used for the rating buttons. 
4. Users can edit their own reviews.
5. Users can't edit or delete reviews created by another users.

- Staff Course Managment 
Staff users can manage the courses on the website.

Staff users can:
1. Add a new course.
2. Edit an existing course
3. Delete a course.
These option are protected and are not available to normal users. 

- Responsive Design
The website was made to work on different screen sizes. 

- Futures Features
some features could be added in the future:

1. User profiles.
2. Courses images. 
3. More course categories
4. more payment option.

# Technologies Used 

- Languages 
1. HTML used to create the structure of the website pages.
2. CSS used to style the website. 
3. JavaScript used for course search and the review ratting buttons.
4. Python used for the backends logic of the website.

- Frameworks and Libraries
1. Django 
2. Bootstrap 
3. Django Crispy Forms
4. Django Alluath 
5. WhiteNoise

- Database
1. PostgreSQL

- Payment
1. stripe

- Deployment and Development Tools
1. Heroku 
2. git 
3. github
4. VS code

# Database Design 
Webcode Center uses a relational database to store the website 

the project has four main models:

Course Model 
the Course model stores information about each course.

it contains:
1. Title- stores the name.
2. description- stores information about the course.
3. What will you learn - explains what the user can learn form the course.
4. price - stores the price of the course. 

- Lessons Model 
the lessons model stores the lessons for each course.
it contains:
1. Course - connects the lessons to a course. 
2. Title - stores the lessons title. 
3. Content . stores the lessons content. 

- Review Model 

the review model stores reviews created by users.
it contains:

1. User - connects the review to the user who created it. 
2. Course - connects the review to a course.
3. Content - stores the review text.
4. Rating - stores a rating between 1 and 10. 

- Enrollment Model 

The Enrollemnt model stores the courses purchased by users. 

it contains:

1. User - connect the purchase to a user
2. Course - connects the purchase to a course.
3. Purchased at - stores the date and time of the purchase.


- Model Relationships

The main relationships are:

1. One Course can have many Lessons.
2. One Course can have many Reviewa. 
3. One Course can have many Enrollments.
4. One User can have Review. 
5. One User can have Enrollments.

These relationships help connect users, courses, lessons, reviews and purchased courses.

# Authentication and Authorization

Webcode center uses Django Alluath for user
authentication.
Users can create an account, confrim their email address, login and logout.

some features are only available for logged in users.

- Logged in Users 
Logged in users can:

1. Buy courses.
2. View their purchased courses in My Courses.
3. Access lessons from courses they purchased.
4. Add reviews.
5. Edit their own reviews.
6. Delete their own reviews.

- Staff Users 
staff users have extra premissions for managing courses.
they can:
1. Add courses.
2. Edit courses.
3. Delete courses.

- Course Access 
Course lessons are protected.

The website checks if the logged in user has purchased the course if the course has been purchased the lessons are displayed.
this helps make sure that paid course content is only available to users who purchased the course. 

# Stripe Payments

Webcode Center uses Stripe to process course payments.

When a logged in user chooses to buy a course, they are taken to the checkout page. The checkout page display the course name, price and a Stripe card field.

After a successful payment:

1. The payment is confirmed.
2. An Enrollment is created for the user and course.
3. The course is added to the user's My Course page.
4. The user can access the lessons of the purchased course.
5. A success message is display to the user.

If the payment is not successful, the user receives an error message.

The website also checks if the user already purchased the course. This helps prevent the same course from being purchased again.


# Testing 
The Webcode Center website was manually tested during development and after deployment.

- Manual Testing
The main features of the website were tested to make sure they work correctly.

| Feature | Action | Result |
| --- | --- | --- |
| Register | Create a new account | Pass |
| Login | Login with correct details | Pass |
| Logout | Login with correct details | Pass |
| Course Search | Search for a course | Pass |
| Course List | Open the Course page | Pass |
| Course Details | Click view course | Pass |
| Buy Course | Click buy | pass |
| Stripe paayment | Make a test payment | pass |
| My Courses | Open My course after payment | pass |
| Course Lessons | Open a purchased course | Pass |
| Protected Lessons | Open a ciurse without buying it | Pass |
| Add Review | Add a review and rating | Pass |
| Edit Review | Edit my  review | Pass |
| Delete Review | Delete my review | Pass |
| Add Course | Add course as staff | Pass |
| Edit Course |  Edit course as staff | Pass | 
| Delete Course |  Delete a course as staff | Pass | 
| Staff Protection |  Try course managment as a normal user | Pass |
| Duplicate Purchased | Try to buy the same course again | Pass |
| Payment Feedback | Test successful and failed payment | Pass |


# Development Cycle
- Planning Phase

I started by planning the main goal of Webcode Center. The goal was to create a Website where users can view coding courses, buy and access their lessosns.
I decided on the main features such as user authentication courses lessons reviews payments and My courses. I also created user stories to help plan the project. 

- Design Phase 
I planned a simple design for the website. I used black and gold as the main colours and used Bootstrap to help make the pages responsive.
The main pages were kept simple so users can easily find courses view course information and access their purchased courses.

- Development Phase 
I built the project using. Django, Pyhton, HTML, CSS and 
JavaScript.

I created separate Django apps for courses and checkout.
Django Alluath was used for user authentication and Stripe 
Was used for course payments.

I created models for courses, lessons, reviews and enrollment. These models are connected using relationships in the database.

- Testing Phase 
I tested the main features of the website manually during development. 
I tested user registration, login, courses, reviews, Stripe 
payments, purchased courses and staff features.
I also used validators to check HTML, CSS JavaScript and Python code.

- Debugging and Improvment 
I fixed different problems during the development of the project, including:
1. User authentication problems.
2. Course page layout problems. 
3. Stripe checkout problems.
4. Database and migration problems.
5. Static files not loading correctly after deployment.
6. Heroku deployment problems.
7. HTML validation problems.
I tested the website again after fixing the problems.

# Deployment 
This project was deployed to Heroku from a GitHub repository.

- Creating GitHub Repository 
1. I created a new GitHub repository for the project.
2. I added my Django project files to the repository.
3. I used Git commands to add commit and push the project files to GitHub.

- Creating the Heroku App 
1. I signed in to Heroku.
2. I clicked New and selected Create New App.
3. I entered the app new.
4. I selected the Europe region.
5. I clicked Create App.

- Preparing the project for Deployment 

1. I installed Gunicorn using pip3 install gunicorn.
2. I updated the requirements file using pip3 freeze > requirements.txt.
3. I created a Procfile in the root directory.
4. Inside the Procfile, I added web: gunicorn
webcode_center.wsgi.
5. I added the Heroku app hostname to ALLOWED_HOSTS.
6. I configured static files using WhiteNoise and STATIC_ROOT.


- PostgreSQL Database

1. I added a PostgreSQL database to the Heroku app.
2. I added the database configuration to the project.
3. I ran the Django migrations on Heroku to create the database tables.

- Heroku Config Vars 
In the Heroku settings tab i opened config vars and added
the required environment variables.

The secret values are stored in Config Vars and are not included in the GitHub repository.

- Deploying on Heroku 
1. I opened the Deploy tab in Heroku.
2. I selected GitHub as the deployment method.
3. I connected my GitHub repository to Heroku.
4. I deployed the main branch.
5. After the build finished I opened the deployed website.
6. I tested the main features to make sure the deployed website was working  correctly.

- Local Development
To run the project locally:

1. Clone the GitHub repository.
2. Open the project folder in the terminal.
3. Create a virtual environment.
4. Activate the environment.
5. Install the required packages using pip3 install -r requirements.txt.
6. Add the required environment variables.
7. Run the database migrations using python3 manage.py migrate.
8. Start the development server using python3 manage.py runserver.
9. Open the local server in the browser.
The required secret keys and passwords are not included in the GitHub repository and need to be added as environment variables.

- Secuirty 
Secuirty was considered during the development and deployment of Webcode Center.

1. Secret keys and passwords are not stored in the GitHub repository.
2. Sensitive information is stored using environment variables.
3. The local env.py file is included in .gitignore.
4. Heroku Config Vars are used to store secret values on the deployed website.
5. DEBUG is set to False in the deployed version.
6. Stripe secret information is stored in environment variables.
7. Staff-only features are protected from normal users.
8. Users can only edit or delete their own reviews.
9. Course lessons are only available to users who purchased the course. 

- GitHub and Git
Git and GitHub were used for version control during the development of Webcode Center.

I used Git to save changes during the development of the project.
The main Git commands used were:
1. git add . to add the changes files
2. git commit -m "--" to save the changes with a commit message.
3. git push to push the changes to GitHub.

GitHub was used to store the project repository and keep the development history 
I made commits during development when adding features fixing problems and making changes to the project.

# Bugs and Fixes 
1. Bug: Static files were not loading correctly after deployment.
2. Cuase: Static files were not configured correctly for Heroku.
3. Fix: Configured WhiteNoise and STATIC_ROOT for the deployed project.
4. Bug: The Heroku apllication showed a DisallowedHost error.
5. Cuase: The Heroku hostname was not included in ALLOWED_HOSTS.
6. Fix: Added the Heroku apllication hostname to ALLOWED_HOSTS.
7. Bug: The heroku  application did not start correctly.
8. Cause: The Procfile was not configured correctly.
9. Fix: Corrected the Procfile and used Gunicorn to run the Django application.
10. Bug: The database did not work correctly during the first deployment.
11. Cause: PostgreSQL and DATABASE_URL were not configured correctly.
12. Fix: Added the PostgreSQL dartabase and configured the database settings.
13. Bug: HTML validation showed errors in some pages.
14. Cause: Some templates had extra closing div tags.
15. Fix: Removed the extra HTML tags and tested the rendered pages again.
16. Bug: The sign up form caused HTML validation warnings.
17. Cause: The output created HTML validation warnings.
18. Fix: Used Crispy Forms to display the form correctly.
19. Bug: Some navigation bar CSS was not working correctly.
20. Cuase: Some CSS class names did not match the  class names used in template.
21. Fix: Corrected the navbar class names in the CSS file.
22. Bug: Pyhton validation showed formatting problems.
23. Cause: Some Python files had spacing and formatting issues.
24. Fix: the reported issues and checked the code again with Flake8
25. Bug; Pyhton Error happened in the urls.py file.
26. Cause: I wrote django.conf instead of django.conf.
27. Fix: i corrected the import from Django.cnof to django.conf.

# Balsamiq WireFrame design

![courses.page](images/Screenshot%202026-09-19%20at%2014.55.20.png)

![courses.mobile](images/Screenshot%202026-09-19%20at%2014.57.21.png)

![courses.tablet](images/Screenshot%202026-09-19%20at%2014.59.09.png)

![coursein.lap](images/Screenshot%202026-09-19%20at%2015.11.52.png)

![coursein.tablet](images/Screenshot%202026-09-19%20at%2015.12.57.png)

![coursein.mobile](images/Screenshot%202026-09-19%20at%2015.14.06.png)

![check.mobile](images/Screenshot%202026-09-19%20at%2016.51.14.png)

![checkin.mob](images/Screenshot%202026-09-19%20at%2016.52.21.png)

![checkin.tab](images/Screenshot%202026-09-19%20at%2017.26.57.png)

![checkin.mb](images/Screenshot%202026-09-19%20at%2017.27.50.png)

![checkin.mb](images/Screenshot%202026-09-19%20at%2017.37.50.png)

![checkin.mb](images/Screenshot%202026-09-19%20at%2017.38.56.png)

![checkin.mb](images/Screenshot%202026-09-19%20at%2017.39.27.png)

![checkin.mb](images/Screenshot%202026-09-19%20at%2017.42.31.png)

![checkin.mb](images/Screenshot%202026-09-19%20at%2017.43.02.png)

![checkin.mb](images/Screenshot%202026-09-19%20at%2017.44.31.png)

![checkin.mb](images/Screenshot%202026-09-19%20at%2017.47.02.png)

![checkin.mb](images/Screenshot%202026-09-19%20at%2017.47.53.png)

![checkin.mb](images/Screenshot%202026-09-19%20at%2017.48.31.png)



# Validators
- HTML Validator
This is validation of all HTML pages and section

WebCode Courses Page
![html](images2/Screenshot%202026-09-19%20at%2020.11.47.png)

WebCode Course Page
![html](images2/Screenshot%202026-09-19%20at%2020.12.20.png)

WebCode Login Page
![html](images2/Screenshot%202026-09-19%20at%2020.12.52.png)

WebCode SignUp Page
![html](images2/Screenshot%202026-09-19%20at%2020.13.18.png)

WebCode MyCourses Page
![html](images2/Screenshot%202026-09-19%20at%2020.13.53.png)

WebCode Checkout Page
![html](images2/Screenshot%202026-09-19%20at%2020.14.24.png)

WebCode Add Review Page 
![html](images2/Screenshot%202026-09-19%20at%2020.14.53.png)

WebCode Edit Review Page
![html](images2/Screenshot%202026-09-19%20at%2020.15.44.png)

WebCode Edit Course Page (only Admin)
![html](images2/Screenshot%202026-09-19%20at%2020.17.13.png)

WebCode Add Course Page (only Admin) 
![html](images2/Screenshot%202026-09-19%20at%2020.17.53.png)

WebCode Delete Course Page (only Admin) 
![html](images2/Screenshot%202026-09-19%20at%2020.18.32.png)

WebCode Logout Page 
![html](images2/Screenshot%202026-09-19%20at%2020.19.04.png)

WebCode Payment Success Page
![html](images2/Screenshot%202026-09-21%20at%2012.17.39.png)

WebCode Confrim Email Page
![html](images2/Screenshot%202026-09-01%20at%2019.50.43.png)

WebCode Account Email confrim Page
![html](images2/Screenshot%202026-09-01%20at%2019.51.17.png)


- CSS Validator
![CSS](images2/Screenshot%202026-09-19%20at%2020.20.42.png)

- JavaScript Validator

webcode.js
![JavaScript](images2/Screenshot%202026-09-19%20at%2020.24.46.png)

checkout.js
![JavaScript2](images2/Screenshot%202026-09-19%20at%2020.25.24.png)

- Python Validator
1. checkout/payment_webhook.py
![python1](images2/Screenshot%202026-09-19%20at%2020.01.02.png)

2. checkout/urls.py
![python2](images2/Screenshot%202026-09-19%20at%2020.02.22.png)

3. checkout/views.py
![python3](images2/Screenshot%202026-09-19%20at%2020.02.57.png)

4. checkout/webhook_views.py
![python4](images2/Screenshot%202026-09-19%20at%2020.03.28.png)

5. courses/admin.py
![python5](images2/Screenshot%202026-09-19%20at%2020.03.59.png)

6. courses/forms.py
![python6](images2/Screenshot%202026-09-19%20at%2020.04.37.png)

7. courses/models.py
![python7](images2/Screenshot%202026-09-19%20at%2020.05.12.png)

8. courses/urls.py
![python8](images2/Screenshot%202026-09-19%20at%2020.05.42.png)

9. courses/views.py
![python9](images2/Screenshot%202026-09-19%20at%2020.06.14.png)

10. webcode_center/urls.py
![python10](images2/Screenshot%202026-09-19%20at%2020.09.46.png)

- Flake8 python
![pythonflake8](images2/Screenshot%202026-09-21%20at%2013.35.45.png)


# Browser and device test

1. Desktop (≥1024px) : Chrome and Safari
2. Tablet  (768px): Chrome and Safari
3. Mobile (≤375px): Chrome and Safari

# LightHouse (chrome devtools)
1. Best Practices: 100
2. Performance: 91
3. SEO: 90
4. Accessibilty: 89

# Credits 
- Content and Design Inspiration
The goal of Webcode Center was to create a simple website 
for users who want to learn web development.

The main idea was to allow users to view coding courses,
buy a course and access the lessons after payment.
The website also allows users to add reviews and ratings for courses.

- Interface and Layout 
I followed a simple design approach to make the website easy to use and navigate.
Black and gold were used as the main colours of the website. Bootstrap used to help create the layout and make the website responsive on the desktop, tablet and mobile devices.
The course cards buttond navigation bar and forms were kept simple and easy to understand.
- Libraries and tools

1. Django 
I used Django as the main framework to build rhe application, handle routing models views and users authentication.

2. Django AllAuth
I used Django AllAuth for users registration, login, logout and email verification.

3. Stripe
I used Stripe to process course payments.

5. Bootstrap
I used Bootstrap to help create the layout and make the website responsive.

6. GoogleFonts
I used GoogleFonts to apply the Orbitron font to the website.

7. PostgreeSQL
I used PostgreSQL as a realtional database for the project

8. GitHub 
I used GitHub for verison control and store the project repository.

9. Heroku 
I used Heroku to deploy and host the project online.

about AI I used AI (copilot) during the development of this project 
strictily as a learning tool to help understand. all the code in the project was written modifided and fully understood by me. No AI generated code was copied directly into the project. AI was only consulted in specific 
situations to help identify issues i remain fully responsible for the project's structure, code decisions and final implementation.
