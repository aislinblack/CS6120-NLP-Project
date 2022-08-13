
### BERT Implementation of CovQA

This section contains the code and the predicted output data to run and evaluate the BERT model for COVID Question Answering.

- The nlp_BERT.ipynb is the notebook containing the code. run this notebook (prefereably on Google Collab or equivalent online environment for added computational power)
- questions_bert.json and answers_bert.json have been derived from the Covid-QA-more-focused.json. It contains the question and the expected answer (ground truth) for the Covid-QA dataset
- predictions_bert.json is the stored predictions of the BERT model
- All the evaluation metrics are calculated by comparing the answers_bert.json and the predictions_bert.json
