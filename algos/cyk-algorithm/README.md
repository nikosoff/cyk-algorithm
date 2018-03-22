# CYK-algorithm

a.k.a. Cocke–Younger–Kasami algorithm 

The rules should be in a Chomsky Normal Form(CNF) grammar. <br />
A grammar is in a Chomsky Normal Form, if each production rule has one of the following forms: <br /><br />
* A -> BC <br />
* A -> a <br />
* A -> ε <br />

where A,B,C are non-terminal symbols, a is a terminal symbol and ε is an empty string. <br />

rules.txt and rules2.txt contain context-free grammars of this form. <br />

Additionally, the script file prints the parse tree/trees that represents the syntactic structure of the given string according to the provided grammar. <br />

For example:

python cyk.py rules2.txt "fruit flies like a banana" <br />

outputs:

The sentence "fruit flies like a banana" is recognized by the grammar <br />
S <br />
&nbsp; |-NP <br />
&nbsp; &nbsp; |-Adj <br />
&nbsp; &nbsp; &nbsp;    |-fruit <br />
&nbsp; &nbsp; |-Noun <br />
&nbsp; &nbsp; &nbsp;    |-flies <br />
&nbsp; |-VP <br />
&nbsp; &nbsp;  |-V <br />
&nbsp; &nbsp; &nbsp;   |-like <br />
&nbsp; &nbsp;  |-NP <br />
&nbsp; &nbsp; &nbsp; |-Det <br />
&nbsp; &nbsp; &nbsp; &nbsp;     |-a <br />
&nbsp; &nbsp; &nbsp;   |-Noun <br />
&nbsp; &nbsp; &nbsp; &nbsp;     |-banana <br />
