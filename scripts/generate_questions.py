import random
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

def generate_loop_question(output_dir="questions", start_range=(1, 5), end_range=(6, 15), id_prefix="gen_loop"):
    """Generate a loop question using the apply_code.md template."""
    start = random.randint(start_range[0], start_range[1])
    end = random.randint(end_range[0], end_range[1])
    
    # Generate a unique ID
    unique_id = f"{id_prefix}_{random.randint(1000, 9999)}"
    
    # Create the code snippet and question text
    code_snippet = f"```csharp\nfor(int i = {start}; i < {end}; i++) {{ /* ... */ }}\n```"
    question_text = f"Explain what this loop does for i = {start} to {end - 1}."
    
    # Create front matter
    front_matter = {
        "id": unique_id,
        "question_text": question_text,
        "metadata": {
            "topic": "loops",
            "bloom_level": "apply",
            "difficulty": 2,
            "tags": ["loops", "iteration"]
        }
    }
    
    # Load the template
    template_content = load_template('apply_code.md')
    
    # Replace placeholders
    replacements = {
        "CODE_SNIPPET": code_snippet,
        "QUESTION_TEXT": question_text
    }
    filled_template = substitute_placeholders(template_content, replacements)
    
    # Add front matter to the filled template
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

def generate_off_by_one_question(output_dir="questions", id_prefix="off_by_one"):
    """Generate an off-by-one concept question with parameterized variations."""
    
    # Helper function to generate array-related code
    def generate_array_code(size, operation):
        array_name = random.choice(["numbers", "values", "data", "items"])
        if operation == "print":
            return f"for(int i = 0; i < {array_name}.Length - 1; i++) {{ Console.WriteLine({array_name}[i]); }}"
        elif operation == "process":
            return f"for(int i = 1; i <= {size}; i++) {{ {array_name}[i] = i * 2; }}"
        return f"for(int i = 0; i < {array_name}.Length - 1; i++) {{ {array_name}[i] = i; }}"

    # Generate random ranges for number sequences
    start = random.randint(1, 5)
    end = random.randint(start + 3, start + 8)
    size = random.randint(5, 10)

    # Define possible variations with parameterization
    variations = [
        # Basic off-by-one with random range
        {
            "loop_code": f"for(int i = {start}; i < {end}; i++) {{ Console.WriteLine(i); }}",
            "intention": f"print the numbers {start} through {end}",
            "hint_focus": "termination",
            "difficulty": 2
        },
        # Including zero unintentionally
        {
            "loop_code": f"for(int i = 0; i <= {end}; i++) {{ Console.WriteLine(i); }}",
            "intention": f"print the numbers 1 through {end}",
            "hint_focus": "starting",
            "difficulty": 2
        },
        # Array indexing error with size parameter
        {
            "loop_code": generate_array_code(size, "process"),
            "intention": f"fill an array of size {size} with even numbers (2, 4, 6, etc.)",
            "hint_focus": "array indexing",
            "difficulty": 3
        },
        # Missing last array element
        {
            "loop_code": generate_array_code(size, "print"),
            "intention": "print all elements in the array",
            "hint_focus": "array length calculation",
            "difficulty": 3
        },
        # Subtle expression-based condition (harder)
        {
            "loop_code": f"for(int i = 0; i < (size + 1) / 2; i++) {{ Process(i); }}",
            "intention": "process half of the elements (rounded up)",
            "hint_focus": "division expression",
            "difficulty": 4
        },
        # Complex boundary condition
        {
            "loop_code": f"while(start + offset < end - 1) {{ Process(start + offset++); }}",
            "intention": "process all values between start and end",
            "hint_focus": "compound condition",
            "difficulty": 4
        }
    ]
    
    # Choose a random variation
    variation = random.choice(variations)
    
    # Generate a unique ID
    unique_id = f"{id_prefix}_{random.randint(1000, 9999)}"
    
    # Create front matter
    front_matter = {
        "id": unique_id,
        "metadata": {
            "topic": "loops",
            "bloom_level": "analyze",
            "difficulty": variation["difficulty"],
            "tags": ["loops", "off-by-one", "debugging"]
        }
    }
    
    # Load the template
    template_content = load_template('loop_off_by_one_concept.md')
    
    # Replace placeholders
    replacements = {
        "LOOP_CODE": variation["loop_code"],
        "INTENTION": variation["intention"],
        "HINT_FOCUS": variation["hint_focus"]
    }
    filled_template = substitute_placeholders(template_content, replacements)
    
    # Add front matter to the filled template
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

def generate_loop_mechanics_question(output_dir="questions", id_prefix="loop_mechanics"):
    """Generate a question testing understanding of loop mechanics."""
    # Implementation coming in next message...

def generate_infinite_loop_question(output_dir="questions", id_prefix="infinite_loop"):
    """Generate a question about identifying and fixing infinite loops."""
    # Implementation coming in next message...

