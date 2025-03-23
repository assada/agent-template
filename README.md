# AI RAG Agent Template

This template provides a flexible foundation for building RAG (Retrieval-Augmented Generation) agents with support for multiple LLM providers, embeddings, and vector stores.

## Architecture

The template follows a clean hexagonal architecture with clear separation of concerns:

- **Domain**: Core business logic, interfaces, and models
- **Infrastructure**: Implementation details (LLMs, vector stores, embedders)
- **Services**: Orchestration of domain and infrastructure components

## Quick Start

1. Create .env with valid values. `cp .env.dist .env`
2. `docker-compose up --build`.
3. Go to http://localhost:8080/docs
4. Use run_consumer.py to process queued tasks in Redis.
5. Use fill_vector_store.py to embed and store embedings in Chroma.

## Extending the Template

### Creating Custom Agent

1. Create new implementation of `AgentInterface` in the infrastructure layer (check DefaultAgent implementation)
2. You can setup custom vector store, custom embeder and other mandatory things.

### Adding a New LLM Provider

1. Create a new implementation of `LLMInterface` in the infrastructure layer
2. Update the factory method in `LLMService` to include your new provider

### Customizing Prompt Formatting

1. Create a new implementation of `PromptInterface`
2. Initialize the `PromptService` with your custom formatter

## Requirements

- Python 3.11+
- Dependencies listed in requirements.txt

## Todo

* Add example SQL Db quety for context

## License

MIT