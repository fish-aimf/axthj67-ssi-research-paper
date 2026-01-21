# Investigation 2 — Instructions for Generating Question Sets  
(Use this file as the operational manual for Investigation 2.  
Follow all steps exactly. Do not modify formatting or wording.)

Investigation 2 differs from Investigation 1 in that:
- Question sets are generated **per subject**, not per question type.
- Each subject’s question set contains mixed question types.
- Skips can be applied if a subject cannot support a question type.
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


# 1. Generate the Original Question Set

For each subject, open a new instance of **GPT-5.1** and provide this **exact prompt**:

```
You are participating in a research paper investigating semantic stability across different question types. 
You are required to generate questions for the given academic subject.

The questions must be generated in the following exact order of question types:

1. 6 computational-numerical questions  
2. 6 procedural-how-to questions  
3. 6 conceptual-definition questions  
4. 6 analytical-multistep-reasoning questions  
5. 6 interpretive-contextual questions  
6. 6 evaluative-normative questions  
7. 6 design-methodological questions  
8. 6 closed-factual questions  

If you determine that the subject cannot reasonably support a specific question type 
(e.g., computational/numerical questions in English Language), 
you must SKIP that question type. 

You can generate a variable number of questions. Based on which question types are acceptable. 

Generate the questions in the following strict response format, with no extra dialogue:

Q1) Question content  
Q2) Question content  
Q3) Question content  
...
Qlast question number) Question content

Your given academic subject is:
**INSERT SUBJECT HERE (BOLDED)**

Generate questions following the rules above.
Please provide the questions inside a text box \`\` for easy copy and pasting reasons. The Set letter should be outside. 
At the bottom, you should include which question type is ommited, if any. In this exact format including the name of the question type, and nothing else.


 Explaination of question types:
 Closed-Factual
These questions ask for a single, specific fact with a clearly correct answer and little room for interpretation.
Example: “What is the atomic number of carbon?”

Computational / Numerical
These questions require carrying out a calculation or applying a formula to given inputs to produce a numeric result.
Example: “Calculate the 95% confidence interval for a mean given n = 25, mean = 50, sd = 8.”

Procedural / How-to
These questions ask for a sequence of steps or instructions to complete a task or process.
Example: “List the steps to perform a two-sample t-test on independent data.”

Conceptual-Definition
These questions ask for an explanation or definition of a key concept, principle, or idea.
Example: “Explain statistical power in simple terms.”

Analytical / Multi-step Reasoning
These questions require reasoning through multiple steps, connecting evidence or ideas to reach a conclusion.
Example: “Given falling tax revenues and rising pensions, analyze short- and long-term budget policy options.”

Interpretive / Contextual
These questions involve interpreting meaning from texts, images, or situations where multiple reasonable interpretations are possible.
Example: “Interpret the themes of alienation in this short passage.”

Evaluative / Normative
These questions ask for judgments, opinions, or recommendations, usually supported with reasons.
Example: “Should governments subsidize electric vehicles? Argue for or against.”

Design / Methodological (Trade-off)
These questions ask you to design a system, experiment, or solution under constraints, often requiring justification of choices.
Example: “Design a randomized trial to test an online math tutoring app.”




```

### After receiving the 40 questions:
- Verify you have the questions and run it through the question semantic stability checker.
- create the ssi_of_questions file.
- create a 
- Verify rollover rules were correctly applied when necessary.

Only after full verification may you proceed to Step 2.



# 2. Generate Sets A–E (Semantically Identical Rephrasings)

For each subject, open a **new, separate instance** of GPT-5.1 and provide this **exact prompt**:

```
You are to review the following questions and generate 5 different rephrased versions: Set A, Set B, Set C, Set D, and Set E.

All sets must be semantically identical to the original questions while differing only in wording or phrasing. 
ENSURE that the semantic stability of each question remains as close to semantically identical as possible.

Respond in the following strict format and do not include any additional dialogue:

Set A:
Q1a)
Q2a)
Q3a)
...
Qlast question numbera)

Set B:
Q1b)
Q2b)
Q3b)
...
Qlast question numberb)

Set C:
Q1c)
...
Qlast question numberc)

Set D:
Q1d)
...
Qlast question numberd)

Set E:
Q1e)
...
Qlast question numbere)

Each group of corresponding questions (Q1a–Q1e, Q2a–Q2e, etc.) must be semantically identical. 
You must not change the underlying meaning, question type, structure, or intent in any way and rephrase it. 
Return your response in this exact format with no filler or extra text with each individual set each inside its own text box for easy copy pasting \`\`
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
