# Model deployment on cloud  with CI/CD pipeline 
This exercise aims to look at end to end machine learning and deep learning. This includes setting up the project, download data, transforming it and then training models on it and evluating them and then using a CI/CD pipeline deploying it on cloud

Problem Statements that we are trying to solve: This project understands how the student's performance (test scores) is affected by other variables such as Gender, Ethnicity, Parental level of education, Lunch and Test preparation course.

Dataset Source [Kaggle: Students performance in exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977) <br>
The data consists of 8 column and 1000 rows.

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
A: In `src` folder we will be adding multiple folders and files <br>
0. `__init__.py` to make src a package <br>
1. A `components` folder with several files <br>
    i. `__init__.py` <br>
    ii. Data Ingestion: `data_ingestion.py` <br>
    iii. Data Transformation `data_transformation.py` <br>
    iv. Model trainer `model_trainer.py` <br>
2. `pipeline` folder with files: <br>
    i. `__init__.py`
    ii. Training pipeline `train_pipeline.py` <br>
    iii. Prediction pipeline `predict_pipeline.py`<br>
3. File `exception.py`
4. `logger.py` When this is run in cmd `python src/logger.py` log folder/files are created in our project. These logs will helps us keep track of errors, issues etc.
5. `utils.py`

While testing that the code is working properly use the commmnds like `python -m src.start.go` to select a specific file to run

## How to use notebooks and convert into .py scripts later
For the actual data science part where notebooks are preferred (exploration and experimentation). One can do all of it in notebooks and then export all of that in `.py` script very easily.
For example for the training part. In the notebook's first cell write `#|default_exp model_training` where `#|default_exp` is the function and `model_training` is going to be name of the script file. And in every cell that is needed to be exported to the script add `#|export` <br>
And in the end of the notebook run 
```
from nbdev.export import notebook2script
notebook2script('app.ipynb)
```
Model evaluation
Mdoel deployment-



## To keep pushing it to Github
```
git remote -v 
git remote add origin https://github.com/mahumt/Deploy_ML_model_on_site
git add .
git commit -m "updates to schema and sql files"
git push origin main
```