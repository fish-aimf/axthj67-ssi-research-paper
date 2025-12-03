# Investigation 1: Correlation Between Question Type and Answer SSI

## Question Types and Expected Semantic Stability Index (SSI)

### Table: Question Types, Descriptions, Expected SSI, Rationale, and Examples

| **Question Type** | **Description** | **Expected SSI (approx.)** | **Why (Rationale)** | **Example** |
|-------------------|-----------------|-----------------------------|----------------------|--------------|
| **Closed-Factual** | Requests a single verifiable fact or short factual statement with little room for interpretation. | **High (0.80–1.00)** | Answers are bounded by factual knowledge stored in model parameters; low interpretive freedom → high semantic consistency across repeats and models. Variation usually indicates retrieval error or hallucination. | “What is the atomic number of carbon?” |
| **Computational / Numerical** | Requires explicit calculation, numeric output, or formula application with clearly defined procedures and inputs. | **High–Medium (0.70–0.90)** | Numerical tasks constrain acceptable outputs; differences come from rounding or calculation variance. Deterministic steps → high SSI. Stochastic decoding or skipped steps → lower SSI. | “Calculate the 95% CI for a mean given n=25, mean=50, sd=8.” |
| **Procedural / How-to** | Stepwise instructions or procedural sequences where order and completeness matter. | **Medium (0.60–0.80)** | Canonical sequences exist, but variability in granularity or assumed context leads to moderate stability. Some steps are optional, which changes phrasing. | “List the steps to perform a two-sample t-test on independent data.” |
| **Conceptual-Definition** | Requests concise explanation of a core concept, principle, or mechanism. | **Medium (0.55–0.80)** | Many synonymous phrasings are possible; meaning stays similar while wording shifts. SSI depends on consistent propositional content. | “Explain statistical power in simple terms.” |
| **Analytical / Multi-step Reasoning** | Requires chained reasoning, inference, or argumentation to reach a conclusion. | **Medium–Low (0.45–0.70)** | Models choose different reasoning paths or emphasize different evidence → semantic variation increases. Chain-of-thought diversity reduces stability. | “Given falling tax revenues and rising pensions, analyze short- and long-term budget policy options.” |
| **Interpretive / Contextual** | Interpretation of documents, images, artworks, or cases where multiple plausible readings exist. | **Low (0.25–0.50)** | High subjectivity and reliance on background assumptions cause large variability; semantic equivalence is difficult to maintain. | “Interpret the themes of alienation in this short passage.” |
| **Evaluative / Normative** | Requests value judgments, recommendations, or stances, often with justification. | **Low–Medium (0.30–0.60)** | Models may have different normative priors and justify decisions differently → moderate-to-low SSI. | “Should governments subsidize electric vehicles? Argue for or against.” |
| **Design / Methodological (Trade-off)** | Designing experiments, systems, or products under constraints, requiring specification and justification. | **Low–Medium (0.35–0.65)** | High creativity and many valid solutions produce diversified outputs. SSI depends heavily on strictness of constraints. | “Design a randomized trial to test an online math tutoring app.” |

---

## Methodology for Evaluating SSI of Each Question Type

1. **Generation of Question Sets**  
   For each question type, GPT-5.1 generates **5 sets of 30 questions**.  
   - Questions are labeled **1–30**.  
   - Sets are labeled **A–E** → each question has versions **xa, xb, xc, xd, xe**.  
   - Rephrasings must be *semantically very similar to identical*.

   Across 8 question types:  
   **5 sets × 30 questions × 8 types = 1200 questions**  
   (Your text said 1350; adjust depending on final count.)

2. **Ensuring High Question SSI**  
   - Each generated question is scored for semantic similarity (Question SSI).  
   - Questions with **SSI < 0.95** are manually revised until stable.  
   - Ensure **no two questions are overly similar** within a set.

3. **Independent Model Instances for Answer Collection**  
   - A new model instance is opened for each set.  
   - Each instance answers exactly **one set of 30 questions**.  
   - No model receives two sets simultaneously to avoid cross-influence.

4. **Data Storage and Structure**  
   - All answers (30 × 5 sets × 8 types) are stored in a consolidated JSON file.  
   - This process repeats for all models tested.

5. **Vectorization and Embeddings**  
   - Responses are converted into **768-dimensional embeddings**.  
   - Similarities are calculated using **cosine similarity**.  
   - Result → **Answer SSI** for each question instance.

6. **Computing Question Type Stability**  
   - For each type, compute:  
     - mean Answer SSI  
     - mean Question SSI  
     - ratio **AnswerSSI / QuestionSSI** → *question grade*  
   - The average SSI across all types is normalized to **1.0**, forming the  
     **Answer Type Stability Index**.  
     - > 1 → more stable than average  
     - < 1 → less stable than average

7. **Statistical Analysis and Visualization**  
   For each question type:  
   - Z-scores  
   - mean and median  
   - scatter plots  
   - bar charts  

8. **Models Evaluated**  
   - **OpenAI GPT-5.1 Standard**  
   - **Claude Sonnet 4.5**  
   - **DeepSeek V3.2-Exp**  
   - **Gemini Flash 2.5**

---

## Final Output

The compiled results determine:  
- How stable each question type is across models  
- Which types reliably produce semantically stable responses  
- An empirically grounded **Answer Type Stability Index** usable for future benchmarking

