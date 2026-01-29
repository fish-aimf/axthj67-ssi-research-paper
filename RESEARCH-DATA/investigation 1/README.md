# Investigation 1: Correlation Between Question Type and Answer SSI

## Question Types and Expected Semantic Stability Index (SSI)

### Table: Question Types, Descriptions, Expected SSI, Rationale, and Examples

| **Question Type** | **Description** | **Examples** | **Rationale** | **Expected SSI (approx.)** |
|-------------------|-----------------|--------------|---------------|----------------------------|
| **Closed-Factual** | Requests a single, objectively verifiable fact with a canonical answer found in reference materials. The question has minimal ambiguity and expects a brief, specific response (typically 1-3 sentences). The answer can be checked against authoritative sources. No calculation, interpretation, or multi-step reasoning is required—just retrieval of established knowledge. | • "What is the atomic number of carbon?"<br>• "Who wrote 'Pride and Prejudice'?"<br>• "What is the capital of Australia?"<br>• "In what year did World War II end?"<br>• "What is the boiling point of water at sea level?" | Answers are constrained by factual knowledge stored in model parameters with virtually no interpretive freedom, leading to extremely high semantic consistency across repeated queries and different models. Variation typically indicates retrieval errors or hallucinations rather than legitimate alternative phrasings. | **0.90–1.00** |
| **Computational / Numerical** | Requires explicit mathematical calculation, formula application, or algorithmic execution with clearly defined inputs and procedures. The question specifies all necessary parameters (numbers, conditions, formulas) and expects a numeric answer or structured quantitative output. The solving process follows deterministic steps with minimal interpretive freedom. | • "Calculate the 95% confidence interval for a mean given n=25, mean=50, sd=8."<br>• "What is 347 × 892?"<br>• "Solve for x: 3x + 7 = 22"<br>• "Find the area of a circle with radius 5 cm."<br>• "Compute the compound interest on $1000 at 5% annually for 3 years." | Numerical tasks severely constrain acceptable outputs since mathematical operations have correct answers. Differences arise primarily from rounding conventions or calculation variance. Deterministic solving steps lead to high SSI, though stochastic decoding or skipped intermediate steps can reduce it slightly. | **0.80–1.00** |
| **Procedural / How-to** | Requests a sequence of ordered steps, instructions, or procedures to accomplish a specific task or operation. The question expects a structured workflow where order matters and key steps should not be omitted. The task has an established methodology but may allow variation in granularity, phrasing, or optional sub-steps. | • "List the steps to perform a two-sample t-test on independent data."<br>• "How do I change a car tire?"<br>• "Describe the procedure for sterilizing laboratory glassware."<br>• "What are the steps to file a tax return?"<br>• "Explain how to bake chocolate chip cookies from scratch." | Canonical sequences exist for most procedural tasks, but variability emerges from differences in assumed prior knowledge, level of detail, and whether optional or context-dependent steps are included. This leads to moderate stability—the core sequence remains similar but phrasing and granularity vary. | **0.70–0.90** |
| **Conceptual-Definition** | Requests a clear, concise explanation of a specific concept, principle, theory, or mechanism. The question asks "what is" or "explain" a defined term or idea, expecting a focused definition or description (typically 2-5 sentences) that captures the essential meaning without requiring extended analysis or application. | • "Explain statistical power in simple terms."<br>• "What is photosynthesis?"<br>• "Define cognitive dissonance."<br>• "What does 'opportunity cost' mean in economics?"<br>• "Explain the concept of blockchain." | Multiple semantically equivalent phrasings exist for most concepts, allowing models to express the same core meaning through different word choices and sentence structures. SSI depends on consistency of propositional content rather than exact wording, resulting in moderate-to-high stability. | **0.65–0.90** |
| **Analytical / Multi-step Reasoning** | Requires chained logical reasoning, inference across multiple premises, or argumentation to reach a conclusion. The question presents a scenario or problem requiring the model to connect evidence, weigh factors, and synthesize information through multiple reasoning steps. The answer structure is relatively unconstrained beyond logical coherence. | • "Given falling tax revenues and rising pension obligations, analyze short- and long-term budget policy options."<br>• "Why did the Roman Empire fall? Consider political, economic, and military factors."<br>• "Compare the effectiveness of renewable energy subsidies versus carbon taxes."<br>• "How does inflation affect different income groups?"<br>• "Analyze the causes of the 2008 financial crisis." | Models can choose different reasoning paths, emphasize different pieces of evidence, and structure arguments in various ways while remaining logically sound. This chain-of-thought diversity increases semantic variation. Different valid analytical frameworks lead to moderate SSI. | **0.55–0.80** |
| **Evaluative / Normative** | Requests value judgments, recommendations, ethical assessments, or normative stances on issues where multiple defensible positions exist. The question explicitly or implicitly asks for an evaluation based on values, preferences, or normative criteria, often requiring justification of the position taken. | • "Should governments subsidize electric vehicles? Argue for or against."<br>• "Is capital punishment ethically justifiable?"<br>• "Evaluate whether remote work is better than office work."<br>• "Should social media companies moderate political speech?"<br>• "Are standardized tests fair measures of student ability?" | Models may adopt different normative frameworks, prioritize different values, and construct different justifications for their positions. Even when reaching similar conclusions, the reasoning paths and emphasis vary significantly, leading to low-to-moderate SSI. Fundamental value differences produce higher variation. | **0.40–0.70** |
| **Design / Methodological (Trade-off)** | Requests the design of an experiment, system, study, product, or intervention under specified constraints. The question requires creative problem-solving, specification of components and parameters, and justification of design choices among multiple valid alternatives. Trade-offs between competing objectives must be navigated. | • "Design a randomized trial to test an online math tutoring app."<br>• "Create a survey to measure customer satisfaction with a new product."<br>• "Design an algorithm to detect fraudulent credit card transactions."<br>• "Plan a 6-month marketing campaign for a startup."<br>• "Propose an experimental design to test the effect of sleep on memory." | High creative freedom and numerous valid design solutions produce diverse outputs. Different models may prioritize different trade-offs (cost vs. precision, simplicity vs. comprehensiveness). SSI varies based on constraint strictness—tighter specifications increase consistency, while open-ended designs reduce it. | **0.45–0.75** |
| **Interpretive / Contextual** | Requests interpretation of texts, images, artworks, historical events, or ambiguous scenarios where multiple plausible readings exist. The question requires subjective judgment, contextual understanding, and inference beyond explicit information. There is no single "correct" interpretation, though some may be more defensible than others. | • "Interpret the themes of alienation in this short passage."<br>• "What does this abstract painting convey?"<br>• "Analyze the symbolism in the final scene of this film."<br>• "What was Shakespeare trying to say about power in Macbeth?"<br>• "Interpret the geopolitical implications of this news event." | High subjectivity combined with reliance on implicit background assumptions causes substantial variability. Different valid interpretive frameworks, emphasis on different textual/visual elements, and varying contextual knowledge make semantic equivalence difficult to maintain, resulting in low SSI. | **0.35–0.60** |
---

## Methodology for Evaluating SSI of Each Question Type

1. **Generation of Question Sets**  
   For each question type, GPT-5.1 generates **5 sets of 30 questions**.  
   - Questions are labeled **1–30**.  
   - Sets are labeled **A–E** → each question has versions **xa, xb, xc, xd, xe**.  
   - Rephrasings must be *semantically very similar to identical*.

   Across 8 question types:  
   **5 sets × 30 questions × 8 types = 1200 questions**  

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

