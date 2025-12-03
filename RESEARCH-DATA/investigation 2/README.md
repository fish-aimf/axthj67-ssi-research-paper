# Subject-Based Semantic Stability Evaluation Methodology

## Fields of Interest

The following subjects are included in the evaluation:

- Mathematics  
- Physics  
- Chemistry  
- Biology  
- Computer Science  
- History  
- Philosophy  
- Economics  
- English Language  
- Ethics  

---

## Hierarchy of Semantic Stability (Previously Established)

From highest expected Semantic Stability Index (SSI) to lowest:

1. **Closed-Factual**  
2. **Computational / Numerical**  
3. **Procedural / How-to**  
4. **Conceptual Definition**  
5. **Analytical / Multi-step Reasoning**  
6. **Interpretive / Contextual**  
7. **Evaluative / Normative**  
8. **Design / Methodological (Trade-off)**

This ranking determines how questions for each subject are distributed.

---

## Question Generation per Subject

For every subject (Math, Physics, English, etc.), GPT-5.1 will be instructed to generate:

- **5 Computational / Numerical**
- **10 Procedural**
- **8 Conceptual Definition**
- **3 Analytical / Multi-step Reasoning**
- **3 Interpretive**
- **3 Evaluative / Normative**
- **3 Design / Methodological**
- **5 Closed-Factual**

**Total = 40 questions per subject**, arranged from **least stable → most stable**.

### Handling subjects where question types do not apply
If a question type cannot be meaningfully generated for a subject  
(e.g., *computational questions in English language*), then:

- The number of skipped questions is **added to the next available question type** to maintain a total of **40 questions**.
- The relative ordering of stability is preserved.

---

## Production of Question Sets A–E

1. GPT-5.1 is given the **40-question master set** for a subject.  
2. It must generate **5 rephrased versions** of the entire set (A, B, C, D, E).  
3. Rephrasings must keep **semantic meaning nearly identical**.

### Semantic Stability Validation
- Each question in sets A–E is checked.  
- If semantic similarity **< 0.95**, it is regenerated manually.  
- Final sets must be highly stable to avoid contamination of results.

---

## Collecting Model Responses

1. **A completely new chatbot instance** is opened for each question set.  
2. Each instance answers **one set only** to avoid cross-set influence.  
3. Models are prompted to output:
   - **Only the answers**
   - **No headings or commentary**

Responses from all 5 sets are recorded.

---

## Calculating Semantic Stability

For each subject:

1. Responses are vectorized using embeddings.  
2. Cosine similarity is calculated for every question across the 5 sets.  
3. This yields the **Answer Semantic Stability Index (Answer SSI)** per question.  
4. Average stability is computed across all 40 questions → **subject average SSI**.

---

## Subject Semantic Stability Grades

1. Each subject’s mean SSI is normalized so that the **overall mean across subjects = 1**.  
2. A “Subject Semantic Stability Grade” is defined:
   - **> 1** → more semantically stable than average  
   - **< 1** → less semantically stable than average  

This measures how stable a subject is for a given AI model.

---

## Repeating Across All Chatbot Models

This process is repeated for:

- GPT-5.1  
- Claude Sonnet 4.5  
- DeepSeek V3.2-Exp  
- Gemini Flash 2.5  
- (and any future models under evaluation)

For each model:

- A subject grade is produced.  
- The average subject grade is computed.  
- This gives the **model’s overall subject-level semantic stability**.

---

## Final Comparison

By comparing these normalized subject scores:

- We determine **which subjects each model is strongest or weakest at**, and  
- Which AI model overall offers the **greatest semantic stability across all subjects**.

