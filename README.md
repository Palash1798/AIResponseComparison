# AI Response Comparison


This Python script compares the responses from **OpenAI's ChatGPT** (`gpt-3.5-turbo`) and **Anthropic's Claude** (`claude-3-sonnet-20240229`) for the same prompt, and saves the results into a Markdown file (`ai_response_comparison.md`).

## Features

- Fetches AI-generated responses from both **ChatGPT** and **Claude**
- Uses the latest **OpenAI Python SDK (>=1.0.0)** syntax
- Saves output in **Markdown format** for easy readability
- Displays:
  - The original prompt
  - Timestamp of execution
  - Responses from both models
  - Basic comparison metrics (word counts)

## Requirements

### Python Version

- Python **3.8+** recommended

### Dependencies

Install the required libraries:

```bash
pip install openai anthropic
```

## Setup

1. Clone or download this repository.
2. Install dependencies (see above).
3. Set your API keys inside the script:
   ```python
   OPENAI_API_KEY = "your-openapi-api-key"
   ANTHROPIC_API_KEY = "your-anthropic-api-key"
   ```
   - **OpenAI** key: [Get it here](https://platform.openai.com/account/api-keys)
   - **Anthropic** key: [Get it here](https://console.anthropic.com/account/keys)

## Usage

Run the script:

```bash
python compare_llms.py
```

Example console output:

```
Getting responses from AI models...
Responses saved to 'ai_llm_response_comparison.md'.
```

## Output

The generated `ai_llm_response_comparison.md` will look like this:

```markdown
# AI Response Comparison

**Prompt:** Explain quantum computing to a 10-year-old

**Timestamp:** 2025-08-09 20:45:00

## Claude AI Response

<Claude's answer here>

## ChatGPT Response

<ChatGPT's answer here>

## Comparison Summary

- Claude response word count: **120**
- ChatGPT response word count: **115**
```

## Notes

- The **free OpenAI API key** only works with `gpt-3.5-turbo`.
- `gpt-4` or `gpt-4o` require a paid OpenAI account.
- Claude API calls use `claude-3-sonnet-20240229` but can be swapped for any available Claude model.

## License

This project is released under the MIT License.
