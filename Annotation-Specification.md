# Aspect-level sentiment annotation specification for peer review comments
## 1 Labeling Rules
For the convenience of labeling, this paper first divides the target text into sentences and import them into Excel. The aspect words are extracted by using a series of rules such as the relationship between aspect words and opinion words (reference to the DP algorithm), and the (opinion words, syntactic relationship, aspect words, review sentences) are stored in the excel file in rows. Combined with the relationship between the opinion words and aspect words, the sentiment tendency of the aspects in each review sentence is manually judged, and the sentiment polarity is marked. 
The annotations are divided into four categories: positive sentiment, negative sentiment, neutral sentiment, and fuzzy sentiment. The specific labeling method is shown in Table 1.  
| Sentiment classification of aspects | Definition | Label |
|---------------:|--------------------|------|
|negative sentiment aspect| The sentiment contained in this aspect is derogatory | -1 |
|neutral sentiment aspect| The sentiment contained in this aspect is neutral | 0  |
|positive sentiment aspect| The sentiment contained in the aspect is positive | 1  |
|fuzzy sentiment aspect| Unable to determine the sentiment of the aspect or determine that the word is not an aspect | 2 |

## 2 Annotation Process
During the labeling process, the sentiments of the aspect words contained in each review sentence are labeled by three annotators who are all NLP researchers and are familiar with the peer review process in the corresponding field. In the annotation framework of this paper, each annotator must annotate the corresponding sentiment for the aspect existing in the review sentence, and the sentiment polarity corresponding to each aspect is one of four labels-"positive", "negative", "neutral" and "fuzzy". First, this paper uses the Stanfordnlp tool to analyze the review sentences syntactically, and uses the syntactic relationship between opinion words and aspect words to extract the aspect words existing in the review sentence. The syntactic relationship includes amod, subj, conj, etc. Then, the annotation corpus is divided into three parts. For each annotation corpus, two people independently complete the corresponding sentiment annotation of the aspects in the review sentence, and test the consistency of the annotation results of the two people. For the data with inconsistent annotation, the third person makes the final annotation. Finally, perform statistics on the marked data.   

