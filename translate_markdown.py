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
        "model": "Qwen/Qwen2.5-7B-Instruct",  # Adjust if your model has a specific name
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
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(translated_content)
        print(f"Translation saved to {output_path}")
    except Exception as e:
        print(f"Error saving translation: {e}")


def process_directory(source_dir="docs/en", target_dir="docs/de"):
    """Process all markdown files in the source directory and its subdirectories."""
    for root, dirs, files in os.walk(source_dir):
        # Calculate the corresponding target directory
        rel_path = os.path.relpath(root, source_dir)
        target_path = os.path.join(target_dir, rel_path)

        for file in files:
            # Skip non-markdown files and .yml files
            if not file.endswith(".md") or file.endswith(".yml"):
                continue

            source_file = os.path.join(root, file)
            target_file = os.path.join(target_path, file)

            print(f"Processing {source_file}...")

            # Read the markdown content
            content = read_markdown_file(source_file)

            # Translate the content
            print(f"Translating {source_file}...")
            translated_content = translate_with_vllm(content)

            if translated_content:
                # Save the translated content
                save_translated_markdown(translated_content, target_file)
            else:
                print(f"Translation failed for {source_file}")


def main():
    print("Starting translation of all markdown files from docs/en to docs/de...")
    process_directory()
    print("Translation process completed.")


if __name__ == "__main__":
    main()
