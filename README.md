# CovQuA: A COVID Question Answering Machine
## By Group 7: Aislin Black, Akanksha Agnihotri, Divyangana Pandey, Raksha Ramkumar, Ashish Jeldi

### Abstract 

We implemented 3 Question Answering Models (GPT, BERT, and ALBERT) to answer questions about COVID-19. GPT had precision 0.871, recall 0.889, and f1 score 0.878. BERT had precision 0.908, recall 0.875, and f1 score 0.891. ABERT had precision 0.908, recall 0.872, and f1 score 0.890. 
This project is interesting because it helps developers evaluate which model to build when they wish to select a model depending upon the dataset they have and the usage of the question and answering in terms of speed and accuracy of the model to best serve the people it is designed for. 

### The code

In the folders GPT, Bert, and Albert, you will find the jupyter notebooks and instructions for running each of the three models. The data folder contains the data we used to test our models


### Testing
The test_application.py is a user-friendly application that lets the user observe how well (or poorly) the three models perform. It prompts the user to enter the context and the question as the inputs and generates the outputs.

(Note that the test_application.py was run on Google Collab and hence has few initial pip install statements. These can be ignored if you already have all the required libraries installed in your system)
