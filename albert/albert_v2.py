
from transformers import (
  AlbertConfig,
  AlbertForQuestionAnswering,
  AlbertTokenizer
)

from transformers import pipeline

modelname = 'ktrapeznikov/albert-xlarge-v2-squad-v2'

model = AlbertForQuestionAnswering.from_pretrained(modelname)
tokenizer = AlbertTokenizer.from_pretrained(modelname)

albert = pipeline('question-answering', model=model, tokenizer=tokenizer)

