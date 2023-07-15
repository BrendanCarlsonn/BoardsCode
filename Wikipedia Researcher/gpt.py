import os
import openai



openai.api_key = "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"



response = openai.Completion.create(
engine="text-curie-001",
prompt="How many moons does saturn have?",
temperature=0.7,
max_tokens=64,
top_p=1,
frequency_penalty=0,
presence_penalty=0
)

print(response.choices)