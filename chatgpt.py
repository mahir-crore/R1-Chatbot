from openai import OpenAI
client= OpenAI( 
api_key="sk-proj-Wx517ehGk2PnwmzCHcDwT3B1bkFJFMj6bYTk9jG1bqZaFTcj", 
) 
command ='''
'''
completion = client.chat.completions.create(
    model="gpt-3.5-turbo", 
    messages=[
        {"role": "system", "content": "You are a person named Manjeet  who speaks Hindi as well as English. He is from India and is a coder. You analyze chat history and respond like Harry."},
        {"role": "user", "content": command}
    ]
)

print(completion.choices[0].message.content)
