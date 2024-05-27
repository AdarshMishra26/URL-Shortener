import os
from dotenv import load_dotenv
from flask import Flask, request, redirect, jsonify, render_template
from pymongo import MongoClient
import string
import random
from datetime import datetime

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Use your MongoDB connection string from environment variable
mongo_uri = os.getenv("MONGODB_URI")
if not mongo_uri:
    raise ValueError("MongoDB URI is not set in the environment variables.")

try:
    client = MongoClient(mongo_uri)
    db = client['url_shortener']  # Database name from your connection string
    urls = db['urls']  # Collection name
    print("Connected to MongoDB successfully!")
except Exception as e:
    print("Error connecting to MongoDB:", e)

def generate_short_url(urls_collection):
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    if urls_collection.find_one({'short_url': short_url}):
        return generate_short_url(urls_collection)
    return short_url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.json['original_url']
    short_url = generate_short_url(urls)
    urls.insert_one({
        'original_url': original_url,
        'short_url': short_url,
        'created_at': datetime.utcnow()
    })
    return jsonify(short_url=short_url)

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
    url = urls.find_one({'short_url': short_url})
    if url:
        return redirect(url['original_url'])
    return jsonify(error='URL not found'), 404

if __name__ == '__main__':
    app.run(debug=True)
