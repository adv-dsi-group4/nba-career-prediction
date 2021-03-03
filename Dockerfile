FROM jupyter/scipy-notebook:5cb007f03275

RUN conda install -c conda-forge imbalanced-learn

RUN conda install xgboost

RUN conda install boto3

RUN conda install s3fs

RUN conda install lime

RUN conda install hyperopt

RUN conda install graphviz

ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/work"

RUN echo "export PYTHONPATH=/home/jovyan/work" >> ~/.bashrc

WORKDIR /home/jovyan/work