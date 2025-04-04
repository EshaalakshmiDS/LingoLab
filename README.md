# LingoLab - Chat your way to better English

## Overview
The English Language Learning Chatbot is an interactive application designed to assist users in improving their English grammar skills. By leveraging advanced language processing capabilities, the chatbot provides real-time feedback on grammatical errors, offers explanations for corrections, and generates personalized learning plans based on user input. 

This project is an English Language Learning Chatbot that provides users with two functionalities:
1. To use the built-in dataset, enter 1. This will load the necessary data and you'll be prompted to enter your desired model name.
2. To input your own sentences for analysis, enter 2. You can then type in a sentence and provide the model name.
Choose either 1 or 2 and follow the prompts for a tailored chatbot experience.

## Key Features
- **Grammar Checking**: 
  - Users can input sentences or paragraphs, and the chatbot analyzes the text for grammatical errors.
  - Corrections are provided along with explanations to help users understand their mistakes.

- **Feedback Mechanism**:
  - The chatbot gives overall feedback on the user's grammar, highlighting strengths and areas for improvement.
  - A score out of 10 is provided to quantify the user's grammar proficiency.

- **Confidence Scoring**:
  - The chatbot assesses its confidence in the corrections made, providing a percentage score based on the quality of input, model limitations, and consistency of corrections.

- **Learning Plans**:
  - Based on the user's performance, the chatbot generates a customized learning plan that outlines specific areas for improvement and recommended resources.

- **Synonyms and Rephrasing**:
  - The chatbot suggests synonyms, antonyms, and better word choices to enhance vocabulary.
  - It can also rephrase sentences to improve clarity and tone.

- **User-Friendly Interface**:
  - The chatbot operates through a simple command-line interface, allowing users to choose between using a default dataset or entering their own sentences for analysis.

## Requirements
- Python 3.x
- `dotenv` library for environment variable management
- `groq` library for interacting with the language model

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:
   ```bash
   pip install python-dotenv groq
   ```

3. Create a `.env` file in the project root and add your Groq API key:
   ```plaintext
   GROQ_API_KEY=your_api_key_here
   ```

## Usage
1. Run the chatbot:
   ```bash
   python main.py
   ```

2. Follow the prompts to either use the default dataset or enter your own sentences for analysis.

## Default Dataset
The default dataset includes the following sentences with different english issues:
- "Yesterday I go to the park and see many peoples. There was a lot of childs playing. I meet with my friend and we talks about our exams. Then we goes to a restaurant and order two sandwichs. It was fun day."
- "The weather is too cold today. I am thinking to wear a warm jacket. I did a big mistake in my test, and my teacher become very angry. She told me to do the correction. I am having a headache now, so I will eat a medicine."
- "Its a beautifull day outside but I cant go becuz I have alot of work. My friend’s are going to the beach, and theyre having fun. I should of finished my work earlier. But, I didnt."
- "Today morning I woke up late, so I rushed for my office. In the way, I met my colleague. He suggested me to not worry and take it easy. But I was still hurry. When I reached office, my boss told that why I am late? I didn’t gave proper answer."
- "I was so tired, so I took a sleep early."

## Contributing
The ultimate objective is to develop a powerful, AI-driven full-stack application!
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to the developers of the Groq API for providing the language model.
- Special thanks to the contributors of the libraries used in this project.
