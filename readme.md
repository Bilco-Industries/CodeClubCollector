# Welcome to the code club data logger 
This code base runs a small web server using [flask](https://flask.palletsprojects.com/en/stable/)

There are some fairly advanced concepts in here so don't worry if you don't understand all of it, I've tried to add as many comments as possible to try to guide you through how this all works. 

## Technologies used 
### Python
This is the main programming language in this project it is used to connect to the database, build web pages to display to the user and accept data from your pico which it then shows on a web page.

### HTML (Hyper Text Markup Language)
This is the standard method of building web pages, all web browsers read these files and turn them into what you see on your screen.

### CSS (Cascading Style Sheets)
CSS is used to modify how HTML is displayed to a user, it tells the browser everthing about how it should format the HTML, for example where to position things on the page and what colour they should be.

### JS (JavasScript)
JS is what makes web pages interactive, every time you click a button on a website there is some JavaScript that runs to do whatever that button is supposed to do. 

### Sql (Structured Query Language) and SQlite
SQlite is a database which we use to store all of the data that is displayed to the user on the site, SQL is the language that is used to communicate with the database. You can think of SQlite as a glorified spreadsheet, in fact you can use a modified version of SQL to do fancy things inside a spreadsheet. 

## Naming conventions

This can be a controversial topic amongst programmers and may hours have been ~~wasted~~
*well spent* discussing nameing conventions but to summarise:

Different programming languages have different (usually) unnoficial standards for how you should name things which have been followed in this project.

You don't have to follow these standards in your own code and functionally they don't make a difference so for now pick one you like and stick to it. They are useful if you're working in a team becuase it makes the code easier to read if everyone is naming their varaibles in the same way. 

### Python
Traditionally python used snake_case for it's variable and function names.

You may notice some places where things like SHOUTING_SNAKE_CASE has been used. This means that a variable is "constant" and should not be changed while the program is running, python doesn't prevent you from changing these variables so naming them in this way makes it clear to other programmers (and yourself) that you should not change that variable in your code.

You may also see some functions and variables prefixed with _. This means that a function or variable is "private", that means that it should not be used outside of the file it definied in. You can see examples of this in [database.py](database/sqlite.py) the _connect function should not be called outside of that file, whereas get_data_for_user is intended to be called by other functions.  

### JavaScript

JavaScript uses a different naming convention called camelCase where each word after the first one in a variable or function name starts with a capital letter
