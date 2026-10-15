# first API call wrt gemini 
import google.generativeai as genai
import os
from dotenv import load_dotenv

#Load thr api key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

#Create a model instance with config
# 2.0,2.5,3.5 ,2.0 is out dated so we use 3.8 and if it is not supported then we reduce
model=genai.GenerativeModel(model_name="gemini-3.8-flash",generation_config={"temperature":0.7,"max_output_tokens":150},system_instruction="You"\"are a concise AI tutor."\"Answe in 2-3 sentences.",)
# call the model
result = model.generate_context("What is vector database?")
print(result.text)
print(f"Tokens:{result.usage_metadata.total_token_count}")
