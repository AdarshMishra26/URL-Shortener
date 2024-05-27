
# URL Shortener

This is a simple URL shortener web application built with Flask and MongoDB.

## Introduction

This application allows users to shorten long URLs into shorter, more manageable links. It's useful for sharing URLs in a concise manner, especially on platforms with character limits like Twitter.

## Features

- Shorten long URLs into unique short URLs.
- Redirect users from short URLs to their original long URLs.
- Uses MongoDB to store URL mappings.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Flask
- pymongo
- MongoDB Atlas account (or local MongoDB server)

## Installation

1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/yourusername/URL-Shortener.git
    ```

2. Install dependencies using pip.

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Sign up for a MongoDB Atlas account or set up a local MongoDB server.

2. Replace the MongoDB connection string in `app.py` with your own.

    ```python
    # Replace the connection string below with your MongoDB connection string
    client = MongoClient('mongodb+srv://username:password@your-cluster-url/')
    ```

## Usage

1. Run the Flask application.

    ```bash
    python app.py
    ```

2. Access the application in your web browser at `http://localhost:5000`.

3. Enter a long URL in the provided form and submit to get a shortened URL.

4. Use the generated short URL to redirect to the original long URL.

## Notes

- The application uses a randomly generated string of characters as the short URL key.
- Duplicate short URLs are avoided by checking if the generated key already exists in the database.

## Disclaimer

- This application is intended for educational purposes only.
- Ensure proper security measures are implemented before deploying to production environments.
