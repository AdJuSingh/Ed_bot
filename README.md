# Chatbot_for _personalized_learning
Rasa Chatbot for Personalized Learning in AI and ML

Description:
This project is a conversational AI chatbot built using Rasa Open Source, designed to support learners in the fields of Artificial Intelligence and Machine Learning. By understanding user intents and providing relevant responses, the chatbot serves as a helpful guide for learners by answering questions, offering detailed explanations, and navigating various AI/ML concepts. For more information, visit the GitHub repository.

Features
Custom-Trained Model: Leverages machine learning to interpret user intents and extract relevant entities.
Domain-Specific Expertise: Tailored specifically for the AI and machine learning educational domain.
Multi-Intent Handling: Processes and responds to complex, multi-layered queries effectively.
Integration-Ready: Easily integrates with platforms like Telegram, Slack, or custom websites.
Installation
Prerequisites:

Python 3.8 or later
Rasa Open Source
Virtual environment (recommended)
Steps:

Clone the Repository:
bash
Copy
Edit
git clone https://github.com/Thrinadh-13/Chatbot_for_Personalized_Learning  
Navigate to the Project Directory:
bash
Copy
Edit
cd PythonProject2  
Create and Activate a Virtual Environment:
For Linux/Mac:
bash
Copy
Edit
python -m venv .venv  
source .venv/bin/activate  
For Windows:
bash
Copy
Edit
python -m venv .venv  
.venv\Scripts\activate  
Install Dependencies:
bash
Copy
Edit
pip install -r requirements.txt  
Training the Model
Modify the nlu.yml, stories.yml, and domain.yml files as needed.
Train the model:
bash
Copy
Edit
rasa train  
The trained model will be saved in the models/ directory.
Running the Chatbot
On the Command Line:
Run the chatbot interactively:

bash
Copy
Edit
rasa shell  
As a Server:
Run the chatbot as a server:

bash
Copy
Edit
rasa run  
Files and Directories
data/: Contains training data for intents and stories.
domain.yml: Defines intents, entities, actions, and responses.
models/: Stores trained models.
actions/: Holds custom action scripts.
config.yml: Specifies the pipeline and policies used for the chatbot.
Future Enhancements
Add support for new features and functionalities.
Enhance training data for improved intent classification and entity recognition.
Expand integration with external APIs for advanced interactions.
License
Provide the appropriate license information for the project.

Contributors
Lead Developer: Aditi Jai Singh








