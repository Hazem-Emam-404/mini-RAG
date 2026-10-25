# mini-RAG

This is a minimal implementation of Retrieval-Augmented Generation (RAG) using LangChain. It demonstrates how to build a simple RAG system that retrieves relevant documents from a vector store and generates responses based on those documents.

## Requirements

python >= 3.12

## Install Python using miniconda

1) Download and install [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install/) for your operating system.
2) Create a new conda environment and activate it:

```bash
conda create -n mini-rag python=3.12
```
3) Activate the environment:

```bash
conda activate mini-rag
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Setup Environment Variables

```bash
cp .env.example .env
```
set the values in the `.env` file according to your configuration.