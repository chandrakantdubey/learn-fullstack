# Loki

**Role:** Awareness | **Layer:** Logs

## Mental model
Loki stores log streams indexed primarily by labels rather than indexing every log field like a traditional search engine.

## Learn
- labels and streams
- LogQL
- ingestion and retention
- parsing at query time
- correlation with traces

## Production
Keep labels low-cardinality, avoid embedding request-specific IDs into labels, control retention and correlate logs with trace IDs for efficient debugging.
