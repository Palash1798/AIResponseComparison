import os
from openai import OpenAI
import anthropic
from dotenv import load_dotenv

# Load keys from .env
load_dotenv()

# Get API keys
openai_api_key = os.getenv("OPENAI_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

# Initialize clients
client_oai = OpenAI(api_key=openai_api_key)
client_claude = anthropic.Anthropic(api_key=anthropic_api_key)

PROMPT = "Explain quantum computing to a 10-year-old."

def query_openai(prompt):
    """Query GPT-3.5 Turbo"""
    resp = client_oai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return resp.choices[0].message.content.strip()

def query_claude(prompt):
    """Query Claude 3.5 Sonnet"""
    resp = client_claude.messages.create(
        model="claude-3-5-sonnet-latest",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.content[0].text.strip()

if __name__ == "__main__":
    gpt_output = query_openai(PROMPT)
    claude_output = query_claude(PROMPT)

    print("\n=== GPT-3.5 Turbo ===\n", gpt_output)
    print("\n=== Claude 3.5 Sonnet ===\n", claude_output)

    report = f"""# LLM Comparison Report

**Prompt:** {PROMPT}

## GPT-3.5 Turbo
{gpt_output}

## Claude 3.5 Sonnet
{claude_output}

---

**Observations:**  
- Compare tone, simplicity, and metaphors.
- Look for factual differences or omissions.
"""
    with open("llm_comparison.md", "w", encoding="utf-8") as f:
        f.write(report)

    print("\nReport saved to llm_comparison.md")
