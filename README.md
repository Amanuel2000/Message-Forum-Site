# Discussion and Message Forum Site
<img src="image1.JPG">
## Description
- Forums are a powerful way of communication between large number of individuals and it has been used in social media apps and other mass populous communication mediums. 
- Forums nowadays have a problem of being too massive with different sub forums with different topics that it has gotten hard to use especially the famous ones. 

- The final outcome of the project creates a forum site that is specific to a certain topic and there are no groupings that create echo chambers.

- The site tries to help on the mentioned problems by being  useful to communicate openly with different idea people and to have a shared understandable knowledge between the different groups.

- After the completion of the project a functioning forum site with message management, comment management with attached message. Also vote count for message and comment is also added. 

- Messages and comments with the highest relevance and showed more clearly by the use of votes. There is search filter added for users to find what they want. It also has management side for forum manager users to manage the proper interaction between users.

- There is a functionality that can be used by all users to report a message or comment based on their 
opinion if they deem it inappropriate or unreadable or other factors. Because there may be abusers 
or other type of users that can use the system for other purpose that the main goal of the site. So 
form manager users see this reports and use their own judgement to take action
## Scope 
 
- The scope of the project is to develop a web-based messaging forum site that will have a specific topic that users will come for that specific topic and know what kind of information they will find. It will have subtopics of the main topic that will give more specificity for users to find their wants easily

## System Development Methodology
- The development strategy used for the project will be RAD which is agile so its iterative and capable of change. Agile development compared to others is with repeated phases for additional functionality. Additions or changes in requirement or functionality can be handled better through  agile development, because it’s not only one way to develop the project it’s through cycles which doesn’t make it rigid but capable of change

## System Development Tool
- ### Flask:  
it is a web framework, it's a Python module that lets you develop web applications easily. It's has a small and easy-to-extend core: it's a microframework that doesn't include an ORM (Object Relational Manager) or such features. It does have many cool features like url routing, template engine.
- ### Jinja: 
it is a web template engine for the Python programming language. It was created by Armin Ronacher and is licensed under a BSD License. Jinja is similar to the Django template engine but provides Python-like expressions while ensuring that the templates are evaluated in a sandbox.
- ### Python: 
it is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis. Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn't specialized for any specific problems.
- ### MySQL:
it is a relational database management system (RDBMS) developed by Oracle that is based on structured query language (SQL). A database is a structured collection of data. It may be anything from a simple shopping list to a picture gallery or a place to hold the vast amounts of information in a corporate network.
- ### HTML:
HTML stands for Hyper Text Markup Language. HTML is the standard markup language for creating Web pages. HTML describes the structure of a Web page. HTML consists of a series of elements. HTML elements tell the browser how to display the content.
- ### CSS:
CSS stands for Cascading Style Sheets. CSS describes how HTML elements are to be displayed on screen, paper, or in other media. CSS saves a lot of work. It can control the layout of multiple web pages all at once. External stylesheets are stored in CSS files.

- ### JavaScript:
JavaScript is a lightweight programming language that web developers commonly use to create more dynamic interactions when developing web pages, applications, servers, and or even games. Developers generally use JavaScript alongside HTML and CSS The scripting language works well with CSS in formatting HTML elements

- ### Bootstrap
Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first  front-end web development. It contains CSS and (optionally) JavaScript-based design templates  for typography, forms, buttons, navigation, and other interface components.
- ### Visual Studio Code
 it also commonly referred to as VS Code, is a source-code editor made by Microsoft with the Electron Framework, for Windows, Linux and macOS. Features include support for debugging, syntax highlighting, intelligent code completion, snippets, code refactoring, and embedded Git.

## Business Rules
The system is role-based sort of system. Currently only four roles are used. One is an administrator role next is forum manager and the other is normal user role and the last is non logged in user role.

