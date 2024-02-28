from openai import OpenAI

def send_to_gpt3(variable, model="gpt-3.5-turbo-0613", temperature=0.7, max_tokens=150):
   
    file_path = 'key.txt'  # Replace 'your_file.txt' with the path to your file

    # Open the file and read its contents
    with open(file_path, 'r') as file:
        api_key = file.read()

    # Now, file_content contains the text from the file

    # Set the api key for the OpenAI object
    OpenAI.api_key = api_key

    # Create the client using the OpenAI object
    client = OpenAI(api_key=api_key)

    prompt = variable

    # Use the client to generate a response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a python coding assistant."},
            {"role": "user", "content": prompt},
        ]
        )
    content = response.choices[0].message.content
    return content
    

