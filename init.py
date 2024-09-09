from flask import Flask
from flask_cors import CORS
import os
#from dotenv import load_dotenv
# load_dotenv()

app = Flask("VoiceNoteServer")
cors = CORS(app, supports_credentials=True)
dbURI = 'sqlite:///sqlite.db'
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

# Images storage
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # maximum size of uploaded content
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']  # supported file types
app.config['UPLOAD_FOLDER'] = 'upload/'  # location of user uploaded content