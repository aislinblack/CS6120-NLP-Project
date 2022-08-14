GPT Impementation on CovQuA 


This section contains the code and the predicted output data to run and evaluate the GPT model for COVID Question Answering.

We did make a Dialogue Answering GPT model to first test the model and  understand in depth how GPT model gets trained over a data set using the open ai libraries. 

Using this concept we applied it over the Covid dataset in the main program gpt.ipynb (run the avove files prefereably on Google Collab or equivalent online environment for added computational power)

This gives us the idea of the perplexity of the GPT model , so that we can decide the correct usage of the GPT in comparison with Albert and Bert model.

______.json and _______bert.json have been derived from the Covid-QA-more-focused.json. It contains the question and the expected answer (ground truth) for the Covid-QA dataset
______________.json is the stored predictions of the GPT model

All the evaluation metrics are calculated by comparing answers and predictions 
