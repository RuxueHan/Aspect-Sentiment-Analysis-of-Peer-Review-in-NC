# Aspect-Based Sentiment Evolution and its Correlation with Review Rounds in Multi-Round Peer Reviews: A Deep Learning Approach

## Overview
<b> Data and source Code for the paper "Aspect-Based Sentiment Evolution and its Correlation with Review Rounds in Multi-Round Peer Reviews: A Deep Learning Approach".</b>

This paper aims to investigate the distribution and changes of sentiment on the fine-grained aspect level throughout multiple rounds of review, as well as explore the correlation between aspect sentiments in the review comments and the number of review rounds.
The main research contents include three parts: 
* The construction of aspect sentiment annotation corpus of review comments.
* The automatic classification of aspect sentiment.
* The analysis of aspect sentiment distribution changes across multiple review rounds along with their correlation with the number of review rounds.

### Directory structure
<pre>
Aspect-Sentiment-Analysis-of-Peer-Review-in-NC                Root directory
├── Code                                                      Source code folder
│   ├── Round_Split.py                                        Source code for review rounds segmentation
│   ├── Review_Sentence .py                                   Source code for extracting sentences containing comments on aspects
│   ├── Model_Input_Data_Preprocessing.ipynb                  Source code for preprocessing of data input to the model
│   └── Aspect_Sentiment_Score.py                             Source code for calculating aspect sentiment score
├── Dataset                                                   Dataset folder
│   ├── Review_Aspect_Clusters.xlsx                           Aspect clusters of peer review comments
│   ├── Annotated_Corpus.xlsx                                 Our annotated dataset
│   ├── nc_train_data.xlsx                                    Training dataset
│   └── nc_test_data.xlsx                                     Testing dataset
├── Annotation-Specification.md                               Aspect-level sentiment annotation specification for peer review comments
└── README.md
</pre>
