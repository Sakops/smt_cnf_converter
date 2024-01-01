from sympy.logic import SOPform
from sympy import symbols

def introduce_labels(clause):
    a, b, c, d, e = symbols('a b c d e')
    labels = []

    for idx, term in enumerate(clause.split(), start=1):
        labels.append(f'(!l{idx} | {term})')

    return ' & '.join(labels)

def negate_clause(clause):
    return f'(!{clause.replace("&", " & ").replace("|", " | ").replace("(", "(!").replace(")", ")")})'

def convert_to_smt_format(clause):
    clauses = clause.split(" | ")
    smt_clauses = []

    for idx, cl in enumerate(clauses, start=1):
        terms = cl.split(" & ")
        smt_clause = ' & '.join([f'(!l{idx} | {term})' for term in terms])
        smt_clauses.append(smt_clause)

    return ' & '.join(smt_clauses)

my_clause = (
    "(!e & !d & !a & !c) | "
    "(d & b & a & e) | "
    "(!e & !b & a & c) | "
    "(!e & b & c & d) | "
    "(!c & !b & !a & !d) | "
    "(b & a & !c & d) | "
    "(b & c & !d & a) | "
    "(!d & e & b & !a) | "
    "(!d & !c & !a & !b) | "
    "(!c & b & e & d) | "
    "(!b & a & !e & !d) | "
    "(!e & !a & !b & c) | "
    "(!e & !d & !b & !a) | "
    "(!c & !d & a & !e) | "
    "(d & !c & a & e) | "
    "(c & b & !e & d) | "
    "(b & c & !e & !d) | "
    "(c & b & !d & a)"
)

result = convert_to_smt_format(my_clause)
negated_result = negate_clause(result)

# Print the result on the console
print(f'({result}) & ({negated_result})')

# Write the result to a file
with open('output.txt', 'w') as file:
    file.write(f'({result}) & ({negated_result})')
