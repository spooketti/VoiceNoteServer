import openai
import speech_recognition as sr
import os
from dotenv import load_dotenv
class Speechtonotes:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv('GPTAPI_KEY')

        self.text="default text"
        pass  
    
    
    def speechToText(self, filename):
        recognizer = sr.Recognizer()
        with sr.AudioFile(filename) as audio_file:
            audio = recognizer.record(audio_file)
            text = recognizer.recognize_google(audio)
        file=open("test.txt","w")
        file.write(text)
        file.close()
    def update_text(self):
        filereader=open("test.txt","r")
        self.text=filereader.read()
        filereader.close()
        
    def speechToTextWithNotes(self, filename):
        recognizer = sr.Recognizer()
        with sr.AudioFile(filename) as audio_file:
            audio = recognizer.record(audio_file)
            text = recognizer.recognize_google(audio)
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that converts text into bulleted notes."},
                {"role": "user", "content": f"Please convert the following lecture into very concise bulleted notes:\n\n{text}"}
            ],
            max_tokens=500,
            temperature=0.7
        )
        notes = response.choices[0].message.content
        return notes


    def getNotes(self):
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that converts text into bulleted notes."},
                {"role": "user", "content": f"Please convert the following lecture into very concise bulleted notes:\n\n{self.text}"}
            ],
            max_tokens=500,
            temperature=0.7
        )
        notes = response.choices[0].message.content
        return notes
        
        
