# Problem Statement
We were able to provide personilzed learning in the past through personal iteraction of instructor with student. They understood the level of the student and provided necessary steps/ material for student to advance before they move into next topic. But currently becuase of advancement of technology and change of teaching methods where we are moving from personalized instructor based approach to mere tests, it is becoming increasingly difficult to provide the well needed attention and care to studnets. 

Riid's want to bring the personalized approach to the new and online learning world by suggesting students steps to take before they move on to next topic.

# Objective
Create algorithms for "Knowledge Tracing," the modeling of student knowledge over time. The goal is to accurately predict how students will perform on future interactions. You will pair your machine learning skills using Riiid’s EdNet data.

# Link
https://www.kaggle.com/c/riiid-test-answer-prediction/overview


# Evaluation & Timeline
Submissions are evaluated on Area under ROC curve or accuracy of the model. 
* Jan-7 2021 Final deadline

# Code Requirements
n order for the "Submit to Competition" button to be active after a commit, the following conditions must be met:

* CPU Notebook <= 9 hours run-time
* GPU Notebook <= 9 hours run-time
* TPU Notebook <= 3 hours run-time
* Freely & publicly available external data is allowed, including pre-trained models
Submission file must be named submission.csv

# Datasets
5 Datasets are provided
* Train.csv: 
    * Data to train our model
    * Contains multiple users data overtime capturing their multiple interactions on lectures and questions.
    * It also captures time spent in answering previous questions and whether he looked into explanationf of previous questions or not. 
    * task container id for batching of questions. Relationship with bundle id is notknown.
* Lecures.csv(Map on content_id when content type =1)
    * Data containig different lectures and their
    * Contains multiple hierarchy
    * type of -> part -> tags
    * Part : The relevant section of the TOEIC test.
    * Tags can be further used for clustering
* Questions.csv (Map on content_id when content type =0)
    * Data contains question id , bundle id , part , tags and correct answer.
    * Tags can be furthered clustered.
    * Which questions belong to which lectures is missing .

---
# Preliminary Observation
1. The impact of user starting at different period of time is not covered. What it means is that an user will probably cover more on weekends than weekdays or vice versa.
2. The relationship between questions and lectures is not provided.
3. Some lectures might be related and there might be progression involved in lecutres which is again not covered.
4. Estimatoins are to be based on previous question answered for a particular user and some users may not have any data at all for previous interactions or will be new in test set.
5. Users can be active on platform or can be sporodoic and based on that they might have some impact on the performance. 
6. Students generally tend to forget as time passes what is that rate is not provided.


# Key Questions to Answer
1. How to visualize user intraction on time scale and identify events?
2. Relationship between questions and lectures?
3. Relationship between lectures?
    * What lecutres are together?
    * What lectures are mandatory before proceeding to the next one?
4. What is the impact of time on student answering a question wrong? How long does it take a user to forget?




