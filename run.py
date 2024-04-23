# Import Libraries 
from producer_app import app
import os


if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0", port=os.getenv('PORT', 5002))