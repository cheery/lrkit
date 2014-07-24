# LRKit

LRKit is a parser generator for canonical LR(1) parsers. It is designed towards experimentation, rapid design of programming language grammars and keyboard user interfaces.

To start out read the [Manual](lrkit/manual.md).

To understand LR parsers, read the [blog post](http://boxbase.org/entries/2014/jul/21/LR1-parsers/) that this module originated from.

## Prior use

Successfully parsed a calculator. Seems to be able to parse larger languages too, but requires further study to verify. Work in progress. 

## Features

 * Canonical LR(1) parser generator and parser engine
 * Grammar construction language
 * Tokenizer for indented languages that do not have parenthesis spanning across a line.
 * File offset based numbering for tokens.
 * (Incomplete) caching of the produced grammar.
 * (Incomplete) diagnosis of conflicting grammars.
 * (Incomplete) syntax error reporting system.
 * Compantmentalized source code structure. Should be easy to understand and read.

