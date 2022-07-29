Test all delimeter with spaces at ends:
>>> text_indentation("Hello   :     Holberton    ?    school.    fooo     ")
Hello:
<BLANKLINE>
Holberton?
<BLANKLINE>
school.
<BLANKLINE>
fooo
Test just delimeter:
>>> text_indentation(".?:")
.
<BLANKLINE>
?
<BLANKLINE>
:
<BLANKLINE>
Test string with the spaces:
>>> text_indentation("    Holberton")
Holberton
Test just delimeters:
>>> text_indentation("  ?  ")
?
<BLANKLINE>
Test nonindent inside indent
>>> text_indentation("?Hello.")
?
<BLANKLINE>
Hello.
<BLANKLINE>
Test existing newline:
>>> text_indentation("?\n\n.\n\n:")
?
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
.
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
:
<BLANKLINE>
Test none:
>>> text_indentation(None)
Traceback (most recent call last):
...
TypeError: text must be a string
Test num:
>>> text_indentation(33)
Traceback (most recent call last):
...
TypeError: text must be a string
Test string with some spaces:
>>> text_indentation("        Holberton          ")
Holberton
Test string with an empty string:
>>> text_indentation("")
Test string with an empty string (2):
>>> text_indentation("      ")
Test:
>>> text_indentation("Hello: Holberton")
Hello:
<BLANKLINE>
Holberton
Test delimeters with spaces:
>>> text_indentation("      ?:  :  ")
?
<BLANKLINE>
:
<BLANKLINE>
:
<BLANKLINE>
Test newline:
>>> text_indentation("\n")
<BLANKLINE>
Test newlines:
>>> text_indentation("\n\n")
<BLANKLINE>
<BLANKLINE>
Test newline 3:
>>> text_indentation("Hello\n\n")
Hello
<BLANKLINE>
Import module:
>>> text_indentation = __import__('5-text_indentation').text_indentation
Test no delimeters:
>>> text_indentation("Hello Holberton")
Hello Holberton
Test string with spaces:
>>> text_indentation("Holberton    ")
Holberton
Test all delimeters!:
>>> text_indentation("Hello: Holberton? school. fooo")
Hello:
<BLANKLINE>
Holberton?
<BLANKLINE>
school.
<BLANKLINE>
fooo
Test all delimeters with some spaces:
>>> text_indentation("Hello   :   Holberton  ?  school.  fooo")
Hello:
<BLANKLINE>
Holberton?
<BLANKLINE>
school.
<BLANKLINE>
fooo
