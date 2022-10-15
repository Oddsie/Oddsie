# What is Oddsie?
Oddsie is a programming language which transpiles to Python.  
FUN FACT ALERT: The name "Oddsie" comes from my cat Odds' nickname.  
I have big dreams for Oddsie. Since it's the first (working) programming language I've ever made.  
Oddsie is cool, yo!  
So why not contribute?  
LINK: https://oddsie.github.io/site
# Example
numberguess.od: A simple number-guessing game.
```
use-random
display-"NUMBER;sGUESS"
var-guess=int(input(":"))
var-actual=random.randint(1, 10)
if-guess==actual:
	display-"Good Guess!"
end
otherwise:
	display-"Incorrect! Number was "+str(actual)+"!"
end
```
# What do I need to code in Oddsie?
- Linux
- Python 3.7 and up
- Oddsie
