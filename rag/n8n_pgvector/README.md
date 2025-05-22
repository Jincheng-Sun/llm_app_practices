# RAG with n8n and pgvector

This project demonstrates how to deploy a local, end-to-end RAG (Retrieval-Augmented Generation) workflow using n8n for orchestration and a PostgreSQL database with pgvector for vector storage. It is designed for on-premise or offline GenAI experimentation and prototyping.

---

## Prerequisites

- Docker and Docker Compose installed on your local machine.
- An embedding model and a chat model from any of the providers (in this example, Azure AI Foundry).

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Jincheng-Sun/llm_app_practices.git
cd llm_app_practices/rag/n8n_pgvector
```

This example's folder structure is:
```
n8n_pgvector/
├── documents/
├── compose.yaml
├── RAG_example_with_N8N.json
├── README.md
└── postgres/
    └── schema.sql
```

### 2. Configure environment and credentials
Replace credentials (e.g., Azure and PostgreSQL) as needed in your .env file or directly in docker-compose.yml.

Make sure you mount a local folder (in this example, `documents` folder) to the n8n container for RAG documentation 
ingestion.

### 3. Start the application stack
```bash
docker compose up --build
```
This will start:

n8n on http://localhost:5678

PostgreSQL with pgvector support on port `5432`

### 4. Set up the n8n workflow
Visit http://localhost:5678 and create a local user account (data is stored locally only).

Import the sample workflow from current directory: `RAG_example_with_N8N.json`.

Configure the following credentials inside n8n:
- Azure OpenAI Account credentials (for embedding and chat models)
- PostgreSQL credentials (for vector store)

Default vector store and chunking configuration are as follows:
- Chunk size: 1024
- Overlap: 256
- Database name: example_db
- Table name: embeddings
- Table columns: id (UUID), text (TEXT), metadata (JSONB), vector (VECTOR[1536])

### 5. Test the ingestion workflow
Place your .pdf files in the `documents` folder (volume mounted in the container) and run the workflow to ingest.

### 6. Test retrieval workflow
Modify the default prompt template or Q&A logic as needed, connect the Chat Trigger node to either Q&A workflow.

Click `Open Chat` in the UI to start testing the workflow with some questions.

## Notes
When you customize this application, make sure the N8N workflow changes align with the table schema and compose file

## References
[Part 1: Setup with PostgreSQL and pgvector](https://dev.to/yukaty/setting-up-postgresql-with-pgvector-using-docker-hcl)

[PGVector Vector Store node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector/)

[This RAG AI Agent with n8n + Supabase is the Real Deal](https://youtu.be/PEI_ePNNfJQ?si=Pi9lG0L9vAtWPXUG)