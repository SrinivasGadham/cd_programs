# cd_programs
Cd programs Vi Sem
SET-1
1)	Develop a lexical analyzer or standalone scanner to recognize a few patterns without Lex tool. (Ex. identifiers, constants, comments, operators, special characteers etc.)    for the statement
Left Recursion: The grammar : A -> Aa | a is left recursive. Top down parsing techniques cannot handle left recursive grammar so we convert left recursion into right recursion    [L5][CO1]   

2)	Demonstrate lexical analyzer tool.
A word processor capitalizes the characters of a statement                                   [L5][CO2]   
Consider the statement: “failure will never overtake me if my determination to succeed is strong enough “   

SET-2

1)	Write a program for Tokenization (counting the no. of characters, lines, spaces, tabs etc..,).                  
      Consider the statement: “At least for the people who send me mail about a new language that   
           they're designing, the general advice is:         do it to learn about how to write a compiler.”  
                                                                                                                        [L5][CO1]   
2)	Implement Parser with Scanner using LEX and YACC tool.                    [L5][CO2]  
Demonstrate the operation of Calculator: 23*4+(12/4)-9

SET-3
1)	Generate Canonical Collection of LR(0) items:
Consider: Grammar for arithmetic expression  E->E+E| E-E| E*E| E/E | id    [L5][CO3]

2)	Implement Parser with Scanner using Lex and Yacc tools.
Convert the expression a*b+(c-d) to postfix expression                                    [L5][CO3]   


SET-4
1)	Write a program using Lex and YACC tool to accept an input string for the grammar.
Consider : A->aAb| ε                                                                                          [L5][CO2]

2)	Implement mini compiler with phases.                                                               [L5][CO2]    
To recognize a valid variable which starts with a letter followed by any number of letters or digits.                                          



SET-5
1)	Write a program to implement Scanner application or token separator using Lex tool for the statement:                                                                                            [L5][CO2]   
  A grammar is left recursive if it has a non-terminal A such that there is a
derivation. A ⇒ Aα  for some string α                                                                                    
2)	Write a program to generate target code (in assembly language).       [L5][CO6]   
Consider:   t1 = in1 + in2
t2 = t1 + in3
t3 = t2 - in4
out = t3.


SET-6
1)	Write a program to find FOLLOW elements for the grammar.       [L5][CO3]  
 Consider the grammar: AB+C.
                                             Ba
                                             Cb

2)	Implement Parser with Scanner, without Scanner.   
Note: Recognize valid identifier.                                                          [L5][CO2]   


SET-7
1)	Write a program to implement language to an intermediate form (e.g. three-address code).                                                                                                      [L5][CO4]   
Consider the statement: out = in1 + in2 + in3 - in4
2)	Implement Lexical analyzer to find vowels and consonants for the statement: 
In some ways, programming is like painting. You start with a blank canvas and certain basic raw materials. You use a combination of science, art, and craft to determine what to do with them                           [L5][CO2]


SET-8
1)	Write a program to simulate Symbol table Management.     
Create Operations: Insert, Update, Search and Delete with respect to Token ID                 
                                                                                                                [L5][CO4]   
2)	Write a Lex program to identify the Octal or Hexadecimal number..    [L5][CO2]   


SET-9
1)	Write a Program to generate predictive LL1 parsing table.                         [L5][CO3]
Note: Eliminate Left Recursion if exists for the given grammar
i.	Evaluate FIRST and FOLLOW elements
ii.	Verify whether multiple entries existed or not.
2)	b) Write a Program to generate predictive LL1 parsing table for the grammar  [L5][CO3]
           SA/Bd
           Aa
           Bc                                 



SET-10
1)	Implement Lexical Analyzer phase of compiler.                                                 [L5][CO2] 
       For regular expressions of identifier, keywords, starting with letter ‘i’.   
            
2)	Write a program to improve target code with the help of optimization techniques. [L5][CO5]                                                                            
 while(i<100)
{
 a = sin(x)/cos(x) + i;
 i++;
}                                                                                                         





SET-11
1)	Demonstrate lexical analyzer tool.
Find even or odd number using LEX tool.                            [L5][CO2]   

2)	Write a program to implement Recursive Decent Parser.                               [L5][CO3]  
Consider the grammar: E->E+T | T
                                      T->T*F | F
                                      F->(E) | id 



SET-12
1)	Write a program to find FIRST elements for the given grammar. 
consider the grammar as EE+T | T   Ta where E,T stands for Expression and Term respectively.                                                                                                 [L5][CO3]   
2)	Write a program using Lex and Yacc tool to recognize a valid arithmetic expression that uses operator +, –, * and /.                                                                                    [L5][CO2]







                                                  

SET-13
1)	Implementing parser for small language   
Note: consider Operators as Root(s)/Parent  and Operands as leaf/child          [L5][CO2]

2)	Implement Parser with Scanner using Yacc/Bison and Lex tool.
A language processor recognizes a whether a string is palindrome or not.                                                          
                                                                                                                               [L5][CO2]


SET-14
1)	Tokenization by constructing DFA of Lexical Analyzer                        [L5] [CO1]
       Show whether a string is keyword or not.

2)	Implement lexical analyzer phase of compiler.        
A phase of language processor that checks whether number has integer or real value.
                                                                                                                    [L5][CO2]

