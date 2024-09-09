import openai

# Set your OpenAI API key
openai.api_key = "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"

class Speechtonotes:
    def __init__(self):
        openai.api_key = "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"
        pass  

    def getNotes(self, Lecture):
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an assistant that converts text into bulleted notes."},
                {"role": "user", "content": f"Please convert the following lecture into bulleted notes:\n\n{Lecture}"}
            ],
            max_tokens=500,
            temperature=0.7
        )
        notes = response['choices'][0]['message']['content']
        return notes
        
        
