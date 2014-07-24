import lrkit.canonical
from lrkit import Parser, Rule, rule, SnError
from sys import exit

specials = {
        "*": "*",
        "/": "/",
        "%": "%",
        "+": "+",
        "-": "-",
        "0": "0",
        "(": "(",
        ")": ")",
        ",": ",",
}

rules = [
    rule("Program", "Expr"),
    rule("Program"),
    rule("Expr",    "Sum"),
    rule("Sum",     "Sum", "SumOp", "Product"),
    rule("Sum",     "Product"),
    rule("Product", "Product", "ProductOp", "Term"),
    rule("Product", "Term"),

    rule("ProductOp", "*"),
    rule("ProductOp", "/"),
    rule("ProductOp", "%"),
    rule("SumOp", "+"),
    rule("SumOp", "-"),
    rule("Term", "symbol"),
    rule("Term", "(", "ExprList", ")"),

    rule("ExprList"),
    rule("ExprList", "Expr"),
    rule("ExprList", "ExprList", ",", "Expr"),
]

def visit(rule, pos, data):
    print "reduction", rule, pos, data
    return None

results = lrkit.canonical.simulate(rules, "Program")
if len(results.conflicts):
    lrkit.diagnose(results)
    exit(1)

parser = Parser(results, visit)
from sys import stdin

while True:
    try:
        index = 0
        source = stdin.readline()
        for token in lrkit.tokenize(source, specials):
            parser.step(token.start, token.stop, token.group, token.value)
            index = token.stop
        result = parser.step(index, index, None, None)
    except SnError, e:
        print "-"*20
        print lrkit.snippet(e.start, e.stop, source)
        print "SN ERROR:", e.message
        parser.reset()
