# Part B Q2 — Reward Function Design

## Why each component is necessary

**Correctness reward** ensures that the response actually answers the task correctly rather than only sounding fluent or stylistically appropriate.

**Format reward** encourages outputs that are complete and well-formed, reducing truncated, malformed, or badly structured responses.

**Style reward** encourages adherence to Yoda-style expression, which is important because correctness alone does not guarantee the required stylistic form.

## Do the obtained rewards match expectations?

Yes, broadly they should. A good Yoda-style answer that preserves the original meaning should receive high correctness and style rewards, and usually a good format reward as well. 
A fluent but standard-English response should still score well on correctness and format, but lower on style. 
An unrelated response may still receive some format reward if it is grammatically complete, but should receive a much lower correctness score and usually a lower total reward overall.

## Reward Scores for 3 Diverse Responses

### Example 1
**Response:** For knowledge and defense, the Force a Jedi uses.
- Correctness Reward: `0.9605`
- Format Reward: `1.0000`
- Style Reward: `0.9777`
- Total Reward: `0.9753`

### Example 2
**Response:** A Jedi uses the Force for knowledge and defense.
- Correctness Reward: `1.0000`
- Format Reward: `1.0000`
- Style Reward: `0.0000`
- Total Reward: `0.6000`

### Example 3
**Response:** The turning radius or turning circle of a vehicle, the radius of the smallest circular turn that the vehicle is capable of making, is.
- Correctness Reward: `0.0983`
- Format Reward: `1.0000`
- Style Reward: `0.9839`
- Total Reward: `0.6329`
