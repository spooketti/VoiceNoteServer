import openai
import speech_recognition as sr


class Speechtonotes:
    def __init__(self):
        openai.api_key = "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"
        self.text="default text"
        pass  
    
    
    def speechToText(self, filename):
        recognizer = sr.Recognizer()
        with sr.AudioFile(filename) as audio_file:
            audio = recognizer.record(audio_file)
            text = recognizer.recognize_google(audio)
        file=open("Lecture.txt","w")
        file.write(text)
        file.close()
    def update_text(self):
        filereader=open("Lecture.txt","r")
        self.text=filereader.read()
        filereader.close()


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
        
        
