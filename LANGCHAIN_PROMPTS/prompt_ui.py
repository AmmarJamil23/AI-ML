from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

st.header('Research Tool')

model = ChatOpenAI(
    model="gpt-3.5-turbo"
)

paper_input = st.selectbox("Select Research Paper Name", ["Attention is all You need", "BERT: Pre-training of the Deep Bidirectional Tranformers", "GPT-3: Language Models are few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style", ["Beginner-friendly", "Technical", "Code-Oriented", "Mathmatical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])


template = PromptTemplate(
    template="""
You are an expert AI research assistant with strong knowledge of machine learning and deep learning.

Task:
Explain the research paper titled "{paper_input}".

Audience & Style:
- Target explanation style: {style_input}
- Adapt your language, depth, and terminology to match this style.
- Avoid unnecessary jargon unless the style is technical or mathematical.

Length Requirement:
- Explanation length: {length_input}
- Follow this length strictly.

Content Guidelines:
1. Start with a brief overview of the problem the paper addresses.
2. Explain the core idea and motivation behind the paper.
3. Describe the key methodology or architecture used.
4. Highlight the main contributions and results.
5. Mention why this paper is important in the context of machine learning research.

Quality Constraints:
- Be accurate and factual.
- Be clear and logically structured.
- Use headings or paragraphs where appropriate.
- Do not hallucinate results or claims.
- If mathematical, explain intuition along with formulas (if relevant).

Output Format:
- Well-structured paragraphs
- No bullet points unless the style is technical or code-oriented
- No emojis
- Professional academic tone

Now generate the explanation.
""",
    input_variables=["paper_input", "style_input", "length_input"]
)


prompt = template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
})

if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result)