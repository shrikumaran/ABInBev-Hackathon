# ABInBev-Hackathon

>An end to end deep learning approach to extract information from shipping records

Top 8 out of 150+ teams

## 1. Introduction

We present an end to end deep learning approach to detect valuable information from shipping records and extract it. We first detect all the words in an image using PyTesseract. We then cluster together words which make sense as a heading using DBSCAN clustering for ex: . Then these clustered words are passed to a LayoutLM model. Which predicts whether each cluster is a question or answer. If it's a question then it's considered as a field. The corresponding question and answer is then exported as a json file.
We then use a TableNet model to extract the regions where tables are present, the contents in the detected regions are exported to the json file.


