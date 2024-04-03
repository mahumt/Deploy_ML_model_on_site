# Model deployment on AWS  with CI/CD pipeline using Github Actions 

## Setting up project 
1- Set up repo (use command line to navigate to folder created for this project) <br>
    - new environment use `py -3.10 -m virtualenv deploy_ex_venv` <br>
    - activate env `.\deploy_ex_venv\Scripts\activate` <br>
    - initalize repository `git init` <br>
    - `setup.py` - Create a setup file. This helps us install everything needs for the application when we use our requirements command  <br>
    - create src folder and `__init__.py` empty file in <br>
    - create `requirements.txt` <br>
    - Use  `py -3.10 -m pip install -r requirements.txt` - this will install packages + all setup modules in a folder called  deploy_models.egg-info <br>
<br>
All of credentials, exceptions will be added in src folder as we go along

## Structure of project
A: In `src` folder we will be adding multiple folders and filw
1. A `components` folder with several files <br>
    i. `__init__.py` <br>
    ii. Data Ingestion: `data_ingestion.py` <br>
    iii. Data Transformation `data_transformation.py` <br>
    iv. Model trainer `model_trainer.py` <br>
2. `pipeline` folder with files: <br>
    i. `__init__.py`
    ii. Training pipeline `train_pipeline.py` <br>
    iii. Prediction pipeline `predit_pipeline.py`<br>
3. File `exception.py`
4. `logger.py`
5. `utils.py`

Model evaluation
Mdoel deployment-