# Part A - Q1: Baseline Inference

- **Run ID:** `PartA_Q1_20260320_164354_UTC`
- **Model path:** `/workspace/tbx/Llama-3.2-3B-Instruct/`
- **Dtype:** `torch.bfloat16`
- **Generation config:** `{'max_new_tokens': 128, 'temperature': 0.0, 'top_p': 1.0}`

## What was done

1. Loaded the base model.
2. Created a prompt template suitable for the chat model.
3. Ran 3 inference examples.

## Deliverable required by Q1

- Memory usage (VRAM)
- Generated text

## Environment

- **timestamp_utc**: 2026-03-20 16:43:54
- **python**: 3.10.19
- **platform**: Linux-5.15.0-140-generic-x86_64-with-glibc2.35
- **torch_version**: 2.5.1+cu121
- **cuda_available**: True
- **transformers_version**: 5.2.0.dev0
- **cuda_device_count**: 6
- **cuda_device_name_0**: NVIDIA GeForce RTX 3090
- **cuda_capability_0**: (8, 6)
- **cuda_total_vram_mb_0**: 24135.2

## Prompt template

```
Prompt template used for PartA_Q1 baseline inference:
- System role: instructs the model to answer accurately, concisely, and factually
- User role: provides the question in the format 'Question: <text>'
- Chat template: tokenizer.apply_chat_template(..., add_generation_prompt=True)
```

## Summary table

| question                                          | generated_text                                                                                                                                                                                                                                                |   latency_s |   peak_vram_mb |
|:--------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------:|---------------:|
| who sang what in the world's come over you        | I couldn't find any information on a well-known song called "The World's Come Over You." Could you provide more context or details about the song, such as the genre, era, or artist?                                                                         |      1.6258 |        1901.37 |
| where did they film diary of a wimpy kid          | The Diary of a Wimpy Kid film series was primarily filmed in Vancouver, British Columbia, Canada.                                                                                                                                                             |      0.8482 |        1901.39 |
| when did fosters home for imaginary friends start | I couldn't find any information on a well-known TV show or media franchise called "Fosters Home for Imaginary Friends." However, I think you may be referring to the animated TV series "Foster's Home for Imaginary Friends," which aired from 2004 to 2009. |      2.3462 |        1901.35 |

## Per-example outputs


### Example 1

**Question:** who sang what in the world's come over you

**Peak VRAM (MB):** 1901.37

**Latency (s):** 1.6258

**Generated text:**
```
I couldn't find any information on a well-known song called "The World's Come Over You." Could you provide more context or details about the song, such as the genre, era, or artist?
```

### Example 2

**Question:** where did they film diary of a wimpy kid

**Peak VRAM (MB):** 1901.39

**Latency (s):** 0.8482

**Generated text:**
```
The Diary of a Wimpy Kid film series was primarily filmed in Vancouver, British Columbia, Canada.
```

### Example 3

**Question:** when did fosters home for imaginary friends start

**Peak VRAM (MB):** 1901.35

**Latency (s):** 2.3462

**Generated text:**
```
I couldn't find any information on a well-known TV show or media franchise called "Fosters Home for Imaginary Friends." However, I think you may be referring to the animated TV series "Foster's Home for Imaginary Friends," which aired from 2004 to 2009.
```