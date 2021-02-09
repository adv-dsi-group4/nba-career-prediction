FROM jupyter/scipy-notebook:0ce64578df46

RUN conda install xgboost

RUN conda install boto3

RUN conda install s3fs

RUN conda install lime

RUN conda install hyperopt

RUN conda install graphviz

ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/work"

RUN echo "export PYTHONPATH=/home/jovyan/work" >> ~/.bashrc

WORKDIR /home/jovyan/work