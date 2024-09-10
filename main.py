from flask import Flask, request, jsonify, make_response, Response
from threading import Thread
from init import app
from init import cors
import time
from Speechtonotes import Speechtonotes
speechNoteClass=Speechtonotes()
from io import BytesIO
from pydub import AudioSegment

@app.route('/')
def home():
    return "VoiceNote Server"


@app.route("/recieveAudio/",methods=["POST"])
def recieveAudio():
    audioFile = request.files.get("why")

    # Convert the in-memory bytes to a format readable by pydub
    # audio = AudioSegment.from_file(audioFile, format='wav')  # Adjust format if needed
    return speechNoteClass.speechToTextWithNotes(audioFile)


@app.before_request
def before_request():
    # Check if the request came from a specific origin
    allowed_origin = request.headers.get('Origin')
    if allowed_origin in ['http://localhost:4100', 'http://172.27.233.236:3000', 'https://spooketti.github.io']:
        cors._origins = allowed_origin

def run():
  app.run(host='0.0.0.0',port=8086)



run()