import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import pandas as pd
import os
import re
import json

# Defining hyperparameters

VOCAB_SIZE = 8192
MAX_SAMPLES = 50000
BUFFER_SIZE = 20000
MAX_LENGTH = 40
EMBED_DIM = 256
LATENT_DIM = 512
NUM_HEADS = 8
BATCH_SIZE = 64

def load_squad_data():
  data = {}
  with open("../data/SquAd-dev-set.json") as file:
    js = json.load(file)
    data = js["data"]
  return pd.DataFrame(data)



data = load_squad_data()
print(data)
title = data.loc[:, "title"]
paragraphs = data.loc[:, "paragraphs"]
print(paragraphs[0][0])

def preprocess_text(sentence):
  sentence = tf.strings.lower(sentence)
  # Adding a space between the punctuation and the last word to allow better tokenization
  sentence = tf.strings.regex_replace(sentence, r"([?.!,])", r" \1 ")
  # Replacing multiple continuous spaces with a single space
  sentence = tf.strings.regex_replace(sentence, r"\s\s+", " ")
  # Replacing non english words with spaces
  sentence = tf.strings.regex_replace(sentence, r"[^a-z?.!,]+", " ")
  sentence = tf.strings.strip(sentence)
  sentence = tf.strings.join(["[start]", sentence, "[end]"], separator=" ")
  return sentence






