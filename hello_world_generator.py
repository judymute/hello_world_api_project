from openai import OpenAI

client = OpenAI(api_key='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')

# Replace "your_api_key_here" with your actual OpenAI API key

response = client.chat.completions.create(model="gpt-3.5-turbo",  # Adjust the model if necessary
messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Generate a creative 'Hello World' message in the style of a friendly greeting."}
])

print(response.choices[0].message.content)
