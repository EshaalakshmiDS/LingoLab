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
"Yesterday I go to the park and see many peoples. There was a lot of childs playing. I meet with my friend and we talks about our exams. Then we goes to a restaurant and order two sandwichs. It was fun day.",
"The weather is too cold today. I am thinking to wear a warm jacket. I did a big mistake in my test, and my teacher become very angry. She told me to do the correction. I am having a headache now, so I will eat a medicine.",
"Its a beautifull day outside but I cant go becuz I have alot of work. My friend’s are going to the beach, and theyre having fun. I should of finished my work earlier. But, I didnt.",
"Today morning I woke up late, so I rushed for my office. In the way, I met my colleague. He suggested me to not worry and take it easy. But I was still hurry. When I reached office, my boss told that why I am late? I didn’t gave proper answer.",
"I was so tired, so I took a sleep early."
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


