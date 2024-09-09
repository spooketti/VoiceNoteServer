import openai
import speech_recognition


class Speechtonotes:
    def __init__(self):
        openai.api_key = "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"
        self.text="default text"
        pass  
    
    
    def speechToText():
        listner = speech_recognition.Recognizer()
        audio_file = speech_recognition.AudioFile('example.mp3')
        audio = speech_recognition.record(audio_file)
        text = speech_recognition.recognize_google(audio)
        print(text)
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
        
        
