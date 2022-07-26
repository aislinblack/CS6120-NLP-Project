from albert_v2 import albert

context = "New Zealand (Māori: Aotearoa) is a sovereign island country in the southwestern Pacific Ocean. It has a total land area of 268,000 square kilometres (103,500 sq mi), and a population of 4.9 million. New Zealand's capital city is Wellington, and its most populous city is Auckland."
questions = ["How many people live in New Zealand?",
             "What's the largest city?"]

# Run method
predictions = albert({'question': 'What organization is the IPCC a part of?', 'context': context})

print("prediction")