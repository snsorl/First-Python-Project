"""
Tiny Python backend using Flask + SQLite.
Run:  pip install flask flask-cors
      python app.py
Then open http://localhost:5000
"""
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3, os

app = Flask(__name__, static_folder=".")
CORS(app)

DB = "data.db"

# --- DB setup ---------------------------------------------------------
def db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL
            )
        """)
init_db()

# --- Flask:  API endpoints for backEnd
@app.get("/api/messages")
def list_messages():
    rows = db().execute("SELECT id, text FROM messages ORDER BY id DESC").fetchall()
    return jsonify([dict(r) for r in rows])

@app.post("/api/messages")
def add_message():
    text = (request.json or {}).get("text", "").strip()
    if not text:
        return jsonify({"error": "text required"}), 400
    with db() as conn:
        cur = conn.execute("INSERT INTO messages (text) VALUES (?)", (text,))
        return jsonify({"id": cur.lastrowid, "text": text}), 201

# --- Serve the frontend HTML files ------------------------------------
@app.get("/")
def home():
    return send_from_directory(".", "index.html")

@app.get("/<path:path>")
def static_files(path):
    return send_from_directory(".", path)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
