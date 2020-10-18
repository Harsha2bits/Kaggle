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
# Key Questions to Answer

- [x] checking
- [] click here

[Render this](https://www.google.com)

![Checking](https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MY9K2_VW_34FR+watch-44-stainless-gold-cell-6s_VW_34FR_WF_CO?wid=750&hei=712&trim=1,0&fmt=p-jpg&qlt=80&op_usm=0.5,0.5&.v=1599269261000,1599537309000)

