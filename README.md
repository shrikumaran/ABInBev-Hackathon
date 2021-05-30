# ABInBev-Hackathon

>An end to end deep learning approach to extract information from shipping records

Top 8 finalists out of 150+ teams

## Introduction

We present an end to end deep learning approach to detect valuable information from shipping records and extract it. We first detect all the words in an image using PyTesseract. We then cluster together words which make sense as a heading using DBSCAN clustering. Then these clustered words are passed to a LayoutLM model. Which predicts whether each cluster is a question or answer. If it's a question then it's considered as a field. The corresponding question and answer is then exported as a json file.
We then use a TableNet model to extract the regions where tables are present, the contents in the detected regions are exported to the json file.

## Running it

Download the marmot dataset from this drive link:
https://drive.google.com/drive/folders/1X_8WLSGwMpm4w3K3vVR-n9lNcyX3pj5t?usp=sharing

You can also help yourself with the pretrained weights I have in the above drive link. 
