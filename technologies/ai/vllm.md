# vLLM

**Role:** Primary | **Layer:** LLM inference

## Mental model
vLLM is an inference engine optimized for serving transformer models efficiently, using techniques such as continuous batching and efficient KV-cache management.

## Learn
- model loading and serving
- batching and scheduling
- KV cache
- throughput vs latency
- quantization concepts
- OpenAI-compatible serving
- GPU memory management

## Production
Measure tokens/sec, time-to-first-token, inter-token latency, concurrency and GPU utilization. Bound context lengths, monitor memory and queueing, and pin model artifacts.

## Related
PyTorch, Hugging Face Transformers, Kubernetes, OpenAI SDK.
