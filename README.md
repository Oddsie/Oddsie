# What is Oddsie?
 Oddsie is a programming language which can be transpiled to Python or can be "compiled" by using Pyinstaller (To do that Pyinstaller must be installed).  
Oddsie is designed to be an alternative to Python. Think of it as Python's weird sibling. It is also fully compatible with Python.
# Examples
```oddsie
use:random
display:"NUMBER GUESS"
var:guess=int(input(""))
var:actual=random.randint(1, 10)
if:guess==actual:(
	display:"Good Guess!"
)
otherwise(
	display:"Incorrect! Number was "+str(actual)+"!"
)
```
*^ numberguess.od ^*
```oddsie
;:Really Complicated Hello World
set:HelloWorld-(
	var:txt=""
	define:uno():(
		var:txt=txt+"Hello, "
	)
	define:dos():(
		var:txt=txt+" world!"
	)
	define:tres():(
		display:txt
	)
)
var:hw=HelloWorld()
do:hw.uno
do:hw.dos
do:hw.tres
```
*^ reallycomplicatedhelloworld.od ^*
# What do I need to code in Oddsie?
- Linux
- Python 3.7 and up
- Oddsie