## 3 Judgment Standard
### 3.1 Judgment standard of neutral aspect sentiment
(1) A direct description of the dissertation work, where the modifiers involved are neutral.<br/>
Eg: This manuscript describes a study on the development of a conditional Por-KO, liver humanized chimeric mouse ***model*** and its ***utility*** for the assessment of drug metabolism.<br/>
(Note: Words marked in italics in the review sentence are attributes, as the same below.)<br/>
(2) The modifiers for aspects are neutral, such as other, many, some, proposed, etc. <br/>
Eg: The authors mention that mutations in pik3ca and tp53 are mutually exclusive in breast cancer; but did not indicate if the analysis showed significance in other/all cancer ***types***. <br/>
(3) Aspects that are only mentioned but not evaluated in the sentence are neutral, and the components of the sentence are neutral<br/>
Eg: The paper presents a novel method for answering “How many …?” questions in the VQA ***datasets***.<br/>
### 3.2 Judgment standard of negative aspect sentiment  
(1) Words that modify aspect words are derogatory words<br/>
Eg: The ***re-referencing*** of previous figures out of order is confusing.<br/>
(2) The aspect word itself has negative emotions<br/>
Eg: There is a ***typo*** in expression 2 in fig s1.<br/> 
(3) Sentences containing questions from reviewers about some aspect of the paper<br/>
Eg: Do you mean the ***average*** of all hindcast available at that year?<br/> 
(4) Reviewers use derogatory terms to express their mood or emotions about an aspect <br/>  Eg: I'm not sure what these discrepancy values ***mean***. <br/> 
(5) Include the reviewer's expectations regarding a particular aspect of the paper, suggesting improvements for enhancement, or pointing out the issues the author hasn't addressed yet. If the reviewer believes that addressing these issues would lead to improvement, the sentiment associated with this aspect is considered negative.<br/>
Eg: The inset ***plot*** would benefit greatly from more explanation.<br/>
Eg: These are interesting areas for future research, so i hope you can address my concerns above so that ***discussion*** on these important issues can progress.<br/> 
(6) Suggestions or requirements for a certain aspect of the article, such as: the sentence contains the words need, must, please, etc.<br/> 
Eg: There are several ***aspects*** of the current manuscript that were distracting and need to be addressed.<br/> 
(7) There is a transition word before the clause where the aspect is located, and the previous sentence is a positive emotion<br/>
Eg: The ***model*** is well described but the authors should pay more effort to walk through the reader of the dynamic development how the ***structure*** evolves towards the presented ***outcome***.<br/>
### 3.3 Judgment standard of positive aspect sentiment
(1) Sentiment words that modify aspects are positive words<br/> 
Eg：I agree with the authors that this is a very important new set of vapour ***observations*** that allows new ***insights*** into key isotopic processes.<br/>
(2) The aspect word itself has a positive sentiment<br/>
Eg：There are several ***findings*** and ***contributions*** reported in this paper.<br/>
(3) Reviewers use compliments when expressing their mood or emotions about aspects<br/>
Eg：I very much like the ***data***, the ***observations*** and i am sure that the authors are right that microbial processes result in the effects they observe.<br/>
(4) The sentence contains praise words to describe the paper, such as cost reduction, time reduction and performance improvement, etc.<br/>
Eg：They achieved interesting ***performance*** levels (projected retention time, 1 y; programming voltage range, within +/- 10 v; max strain, 2.8%; etc).  <br/>
(5) Sentences contain different emotional information, which are positive emotions as a whole; that is, positive emotions are included after transition sentences<br/>
Eg：My personal sense is that this is still mostly a strawman argument, but i appreciate the ***effort*** that the authors have done to address it.<br/> 
(6) Although some emotional words do not appear together with aspect words, they also express emotional expressions for a certain aspect (syntax relation xcomp). The common ones are:<br/> 
clearly：‘clarity’ +1;<br/>
well described：‘description’ +1<br/>
well written: writing+1<br/>    
easy read ,easy follow, easy understand：‘readability’+1;<br/>
### 3.4 Judgment Standard of Modal Verb
(1) Can / could: expressing the ability to accomplish something, positive sentiment<br/>
(2) Can / could +Comparatives: negative sentiment<br/>
(3) Could / would +Positive sentiment words: negative sentiment<br/>
(4) Could / would +Comparatives: negative sentiment<br/>
(5) Should / shall +Comparatives: negative sentiment<br/>
(6) Should / shall +Negative words: negative sentiment<br/>
(7) Should + do / suggest / please / encourage / recommend: negative sentiment<br/>
(8) Need+Negative words: positive sentiment；Need+Comparatives: negative sentiment；Need：negative sentiment<br/>
(9) Must+Negative words: positive sentiment；Must+Comparatives: negative sentiment<br/>
(10) Have to / had better / better +Negative words: positive sentiment<br/>
## 4 Notes
(1) First, determine whether the sentence has an sentimental tendency, and then mark the sentimental polarity of the aspect，If cannot judge the sentimental tendency of the aspect, refer to the overall sentiment of the sentence.<br/>
(2) Only judge the sentiment polarity of the aspect words extracted from the table.<br/>
(3) If there is no transition word, then the emotional polarity of the aspects involved before and after the sentence is the same.<br/>
(4) Entity and aspect sentimental tendencies are the same, such as “the result of experiment” where the polarity of "result" and "experiment" is the same.<br/>
(5) If an aspect in a sentence is repeatedly extracted, if the aspect appears multiple times in the sentence and there is no obvious sentimental transition word, the polarity is the same; if it appears only once, the second mark is 2.<br/>
(6) For the advantages or disadvantages mentioned in the sentence, the sentimental polarity of the aspect of the sentence corresponds to it.<br/>
