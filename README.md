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
We release our self-annotated dataset in *Dataset* directory, it contains 5,063 review sentences with annotated aspect sentiments, including 1,498 positive, 1,652 neutral and 1,913 negative aspect sentiment sentences respectively.

<li><b>nc_train_data.xlsx</b>: Traning dataset for classification of aspect sentiment in review comment, it contains 4,050 records from <b>Annotated_Corpus.xlsx</b>.
<li><b>nc_test_data.xlsx</b>: Testing dataset for classification of aspect sentiment in review comment, it contains 1,013 records from <b>Annotated_Corpus.xlsx</b>.

<b>Each line of Annotated_Corpus includes: </b>
<li>URL: URL of peer review file in Nature Communications.    
<li>DOI: DOI of Paper in Nature Communications.
<li>Sentiment calculated by machine rules: Sentiments in review sentences calculated by machine rules.
<li>Opinion words: Opinion words in sentences of review comments.
<li>Syntactic relationship: Syntactic relations between aspect words and opinion words in review sentences.
<li>Label polarity: '1' (positive), '-1' (negative), '0' (neutral)
<li>Aspect words: Aspect words in sentences of review comments.
<li>Review sentence: Peer review sentence text
