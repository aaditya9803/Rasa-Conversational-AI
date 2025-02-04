# Conversational AI chatbot to Diagnose Stroke

https://github.com/aaditya9803/Rasa-Conversational-AI


# Installation

Versions:
- Python 3.10.16
- rasa 3.6.20


# Data

The Stroke Prediction Dataset was accessed from following source:

https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset


# Usage

After downloading the project files in a project folder, do the following steps:

1. Download Anaconda Navigator
    https://www.anaconda.com/download/success
2. Launch Anaconda Prompt
3. Create Conda Environment
    `conda create --name rasa-bot python==3.10.16`
4. Activate Conda Environment
    `conda activate rasa-bot`
5. Go to the Project folder
    `cd project-folder`
6. Install all the required packages in requirements.txt
    `pip install -r requirements.txt`
7. Train the Rasa model
    `rasa train`
8. Start Rasa action server
    `rasa run actions -p 8080`
9. Start Rasa Shell
    `rasa shell`
