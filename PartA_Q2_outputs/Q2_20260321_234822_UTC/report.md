# Q2 LoRA SFT Record

- Run ID: `Q2_20260321_234822_UTC`
- Model: `/workspace/tbx/Llama-3.2-3B-Instruct/`
- Dataset: `/workspace/tbx/yoda_sentences/sentences.csv`
- Dtype: `torch.bfloat16`
- Train size: `648`  |  Val size: `72`
- Hyperparams: epochs=3, lr=0.0002, bs=4, grad_accum=1, max_len=256, warmup_steps=30
- Demo mode: `hard`  |  Demo N: `15`

## Deliverables
- Training Loss vs Steps: `loss_curve.png`
- Three examples before and after SFT: `before_after.json` and `demo_before_after.md`