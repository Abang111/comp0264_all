# Q4 Deliverable — SFT to Respond like Yoda

- Base model: `/workspace/tbx/Llama-3.2-3B-Instruct/`
- Train samples: 500
- Val samples: 200
- Test samples: 500
- Final train loss: `3.1595`
- Final val loss: `None`
- Best val loss: `None`

## Before vs After SFT (3 Test Examples)

### Example 1
**Question:**
```
lucknow congress session 1916 was presided over by—
```
**Correct answer:** Lucknow Pact Muhammad Ali Jinnah, then a member of the Congress as well as the League, made both the parties reach an agreement to pressure the British government to adopt a more liberal approach to India and give Indians more authority to run their country, besides safeguarding basic Muslim demands. Jinnah is seen as the mastermind and architect of this pact.[citation needed] (key: N/A)

**Reference Yoda answer:**
```
To pressure the British government to adopt a more liberal approach to India, to run their country, and basic Muslim demands safeguard, the pact did. A mastermind and architect of this pact, Muhammad Ali Jinnah is seen. The Congress as well as the League, a member of, he was.
```

**Before SFT:**
```
Maharaja of Bikaner, it was.
```
**After SFT:**
```
Raja of Bhopal
```

### Example 2
**Question:**
```
when did the first chipotle on evans open
```
**Correct answer:** Chipotle Mexican Grill Founder Steve Ells attended the Culinary Institute of America in Hyde Park, New York. Afterward, he became a line cook for Jeremiah Tower at Stars in San Francisco.[19] There, Ells observed the popularity of the taquerías and San Francisco burritos in the Mission District. In 1993, Ells took what he learned in San Francisco[20] and opened the first Chipotle Mexican Grill in Denver, Colorado, in a former Dolly Madison Ice Cream store at 1644 East Evans Avenue,[21] near the University of Denver campus, using an $85,000 loan from his father.[18] Ells and his father calculated that the store would need to sell 107 burritos per day to be profitable. After one month, the original restaurant was selling over 1,000 burritos a day.[15] The second store opened in 1995 using Chipotle's cash flow, and the third was opened using an SBA loan. To fund more growth, Ells' father invested $1.5 million. Afterwards, Ells created a board of directors and business plan, raising an additional $1.8 million for the company.[22] Ells had originally planned to use funds from the first Chipotle to open a fine-dining restaurant, but instead focused on Chipotle Mexican Grill when the restaurants saw success.[23][24] (key: N/A)

**Reference Yoda answer:**
```
Attended the Culinary Institute of America in Hyde Park, New York, the Founder of Chipotle Mexican Grill, Steve Ells did. A line cook for Jeremiah Tower at Stars in San Francisco, he became. The popularity of the taquerías and San Francisco burritos in the Mission District, he observed. In 1993, the first Chipotle Mexican Grill in Denver, Colorado, he opened. An $85,000 loan from his father, he used. Near the University of Denver campus, in a former Dolly Madison Ice Cream store, the first store was. 107 burritos per day, to be profitable,
```

**Before SFT:**
```
"1995, it opened."
```
**After SFT:**
```
I do not have access to real-time data or specific store locations, but I can tell you that Chipotle Mexican Grill was founded in 1993 by Steve Ells
```

### Example 3
**Question:**
```
when did the us start using agent orange in vietnam
```
**Correct answer:** Agent Orange In mid-1961, President Ngo Dinh Diem of South Vietnam asked the United States to conduct aerial herbicide spraying in his country.[21] In August of that year, the Republic of Vietnam Air Force conducted herbicide operations with American help. But Diem's request launched a policy debate in the White House and the State and Defense Departments. However, U.S. officials considered using it, pointing out that the British had already used herbicides and defoliants during the Malayan Emergency in the 1950s. In November 1961, President John F. Kennedy authorized the start of Operation Ranch Hand, the codename for the U.S. Air Force's herbicide program in Vietnam. (key: N/A)

**Reference Yoda answer:**
```
In mid-1961, President Ngo Dinh Diem of South Vietnam asked the United States to conduct aerial herbicide spraying in his country. In August of that year, the Republic of Vietnam Air Force conducted herbicide operations with American help. But Diem's request launched a policy debate in the White House and the State and Defense Departments. However, U.S. officials considered using it, pointing out that the British had already used herbicides and defoliants during the Malayan Emergency in the 1950s. In November 1961, the U.S. Air Force's herbicide program in Vietnam
```

**Before SFT:**
```
"1961, US military began spraying Agent Orange over Vietnam."
```
**After SFT:**
```
The use of Agent Orange began in 1961, but it was primarily used during the Vietnam War (1959-1975)
```
