# Aspect-Based Sentiment Evolution and its Correlation with Review Rounds in Multi-Round Peer Reviews: A Deep Learning Approach

## Overview
<b> Data and source Code for the paper "Aspect-Based Sentiment Evolution and its Correlation with Review Rounds in Multi-Round Peer Reviews: A Deep Learning Approach".</b>

This paper aims to investigate the distribution and changes of sentiment on the fine-grained aspect level throughout multiple rounds of review, as well as explore the correlation between aspect sentiments in the review comments and the number of review rounds.
The main research contents include three parts: 
* The construction of aspect sentiment annotation corpus of review comments.
* The automatic classification of aspect sentiment.
* The analysis of aspect sentiment distribution changes across multiple review rounds along with their correlation with the number of review rounds.

## Directory structure
<pre>
Aspect-Sentiment-Analysis-of-Peer-Review-in-NC            Root directory
├── Code                                                  Source code folder
│   ├── Round_Split.py                                    Source code for review rounds segmentation
│   ├── Review_Sentence.py                                Source code for extracting sentences containing comments on aspects
│   ├── Model_Input_Data_Preprocessing.ipynb              Source code for preprocessing of data input to the model
│   └── Aspect_Sentiment_Score.py                         Source code for calculating aspect sentiment score
├── Dataset                                               Dataset folder
│   ├── Review_Aspect_Clusters.xlsx                       Aspect clusters of peer review comments
│   ├── Annotated_Corpus.xlsx                             Our annotated dataset
│   ├── nc_train_data.xlsx                                Training dataset
│   └── nc_test_data.xlsx                                 Testing dataset
├── Annotation-Specification.md                           Aspect-level sentiment annotation specification for peer review comments
└── README.md
</pre>

## Dataset Discription
- <code>./Dataset/Review_Aspect_Clusters.xlsx</code> Aspect Clusters of Peer Review Comments, it contains 370 review aspect words categorized into 11 clusters.
- <code>./Dataset/Annotated_Corpus.xlsx</code> Our self-annotated dataset, it contains 5,063 review sentences with annotated aspect sentiments, including 1,498 positive, 1,652 neutral and 1,913 negative aspect sentiment sentences respectively. <br/>
  <b>Each line of Annotated_Corpus includes:</b> <br/>
  URL: URL of peer review file in Nature Communications.<br/>
  DOI: DOI of Paper in Nature Communications.<br/>
  Sentiment calculated by machine rules: Sentiments in review sentences calculated by machine rules.<br/>
  Opinion words: Opinion words in sentences of review comments.<br/>
  Syntactic relationship: Syntactic relations between aspect words and opinion words in review sentences.<br/>
  Label polarity: '1' (positive), '-1' (negative), '0' (neutral)<br/>
  Aspect words: Aspect words in sentences of review comments.<br/>
  Review sentence: Peer review sentence text<br/>
- <code>./Dataset/nc_train_data.xlsx</code> Traning dataset for classification of aspect sentiment in review comment, it contains 4,050 records from Annotated_Corpus.xlsx.
- <code>./Dataset/nc_test_data.xlsx</code> Testing dataset for classification of aspect sentiment in review comment, it contains 1,013 records from Annotated_Corpus.xlsx.

## Quick Start
- <code>python ./Code/Round_Split.py</code> Execute this to segment and save peer review files in Nature Communications based on the review rounds.
- <code>python ./Code/Review_Sentence.py</code> Execute this to extract review sentences containing comments on review aspects.
- Automatic classification of aspect sentiment in review comments:<br/>
We train 12 deep learning-based aspect sentiment classification models, among these LSTM, TD-LSTM, TC-LSTM, ATAE-LSTM, MEMNET, IAN, AOA, BERT-SPC, AEN-BERT, LCF-BERT models are constructed using the open source code released by songyouwei et al.[[ABSA-PyTorch](https://github.com/songyouwei/ABSA-PyTorch)], LCFS-BERT model is constructed using the open source code released by Phan et al.[[LCFS-BERT](https://github.com/HieuPhan33/LCFS-BERT)], aspect sentiment classification model based on FT-RoBERTa is constructed using the open source code released by Dai et al.[[RoBERTaABSA](https://github.com/ROGERDJQ/RoBERTaABSA)]. Then,we evaluate this models on our annotated dataset, the performance-optimal model LCF-BERT-CDM is applied for the automatic classification of unannotated aspect sentiment corpora.
- <code>python ./Code/Aspect_Sentiment_Score.py</code> Execute this to calculate aspect sentiment score of review comments.

## Citation
Please cite the following paper if you use this code and dataset in your work.
    
> Aspect-Based Sentiment Evolution and its Correlation with Review Rounds in Multi-Round Peer Reviews: A Deep Learning Approach. ***Journal of Informetrics***, 2024, (submitted). [[doi]]() [[Dataset & Source Code]](https://github.com/RuxueHan/Aspect-Sentiment-Analysis-of-Peer-Review-in-NC)

