import os
from openai import OpenAI



def send_to_gpt3(variable, model="gpt-3.5-turbo-0613", temperature=0.7, max_tokens=150):
   
    OpenAI.api_key = os.getenv('OPENAI_API_KEY')
    print(f"API Key: {api_key}")

    client = OpenAI()

    prompt = variable


    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a python coding assistant."},
            {"role": "user", "content": prompt},
        ]
        )
    
send_to_gpt3("This is a test")