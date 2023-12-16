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
│   ├── Review_Sentence .py                               Source code for extracting sentences containing comments on aspects
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
  <b>Each line of Annotated_Corpus includes: </b>
  URL: URL of peer review file in Nature Communications.    </b>
  DOI: DOI of Paper in Nature Communications.</b>
  Sentiment calculated by machine rules: Sentiments in review sentences calculated by machine rules.</b>
  Opinion words: Opinion words in sentences of review comments.</b>
  Syntactic relationship: Syntactic relations between aspect words and opinion words in review sentences.</b>
  Label polarity: '1' (positive), '-1' (negative), '0' (neutral)</b>
  Aspect words: Aspect words in sentences of review comments.</b>
  Review sentence: Peer review sentence text</b>
- <code>./Dataset/nc_train_data.xlsx</code> Traning dataset for classification of aspect sentiment in review comment, it contains 4,050 records from <b>Annotated_Corpus.xlsx</b>.
- <code>./Dataset/nc_test_data.xlsx</code> Testing dataset for classification of aspect sentiment in review comment, it contains 1,013 records from <b>Annotated_Corpus.xlsx</b>.


