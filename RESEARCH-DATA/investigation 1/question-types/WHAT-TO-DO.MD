# Instructions for Generating Question Sets
(Meaning unchanged — only clarity and formatting improved.)

For each question-type folder, there are **five question prompts**.  
For each prompt, you must ask **OpenAI GPT-5o** the following **exact** prompt.

---

## **Prompt 1 — Generate the 30 Base Questions**  
Copy-paste **this exact text**:

```
You are participating in a research paper investigating different question types
and you are required to generate me 30 questions, no more and no less unless specified otherwise of your given question type. 
It should consist 3 questions each of questions from Mathematics, Physics, Chemistry, Biology, Computer science, History, Philosophy, Economics, English Language, Ethics. 
No more and no less and that only if you are very certain such a question type is impossible to be formed from a certain subject, skip the subject. 
Reply in this exact format without any other dialog or excessive wordidng
Q1) Question content
Q2) Question content
Q3) Question content
....
Q30) Question content


Your given question type is:
INSERT THE GIVEN QUESTION TYPE OVER HERE (BOLDED)
You are to generate 30 questions of only such a question type unless of such a question is impossible, then you are allowed to skip.
 Give your response in a copy paste text box such that it would be easy to copy your response

```

After GPT-5o generates the 30 questions, you must perform a **manual review** to ensure they are acceptable.

Only after a full manual review may you continue to Prompt 2.

---

## **Prompt 2 — Generate Sets A–E (Semantically Identical Rephrasings)**  
Ask a **separate instance** of GPT-5o the following **exact** prompt:

```
You are to review the following questions, and generate 5 different versions, set A, set B, Set C, Set D, Set E 
The sets are to be semantically Identical yet with different wording. 
ENSURE THEY ARE SEMANTICALLY IDENTICAL or close to semantically identical. 
Respond in the following format: 
Set A:
Q1a)
Q2a)
Q3a)
Q4a)
...
Q30a)
Set B:
Q1b)
Q2b)
Q3b)
...
Set E:
...
Q30e 

Where Q1a), Q1b), Q1c), Q1d), Q1e) All are semantically identical, just rephrased. 
You are not to change the fundemental question type or underlying meaning at all. 
Return in this exact format with no filler or excessive text. Ensure you seperate each question set with seperate text boxes for easy copying. ` ` Also do not include the Set X: Inside the text box. 


PASTE THE PREVIOUS QUESTION SET HERE
```

---

After receiving all sets, **copy and paste** the final A–E question sets into the `.txt` files within each question-type folder.



After getting the questions, open a new instance of the LLM and paste in a single question set, Telling it to reply in this exact format do not reuse an instance

```
Question set over here 

Reply to these questions in this exact format without additional words
A1a)
A2a)
A3a)
A4a)
Changing only the letter in front from Q for question to A for answer

```

