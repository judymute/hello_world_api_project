from flask import Flask, render_template
from openai import OpenAI

app = Flask(__name__)

# Replace "your_api_key_here" with your actual OpenAI API key
client = OpenAI(api_key='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')

@app.route('/')
def hello_world():
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Generate a creative 'Hello World' message in the style of a friendly greeting. Keep your sentence to 1 sentence. You must include the phrase: 'Hello World' in your message."}
    ])
    message = response.choices[0].message.content
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
