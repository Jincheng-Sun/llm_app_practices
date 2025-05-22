CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE embeddings (
    id SERIAL PRIMARY KEY,
    metadata JSONB,
    text TEXT,
    embedding vector(1536)
);