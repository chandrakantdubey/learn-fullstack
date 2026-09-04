# vLLM

**Role:** Primary | **Layer:** LLM inference

## Mental model
vLLM is an inference/serving engine designed to execute transformer workloads efficiently under concurrent traffic. The hard problem is not just model execution; it is scheduling requests and managing KV-cache memory while meeting latency and throughput objectives.

```text
requests
  -> admission/queue
  -> scheduler
  -> model execution
  -> KV cache
  -> streamed tokens
```

## Core concepts
Understand model loading, tokenizer compatibility, batching, continuous batching, KV-cache management, GPU memory, sequence length and concurrent generation.

## Latency metrics
Track:
- time to first token
- inter-token latency
- total request latency
- queueing time
- tokens/sec
- concurrent requests
- GPU utilization
- KV-cache/memory pressure

Average latency alone hides queueing and tail behavior.

## Continuous batching
Unlike static batch jobs, online inference receives requests at different times. Continuous batching allows the scheduler to combine useful work dynamically, improving GPU utilization while balancing latency.

## KV cache
Autoregressive generation reuses attention state from previous tokens. KV-cache memory can become a dominant capacity constraint as context length and concurrent sequences grow.

Capacity planning must therefore consider model weights + runtime overhead + KV cache, not just parameter count.

## Production architecture
```text
API gateway
 -> admission control
 -> inference service
    -> scheduler
    -> GPU workers
 -> streaming response
```

Keep authentication, tenant quotas and application policy outside the model server while enforcing safe resource limits at the serving boundary too.

## Capacity and scaling
Scale on workload characteristics, not request count alone. A request generating 1,000 tokens is materially different from one generating 30. Model size, context length, concurrency and output length all affect GPU capacity.

## Reliability
Bound queue depth, request duration, context length and generation length. Define behavior when GPUs are saturated. Do not allow retries to duplicate expensive generation or amplify overload.

## Model lifecycle
Pin model revisions, validate artifacts and tokenizer compatibility, warm instances and define rollout/rollback behavior. GPU model startup can be slow enough that deployment strategy matters.

## Security
Treat model artifacts as supply-chain inputs. Restrict serving endpoints, authenticate callers and enforce tenant/resource quotas. Do not expose administrative controls to untrusted clients.

## Observability
Correlate inference metrics with application traces. Track queueing, GPU utilization, memory, errors, time-to-first-token, inter-token latency and tokens/sec.

## Common mistakes
- capacity planning by parameter count only
- ignoring KV-cache memory
- unlimited context/output lengths
- no admission control
- retry storms during GPU saturation
- measuring only total latency

## Interview-level topics
Continuous batching, KV cache, GPU memory, scheduling, throughput vs latency, TTFT/ITL, model serving, capacity planning and overload control.

## Related
PyTorch, Hugging Face Transformers, Kubernetes, OpenAI SDK.