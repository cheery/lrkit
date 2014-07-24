import lrkit.grammar
from lrkit import Parser, Rule, rule, SnError
from sys import stdin, modules, exit
import math

env = {
    'pi':  math.pi,
    'tau': math.pi*2,
}

specials = {
    "+": "plus",
    "-": "minus",
    "*": "times",
    "/": "divide",
    "%": "modulus",
    "(": "lparen",
    ")": "rparen",
    "=": "assign",
}

def assign(pos, objs):
    sym, value = objs
    env[sym] = value
    return value

def variable(pos, sym):
    if sym not in env:
        raise SnError("{} not in env".format(sym), *pos)
    return env[sym]

def plus(pos, sym):
    return lambda a, b: a+b

def minus(pos, sym):
    return lambda a, b: a-b

def times(pos, sym):
    return lambda a, b: a*b

def divide(pos, sym):
    return lambda a, b: a/b

def modulus(pos, sym):
    return lambda a, b: a%b

def negative(pos, sym):
    return -sym

def binary(pos, objs):
    lhs, op, rhs = objs
    return op(lhs, rhs)

def through(pos, obj):
    return obj

results, attach = lrkit.grammar.load("grammars/calculator.gr", "File")
if len(results.conflicts) > 0:
    lrkit.diagnose(results)
    exit(1)

parser = attach(modules[__name__])

while True:
    try:
        index = 0
        source = stdin.readline()
        for token in lrkit.tokenize(source, specials):
            print token.start, token.stop, token.group, repr(token.value)
            parser.step(token.start, token.stop, token.group, token.value)
            index = token.stop
        result = parser.step(index, index, None, None)
        print result
    except SnError as e:
        print "-"*20
        print lrkit.snippet(e.start, e.stop, source)
        print "SN ERROR:", e.message
        parser.reset()
    except KeyboardInterrupt:
        print
        break
