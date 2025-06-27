# COVID-19 Question Answering with Retrieval-Augmented Generation (RAG)

This project implements a Retrieval-Augmented Generation (RAG) system using LangChain and OpenAI's GPT models to answer questions about the COVID-19 pandemic in the United States. The system retrieves relevant content from a Wikipedia page and uses a language model to generate grounded, context-aware answers.

## Project Objective

The goal of this project is to demonstrate how retrieval-based architectures can enhance the accuracy and relevance of large language models when responding to user queries. Specifically, this system:

- Loads content from a Wikipedia page
- Splits the text into chunks and stores embeddings in a vector store
- Uses a retrieval mechanism to provide context to the language model
- Answers natural language questions based only on retrieved information

## Data Source

The project uses the following Wikipedia article:
- [COVID-19 pandemic in the United States](https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_United_States)

## Technologies Used

- Python
- LangChain
- OpenAI GPT-3.5-Turbo and GPT-4
- Chroma vector store
- WikipediaLoader from LangChain
- Jupyter Notebook for development and experimentation