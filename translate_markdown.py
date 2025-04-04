#!/usr/bin/env python3
import os
import requests
import sys


def read_markdown_file(file_path):
    """Read the markdown file and return its content."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


def translate_with_vllm(content, api_url="http://localhost:8001/v1"):
    """Send content to vLLM API for translation."""

    prompt = f"""Translate the following markdown from English to German. 
IMPORTANT: Keep all markdown formatting intact, especially the links.
Do not translate text inside HTML tags, code blocks, frontmatter (content between --- markers at the top),
and do not translate link URLs (content in parentheses). 

Here's the markdown to translate:

{content}

Translated German markdown:"""

    payload = {
        "model": "deployed_model",  # Adjust if your model has a specific name
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0,
        "max_tokens": 6000,
    }

    try:
        response = requests.post(
            f"{api_url}/chat/completions",
            headers={"Content-Type": "application/json"},
            json=payload,
        )

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            print(f"API error: {response.status_code}")
            print(response.text)
            return None
    except Exception as e:
        print(f"Request error: {e}")
        return None


def save_translated_markdown(translated_content, output_path):
    """Save the translated content to a new file."""
    dir_name = os.path.dirname(output_path)
    file_name = os.path.basename(output_path)
    translated_path = os.path.join(dir_name, "de_" + file_name)

    try:
        with open(translated_path, "w", encoding="utf-8") as file:
            file.write(translated_content)
        print(f"Translation saved to {translated_path}")
    except Exception as e:
        print(f"Error saving translation: {e}")


def main():
    # Path to the markdown file
    markdown_file = "docs/en/1.getting-started/01.introduction.md"
    output_path = "docs/de/1.getting-started/01.introduction.md"
    # Ensure file exists
    if not os.path.exists(markdown_file):
        print(f"File not found: {markdown_file}")
        sys.exit(1)

    # Read the markdown content
    content = read_markdown_file(markdown_file)

    # Translate the content
    print("Sending to vLLM model for translation...")
    translated_content = translate_with_vllm(content)

    if translated_content:
        # Save the translated content
        save_translated_markdown(translated_content, output_path)
    else:
        print("Translation failed.")


if __name__ == "__main__":
    main()
