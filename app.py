from flask import Flask, g,render_template,redirect,url_for,request
import sqlite3
import threading
from collections import namedtuple

app = Flask(__name__)
app.config['DATABASE'] = 'student.db'

Student = namedtuple('Student', ['id', 'name', 'age', 'grade'])

@app.route('/')
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    
    students = [Student(*student) for student in students]
    return render_template('index.html', students=students)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        
       
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)', (name, age, grade))
        db.commit()
        
        return redirect(url_for('index'))
    else:
        
        return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM students WHERE id = ?', (id,))
    student = cursor.fetchone()
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        cursor.execute('UPDATE students SET name = ?, age = ?, grade = ? WHERE id = ?', (name, age, grade, id))
        db.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', student=student)

@app.route('/delete/<int:id>', methods=['POST','GET'])
def delete_student(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('index'))
    

if __name__ == '__main__':
    app.run(debug=True)
