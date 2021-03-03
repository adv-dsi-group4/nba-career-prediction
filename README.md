JumpShot NBA Career Predictor
==============================
This notebook contains an ML model that predicts if a rookie NBA player will last at least 5 years in the league.

Installation instructions
-------------------------
1. Extract all files contained in Group4.zip to ../Group4/

2. Pull the Dockerfile using the following cmd:
	docker pull ajduncanson/nba-modelling

3. Run the Dockerfile using the following cmd:
	Win10 Powershell: docker run  -dit --rm --name nba -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "${pwd}:/home/jovyan/work" -v "${pwd}/src:/home/jovyan/work/src" ajduncanson/nba-modelling
	Mac: docker run -dit --rm --name nba -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "$PWD"/..:/home/jovyan/work ajduncanson/nba-modelling
4. Run the cmd:
	$ docker logs nba --tail 50

5. Find the token URLs (Look for the log lines:  "Copy and paste one of these URLs:
        http://6a69557908cf:8888/lab?token=72d37dec5d9477192d40ee6a91b4d9e4f9213e4826c88b37
     or http://127.0.0.1:8888/lab?token=72d37dec5d9477192d40ee6a91b4d9e4f9213e4826c88b37 ")

6. Copy and paste the URL into a web browser to launch the Jupyter Notebook

7. Navigate to ../notebooks/ and open '_Group4-Final_Notebook1-Logistic_Regression.ipynb' for our chosen model

8. Run the notebook commands to obtain the results

9. Open '_Group4-Final_Notebook2-Random_Forest_and_PD_plots.ipynb' for our supporting PD plots and Random Forest model

10. Run the notebook commands to obtain the results

