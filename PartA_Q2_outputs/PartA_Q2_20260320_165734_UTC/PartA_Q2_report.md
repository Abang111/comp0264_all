# Part A - Q2: Training to Translate

- **Run ID:** `PartA_Q2_20260320_165734_UTC`
- **Model:** `/workspace/tbx/Llama-3.2-3B-Instruct/`
- **Local CSV:** `/workspace/tbx/yoda_sentences/sentences.csv`
- **Dtype:** `torch.bfloat16`
- **Train size:** `500`
- **Val size:** `200`
- **LoRA:** r=16, alpha=32, dropout=0.05, target_modules=['q_proj', 'v_proj']
- **Training:** epochs=3, lr=0.0002, batch_size=4, grad_accum=1, max_seq_length=256
- **Training time (s):** 100.0806

## Deliverable

1. Plot showing Training Loss vs. Steps
2. Three examples of responses before and after SFT

## Main output files

- `PartA_Q2_training_loss_vs_steps.png`
- `before_after_examples.json`
- `PartA_Q2_before_after.md`
- `adapter/`
