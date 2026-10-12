#variables
temperature=0.7 #float 
max_tokens=1024 #int
is_streaming=False #boolen
content_box=None #None

#type hints
model_name: str = "gemini-2.0-flash"
temperature: float = 0.7 #float 
max_tokens: int= 1024 #int
is_streaming: bool = False #boolen
content_box: str|None = None #None
print(type(model_name))

#Strings: immutable | string formating
name="LLM"
score=99.5
#old version
print("hello %s"%name)
print("Score %.1f"%score)

#f-string (py 3.6+)
print(f"hello{name}")
print(f"ScoreP:{score:.1f}")

#expessions inside f-string
word_limit=200
print(f"{'over'if word_limit>150 else'under'}limit")
data={"topic":"RAG"}
print(f"topic:{data['topic']}")

#format specifiers
pi=3.14159265
print(f"{pi:.2f}")

#debugging using =
temp = 0.7
print(f"{temp=}")

#multi line f- string formatting 
user_input = "What is Langchain?"
context_text = "Langchain is a framework for building LLM apps"
system_prompt=f""" you are a helpful AI Tutor.
context provided:{context_text}
student question:{user_input}
Instructions:
-Answer based only on the context above
-if the answer is not in the context ,say "I ont know"
-keep your answers under 3 sentences""".strip()
print(system_prompt)

#lists: ordered, mutable, heterogeneous sequence of elements
# In Gen AI:Chat history, chunks of retrieved documents, embeddings, etc. are stored in lists
# Token sequence 
chat_history:list[dict]=[
    {"role":"user","content":"what is an LLM?"},
    {"role":"assistant","content":"A LLM is a neural network model trained on large amounts of text."}, 
]
# Acess
first_msg = chat_history[0]
print(first_msg) 
print(chat_history[-1]['content']) # last element in the list

#modify
chat_history.append({"role":"user","content":"what is RAG?"})
print(chat_history)
chat_history.pop(0)
print(chat_history)

#iterate
for msg in chat_history:
    print(f"{msg['role'].upper()}:{msg['content']}")

# list of document chunks
chunks:list[str]=[
    "RAG stands for retrieval Augmented Generation",
    "it combines a retriever with generator",
]
#filter chunks based on length
valid_chunks=[c for c in chunks if len(c.split())>=6]
print(valid_chunks)
