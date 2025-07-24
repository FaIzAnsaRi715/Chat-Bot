from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

command = '''
[09:53, 7/24/2025] GadHuu❤️: Good morning babe 😘❤️
[12:07, 7/24/2025] FaIz: Good morning 😒
[12:07, 7/24/2025] GadHuu❤️: Sorry babe kal pata nhi kese nind lakgayi
[13:12, 7/24/2025] FaIz: Acha
😒
'''

completion = client.chat.completions.create(
    model = "deepseek/deepseek-chat-v3-0324:free",
    messages=[
        {"role": "system", "content": "You are a person named Faiz who speaks hindi as well english. He is from India and is a coder. you analyze chat history and respond like Faiz"},
        {"role": "user", "content": command}
    ]
)

print(completion.choices[0].message.content)