def generate_loop_invariant_question(output_dir="questions", id_prefix="loop_invariant"):
    """Generate a question about loop invariants."""
    # Implementation coming in next message...

def generate_nested_loop_question(output_dir="questions", id_prefix="nested_loop"):
    """Generate a question about nested loops."""
    # Implementation coming in next message...

def generate_boolean_expression_question(output_dir="questions", id_prefix="bool_expr"):
    """Generate a boolean expression evaluation question."""
    
    # Define possible variations
    variations = [
        # Basic boolean precedence
        {
            "expression": "true || false && false",
            "initial_values": "All values are boolean literals",
            "evaluation_steps": "1. false && false = false\n2. true || false = true",
            "concepts": "operator precedence with AND (&&) and OR (||)",
            "focus_point": "AND has higher precedence than OR",
            "hint_text": "Evaluate AND operations before OR operations",
            "extra_task": "How would adding parentheses around 'true || false' change the result?",
            "difficulty": 1
        },
        # Short-circuit evaluation
        {
            "expression": "(x > 5) && (y++ < 10)",
            "initial_values": "x = 3, y = 7",
            "evaluation_steps": "1. x > 5 = false\n2. Second part not evaluated due to short-circuiting",
            "concepts": "short-circuit evaluation of boolean expressions",
            "focus_point": "the right side of AND won't execute if the left is false",
            "hint_text": "Consider what happens when the left side of && is false",
            "extra_task": "What will be the value of y after this expression is evaluated?",
            "difficulty": 2
        },
        # De Morgan's Law
        {
            "expression": "!(a && b) || (c && !b)",
            "initial_values": "a = true, b = false, c = true",
            "evaluation_steps": "1. !b = true\n2. a && b = false\n3. !(false) = true\n4. c && true = true\n5. true || true = true",
            "concepts": "De Morgan's Law and operator precedence",
            "focus_point": "how NOT affects boolean expressions",
            "hint_text": "Apply NOT operations first, then evaluate AND, finally OR",
            "extra_task": "Rewrite this expression using De Morgan's Law",
            "difficulty": 3
        }
    ]
    
    # Choose a random variation
    variation = random.choice(variations)
    
    # Generate unique ID
    unique_id = f"{id_prefix}_{random.randint(1000, 9999)}"
    
    # Create front matter
    front_matter = {
        "id": unique_id,
        "metadata": {
            "topic": "expressions",
            "bloom_level": "analyze",
            "difficulty": variation["difficulty"],
            "tags": ["boolean", "operators", "precedence"]
        }
    }
    
    # Load template
    template_content = load_template('boolean_expression.md')
    
    # Replace placeholders
    replacements = {
        "EXPRESSION": variation["expression"],
        "INITIAL_VALUES": variation["initial_values"],
        "EVALUATION_STEPS": variation["evaluation_steps"],
        "CONCEPTS": variation["concepts"],
        "FOCUS_POINT": variation["focus_point"],
        "HINT_TEXT": variation["hint_text"],
        "EXTRA_TASK": variation["extra_task"]
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

def generate_numeric_expression_question(output_dir="questions", id_prefix="num_expr"):
    """Generate a parameterized numeric expression evaluation question."""
    
    def generate_expression(complexity):
        """Generate a random numeric expression of given complexity."""
        if complexity == 1:
            a = random.randint(5, 20)
            b = random.randint(2, 10)
            c = random.randint(2, 8)
            ops = [
                (f"{a} + {b} * {c}", f"{b} * {c} = {b*c}\n{a} + {b*c} = {a + b*c}"),
                (f"{a} - {b} / {c}", f"{b} / {c} = {b//c}\n{a} - {b//c} = {a - b//c}"),
                (f"{a} * ({b} + {c})", f"{b} + {c} = {b+c}\n{a} * {b+c} = {a*(b+c)}")
            ]
            return random.choice(ops)
        elif complexity == 2:
            a = random.randint(10, 30)
            b = random.randint(2, 6)
            c = random.randint(3, 9)
            # Add negative numbers for modulo
            neg_a = -a
            ops = [
                (f"({a} / {b}) * {c} + {a} % {b}", 
                 f"{a} / {b} = {a//b}\n{a} % {b} = {a%b}\n({a//b}) * {c} = {(a//b)*c}\n{(a//b)*c} + {a%b} = {(a//b)*c + a%b}"),
                (f"{neg_a} % {b} + {c} * ({a} / {b})",
                 f"{neg_a} % {b} = {neg_a%b}\n{a} / {b} = {a//b}\n{c} * {a//b} = {c*(a//b)}\n{neg_a%b} + {c*(a//b)} = {neg_a%b + c*(a//b)}"),
                (f"({a} + {b}) / {c} * ({a} % {c})",
                 f"{a} + {b} = {a+b}\n{a} % {c} = {a%c}\n({a+b}) / {c} = {(a+b)//c}\n{(a+b)//c} * {a%c} = {((a+b)//c) * (a%c)}")
            ]
            return random.choice(ops)
        else:
            # Mixed types with multiple conversions
            a = random.randint(5, 15)
            b = round(random.uniform(1.5, 4.5), 1)
            c = random.randint(2, 8)
            d = round(random.uniform(0.1, 0.9), 1)
            ops = [
                (f"{a} / {b} + {c} * {d}",
                 f"{a} / {b} = {a/b:.2f}\n{c} * {d} = {c*d:.2f}\n{a/b:.2f} + {c*d:.2f} = {a/b + c*d:.2f}"),
                (f"({a} + {c}) / {b} - {d} * {c}",
                 f"{a} + {c} = {a+c}\n{d} * {c} = {d*c:.2f}\n({a+c}) / {b} = {(a+c)/b:.2f}\n{(a+c)/b:.2f} - {d*c:.2f} = {(a+c)/b - d*c:.2f}"),
                (f"{a} * {d} / ({b} + {c})",
                 f"{a} * {d} = {a*d:.2f}\n{b} + {c} = {b+c:.2f}\n{a*d:.2f} / {b+c:.2f} = {(a*d)/(b+c):.2f}")
            ]
            return random.choice(ops)
    
    # Define possible variations with parameterized expressions
    variations = [
        # Level 1: Basic arithmetic precedence
        {
            "expression": generate_expression(1),
            "data_types": "All integers",
            "concepts": "operator precedence with arithmetic operators",
            "focus_point": "multiplication and division before addition and subtraction",
            "hint_text": "Remember PEMDAS (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction)",
            "extra_task": "How would adding parentheses around the first two numbers change the result?",
            "difficulty": 1
        },
        # Level 2: Integer division and modulo
        {
            "expression": generate_expression(2),
            "data_types": "All integers",
            "concepts": "integer division truncation and modulo operator",
            "focus_point": "how integer division discards the remainder",
            "hint_text": "Remember that integer division truncates the decimal part",
            "extra_task": "What would be different if these were floating-point numbers?",
            "difficulty": 2
        },
        # Level 3: Mixed type arithmetic
        {
            "expression": generate_expression(3),
            "data_types": "Mixed integers and doubles",
            "concepts": "type conversion in mixed arithmetic",
            "focus_point": "how mixing integers and doubles affects the result type",
            "hint_text": "When mixing integers and doubles, the result is always a double",
            "extra_task": "What would happen if you changed all numbers to integers?",
            "difficulty": 3
        }
    ]
    
    # Choose a random variation
    variation = random.choice(variations)
    
    # Generate unique ID
    unique_id = f"{id_prefix}_{random.randint(1000, 9999)}"
    
    # Create front matter
    front_matter = {
        "id": unique_id,
        "metadata": {
            "topic": "expressions",
            "bloom_level": "analyze",
            "difficulty": variation["difficulty"],
            "tags": ["arithmetic", "operators", "precedence"]
        }
    }
    
    # Load template
    template_content = load_template('numeric_expression.md')
    
    # Replace placeholders
    replacements = {
        "EXPRESSION": variation["expression"][0],
        "EVALUATION_STEPS": variation["expression"][1],
        "DATA_TYPES": variation["data_types"],
        "CONCEPTS": variation["concepts"],
        "FOCUS_POINT": variation["focus_point"],
        "HINT_TEXT": variation["hint_text"],
        "EXTRA_TASK": variation["extra_task"]
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

def generate_mixed_expression_question(output_dir="questions", id_prefix="mixed_expr"):
    """Generate a mixed expression evaluation question."""
    
    # Define possible variations
    variations = [
        # Comparison and arithmetic
        {
            "expression": "(x + 5 > y * 2) && (z % 2 == 0)",
            "variable_definitions": "x: int\ny: int\nz: int",
            "initial_values": "x = 10\ny = 3\nz = 4",
            "evaluation_steps": "1. x + 5 = 15\n2. y * 2 = 6\n3. 15 > 6 = true\n4. z % 2 = 0\n5. 0 == 0 = true\n6. true && true = true",
            "concepts": "mixing arithmetic and boolean operations",
            "focus_points": "arithmetic before comparison, comparison before boolean operations",
            "hint_text": "Evaluate arithmetic first, then comparisons, then boolean operations",
            "extra_task": "What values of x, y, and z would make this expression false?",
            "difficulty": 2
        },
        # Floating-point comparison
        {
            "expression": "Math.Abs((0.1 + 0.2) - 0.3) < 0.0001",
            "variable_definitions": "All floating-point operations",
            "initial_values": "Using floating-point literals",
            "evaluation_steps": "1. 0.1 + 0.2 ≈ 0.30000000000000004\n2. 0.30000000000000004 - 0.3 ≈ 0.00000000000000004\n3. Math.Abs(0.00000000000000004) < 0.0001 = true",
            "concepts": "floating-point precision and comparison",
            "focus_points": "why direct equality comparison with floating-point numbers is problematic",
            "hint_text": "Floating-point arithmetic isn't always exact",
            "extra_task": "Why is using Math.Abs and a small epsilon better than direct equality comparison?",
            "difficulty": 3
        }
    ]
    
    # Choose a random variation
    variation = random.choice(variations)
    
    # Generate unique ID
    unique_id = f"{id_prefix}_{random.randint(1000, 9999)}"
    
    # Create front matter
    front_matter = {
        "id": unique_id,
        "metadata": {
            "topic": "expressions",
            "bloom_level": "analyze",
            "difficulty": variation["difficulty"],
            "tags": ["mixed", "operators", "precedence", "comparison"]
        }
    }
    
    # Load template
    template_content = load_template('mixed_expression.md')
    
    # Replace placeholders
    replacements = {
        "EXPRESSION": variation["expression"],
        "VARIABLE_DEFINITIONS": variation["variable_definitions"],
        "INITIAL_VALUES": variation["initial_values"],
        "EVALUATION_STEPS": variation["evaluation_steps"],
        "CONCEPTS": variation["concepts"],
        "FOCUS_POINTS": variation["focus_points"],
        "HINT_TEXT": variation["hint_text"],
        "EXTRA_TASK": variation["extra_task"]
    }
    filled_template = substitute_placeholders(template_content, replacements)
    
    # Create final content
    markdown_content = "---\n"
    markdown_content += yaml.dump(front_matter, default_flow_style=False)
    markdown_content += "---\n\n"
    markdown_content += filled_template
    
    # Write to file
    file_path = f"{output_dir}/{unique_id}.md"
    with open(file_path, 'w') as f:
        f.write(markdown_content)
    
    return file_path

def generate_truth_table_question(output_dir="questions", id_prefix="truth_table"):
    """Generate a truth table question with parameterized expressions."""
    
    def generate_truth_table(variables, expression_template, show_inputs=True, show_intermediates=True):
        """Generate a truth table with specified variables and expression."""
        # Generate column headers
        headers = variables.copy()
        if show_intermediates:
            headers.extend(["<<INTERMEDIATE>>"])
        headers.append("Result")
        
        # Generate header separator
        separator = "|".join(["-" * len(header) for header in headers])
        
        # Generate all possible combinations of inputs
        num_vars = len(variables)
        rows = []
        for i in range(2 ** num_vars):
            row = []
            for j in range(num_vars):
                value = "T" if (i & (1 << j)) else "F"
                row.append(value if show_inputs else " ")
            if show_intermediates:
                row.extend([" "] * (2 if num_vars > 2 else 1))  # More space for intermediate steps
            row.append(" ")  # Space for final result
            rows.append("|".join(row))
        
        return {
            "headers": " | ".join(headers),
            "separator": separator,
            "rows": "\n".join(rows)
        }
    
    # Define possible variations
    variations = [
        # Level 1: Basic AND/OR
        {
            "variables": ["A", "B"],
            "expression": "A && B",
            "show_inputs": True,
            "show_intermediates": False,
            "concepts": "basic AND operation",
            "focus_point": "both inputs must be true for the result to be true",
            "hint_text": "AND is only true when both inputs are true",
            "extra_task": "What percentage of the rows result in true?",
            "difficulty": 1
        },
        {
            "variables": ["P", "Q"],
            "expression": "P || Q",
            "show_inputs": True,
            "show_intermediates": False,
            "concepts": "basic OR operation",
            "focus_point": "only one input needs to be true for the result to be true",
            "hint_text": "OR is false only when both inputs are false",
            "extra_task": "Compare this truth table with the AND truth table",
            "difficulty": 1
        },
        # Level 1: XOR
        {
            "variables": ["X", "Y"],
            "expression": "X ^ Y",
            "show_inputs": True,
            "show_intermediates": False,
            "concepts": "XOR (exclusive OR) operation",
            "focus_point": "XOR is true when inputs are different",
            "hint_text": "XOR is true when exactly one input is true",
            "extra_task": "How does XOR differ from regular OR?",
            "difficulty": 1
        },
        # Level 2: Implication
        {
            "variables": ["P", "Q"],
            "expression": "!P || Q  // P implies Q",
            "show_inputs": True,
            "show_intermediates": True,
            "concepts": "logical implication (if P then Q)",
            "focus_point": "implication is false only when P is true and Q is false",
            "hint_text": "Think about when 'if P then Q' would be false",
            "extra_task": "Why is !P || Q equivalent to 'if P then Q'?",
            "difficulty": 2
        },
        # Level 2: Multiple NOTs
        {
            "variables": ["A", "B"],
            "expression": "!(A && !B)",
            "show_inputs": True,
            "show_intermediates": True,
            "concepts": "multiple NOT operations",
            "focus_point": "how NOT distributes over AND/OR",
            "hint_text": "First find !B, then A && !B, finally apply outer NOT",
            "extra_task": "Convert this to an equivalent expression without using NOT",
            "difficulty": 2
        },
        # Level 2: Three variables with precedence
        {
            "variables": ["X", "Y", "Z"],
            "expression": "X && Y || Z",
            "show_inputs": True,
            "show_intermediates": True,
            "concepts": "operator precedence without parentheses",
            "focus_point": "AND has higher precedence than OR",
            "hint_text": "First find X && Y, then combine with Z using OR",
            "extra_task": "How would parentheses around 'Y || Z' change the results?",
            "difficulty": 2
        },
        # Level 3: Complex with XOR
        {
            "variables": ["P", "Q", "R"],
            "expression": "(P ^ Q) && !R",
            "show_inputs": False,
            "show_intermediates": True,
            "concepts": "XOR with other operations",
            "focus_point": "XOR precedence and combination with NOT",
            "hint_text": "First compute P ^ Q, then !R, finally combine with AND",
            "extra_task": "When does this expression evaluate to true?",
            "difficulty": 3
        },
        # Level 3: Complex implication
        {
            "variables": ["A", "B", "C"],
            "expression": "(A && B) -> C  // equivalent to !(A && B) || C",
            "show_inputs": False,
            "show_intermediates": True,
            "concepts": "complex implication with multiple conditions",
            "focus_point": "breaking down complex implications",
            "hint_text": "First find A && B, then apply the implication",
            "extra_task": "Write this using only AND, OR, and NOT operators",
            "difficulty": 3
        },
        # Level 3: Nested operations
        {
            "variables": ["P", "Q", "R"],
            "expression": "!(P && Q) || (Q ^ !R)",
            "show_inputs": False,
            "show_intermediates": True,
            "concepts": "nested operations with multiple operators",
            "focus_point": "order of operations with multiple operator types",
            "hint_text": "Break this into smaller sub-expressions",
            "extra_task": "How many intermediate steps are needed?",
            "difficulty": 3
        }
    ]
    
    # Choose a random variation
    variation = random.choice(variations)
    
    # Generate truth table
    table = generate_truth_table(
        variation["variables"],
        variation["expression"],
        variation["show_inputs"],
        variation["show_intermediates"]
    )
    
    # Generate instructions based on difficulty
    if variation["difficulty"] == 1:
        instructions = "Complete the Result column in the truth table below."
    elif variation["difficulty"] == 2:
        instructions = "Complete the intermediate steps and Result column in the truth table below."
    else:
        instructions = "Fill in all values in the truth table below, showing your work in the intermediate columns."
    
    # Generate unique ID
    unique_id = f"{id_prefix}_{random.randint(1000, 9999)}"
    
    # Create front matter
    front_matter = {
        "id": unique_id,
        "metadata": {
            "topic": "expressions",
            "bloom_level": "analyze",
            "difficulty": variation["difficulty"],
            "tags": ["boolean", "truth-tables", "operators"]
        }
    }
    
    # Load template
    template_content = load_template('truth_table.md')
    
    # Replace placeholders
    replacements = {
        "EXPRESSION": variation["expression"],
        "TABLE_INSTRUCTIONS": instructions,
        "COLUMN_HEADERS": table["headers"],
        "HEADER_SEPARATOR": table["separator"],
        "TABLE_ROWS": table["rows"],
        "CONCEPTS": variation["concepts"],
        "FOCUS_POINT": variation["focus_point"],
        "HINT_TEXT": variation["hint_text"],
        "EXTRA_TASK": variation["extra_task"]
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

def generate_variable_assignment_question(output_dir="questions", id_prefix="var_assign"):
    """Generate a question about variable assignment vs equality operators."""
    
    def generate_assignment_code(complexity):
        """Generate code snippets with assignment/equality scenarios."""
        if complexity == 1:
            # Basic assignment vs equality
            x = random.randint(5, 15)
            y = random.randint(1, 10)
            return (
                f"int x = {x};\n"
                f"int y = {y};\n"
                f"if (x = y)\n"
                f"{{\n"
                f"    Console.WriteLine($\"x is {y}\");\n"
                f"}}\n"
                f"Console.WriteLine($\"x is now {{x}}\");",
                f"x: {x}, y: {y}",
                "| Line # | x | y |\n"
                "|--------|---|---|\n"
                f"| 1      |{x}| - |\n"
                f"| 2      |{x}|{y}|\n"
                f"| 3      |{y}|{y}|\n"
                f"| 5      |{y}|{y}|"
            )
        elif complexity == 2:
            # Multiple assignments in conditions
            a = random.randint(1, 10)
            b = random.randint(11, 20)
            return (
                f"int a = {a};\n"
                f"int b = {b};\n"
                f"while (a = b)\n"
                f"{{\n"
                f"    Console.WriteLine(a);\n"
                f"    b--;\n"
                f"}}",
                f"a: {a}, b: {b}",
                "| Line # | a  | b  |\n"
                "|--------|----|----|"
            )
        else:
            # Complex nested conditions
            x = random.randint(1, 5)
            y = random.randint(6, 10)
            z = random.randint(11, 15)
            return (
                f"int x = {x};\n"
                f"int y = {y};\n"
                f"int z = {z};\n"
                f"if (x = y)\n"
                f"{{\n"
                f"    if (y = z)\n"
                f"    {{\n"
                f"        Console.WriteLine(\"All equal\");\n"
                f"    }}\n"
                f"}}\n"
                f"Console.WriteLine($\"x={{x}}, y={{y}}, z={{z}}\");",
                f"x: {x}, y: {y}, z: {z}",
                "| Line # | x | y | z |\n"
                "|--------|---|---|---|\n"
                f"| 1      |{x}| - | - |\n"
                f"| 2      |{x}|{y}| - |\n"
                f"| 3      |{x}|{y}|{z}|"
            )
    
    # Define possible variations
    variations = [
        # Level 1: Basic assignment vs equality
        {
            "code": generate_assignment_code(1),
            "context": "This code is attempting to compare two numbers",
            "concepts": "the difference between assignment (=) and equality comparison (==)",
            "focus_point": "using = in an if condition performs assignment, not comparison",
            "hint_text": "The = operator always performs assignment and returns the assigned value",
            "extra_task": "What would happen if you changed the = to == in the if condition?",
            "difficulty": 1
        },
        # Level 2: Multiple assignments
        {
            "code": generate_assignment_code(2),
            "context": "This code is trying to implement a counting loop",
            "concepts": "assignment operators in loop conditions",
            "focus_point": "assignment in a while condition creates an infinite loop if the assigned value is non-zero",
            "hint_text": "Think about what value is being assigned and returned in the while condition",
            "extra_task": "How many times will this loop execute? Why?",
            "difficulty": 2
        },
        # Level 3: Nested conditions
        {
            "code": generate_assignment_code(3),
            "context": "This code is checking for equality between three variables",
            "concepts": "nested conditions with assignments",
            "focus_point": "how assignments cascade through nested conditions",
            "hint_text": "Track how each assignment changes the values of x, y, and z",
            "extra_task": "Rewrite this code to correctly check for equality between all three variables",
            "difficulty": 3
        }
    ]
    
    # Choose a random variation
    variation = random.choice(variations)
    
    # Generate unique ID
    unique_id = f"{id_prefix}_{random.randint(1000, 9999)}"
    
    # Create front matter
    front_matter = {
        "id": unique_id,
        "metadata": {
            "topic": "variables",
            "bloom_level": "analyze",
            "difficulty": variation["difficulty"],
            "tags": ["variables", "assignment", "equality", "operators"]
        }
    }
    
    # Load template
    template_content = load_template('variable_assignment_equality.md')
    
    # Replace placeholders
    replacements = {
        "CODE_SNIPPET": variation["code"][0],
        "INITIAL_VALUES": variation["code"][1],
        "STATE_TABLE": variation["code"][2],
        "CONTEXT": variation["context"],
        "CONCEPTS": variation["concepts"],
        "FOCUS_POINT": variation["focus_point"],
        "HINT_TEXT": variation["hint_text"],
        "EXTRA_TASK": variation["extra_task"]
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

def generate_variable_scope_question(output_dir="questions", id_prefix="var_scope"):
    """Generate a question about variable scope and shadowing."""
    
    def generate_scope_code(complexity):
        """Generate code snippets with scope scenarios."""
        if complexity == 1:
            # Basic scope
            x = random.randint(5, 15)
            y = random.randint(1, 10)
            return (
                f"int x = {x};\n"
                f"{{\n"
                f"    int y = {y};\n"
                f"    Console.WriteLine($\"Inside: x={{x}}, y={{y}}\");\n"
                f"}}\n"
                f"Console.WriteLine($\"Outside: x={{x}}\");",
                "Variable x:\n"
                "- Scope: Lines 1-6\n"
                "- Accessible: Throughout entire code\n"
                "- No shadowing\n\n"
                "Variable y:\n"
                "- Scope: Lines 3-4\n"
                "- Accessible: Only inside the block\n"
                "- No shadowing",
                f"Line 1: x = {x}\n"
                f"Line 3: y = {y}\n"
                f"Line 4: prints \"Inside: x={x}, y={y}\"\n"
                f"Line 6: prints \"Outside: x={x}\""
            )
        elif complexity == 2:
            # Variable shadowing
            x = random.randint(5, 15)
            inner_x = random.randint(20, 30)
            return (
                f"int x = {x};\n"
                f"{{\n"
                f"    int x = {inner_x};\n"
                f"    Console.WriteLine($\"Inside: x={{x}}\");\n"
                f"}}\n"
                f"Console.WriteLine($\"Outside: x={{x}}\");",
                "Variable x (outer):\n"
                "- Scope: Lines 1-6\n"
                "- Accessible: Lines 1-2 and 5-6\n"
                "- Shadowed in lines 3-4\n\n"
                "Variable x (inner):\n"
                "- Scope: Lines 3-4\n"
                "- Shadows outer x\n"
                "- Only accessible inside the block",
                f"Line 1: outer x = {x}\n"
                f"Line 3: inner x = {inner_x} (shadows outer x)\n"
                f"Line 4: prints \"Inside: x={inner_x}\"\n"
                f"Line 6: prints \"Outside: x={x}\""
            )
        else:
            # Complex nested scopes
            a = random.randint(1, 5)
            b = random.randint(6, 10)
            c = random.randint(11, 15)
            return (
                f"int a = {a};\n"
                f"{{\n"
                f"    int b = {b};\n"
                f"    {{\n"
                f"        int a = {c};\n"
                f"        Console.WriteLine($\"Inner: a={{a}}, b={{b}}\");\n"
                f"    }}\n"
                f"    Console.WriteLine($\"Middle: a={{a}}, b={{b}}\");\n"
                f"}}\n"
                f"Console.WriteLine($\"Outer: a={{a}}\");",
                "Variable a (outer):\n"
                "- Scope: Lines 1-10\n"
                "- Shadowed in lines 5-7\n\n"
                "Variable b:\n"
                "- Scope: Lines 3-9\n"
                "- Accessible in all inner blocks\n\n"
                "Variable a (inner):\n"
                "- Scope: Lines 5-7\n"
                "- Shadows outer a",
                f"Line 1: outer a = {a}\n"
                f"Line 3: b = {b}\n"
                f"Line 5: inner a = {c}\n"
                f"Line 6: prints \"Inner: a={c}, b={b}\"\n"
                f"Line 8: prints \"Middle: a={a}, b={b}\"\n"
                f"Line 10: prints \"Outer: a={a}\""
            )
    
    # Define possible variations
    variations = [
        # Level 1: Basic scope
        {
            "code": generate_scope_code(1),
            "concepts": "basic variable scope and block visibility",
            "focus_point": "variables declared inside a block are only accessible within that block",
            "hint_text": "Pay attention to the curly braces - they define the boundaries of variable scope",
            "extra_task": "What would happen if you tried to access y after the closing brace?",
            "difficulty": 1
        },
        # Level 2: Variable shadowing
        {
            "code": generate_scope_code(2),
            "concepts": "variable shadowing and name resolution",
            "focus_point": "inner variables with the same name hide (shadow) outer variables",
            "hint_text": "When two variables have the same name, the innermost one is used",
            "extra_task": "How could you access the outer x value inside the block?",
            "difficulty": 2
        },
        # Level 3: Complex nested scopes
        {
            "code": generate_scope_code(3),
            "concepts": "nested scopes and multiple variable shadowing",
            "focus_point": "how variable shadowing works across multiple nested scopes",
            "hint_text": "Track each variable's visibility level by level",
            "extra_task": "Add code to access each version of variable 'a' where possible",
            "difficulty": 3
        }
    ]
    
    # Choose a random variation
    variation = random.choice(variations)
    
    # Generate unique ID
    unique_id = f"{id_prefix}_{random.randint(1000, 9999)}"
    
    # Create front matter
    front_matter = {
        "id": unique_id,
        "metadata": {
            "topic": "variables",
            "bloom_level": "analyze",
            "difficulty": variation["difficulty"],
            "tags": ["variables", "scope", "shadowing", "lifetime"]
        }
    }
    
    # Load template
    template_content = load_template('variable_scope.md')
    
    # Replace placeholders
    replacements = {
        "CODE_SNIPPET": variation["code"][0],
        "SCOPE_ANALYSIS": variation["code"][1],
        "EXECUTION_TRACE": variation["code"][2],
        "CONCEPTS": variation["concepts"],
        "FOCUS_POINT": variation["focus_point"],
        "HINT_TEXT": variation["hint_text"],
        "EXTRA_TASK": variation["extra_task"]
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

def generate_variable_state_question(output_dir="questions", id_prefix="var_state"):
    """Generate a question about tracking variable state changes."""
    
    def generate_state_code(complexity):
        """Generate code snippets with state tracking scenarios."""
        if complexity == 1:
            # Basic state changes
            x = random.randint(5, 15)
            y = random.randint(1, 10)
            z = x + y
            return (
                f"int x = {x};\n"
                f"int y = {y};\n"
                f"int z = x + y;\n"
                f"x = z - y;\n"
                f"y = x - z;",
                "x, y, z",
                "|----|---|---|---|\n"
                f"| 1  |{x}| - | - |\n"
                f"| 2  |{x}|{y}| - |\n"
                f"| 3  |{x}|{y}|{z}|\n"
                f"| 4  |{z-y}|{y}|{z}|\n"
                f"| 5  |{z-y}|{z-y-z}|{z}|",
                f"Final values:\nx = {z-y}\ny = {z-y-z}\nz = {z}\n\n"
                "Changes occurred due to:\n"
                "1. Initial assignments\n"
                "2. Addition operation\n"
                "3. Subtraction and reassignment"
            )
        elif complexity == 2:
            # Conditional state changes
            a = random.randint(1, 10)
            b = random.randint(5, 15)
            return (
                f"int a = {a};\n"
                f"int b = {b};\n"
                f"if (a < b)\n"
                f"{{\n"
                f"    a = b;\n"
                f"    b = a / 2;\n"
                f"}}\n"
                f"else\n"
                f"{{\n"
                f"    b = a;\n"
                f"    a = b * 2;\n"
                f"}}",
                "a, b",
                "|----|---|---|\n"
                f"| 1  |{a}| - |\n"
                f"| 2  |{a}|{b}|\n"
                f"| 5  |{b}|{b}|\n"
                f"| 6  |{b}|{b//2}|",
                f"Final values:\na = {b}\nb = {b//2}\n\n"
                "Changes occurred due to:\n"
                "1. Initial assignments\n"
                "2. Conditional execution (a < b)\n"
                "3. Sequential assignments in if block"
            )
        else:
            # Complex dependencies
            x = random.randint(2, 5)
            y = random.randint(3, 7)
            z = random.randint(4, 8)
            return (
                f"int x = {x};\n"
                f"int y = {y};\n"
                f"int z = {z};\n"
                f"x = y * z;\n"
                f"y = z * x;\n"
                f"z = x * y;",
                "x, y, z",
                "|----|---|---|---|\n"
                f"| 1  |{x}| - | - |\n"
                f"| 2  |{x}|{y}| - |\n"
                f"| 3  |{x}|{y}|{z}|\n"
                f"| 4  |{y*z}|{y}|{z}|\n"
                f"| 5  |{y*z}|{z*(y*z)}|{z}|\n"
                f"| 6  |{y*z}|{z*(y*z)}|{(y*z)*(z*(y*z))}|",
                f"Final values:\nx = {y*z}\ny = {z*(y*z)}\nz = {(y*z)*(z*(y*z))}\n\n"
                "Changes occurred due to:\n"
                "1. Initial assignments\n"
                "2. Multiplication and dependencies\n"
                "3. Order of operations affecting final values"
            )
    
    # Define possible variations
    variations = [
        # Level 1: Basic state changes
        {
            "code": generate_state_code(1),
            "concepts": "basic variable state changes and dependencies",
            "focus_point": "how each assignment affects variable values",
            "hint_text": "Track each variable's value line by line",
            "extra_task": "What would happen if you swapped lines 4 and 5?",
            "difficulty": 1
        },
        # Level 2: Conditional state changes
        {
            "code": generate_state_code(2),
            "concepts": "conditional execution and state changes",
            "focus_point": "how conditions affect which state changes occur",
            "hint_text": "First determine which branch executes, then track changes",
            "extra_task": "What would be the final values if the initial values were swapped?",
            "difficulty": 2
        },
        # Level 3: Complex dependencies
        {
            "code": generate_state_code(3),
            "concepts": "complex variable dependencies and state tracking",
            "focus_point": "how changes to one variable affect subsequent operations",
            "hint_text": "Pay attention to the order of assignments and how each value depends on previous values",
            "extra_task": "Explain why the final values grow so large",
            "difficulty": 3
        }
    ]
    
    # Choose a random variation
    variation = random.choice(variations)
    
    # Generate unique ID
    unique_id = f"{id_prefix}_{random.randint(1000, 9999)}"
    
    # Create front matter
    front_matter = {
        "id": unique_id,
        "metadata": {
            "topic": "variables",
            "bloom_level": "analyze",
            "difficulty": variation["difficulty"],
            "tags": ["variables", "state", "tracking", "assignment"]
        }
    }
    
    # Load template
    template_content = load_template('variable_state.md')
    
    # Replace placeholders
    replacements = {
        "CODE_SNIPPET": variation["code"][0],
        "VARIABLE_HEADERS": variation["code"][1],
        "STATE_TABLE_ROWS": variation["code"][2],
        "FINAL_STATE_ANALYSIS": variation["code"][3],
        "CONCEPTS": variation["concepts"],
        "FOCUS_POINT": variation["focus_point"],
        "HINT_TEXT": variation["hint_text"],
        "EXTRA_TASK": variation["extra_task"]
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

# Example usage:
if __name__ == "__main__":
    generate_loop_question()
    generate_off_by_one_question()
    generate_boolean_expression_question()
    generate_numeric_expression_question()
    generate_mixed_expression_question()
    generate_truth_table_question()
    generate_variable_assignment_question()
    generate_variable_scope_question()
    generate_variable_state_question() 