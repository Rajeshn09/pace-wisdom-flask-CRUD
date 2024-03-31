Flask CRUD Operations Project Description
#Overview
🚀 This Flask project implements CRUD (Create, Read, Update, Delete) operations for managing student records. It provides a user-friendly interface for performing these operations, allowing users to add, view, edit, and delete student information.

#Features
Add Student: 📝 Users can add new student records by providing their name, age, and grade.
View Students: 👀 The application displays a list of all existing student records, allowing users to view their details.
Edit Student: ✏️ Users can modify the information of existing students, including their name, age, and grade.
Delete Student: 🗑️ The application allows users to delete student records from the database.


#Project Structure
📁 The project follows a typical Flask application structure:

app.py: The main application file containing the Flask routes and logic.
templates/: Directory containing HTML templates for rendering pages.
static/: Directory for storing static files such as CSS and JavaScript.
models.py: Module defining the database models using SQLAlchemy.
database.db: SQLite database file to store student records.


#Installation and Setup
To run the project locally, follow these steps:

Clone the project repository from GitHub.
Install the required dependencies using pip: pip install -r requirements.txt.
Run the Flask application: python app.py.
Access the application in your web browser at http://localhost:5000.


#Technologies Used
Flask: 🌐 Python web framework used for building the application.
SQLite: 📦 Lightweight relational database management system used for storing student records.
SQLAlchemy: 🗃️ Object-relational mapping (ORM) library used for interacting with the database.
HTML/CSS/JavaScript: 🎨 Frontend technologies used for creating the user interface.
