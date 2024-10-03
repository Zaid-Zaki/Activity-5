import mysql.connector
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'user': 'root',     # Replace with your MySQL username
    'password': '12345678',  # Replace with your MySQL password
    'host': 'localhost',
    'database': 'd'    # Replace with your database name
}

# Function to connect to MySQL
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

# Route to handle the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Backend API to handle data from the frontend
@app.route('/process', methods=['POST'])
def process():
    data = request.json
    number = data['number']
    
    # Process the data (e.g., multiply by 2)
    result = number * 2
    
    # Save the number to the MySQL database
    save_to_db(number)

    return jsonify({'result': result})

# Function to save the number to the MySQL database
def save_to_db(number):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO entries (number) VALUES (%s)', (number,))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True)
