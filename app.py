from flask import Flask
import os 
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

password = os.getenv('SECRET_PASSWORD')

@app.route('/')
def home():
    return f"The password from .env is: {password}"

if __name__ == "__main__":
    app.run(debug=False)
