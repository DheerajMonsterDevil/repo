import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

from langchain.chains import SequentialChain

from langchain.memory import ConversationBufferMemory

import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

st.title('Celeb search results')
input_txt=st.text_input("Search the topic u want")

first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about {name}"
)

person_memory = ConversationBufferMemory(input_key='name',memory_key='chat_history')

llm=OpenAI(temperature=0.8)
chain=LLMChain(llm=llm, prompt=first_input_prompt,verbose=True,output_key='person')

# second_input_prompt = PromptTemplate(
#     input_variables=['person'],
#     template="when was {person} born"
# )
# chain2=LLMChain(llm=llm,prompt=second_input_prompt,verbose=True,output_key='dob')

# parent_chain=SequentialChain(chains=[chain,chain2],input_variables=['name'],output_variables=['person','dob'],verbose=True)

if input_txt:
    st.write(chain.run({'name':input_txt}))