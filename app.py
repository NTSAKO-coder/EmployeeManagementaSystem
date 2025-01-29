from flask import Flask, render_template, request, redirect, url_for
from database import get_db_connection

app = Flask(__name__) # type: ignore

# Home Route
@app.route('/')
def index():
    return render_template('index.html') # type: ignore

# Add Employee Route
@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST': # type: ignore
        first_name = request.form['first_name'] # type: ignore
        last_name = request.form['last_name'] # type: ignore
        email = request.form['email'] # type: ignore
        phone = request.form['phone'] # type: ignore
        department = request.form['department'] # type: ignore

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO employees (first_name, last_name, email, phone, department)'
            'VALUES (%s, %s, %s, %s, %s)',
            (first_name, last_name, email, phone, department)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('view_employees'))
    return render_template('add_employee.html')

# View Employees Route
@app.route('/view')
def view_employees():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM employees;')
    employees = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('view_employees.html', employees=employees)

# Run the App
if __name__ == '__main__':
    app.run(debug=True)
