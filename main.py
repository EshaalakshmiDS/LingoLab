from dotenv import load_dotenv
from groq import Client
import os
from prompts.prompt import system_message

load_dotenv()

groq_api_key = os.environ.get("groq_api_key")
client = Client(api_key=groq_api_key)

def check_grammar(model_name, human_message):
    """
    This function checks the grammar of the user's sentence using the specified model.

    Parameters:
    model_name (str): The name of the model to use for grammar checking.
    human_message (str): The user's sentence to check for grammar errors.
    """
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_message,
                },
                {
                    "role": "user",
                    "content": human_message,
                }
            ],
            model=model_name,
        )

        print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")
        print(chat_completion.choices[0].message.content)
        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")
    except Exception as e:
        print(f"An error occurred: {e}")

# Default dataset
default_dataset = [
    "I has a apple.",
    "She go to the store yesterday.",
    "He don't like the movie.",
    "They was playing soccer.",
    "The cat sleep on the mat."
]

choice = input("Enter '1' to use the default dataset or '2' to enter your own sentence: ")
if choice == '1':
    for sentence in default_dataset:
        model_name = input("\nEnter the model you want to use [e.g., llama3-8b-8192, mixtral-8x7b-32768, gemma2-9b-it, deepseek-r1-distill-llama-70b]: \n")
        human_message = sentence.strip()
        check_grammar(model_name, human_message)
else:
    while True:
        model_name = input("\nEnter the model you want to use [e.g., llama3-8b-8192, mixtral-8x7b-32768, gemma2-9b-it, deepseek-r1-distill-llama-70b]: \n")
        user_input = input("\nEnter your sentence (or type 'exit' to quit): \n")
        if user_input.lower() == 'exit':
            break

        human_message = user_input
        check_grammar(model_name, human_message)


