def is_identifier(token):
    return token.isalpha() or token.startswith("_")

def is_constant(token):
    return token.isdigit()

def is_operator(token):
    return token in ['+', '-', '*', '/']

def tokenize(code):
    tokens = []
    current_token = ""
    in_comment = False

    for char in code:
        if in_comment:
            if char == '\n':
                in_comment = False
        elif char.isalpha() or char == '_':
            current_token += char
        elif char.isdigit():
            current_token += char
        elif char.isspace():
            if current_token:
                if is_identifier(current_token):
                    tokens.append(("IDENTIFIER", current_token))
                elif is_constant(current_token):
                    tokens.append(("CONSTANT", current_token))
                elif is_operator(current_token):
                    tokens.append(("OPERATOR", current_token))
                current_token = ""
        elif char == '/':
            if current_token:
                if is_identifier(current_token):
                    tokens.append(("IDENTIFIER", current_token))
                elif is_constant(current_token):
                    tokens.append(("CONSTANT", current_token))
                elif is_operator(current_token):
                    tokens.append(("OPERATOR", current_token))
                current_token = ""
            if len(code) > 1 and code[code.index(char) + 1] == '/':
                in_comment = True
        else:
            if current_token:
                if is_identifier(current_token):
                    tokens.append(("IDENTIFIER", current_token))
                elif is_constant(current_token):
                    tokens.append(("CONSTANT", current_token))
                elif is_operator(current_token):
                    tokens.append(("OPERATOR", current_token))
                current_token = ""
            tokens.append(("SPECIAL", char))

    if current_token:
        if is_identifier(current_token):
            tokens.append(("IDENTIFIER", current_token))
        elif is_constant(current_token):
            tokens.append(("CONSTANT", current_token))
        elif is_operator(current_token):
            tokens.append(("OPERATOR", current_token))

    return tokens

# Example usage
code = """
Left Recursion: The grammar : A -> Aa | a is left recursive. Top down parsing techniques cannot
 handle left recursive grammar so we convert left recursion into right recursion
"""

tokens = tokenize(code)

for token in tokens:
    token_type, value = token
    print("Token: {}, Value: {}".format(token_type, value))
