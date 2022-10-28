# What is Oddsie?
 Oddsie is a programming language which can be transpiled to Python, can be "compiled" by using Pyinstaller (To do that Pyinstaller must be installed) or can be "interpreted".  
Oddsie is designed to be an alternative to Python. Think of it as Python's weird sibling. It is also fully compatible with Python.
# Examples
```lua
use random
display "NUMBER\sGUESS"
var guess=int(input(":"))
var actual=random.randint(1,10)
if guess==actual:
	display "Good\sGuess!"
end
otherwise:
	display "Incorrect!\sNumber\swas\s"+str(actual)+"!"
end
```
*^ Simple number-guessing game ^*
```lua
;; Really Complicated Hello World
set HelloWorld:
	var txt=""
	function uno():
		var txt=txt+"Hello,"
	end
	function dos():
		var txt=txt+"\sworld!"
	end
	function tres():
		display txt
	end
end
var hw=HelloWorld()
do hw.uno
do hw.dos
do hw.tres
```
*^ An overly complicated Hello, World! program ^*
# What do I need to code in Oddsie?
- Linux (Won't work on Windows)
- Python 3.7 and up
- Oddsie
