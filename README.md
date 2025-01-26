Neupane, Aaditya, 22209307

Stroke Predictor

https://mygit.th-deg.de/an02307/stroke-predictor

https://mygit.th-deg.de/an02307/stroke-predictor/-/wikis/home

# Project Description


Stroke Predictor is a web app that help user predict their chance of having an stroke with the provided information. Students / interested person can learn about Stroke with the help of visulaization. Developers can learn how the data was processed and trained for Stroke Predictor.


# Installation


Versions:

- Python 3.10.16
- streamlit 1.41.1   
- rasa 3.6.20

## How to start

Start rasa actions: `rasa run actions -p 8080`

Start rasa server: `rasa run --enable-api -p 8000`

Start the web app service: `streamlit run main.py`

Open the app in the browser with URL: `http://localhost:8501`

# Data

The Stroke Prediction Dataset was accessed from following source:

https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

Further details about the data are also described in the Wiki.


# Basic Usage

After downloading the project files in a project folder, do the following steps:

1. Download Anaconda Navigator
    https://www.anaconda.com/download/success
2. Launch Anaconda Prompt
3. Create Conda Environment
    `conda create --name stroke-predictor python==3.10.16`
4. Activate Conda Environment
    `conda activate stroke-predictor`
5. Go to the Project folder
    `cd project-folder`
6. Install all the required packages in requirements.txt
    `pip install -r requirements.txt`
7. Train the Rasa model
    `rasa train`
8. Start Rasa action server
    `rasa run action -p 8080`
9. Start Rasa server
    `rasa run --enable-api -p 8000`
10. Start Streamlit Server
    `streamlit run main.py`


Then call the streamlit URL 'localhost:8051', in the browser.

# Implementation of the Requests

This chapter describes how the requests described in the file 'material/sas-ws-24-25-recommendation-requests-en.pdf' (chapter Part2 Requests) are implemented.

1. The pages are in the pages folder of the streamlit project

2. See Wiki (link above)

3. Wiki chapter user persona

4. Wiki chapter use cases

5.-7. The files are stored in the project root directory. The `venv` are not part of the repo. There is a corresponding line in the `.gitignore` file.

8. See data section of this README

9. Data is loaded in the main.py

10. see pages/01_Data_*.py files

11 - 13. See data chapter in the Wiki

14. see file pages/Data_augmentation.py and description in the Wiki.

15. Input widgets are mainly in 05_Model_training.py

16. Scikit-Learn Linear regression and Lasso are used, see 04_Algorithm_selection.py

17. See 'right-fit' chapter in Wiki

18. See 'system persona' chapter in Wiki

19. See 'sample dialogs' chapter in Wiki

20. See 'dialog flow' chapter in Wiki

21. rasa implementation with files:

domain.yml, data/nlu.yml, data/stories.yml, actions/actions.py

22. tbd. The screencast can be created within the browser using the menu item 'Record a screencast' in the Streamlit menu.

# Work done

All work by Aaditya Neupane.