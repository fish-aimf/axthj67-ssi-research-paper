# Investigation 2 — Instructions for Generating Question Sets  
(Use this file as the operational manual for Investigation 2.  
Follow all steps exactly. Do not modify formatting or wording.)

Investigation 2 differs from Investigation 1 in that:
- Question sets are generated **per subject**, not per question type.
- Each subject’s question set contains **40 questions** of mixed question types.
- The question types must follow a fixed hierarchy.
- Rollover rules must be applied if a subject cannot support a question type.
- Five semantically identical variations (Sets A–E) must be produced.
- Each set must be fed into a fresh chatbot instance for response collection.

This document describes how to generate all required files located inside:

```
investigation 2/fields/<SUBJECT NAME>/
```

Each field folder contains:
- PROMPT-SET-A.txt
- PROMPT-SET-B.txt
- PROMPT-SET-C.txt
- PROMPT-SET-D.txt
- PROMPT-SET-E.txt
- LLM-RESPONSE-SET-A.txt
- LLM-RESPONSE-SET-B.txt
- LLM-RESPONSE-SET-C.txt
- LLM-RESPONSE-SET-D.txt
- LLM-RESPONSE-SET-E.txt


# 1. Generate the Original 40-Question Set

For each subject, open a new instance of **GPT-5.1** and provide this **exact prompt**:

```
You are participating in a research paper investigating semantic stability across different question types. 
You are required to generate a total of 40 questions for the given academic subject.

The questions must be generated in the following exact order of question types:

1. 5 computational/numerical questions  
2. 10 procedural/how-to questions  
3. 8 conceptual-definition questions  
4. 3 analytical/multistep-reasoning questions  
5. 3 interpretive/contextual questions  
6. 3 evaluative/normative questions  
7. 3 design/methodological questions  
8. 5 closed-factual questions  

If you determine that the subject cannot reasonably support a specific question type 
(e.g., computational/numerical questions in English Language), 
you must SKIP that question type and ADD the number of skipped questions to the NEXT question type in the list.

You must always generate exactly 40 questions in total.

Generate the questions in the following strict response format, with no extra dialogue:

Q1) Question content  
Q2) Question content  
Q3) Question content  
...
Q40) Question content

Your given academic subject is:
**INSERT SUBJECT HERE (BOLDED)**

Generate 40 questions following the rules above, applying the rollover rule when needed.
```

### After receiving the 40 questions:
- Verify you have **exactly 40 questions**.
- Verify the **ordering of question types** is followed.
- Verify rollover rules were correctly applied when necessary.
- Verify no instructions or formatting rules were violated.

Only after full verification may you proceed to Step 2.



# 2. Generate Sets A–E (Semantically Identical Rephrasings)

For each subject, open a **new, separate instance** of GPT-5.1 and provide this **exact prompt**:

```
You are to review the following 40 questions and generate 5 different rephrased versions: Set A, Set B, Set C, Set D, and Set E.

All sets must be semantically identical to the original questions while differing only in wording or phrasing. 
ENSURE that the semantic stability of each question remains as close to semantically identical as possible.

Respond in the following strict format and do not include any additional dialogue:

Set A:
Q1a)
Q2a)
Q3a)
...
Q40a)

Set B:
Q1b)
Q2b)
Q3b)
...
Q40b)

Set C:
Q1c)
...
Q40c)

Set D:
Q1d)
...
Q40d)

Set E:
Q1e)
...
Q40e)

Each group of corresponding questions (Q1a–Q1e, Q2a–Q2e, etc.) must be semantically identical. 
You must not change the underlying meaning, question type, structure, or intent in any way.
Return your response in this exact format with no filler or extra text.
```

### After GPT-5.1 returns the five sets:
- Copy Set A → PROMPT-SET-A.txt  
- Copy Set B → PROMPT-SET-B.txt  
- Copy Set C → PROMPT-SET-C.txt  
- Copy Set D → PROMPT-SET-D.txt  
- Copy Set E → PROMPT-SET-E.txt  

Do **not** alter them after saving.



# 3. LLM Response Collection Procedure  
(Highly detailed to ensure perfect reproducibility.)

For each subject, you will now collect the outputs produced by GPT-5.1 for Sets A–E.

## 3.1 General Rules
- **Always** open a **fresh chatbot instance** for each set.  
  Never reuse a tab or instance already used by another set.
- Do **not** provide the chatbot with any context from previous chats.
- You must instruct the model **not to include any headers, labels, introductions, or extra text**.
- The model must respond in question-order only.

## 3.2 Instructions to give BEFORE pasting the question set  
For each instance, give this instruction first:

```
When I send the next message, it will contain a list of questions. 
Respond by answering each question in order. 
Do not include any headers, explanations, commentary, or labels. 
Return only the answers, one after another, corresponding to the question order.
```

Wait for GPT-5.1 to acknowledge.

## 3.3 Feeding the prompt set  
Then paste **only** one of the sets:

- PROMPT-SET-A.txt into instance #1  
- PROMPT-SET-B.txt into instance #2  
- PROMPT-SET-C.txt into instance #3  
- PROMPT-SET-D.txt into instance #4  
- PROMPT-SET-E.txt into instance #5  

Press enter and let the model respond.

## 3.4 Saving the model output  
After receiving the answers:

- Save the full output into **LLM-RESPONSE-SET-A.txt**
  (or B, C, D, E accordingly)

Do not edit the text.  
Do not add annotations.  
Do not remove or insert any content.



# 4. Summary of Required Output Files per Subject

Each subject folder must contain:

### Prompt sets:
- PROMPT-SET-A.txt  
- PROMPT-SET-B.txt  
- PROMPT-SET-C.txt  
- PROMPT-SET-D.txt  
- PROMPT-SET-E.txt  

### LLM outputs:
- LLM-RESPONSE-SET-A.txt  
- LLM-RESPONSE-SET-B.txt  
- LLM-RESPONSE-SET-C.txt  
- LLM-RESPONSE-SET-D.txt  
- LLM-RESPONSE-SET-E.txt  

These files constitute the complete dataset for Investigation 2.

# End of Instructions
