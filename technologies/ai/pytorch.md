# PyTorch

**Role:** Primary | **Layer:** AI/ML

## Mental model
PyTorch represents computation as tensor operations. Parameters are tensors whose values are optimized by gradient-based learning. Autograd records operations needed to compute derivatives.

```text
input tensors
   -> model forward pass
   -> loss
   -> backward/autograd
   -> gradients
   -> optimizer step
   -> updated parameters
```

## Tensors
Understand shape, dtype, device, broadcasting, views vs copies, contiguous memory and vectorized operations. Shape mistakes are among the most common deep-learning bugs.

## Autograd
Autograd computes gradients through the computation graph. Know `requires_grad`, gradient accumulation, `detach`, `no_grad` and `inference_mode` conceptually.

Training and inference have different requirements. Do not retain computation graphs unnecessarily during inference.

## Modules
`nn.Module` composes layers and parameters. Know `train()` vs `eval()`, parameter registration, buffers, state dictionaries and checkpoint loading.

## Data pipeline
Datasets and dataloaders control how training data is transformed and batched. Measure data-loader throughput separately from model throughput; a GPU can sit idle because the input pipeline is slow.

## Optimization
Understand loss functions, SGD/Adam-family optimizers, learning rates, schedulers, weight decay, gradient clipping, warmup and batch-size effects. Hyperparameter choices are experiments, not universal constants.

## Mixed precision
Mixed precision can improve throughput and memory usage on supported hardware. Understand autocasting, gradient scaling where applicable and numerical stability.

## Distributed training
Know data parallelism, distributed data parallel concepts, collective communication, synchronization costs and checkpoint coordination. Distributed training adds failure modes and operational complexity.

## Checkpoints
A useful checkpoint includes model state, optimizer state when training resumes, scheduler/scaler state as needed, configuration, data/model versions and reproducibility metadata.

## Inference
Separate model loading from request handling. Warm models before traffic, control concurrency, batch where useful and measure GPU memory, queueing, latency and throughput.

## Production patterns
- Pin compatible framework/CUDA/model versions.
- Validate model artifacts before deployment.
- Bound input shapes and sequence lengths.
- Monitor GPU utilization and memory.
- Separate training and serving environments.
- Make model versions explicit.
- Keep preprocessing/tokenization compatible with the checkpoint.

## Performance
Measure samples/sec or tokens/sec, GPU utilization, memory, host-to-device transfer, data-loader throughput and p50/p95/p99 inference latency. Bigger batches improve utilization only until memory or latency constraints dominate.

## Security
Treat downloaded checkpoints and serialized artifacts as supply-chain inputs. Prefer trusted formats and sources, pin versions, isolate model execution and avoid loading arbitrary executable serialization formats.

## Testing
Test tensor shapes, preprocessing, deterministic fixtures where possible, checkpoint compatibility and inference outputs on representative examples. Integration-test GPU paths separately from CPU/unit logic.

## Common mistakes
- wrong tensor/device/dtype
- forgetting `eval()` during inference
- retaining graphs accidentally
- saving incomplete checkpoints
- GPU underutilization caused by data loading
- training/serving preprocessing drift

## Interview-level topics
Autograd, tensor memory/layout, optimization, mixed precision, data pipelines, distributed training, checkpointing, GPU memory and inference throughput.

## Related
Hugging Face Transformers, scikit-learn, sentence-transformers, vLLM.