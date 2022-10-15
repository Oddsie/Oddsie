# What is Oddsie?
Oddsie is a basic programming language that transpiles to Python. It is designed to be very easy to write and read.
# Example
numberguess.od
`use-random
display-"NUMBER;sGUESS"
var-guess=int(input(":"))
var-actual=random.randint(1, 10)
if-guess==actual:
	display-"Good Guess!"
end
otherwise:
	display-"Incorrect! Number was "+str(actual)+"!"
end,
# What do I need to code in Oddsie?
- Linux
- Python 3.7 and up
- Oddsie
