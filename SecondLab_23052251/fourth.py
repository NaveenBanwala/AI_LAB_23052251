# 4. Create a Python program that functions as an advanced calculator. It
# should take user input for mathematical expressions and evaluate
# them, supporting basic operations, parentheses, and scientific
# notation.


def breakExpression(exp):
    tokens = []
    num = ""

    for i, ch in enumerate(exp):
        if ch.isdigit() or ch == "." or ch == "e" or (ch in "+-" and num.endswith("e")):
            num += ch
        else:
            if num:
                tokens.append(float(num))
                num = ""
            if ch in "+-*/^()":
                tokens.append(ch)

    if num:
        tokens.append(float(num))

    return tokens


def precedence(op):
    if op in "+-":
        return 1
    if op in "*/":
        return 2
    if op == "^":
        return 3
    return 0


def applyOperator(a, b, op):
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/": return a / b
    if op == "^": return a ** b


def evaluate(tokens):
    values = []
    ops = []
    i = 0

    while i < len(tokens):
        token = tokens[i]

        if isinstance(token, float):
            values.append(token)

        elif token == "(":
            ops.append(token)

        elif token == ")":
            while ops and ops[-1] != "(":
                b = values.pop()
                a = values.pop()
                op = ops.pop()
                values.append(applyOperator(a, b, op))
            ops.pop()  # remove '('

        else:  # operator
            while ops and precedence(ops[-1]) >= precedence(token):
                b = values.pop()
                a = values.pop()
                op = ops.pop()
                values.append(applyOperator(a, b, op))
            ops.append(token)

        i += 1

    while ops:
        b = values.pop()
        a = values.pop()
        op = ops.pop()
        values.append(applyOperator(a, b, op))

    return values[0]


print("Advanced Calculator")
print("Supports + - * / ^, parentheses (), scientific notation (e)")
print("Type 'false' to exit")

while True:
    exp = input("Enter expression: ")

    if exp.lower() == "false":
        print("Calculator Closed")
        break

    try:
        tokens = breakExpression(exp)
        result = evaluate(tokens)
        print("Result:", result)
    except Exception as e:
        print("Invalid expression")

# def breakExpresssion(exp):
#     breakSoln =[]
#     num =""
#     for ch in exp :
#         if ch.isdigit() or ch=="." or ch=="e":
#             num+=ch
#         else:
#             if num:
#                 breakSoln.append(float(num))
#                 num=""
#                 if ch in "+-*/^()":
#                     breakSoln.append(ch)

#     if num:
#         breakSoln.append(float(num))

#         return breakSoln
    
# def precedence(op):
#     if op in "+-":
#         return 1
#     if op in "*/":
#         return 2
#     if op in "^":
#         return 3
#     return 0
    
    



# def applyOperator(a, b, op):
#     if op == "+":
#         return a + b
#     if op == "-":
#         return a - b
#     if op == "*":
#         return a * b
#     if op == "/":
#         return a / b
#     if op == "^":
#         return a ** b
    
# def evulate(soln):
#     values = [] 
#     ops =[]

#     i =0
#     while len(soln)>i:
#         num = soln[i]

#         # use isinstance for check check wheather a 
#         #number belongs to which datatype
#         if isinstance(num, float) :
#             values.append(num)

#         elif num =="(" :
#             ops.append(num)

#         elif num ==")" :
#             while ops and ops[-1] != "(" :
#                 b= values.pop()
#                 a=values.pop()
#                 op = ops.pop()
#                 values.append(applyOperator(b,a,op))
#                 ops.pop()
                
#         else:
#             while (ops and precedence(ops[-1]) >= precedence(num)):
#                 b= values.pop()
#                 a=values.pop()
#                 op =ops.pop()
#                 values.append(applyOperator(b,a,op))
#                 ops.append(num)

#     i+=1


#     while ops:
#             b= values.pop()
#             a=values.pop()
#             op = ops.pop()
#             values.append(applyOperator(a,b,op))
#     return values[0]


# print("Advanced Calculator")
# print("+,-,/, ^")
# print("paranthesis () and notations Scientific-> Example Xe3")
# print("enter false for close")

# while True:
#     exp= input("Enter expression")
#     if exp == "false" :
#         print("Closed") 
#         break

#     try:
#         soln= breakExpresssion(exp)
#         result = evulate(soln)
#         print("Result:", result)
#     except:
#         print("Inavlid expression")
