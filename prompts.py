from langchain_core.prompts import PromptTemplate

RESUME_OPTIMIZATION_PROMPT = """
You are an expert Technical Recruiter and ATS Optimization Specialist.

JOB DESCRIPTION:
{job_description}

RESUME TEXT:
{resume_text}

Task:
Provide a Markdown formatted analysis:

1. **Match Score (0-100)**
2. **Missing Keywords**
3. **Profile Summary Rewrite**
4. **Improved Resume Bullet Points**
5. **Final Verdict**

Style:
- Be strict & professional
- Do NOT fabricate skills
- Output valid Markdown
"""

def get_prompt_template():
    return PromptTemplate(
        template=RESUME_OPTIMIZATION_PROMPT,
        input_variables=["job_description", "resume_text"]
    )
    