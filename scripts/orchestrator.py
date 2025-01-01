import yaml
import random
import os
import frontmatter
from generate_questions import generate_loop_question

def load_questions(directory):
    questions = []
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            path = os.path.join(directory, filename)
            post = frontmatter.load(path)
            questions.append(post)
    return questions

def select_template(question_type):
    if question_type == "programmatic":
        return "templates/apply_code.md"
    elif question_type == "knowledge":
        return "templates/knowledge_definition.md"
    elif question_type == "conceptual":
        return "templates/conceptual_question.md"
    else:
        raise ValueError(f"Unknown question type: {question_type}")

def create_assignment(config):
    concept_questions = load_questions('questions')
    
    assignment_content = "# Assignment\n\n"

    # Select knowledge questions
    num_knowledge_questions = config.get("num_knowledge_questions", 0)
    selected_knowledge_questions = random.sample(concept_questions, num_knowledge_questions)

    for question in selected_knowledge_questions:
        template_path = select_template("knowledge")
        with open(template_path, 'r') as f:
            template_content = f.read()
        
        # Replace placeholders with front matter values
        filled_template = template_content.replace("<<CONCEPT_TITLE>>", question.metadata.get("title", ""))
        filled_template = filled_template.replace("<<QUESTION_TEXT>>", question.content)

        assignment_content += filled_template + "\n\n"

    # Generate programmatic questions
    num_programmatic_questions = config.get("num_programmatic_questions", 0)
    for _ in range(num_programmatic_questions):
        output_path = generate_loop_question()
        question = frontmatter.load(output_path)
        template_path = select_template("programmatic")
        with open(template_path, 'r') as f:
            template_content = f.read()

        # Replace placeholders with front matter values
        filled_template = template_content.replace("<<CODE_SNIPPET>>", question.metadata.get("code_snippet", ""))
        filled_template = filled_template.replace("<<QUESTION_TEXT>>", question.content)

        assignment_content += filled_template + "\n\n"

    with open('assignment.md', 'w') as f:
        f.write(assignment_content)

if __name__ == "__main__":
    config = {
        "num_knowledge_questions": 1,
        "num_programmatic_questions": 1,
        "topics": ["arrays"],
        "bloom_levels": ["knowledge"]
    }
    create_assignment(config) 