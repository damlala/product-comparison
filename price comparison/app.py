from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'secretkey'  # Change this in production

DATABASE = os.path.join(os.path.dirname(__file__), 'users.db')

# Mock product data
mock_data = {
    "iphone 14": {
        "Amazon": 999,
        "BestBuy": 950,
        "Hepsiburada": 980,
        "eBay": 910
    },
    "samsung s23": {
        "Amazon": 890,
        "BestBuy": 920,
        "Target": 870,
        "eBay": 899
    }
}

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' not in session:
        return redirect(url_for('login'))

    product = ""
    prices = {}
    best_price_store = ""

    if request.method == "POST":
        product = request.form["product"].lower()
        prices = mock_data.get(product, {})

        if prices:
            best_price_store = min(prices, key=prices.get)

    return render_template("index.html", prices=prices, product=product, best=best_price_store, username=session['username'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password)).fetchone()
        conn.close()

        if user:
            session['username'] = user['username']
            return redirect(url_for('index'))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        try:
            conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return render_template("register.html", error="Username already taken")

        conn.close()
        return redirect(url_for('login'))
    return render_template("register.html")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
