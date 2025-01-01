# Question Generator

A tool for generating and managing course questions, combining hand-made questions, programmatically generated exercises, and textbook-extracted content.

## Table of Contents
- [Directory Structure](#directory-structure)
- [Question Types](#question-types)
  - [Loop Questions](#loop-questions)
  - [Expression Questions](#expression-questions)
- [Adding Questions](#adding-questions)
  - [Manual Creation](#1-manual-question-creation)
  - [Programmatic Generation](#2-generating-programmatic-questions)
  - [Textbook Extraction](#3-extracting-questions-from-textbook)
- [Generating Assignments](#generating-assignments)
- [Templates](#templates)
- [Best Practices](#best-practices)
- [Common Tasks](#common-tasks)
- [Troubleshooting](#troubleshooting)
- [Dependencies](#dependencies)

## Directory Structure

```
course_materials/
├── textbook/           # Course textbook content in Markdown
│   └── chapter1.md
│   └── chapter2.md
├── scripts/           # Core scripts for generating and managing questions
│   ├── extract_definitions.py
│   ├── generate_questions.py
│   └── orchestrator.py
├── templates/         # Templates for different question types
│   ├── apply_code.md
|   ├── knowledge_definition.md
│   ├── loop_mechanics.md
│   ├── infinite_loop.md
│   ├── nested_loop.md
│   ├── loop_invariant.md
│   ├── loop_off_by_one_concept.md
│   └── conceptual_question.md
└── questions/         # Individual question files
    ├── q_polymorphism_01.md
    └── q_arrays_basics_01.md
```

## Question Types

The system supports several types of loop-related questions, each designed to test different aspects of understanding:

### 1. Basic Loop Application
- Template: `apply_code.md`
- Tests basic understanding of loop execution
- Includes code tracing and iteration counting
- Generated using `generate_loop_question()`

### 2. Off-by-One Concepts
- Template: `loop_off_by_one_concept.md`
- Tests understanding of common boundary errors
- Includes variations for:
  - Basic counting loops
  - Array indexing
  - Complex boundary conditions
  - Expression-based conditions
- Generated using `generate_off_by_one_question()`

### 3. Loop Mechanics
- Template: `loop_mechanics.md`
- Tests detailed understanding of loop execution
- Includes:
  - Variable tracing tables
  - Step-by-step execution analysis
  - Loop component explanations
- Generated using `generate_loop_mechanics_question()`

### 4. Infinite Loops
- Template: `infinite_loop.md`
- Tests ability to identify and fix non-terminating loops
- Includes multiple loop variations
- Focuses on termination conditions
- Generated using `generate_infinite_loop_question()`

### 5. Nested Loops
- Template: `nested_loop.md`
- Tests understanding of nested loop behavior
- Includes:
  - Iteration counting
  - Pattern recognition
  - Time complexity analysis
- Generated using `generate_nested_loop_question()`

### 6. Loop Invariants
- Template: `loop_invariant.md`
- Tests understanding of loop correctness
- Includes:
  - Invariant identification
  - Correctness proofs
  - Termination analysis
- Generated using `generate_loop_invariant_question()`

### Expression Questions

The system supports several types of expression evaluation questions:

#### 1. Boolean Expression Evaluation
- Template: `boolean_expression.md`
- Tests understanding of:
  - Operator precedence (AND, OR, NOT)
  - Short-circuit evaluation
  - De Morgan's Law
- Generated using `generate_boolean_expression_question()`
- Difficulty levels:
  - Level 1: Basic precedence
  - Level 2: Short-circuit evaluation
  - Level 3: Complex boolean logic and De Morgan's Law

#### 2. Numeric Expression Evaluation
- Template: `numeric_expression.md`
- Tests understanding of:
  - Arithmetic operator precedence
  - Integer division and modulo
  - Type conversion in mixed arithmetic
- Generated using `generate_numeric_expression_question()`
- Difficulty levels:
  - Level 1: Basic arithmetic precedence
  - Level 2: Integer division and modulo
  - Level 3: Mixed type arithmetic

#### 3. Mixed Expression Evaluation
- Template: `mixed_expression.md`
- Tests understanding of:
  - Combining arithmetic and boolean operations
  - Comparison operators
  - Floating-point precision issues
- Generated using `generate_mixed_expression_question()`
- Difficulty levels:
  - Level 2: Basic mixed operations
  - Level 3: Floating-point comparison

## Expression and Truth Table Questions

The question generator includes comprehensive support for various types of expression evaluation and truth table questions:

### Boolean Expression Questions
- Basic operator precedence (AND, OR, NOT)
- Short-circuit evaluation
- De Morgan's Law applications
- Multiple NOT operations
- XOR operations
- Logical implications
- Complex nested expressions

### Numeric Expression Questions
- Integer arithmetic with operator precedence
- Integer division and modulo operations
  - Special focus on negative number behavior
  - Edge cases with division and modulo
- Mixed-type arithmetic
  - Integer and floating-point combinations
  - Multiple type conversions
  - Precision considerations

### Truth Table Variations
1. Basic Operations (Level 1)
   - AND/OR truth tables
   - XOR (exclusive OR) operations
   - Simple NOT combinations

2. Intermediate Concepts (Level 2)
   - Logical implications (if-then)
   - Multiple NOT operations
   - Three-variable expressions
   - Operator precedence without parentheses

3. Advanced Topics (Level 3)
   - Complex XOR combinations
   - Nested operations with multiple operators
   - Complex implications
   - Truth tables with hidden inputs

Each question type includes:
- Clear instructions and setup
- Intermediate calculation steps (where appropriate)
- Focus points for key concepts
- Additional tasks for deeper understanding
- Difficulty-appropriate hints

### Using the Generators

To generate questions:

```python
# Generate a boolean expression question
generate_boolean_expression_question()

# Generate a numeric expression question
generate_numeric_expression_question()

# Generate a truth table question
generate_truth_table_question()
```

Each generator creates a Markdown file with:
- YAML front matter for metadata
- The question text and setup
- Appropriate placeholders for student work
- Additional tasks and hints
- Difficulty level indicators

## Generating Questions

You can generate questions using the Python script:

```python
from scripts.generate_questions import (
    generate_loop_question,
    generate_off_by_one_question,
    generate_loop_mechanics_question,
    generate_infinite_loop_question,
    generate_nested_loop_question,
    generate_loop_invariant_question,
    generate_boolean_expression_question,
    generate_numeric_expression_question,
    generate_mixed_expression_question
)

# Generate a basic loop question
generate_loop_question()

# Generate an off-by-one question with custom difficulty
generate_off_by_one_question()

# Generate other question types
generate_loop_mechanics_question()
generate_infinite_loop_question()
generate_nested_loop_question()
generate_loop_invariant_question()

# Generate a boolean expression question
generate_boolean_expression_question()

# Generate a numeric expression question with custom settings
generate_numeric_expression_question(
    output_dir="questions",    # Output directory
    id_prefix="num_expr"       # Prefix for question ID
)

# Generate a mixed expression question
generate_mixed_expression_question()
```

### Customizing Question Generation

Each generator function accepts parameters to customize the output:

```python
# Example: Generate a loop question with custom ranges
generate_loop_question(
    start_range=(1, 10),  # Range for start value
    end_range=(11, 20),   # Range for end value
    id_prefix="gen_loop"  # Prefix for question ID
)

# Example: Generate an off-by-one question
generate_off_by_one_question(
    output_dir="questions",  # Output directory
    id_prefix="off_by_one"   # Prefix for question ID
)
```

## Adding Questions

There are three ways to add questions to the system:

### 1. Manual Question Creation

To manually create a question:

1. Create a new Markdown file in the `questions/` directory with a descriptive name (e.g., `q_loops_basics_02.md`).
2. Add the YAML front matter at the top of the file:

```markdown
---
id: q_loops_basics_02
question_text: "Your question text here"
metadata:
  topic: "loops"          # Topic area
  bloom_level: "apply"    # knowledge, understand, apply, analyze, evaluate, create
  difficulty: 2           # 1 (easiest) to 5 (hardest)
  tags: ["loops", "basics"]
---

## Question:

Your question text here.

[Optional] Code snippet or additional content.
```

**Required Metadata Fields:**
- `id`: Unique identifier for the question
- `topic`: Main topic area
- `bloom_level`: One of: knowledge, understand, apply, analyze, evaluate, create
- `difficulty`: Integer from 1-5
- `tags`: List of relevant tags

### 2. Generating Programmatic Questions

Use `generate_questions.py` to create parameterized questions:

```bash
python scripts/generate_questions.py
```

This will:
1. Generate a loop question with random parameters
2. Save it as a new Markdown file in `questions/`

To customize the generation:

```python
from generate_questions import generate_loop_question

# Generate a loop question with custom ranges
generate_loop_question(
    start_range=(1, 10),
    end_range=(11, 20),
    id_prefix="gen_loop"
)
```

### 3. Extracting Questions from Textbook

To extract definition-style questions from your textbook:

1. Add definition callouts in your textbook Markdown:

```markdown
[!definition] Value Type
A value type in C# is a type that holds data directly rather than by reference.
```

2. Run the extraction script:

```bash
python scripts/extract_definitions.py
```

This will:
- Scan all Markdown files in `textbook/`
- Extract definitions and create corresponding question files in `questions/`

## Generating Assignments

Use the orchestrator to create assignments:

```python
from scripts/orchestrator import create_assignment

config = {
    "num_knowledge_questions": 2,    # Number of knowledge-level questions
    "num_programmatic_questions": 1, # Number of generated questions
    "topics": ["arrays", "loops"],   # Filter by topics
    "bloom_levels": ["knowledge", "apply"] # Filter by Bloom's level
}

create_assignment(config)
```

This will:
1. Select questions matching your criteria
2. Format them using appropriate templates
3. Generate `assignment.md`

## Templates

Templates in the `templates/` directory define how different question types are formatted:

### apply_code.md
- For code-based questions
- Uses `<<CODE_SNIPPET>>` placeholder

### knowledge_definition.md
- For definition questions
- Uses `<<CONCEPT_TITLE>>` placeholder

### conceptual_question.md
- For general conceptual questions
- Uses `<<QUESTION_TEXT>>` placeholder

## Best Practices

1. **Question Writing:**
   - Make questions clear and specific
   - Include example answers where appropriate
   - Use consistent formatting for code snippets

2. **Metadata:**
   - Use consistent topic names
   - Assign appropriate difficulty levels
   - Include relevant tags for better filtering

3. **File Organization:**
   - Use descriptive filenames
   - Maintain consistent front matter structure
   - Keep one question per file

## Common Tasks

### Adding a New Question Type

1. Create a new template in `templates/`
2. Add generation function in `generate_questions.py`
3. Update `orchestrator.py` to handle the new type

### Modifying Existing Questions

1. Open the question's `.md` file in `questions/`
2. Edit the front matter or question content
3. Save the file - no additional steps needed

### Bulk Operations

To modify multiple questions:

```python
import frontmatter
import os

for filename in os.listdir('questions'):
    if filename.endswith('.md'):
        post = frontmatter.load(f'questions/{filename}')
        # Make changes to post.metadata or post.content
        frontmatter.dump(post, f'questions/{filename}')
```

## Troubleshooting

1. **Invalid YAML Front Matter:**
   - Ensure proper indentation
   - Check for special characters
   - Verify all required fields are present

2. **Missing Templates:**
   - Verify template files exist in `templates/`
   - Check template names in `orchestrator.py`

3. **Generation Issues:**
   - Check directory permissions
   - Verify Python dependencies are installed
   - Check for valid ranges in generation parameters

## Dependencies

Required Python packages:
```bash
pip install pyyaml python-frontmatter
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

[MIT License](LICENSE) 

### Variable and Assignment Questions

The system supports several types of variable-related questions:

#### 1. Assignment vs Equality
- Template: `variable_assignment_equality.md`
- Tests understanding of:
  - Assignment (`=`) vs equality (`==`) operators
  - Common bugs in conditions
  - State changes from assignments
- Generated using `generate_variable_assignment_question()`
- Difficulty levels:
  - Level 1: Basic assignment vs equality
  - Level 2: Multiple assignments in conditions
  - Level 3: Nested conditions with assignments

#### 2. Variable Scope
- Template: `variable_scope.md`
- Tests understanding of:
  - Block scope boundaries
  - Variable shadowing
  - Variable lifetime
  - Variable accessibility
- Generated using `generate_variable_scope_question()`
- Difficulty levels:
  - Level 1: Basic scope rules
  - Level 2: Variable shadowing
  - Level 3: Complex nested scopes

#### 3. Variable State Tracking
- Template: `variable_state.md`
- Tests understanding of:
  - State changes over time
  - Dependencies between variables
  - Conditional state changes
- Generated using `generate_variable_state_question()`
- Difficulty levels:
  - Level 1: Basic state changes
  - Level 2: Conditional state changes
  - Level 3: Complex dependencies

### Using the Variable Question Generators

You can generate variable-related questions using the Python script:

```python
from scripts.generate_questions import (
    generate_variable_assignment_question,
    generate_variable_scope_question,
    generate_variable_state_question
)

# Generate an assignment vs equality question
generate_variable_assignment_question()

# Generate a scope question with custom settings
generate_variable_scope_question(
    output_dir="questions",    # Output directory
    id_prefix="scope"         # Prefix for question ID
)

# Generate a state tracking question
generate_variable_state_question()
```

Each generator creates questions that include:
- Clear code examples
- State tables for tracking changes
- Scope analysis where relevant
- Step-by-step execution traces
- Common pitfalls and bugs to identify
- Detailed explanations required from students 