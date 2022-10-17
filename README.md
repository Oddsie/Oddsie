# What is Oddsie?
 Oddsie is a programming language which can be transpiled to Python or can be "compiled" by using Pyinstaller (To do that Pyinstaller must be installed).  
Oddsie is designed to be an alternative to Python. Think of it as Python's weird sibling. It is also fully compatible with Python.
# Examples
numberguess.od: A simple number-guessing game.
```
use-random
display-"NUMBER GUESS"
var-guess=int(input(":"))
var-actual=random.randint(1, 10)
if-guess==actual:
	display-"Good Guess!"
end
otherwise:
	display-"Incorrect! Number was "+str(actual)+"!"
end
```
reallycomplicatedhelloworld.od: Overly complicated Hello, World! program.
```
```
# What do I need to code in Oddsie?
- Linux
- Python 3.7 and up
- Oddsie
