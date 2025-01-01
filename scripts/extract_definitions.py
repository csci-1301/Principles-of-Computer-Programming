import re
import yaml
import os
from pathlib import Path

# Get the script's directory
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent

def load_template(template_name):
    """Load a template from the templates directory."""
    template_path = PROJECT_ROOT / 'templates' / template_name
    with open(template_path, 'r') as f:
        return f.read()

def substitute_placeholders(template_content, replacements):
    """Replace placeholders in template with actual values."""
    for key, value in replacements.items():
        placeholder = f"<<{key}>>"
        template_content = template_content.replace(placeholder, value)
    return template_content

def extract_definitions_from_markdown(file_path):
    """Extract definition blocks from markdown files."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    print(f"Processing file: {file_path}")
    print("Content preview:")
    print(content[:500])  # Print first 500 chars to see what we're working with
    
    # Updated regex to handle definitions inside abstract blocks
    pattern = r'(?i)>\[!abstract\]\s*([^\n]+)\n+>>\[!definition\]\s*\n+((?:(?!>>\[!).*?\n)+)'
    matches = re.findall(pattern, content, flags=re.MULTILINE | re.DOTALL)
    
    print(f"\nFound {len(matches)} matches")
    for i, match in enumerate(matches):
        print(f"\nMatch {i+1}:")
        print(f"Title: {match[0].strip()}")
        print(f"Body: {match[1].strip()[:100]}...")  # Print first 100 chars of body
    
    results = []
    for match in matches:
        title = match[0].strip()
        definition_body = match[1].strip()
        results.append((title, definition_body))
    return results

def generate_definition_question(title, definition_body, output_dir="questions", id_prefix="def"):
    """Generate a question from a definition using the knowledge_definition.md template."""
    
    # Generate unique ID based on sanitized title
    sanitized_title = re.sub(r'[^a-zA-Z0-9]', '_', title.lower())
    unique_id = f"{id_prefix}_{sanitized_title}"
    
    # Create front matter
    front_matter = {
        "id": unique_id,
        "metadata": {
            "topic": "definitions",
            "bloom_level": "knowledge",
            "difficulty": 1,
            "tags": ["definitions", "concepts", "terminology"]
        }
    }
    
    # Load template
    template_content = load_template('knowledge_definition.md')
    
    # Create example usage or application
    example_usage = f"Provide an example where understanding {title.lower()} is crucial in programming."
    
    # Replace placeholders
    replacements = {
        "CONCEPT_TITLE": title,
        "CONCEPT_DEFINITION": definition_body,
        "EXAMPLE_USAGE": example_usage,
        "RELATED_CONCEPTS": "List related programming concepts and explain their relationships.",
        "COMMON_MISCONCEPTIONS": f"What are common misconceptions about {title.lower()}?",
        "PRACTICAL_IMPLICATIONS": f"How does {title.lower()} affect program behavior and design?"
    }
    filled_template = substitute_placeholders(template_content, replacements)
    
    # Create final content
    markdown_content = "---\n"
    markdown_content += yaml.dump(front_matter, default_flow_style=False)
    markdown_content += "---\n\n"
    markdown_content += filled_template
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Write to file
    file_path = f"{output_dir}/{unique_id}.md"
    with open(file_path, 'w') as f:
        f.write(markdown_content)
    
    return file_path

def process_textbook_definitions(textbook_dir="textbook", output_dir="questions"):
    """Process all markdown files in the textbook directory and generate questions."""
    generated_files = []
    
    print(f"\nLooking for markdown files in: {textbook_dir}")
    files = os.listdir(textbook_dir)
    print(f"Found files: {files}")
    
    for filename in files:
        if filename.endswith('.md'):
            file_path = os.path.join(textbook_dir, filename)
            print(f"\nProcessing: {filename}")
            definitions = extract_definitions_from_markdown(file_path)
            print(f"Found {len(definitions)} definitions in {filename}")
            
            for title, definition_body in definitions:
                question_file = generate_definition_question(
                    title=title,
                    definition_body=definition_body,
                    output_dir=output_dir
                )
                generated_files.append(question_file)
                print(f"Generated question file: {question_file}")
    
    return generated_files

if __name__ == "__main__":
    textbook_dir = 'textbook'
    output_dir = 'questions'
    
    # Process all definitions and generate questions
    generated_files = process_textbook_definitions(textbook_dir, output_dir)
    
    # Print summary
    print(f"Generated {len(generated_files)} definition questions:")
    for file_path in generated_files:
        print(f"- {file_path}") 