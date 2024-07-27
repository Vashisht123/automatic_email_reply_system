# RAG Pipeline Documentation

## Overview

The Retrieval-Augmented Generation (RAG) pipeline enhances automated responses by combining retrieval-based and generative techniques.

## Components

1. **Retrieval System**:
   - **Data Source**: SQL database containing equipment details.
   - **Query Mechanism**: SQL queries to fetch relevant data based on email content.

2. **Augmented Generation**:
   - **Generation Model**: Use a pre-trained language model to generate responses.
   - **Integration**: Combine retrieved information with generated text to form comprehensive replies.

## Operations

1. **Receive Email**: Incoming emails are categorized and processed.
2. **Retrieval**: Relevant information is fetched from the database.
3. **Generation**: The response is generated using a language model.
4. **Send Response**: The final response is sent back to the sender.

## Tools Used

- **LangChain**: For orchestrating the RAG pipeline.
- **Groq API**: For fast inference with language models.