## Functional Requirements
- User Sign up for new forum users.
- Login functionality.
-  Category and Message page for logged in and non-logged in users.
- Read messages, comments, vote couns for all users.
- Add message for logged in users.
- Edit message for message writer logged in user.
- Add comment for logged in users.
- Edit comment for comment writer logged in user.
- Report message and comments if logged in user found it in-appropriate.
- Vote on message and comment functionality for logged in users can Approve and  Not Approve
- Show vote counts on messages and comments for Approve, Not Approve.
- User management for administrative users.
    - Add User
    - Edit User
    - Delete User
- Category management for administrative users.
    - Add Category
    - Delete Category
- Message Management for forum manager users.
    - Delete Message
    - Delete Comment
- Report Management for forum manager users.
    - Flagged Messages
    - Flagged Comments
## SYSTEM DESIGN
- The Message Forum Site is a web application site that is needed to be accessed with multiple users from different locations at any time. Because of that the system must be networked over internet  to achieve these goals.
From what is gathered in the requirements, the System will have a web server to display the site  and to interact with users. It will also have a database server to store the historical and new data of users

## Proposed Software Architecture
- For the development process and what is currently used is all the frameworks and applications are  stored on a single device making the project a single-tier framework. But if the system is to expand database, front end and back end can be split into three separate devices easily, making it multi-tier framework.  
<img src="software architecture.JPG">

## Security
For security front end validation and server-side validation are user. On front end form validations and auth session is checked when doing work. On server-side user session is checked for permission validation

## Communication
On communication the front end and backend communicate with REST apis. And backend and database communicate with the MySql module installed by pip.

## Presentation Layer
This is what the user will use on its end. And it is developed by the use of python flask for front end 
control and html, css and bootstrap for the look and design of the pages

## Application Layer
This is the part that will control the interactions with the persistent data store and the user’s interaction. Flask and Python, are used for processing the user’s requests and communicating with the database.


## Data Management Layer
This is the place where all the needed historical and current data are stored. Registered user,  messages, comments and other data are all stored on the database. And this project uses MySQL  database. 

In general, the proposed project is designed to be created by these bellow frameworks.
 - Front End: Bootstrap, CSS, HTML5
 -  Back End:  python flask 
 - Database:  MySql DB 8.0
The frameworks mentioned are all open source and free to use and are updated regularly so they are good platforms to pick

## Implementation
- The Project is a web application with persistent data and user interface. So, to accomplish that these frameworks are used
• Windows Operating System
• Falsk Framework
• Python
• MySQL Database

## Mapping Models to Code
### Mapping Associations
    - Unidirectional one-to-one associations
    - Bidirectional one-to-one associations
    - One-to-many associations
The Comments are mapped to Comments Table. Comment Votes are mapped to CommentVotes Table. Messages are mapped to Messages Table. Message Votes are mapped to MessageVotes Table. User are mapped to Users Table. Message Views are mapped to MessageViews Table.

## Screen Images
### Home Page
<img src="static/images/Home Page.JPG">

### Login
<img src="static/images/login.JPG">

### Sign Up
<img src="static/images/Sign up.JPG">

### Dashboard
<img src="static/images/Dashboard.JPG">

### All Messages
<img src="static/images/all-posts.JPG">


### Single Post
<img src="static/images/Single-post.JPG">

### Add Messages
<img src="static/images/Add-Post.JPG">

### Add User
<img src="static/images/add-user.JPG">

### About
<img src="static/images/About.JPG">


### Admin Area
<img src="static/images/admin area.JPG">

 
# Authors :pen:

[Amanuel Fenta Dejen](https://amanuel2000.github.io/)

[Linkedin](https://www.linkedin.com/in/amanuel-fenta-a4683a215/)

[Twitter](https://twitter.com/amanuel_Fenta2/)


[Elias Dewa Ahmed](https://amanuel2000.github.io/)

[Linkedin](https://www.linkedin.com/in/amanuel-fenta-a4683a215/)

[Twitter](https://twitter.com/amanuel_Fenta2/)


[Anania Baharu Tadesse](https://amanuel2000.github.io/)

[Linkedin](https://www.linkedin.com/in/amanuel-fenta-a4683a215/)

[Twitter](https://twitter.com/amanuel_Fenta2/)
