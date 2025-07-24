from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="Enter your API key"
)

command = '''

'''

completion = client.chat.completions.create(
    model = "deepseek/deepseek-chat-v3-0324:free",
    messages=[
        {"role": "system", "content": "You are a person named Faiz who speaks hindi as well english. He is from India and is a coder. you analyze chat history and respond like Faiz"},
        {"role": "user", "content": command}
    ]
)

print(completion.choices[0].message.content)


