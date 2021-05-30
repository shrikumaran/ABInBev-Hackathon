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

LayoutLM is a BERT based model which can classify text into 13 different classes(question, asnwer heading,..). We took our LayoutLM model from huggingfaces and trained it on FUNSD dataset for five epochs. We initially planned on fine tuning it on our own dataset, but we didn't have the time to label the data on our time. So, we just used the model trained on FUNSD, it performed decent enough so we went with it. Run the layoutlm notebook to train your model.

TableNet is a model designed to detect tables and columns on documents. 

Tablenet Paper: https://arxiv.org/abs/2001.01469 Original code: https://github.com/jainammm/TableNet

The orginal code was in tensorflow so I ported it over to PyTorch. 

You can have a look at tablenet notebook to train your model. I first trained 40 epochs on marmot dataset, and then trained it on our dataset for another 150 epochs(yup we overfit it). To label our dataset we first drew bounding boxes using Labelimg, but we needed segmentation masks to train our tablenet model. So, I wrote a script to convert bounding boxes in XML files to segmentation masks. Check out convert_xml2bmp.py to convert your bounding boxes to masks. 

