# Part A - Q2: Before vs After SFT

## Example 1
**English input:** He wrote down a long list of items.

**Reference Yoda target:** A long list of items, down he wrote.

**Before SFT:**
```
"A long list of items, he wrote down, he did."
```
**After SFT:**
```
A long list of items, he wrote down.
```

## Example 2
**English input:** The duke left the park in a silver coach.

**Reference Yoda target:** Left the park in a silver coach, the duke did.

**Before SFT:**
```
"A silver coach, the duke left in, he did."
```
**After SFT:**
```
In a silver coach, the duke left the park, he did.
```

## Example 3
**English input:** A siege will crack the strong defense.

**Reference Yoda target:** Crack the strong defense, a siege will.

**Before SFT:**
```
"A siege, the strong defense will crack."
```
**After SFT:**
```
Crack the strong defense, a siege will.
```
