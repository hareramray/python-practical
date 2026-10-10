"""Course authoring source. Regeneration overwrites notebooks: back up your work first."""
from pathlib import Path
import json
import textwrap
import uuid

ROOT = Path(__file__).resolve().parents[1]
COURSE = []


def clean(text):
    return textwrap.dedent(text).strip() + "\n"


def lesson(title, explanation, code, experiment):
    return (title, explanation, code, experiment)


def exercise(title, prompt, starter, checks, answer, hint):
    return (title, prompt, starter, checks, answer, hint)


def add(slug, title, level, goals, lessons, exercises, project, pitfalls):
    COURSE.append(dict(slug=slug, title=title, level=level, goals=goals,
                       lessons=lessons, exercises=exercises, project=project, pitfalls=pitfalls))


add("00_start_here", "Start here: learn how to learn in a notebook", "Orientation",
    ["Run and edit cells", "Understand notebook state", "Use exercises and checks"], [
    lesson("1. Your first program", "A **code cell** runs Python. A **Markdown cell** contains notes like these. Select the next cell and press Shift+Enter. `print()` displays a value; quoted text is called a string. Lines beginning with `#` are comments.", '''
        # Change the words inside the quotes and run this cell again.
        print("Hello, Python learner!")
        print(2 + 3)
    ''', "Predict the second line before running. Change + to * and rerun."),
    lesson("2. Names remember values", "An assignment uses `=` to give a value a name. A notebook's **kernel** is the running Python process: it remembers names from executed cells, even when you delete their code. Run from top to bottom. Restart Kernel and Run All is a useful way to check that no hidden state is needed.", '''
        minutes_per_day = 30
        days = 5
        weekly_minutes = minutes_per_day * days
        print("Weekly practice:", weekly_minutes, "minutes")
    ''', "Change minutes_per_day to 45. Predict the new result, then run."),
    lesson("3. Your environment", "`import` loads a module: a collection of useful Python tools. We will study modules later. For now, this reports the interpreter actually used by this notebook. Select the project's .venv kernel in VS Code, or Python 3 in the provided JupyterLab launcher.", '''
        import sys
        print("Python:", sys.version.split()[0])
        print("Interpreter:", sys.executable)
    ''', "Find .venv in the interpreter path when using the local setup.")], [
    exercise("A personal greeting", "Assign your chosen name to learner_name and create greeting by joining 'Hello, ' and that name. Use + between strings.", '''
        learner_name = "Learner"
        greeting = None  # Replace None with your expression.
    ''', 'assert greeting == "Hello, " + learner_name', '''
        learner_name = "Learner"
        greeting = "Hello, " + learner_name
        print(greeting)
    ''', '"Hello, " + learner_name'),
    exercise("Practice budget", "You practice 25 minutes on each of 6 days. Assign the total to total_minutes.", 'total_minutes = None', 'assert total_minutes == 150', 'total_minutes = 25 * 6', "Use multiplication: *.")],
    "Add a Markdown cell with your goal and three things you want to build. Add a code cell that calculates your weekly practice minutes. Save with Ctrl+S. This personal note has no single correct answer.",
    "If a cell shows [*], it is still running. Interrupt it if necessary. A NameError often means a needed earlier cell was not run. Undo accidental edits, or use your backup; restarting the kernel does not restore edited code.")

add("01_variables_and_numbers", "Variables, numbers, and types", "Beginner",
    ["Use integers, floats, booleans, and None", "Calculate and convert values", "Recognize floating point limitations"], [
    lesson("1. Values have types", "A variable is a name bound to a value. Integers represent whole numbers, floats approximate decimal numbers, booleans are True/False, and None means no value. `type()` reveals a value's type.", '''
        age = 20
        price = 49.5
        is_learning = True
        result = None
        print(type(age), type(price), type(is_learning), type(result))
        age = age + 1
        print("Next age:", age)
    ''', "Predict type(20.0). Try it in a new cell."),
    lesson("2. Arithmetic", "`/` is division, `//` is floor division, `%` gives the remainder, and `**` raises a power. Parentheses control evaluation order. Floor division rounds down, including for negative values.", '''
        print(17 / 5, 17 // 5, 17 % 5)
        print(2 ** 3, (2 + 3) * 4)
        print(-7 // 3)
        minutes = 135
        print("Hours:", minutes // 60, "Remaining minutes:", minutes % 60)
    ''', "Convert 200 minutes into hours and remaining minutes."),
    lesson("3. Conversion and approximate decimals", "`int()` and `float()` convert numeric text. An f-string inserts values into text. Many decimal fractions cannot be represented exactly as binary floats. Use a tolerance when comparing calculated floats; use Decimal for money later.", '''
        raw_quantity = "3"
        total = int(raw_quantity) * 19.5
        print(f"Total: {total:.2f}")
        print(0.1 + 0.2)
        import math
        assert math.isclose(0.1 + 0.2, 0.3)
    ''', "Predict int(3.9). It truncates toward zero; test int(-3.9) too.")], [
    exercise("Temperature converter", "Convert 30 Celsius to Fahrenheit using F = C * 9 / 5 + 32.", 'celsius = 30\nfahrenheit = None', 'assert fahrenheit == 86', 'celsius = 30\nfahrenheit = celsius * 9 / 5 + 32', "Use celsius in the formula, not a hard-coded answer."),
    exercise("Split a bill", "A bill is 1200, the tip is 10%, and 4 friends split the final amount. Compute per_person.", 'bill = 1200\ntip_rate = 0.10\nfriends = 4\nper_person = None', 'assert per_person == 330', 'bill = 1200\ntip_rate = 0.10\nfriends = 4\nper_person = bill * (1 + tip_rate) / friends', "Add the tip before dividing.")],
    "Build a travel-cost calculator with distance, kilometres per litre, and fuel price. Display litres needed and total cost to two decimals. Try two different journeys and manually check one.",
    "`=` assigns; `==` compares. Numeric text such as '3' is not the number 3. Do not use exact float equality for approximate calculations.")

add("02_strings_and_text", "Strings and practical text processing", "Beginner",
    ["Index and slice text", "Clean and format strings", "Split and join structured text"], [
    lesson("1. Characters and slices", "A string is an immutable sequence of characters. Indexes start at 0; negative indexes count from the end. A slice includes its start but excludes its stop. Slices create new strings.", '''
        language = "Python"
        print(language[0], language[-1])
        print(language[:3], language[3:], language[::-1])
        print(len(language))
    ''', "Predict language[1:4]. Try an empty slice language[3:3]."),
    lesson("2. Clean input", "Methods are operations accessed with a dot. String methods return new strings, so keep the returned value. `strip()` removes surrounding whitespace, not spaces inside the text.", '''
        raw = "  Learn Python  "
        cleaned = raw.strip().lower()
        print(repr(raw), repr(cleaned))
        print(cleaned.replace("python", "coding"))
        print("python" in cleaned, cleaned.startswith("learn"))
    ''', "Try tabs or a newline at each end of raw. Use repr() to see them."),
    lesson("3. Parse and format", "`split()` breaks text into a list of parts. `join()` combines strings using a separator. Real CSV can contain quoted commas; use the csv module in notebook 07 for that.", '''
        items = "tea,coffee,milk".split(",")
        print(items)
        print(" | ".join(items))
        name, score = "Mira", 92.456
        print(f"{name} scored {score:.1f}%")
    ''', "Change the separator and number of decimal places.")], [
    exercise("Username cleanup", "Strip spaces and lowercase '  PyLearner  '. Store the result in username.", 'raw_username = "  PyLearner  "\nusername = None', 'assert username == "pylearner"', 'raw_username = "  PyLearner  "\nusername = raw_username.strip().lower()', "Chain strip() and lower()."),
    exercise("Domain extraction", "Extract the domain from email using split('@'). Assume exactly one @ for this exercise.", 'email = "learner@example.com"\ndomain = None', 'assert domain == "example.com"', 'email = "learner@example.com"\ndomain = email.split("@")[1]', "Choose the second part, index 1.")],
    "Format a receipt with a product name, quantity, unit price, and total. Add aligned columns with f-strings. Verify that changing quantity changes the displayed total.",
    "String indexes outside the string raise IndexError. You cannot assign to text[0]. lower() is useful for simple normalization but is not full validation of an email or username.")

add("03_lists_tuples_dicts_sets", "Collections: lists, tuples, dictionaries, and sets", "Beginner",
    ["Choose a collection for a task", "Update and retrieve values", "Understand aliasing and shallow copies"], [
    lesson("1. Lists and tuples", "A list is an ordered, mutable sequence. A tuple is an ordered sequence whose references cannot be reassigned. Use tuples for fixed groups such as coordinates. A tuple may still contain mutable objects.", '''
        tasks = ["read", "code"]
        tasks.append("review")
        tasks[0] = "predict"
        print(tasks, tasks[:2])
        print("Removed:", tasks.pop())
        point = (10, 20)
        x, y = point
        print(x, y)
    ''', "Append two more tasks and inspect len(tasks)."),
    lesson("2. Dictionaries and sets", "A dictionary maps unique keys to values. `get()` supplies a fallback for a missing key. A set stores unique hashable values and supports membership and set operations; do not depend on its display order.", '''
        student = {"name": "Mira", "score": 80}
        student["score"] = 85
        print(student["name"], student.get("city", "Unknown"))
        topics = {"lists", "strings", "lists"}
        print(sorted(topics))
        print(topics & {"strings", "loops"})
    ''', "Add a city key and compare [] with get() for a missing key."),
    lesson("3. Sharing versus copying", "Assigning a list to another name does not copy it. Both names refer to the same object. `copy()` makes a shallow copy: nested objects remain shared.", '''
        original = [1, 2]
        alias = original
        copied = original.copy()
        alias.append(3)
        print(original, copied)
        assert alias is original
        nested = [[1], [2]]
        shallow = nested.copy()
        shallow[0].append(9)
        print(nested)
    ''', "Use copy.deepcopy(nested) from the copy module and compare nested edits.")], [
    exercise("Unique tags", "Create a sorted list of unique tags from the input list.", 'tags = ["python", "data", "python", "web"]\nunique_tags = None', 'assert unique_tags == ["data", "python", "web"]', 'tags = ["python", "data", "python", "web"]\nunique_tags = sorted(set(tags))', "Build a set, then sort it."),
    exercise("Update inventory", "Start with the dictionary below, add 3 pens to the existing count, and add a ruler with count 1.", 'stock = {"pen": 2, "book": 4}\n# Update stock here.', 'assert stock == {"pen": 5, "book": 4, "ruler": 1}', 'stock = {"pen": 2, "book": 4}\nstock["pen"] += 3\nstock["ruler"] = 1', "Access a dictionary value by its key.")],
    "Represent three books as a list of dictionaries with title, author, and available. Update one book, then extract the unique authors. Explain why each collection fits its role.",
    "list.append() mutates a list and returns None. Do not write items = items.append(x). A dictionary key must be hashable; a list cannot be a key.")

add("04_conditions_and_loops", "Decisions and repetition", "Beginner",
    ["Branch with if/elif/else", "Use for and while loops", "Filter and accumulate results"], [
    lesson("1. Conditions", "Indented blocks belong to the statement above them. Python convention uses four spaces. Comparisons produce booleans; `and`, `or`, and `not` combine conditions. Only the first matching branch runs.", '''
        score = 72
        if score >= 80:
            grade = "A"
        elif score >= 60:
            grade = "B"
        else:
            grade = "Keep practicing"
        print(grade)
        print(0 <= score <= 100)
    ''', "Test scores 59, 60, 79, and 80. Explain each result."),
    lesson("2. for loops", "A for loop visits each item. range(1, 6) yields 1 through 5. enumerate() supplies an index and value; it avoids manually maintaining a counter.", '''
        total = 0
        for number in range(1, 6):
            total += number
        print(total)
        for position, topic in enumerate(["strings", "lists", "loops"], start=1):
            print(position, topic)
        assert total == 15
    ''', "Sum numbers 1 through 10. Predict the total first."),
    lesson("3. while, break, and continue", "A while loop repeats while its condition is true. Update something that can make the condition false. break exits a loop; continue skips the rest of the current iteration.", '''
        remaining = 3
        while remaining > 0:
            print("Attempts left:", remaining)
            remaining -= 1
        for value in [3, -1, 8, 0, 10]:
            if value < 0:
                continue
            if value == 0:
                break
            print("Accepted:", value)
    ''', "Move 0 to the beginning of the list and predict which values print.")], [
    exercise("Even-number total", "Use a loop to sum the even numbers from 1 through 10 into even_total.", 'even_total = 0\n# Write your loop here.', 'assert even_total == 30', 'even_total = 0\nfor n in range(1, 11):\n    if n % 2 == 0:\n        even_total += n', "n % 2 == 0 tests whether n is even."),
    exercise("Passing scores", "Create passed containing scores greater than or equal to 60, in the original order.", 'scores = [40, 60, 95, 59, 70]\npassed = []\n# Write your loop here.', 'assert passed == [60, 95, 70]', 'scores = [40, 60, 95, 59, 70]\npassed = []\nfor score in scores:\n    if score >= 60:\n        passed.append(score)', "Append only when the condition is true.")],
    "Build FizzBuzz for 1–30: print Fizz for multiples of 3, Buzz for multiples of 5, FizzBuzz for both, otherwise the number. Check the 'both' case first. Verify 3, 5, 15, and 16.",
    "range() excludes its stop. An unchanged while condition can loop forever. Do not add or remove list items while iterating over that same list.")

add("05_functions_and_scope", "Functions: reusable building blocks", "Beginner",
    ["Define parameters and return results", "Use defaults and keyword arguments", "Avoid mutable default arguments"], [
    lesson("1. Input, work, output", "A function groups reusable behavior. Parameters name inputs; return sends a result to the caller. print displays a value but does not return it. A function without return returns None.", '''
        def rectangle_area(width, height):
            """Return area in square units."""
            return width * height

        area = rectangle_area(4, 3)
        print(area)
        assert rectangle_area(0, 3) == 0
    ''', "Create a perimeter function and test a 4 by 3 rectangle."),
    lesson("2. Defaults and keyword arguments", "Defaults let callers omit some arguments. A * in a signature makes later parameters keyword-only. Local names inside a function normally stay inside it; prefer explicit inputs over reliance on global variables.", '''
        def final_price(price, *, discount=0.0):
            return price * (1 - discount)

        print(final_price(100))
        print(final_price(100, discount=0.2))
        def add_all(*numbers):
            return sum(numbers)
        print(add_all(1, 2, 3))
    ''', "Call add_all() with no arguments. Predict its result."),
    lesson("3. Safe mutable defaults", "Default arguments are evaluated once when the function is defined. A default list would be shared across calls. Use None and create a new list inside when you need independent containers.", '''
        def add_task(task, tasks=None):
            if tasks is None:
                tasks = []
            tasks.append(task)
            return tasks

        print(add_task("read"))
        print(add_task("code"))
        assert add_task("a") == ["a"]
    ''', "Pass an existing list as tasks. Observe that this function mutates it.")], [
    exercise("Clamp a number", "Implement clamp(value, low, high). Return low below the range, high above it, otherwise value. Assume low <= high.", 'def clamp(value, low, high):\n    pass', 'assert clamp(-2, 0, 10) == 0\nassert clamp(12, 0, 10) == 10\nassert clamp(5, 0, 10) == 5', 'def clamp(value, low, high):\n    return max(low, min(value, high))', "You can use if statements or min() and max()."),
    exercise("Count words", "Return the number of whitespace-separated words. Empty or whitespace-only text has zero words.", 'def count_words(text):\n    pass', 'assert count_words("learn Python daily") == 3\nassert count_words("  ") == 0\nassert count_words("one\\ntwo") == 2', 'def count_words(text):\n    return len(text.split())', "split() without an argument handles repeated whitespace.")],
    "Build a unit-conversion toolkit with at least three small functions. Give each a docstring and test normal, zero, and boundary inputs. Keep printing outside the functions.",
    "Returning a value and displaying it are different. Do not overwrite built-ins with names such as list, str, or sum.")

add("06_errors_and_debugging", "Errors, validation, and debugging", "Intermediate",
    ["Read exception messages", "Catch specific expected errors", "Reproduce and fix a logic bug"], [
    lesson("1. Read the failure", "Exceptions describe why an operation failed. In a traceback, start with the last line, then find the relevant line in your code. These demonstrations catch their expected errors so Run All can complete.", '''
        try:
            int("three")
        except ValueError as error:
            print(type(error).__name__ + ":", error)
        try:
            [10, 20][5]
        except IndexError as error:
            print(type(error).__name__ + ":", error)
    ''', "Try int('3.5'). Explain why float('3.5') succeeds."),
    lesson("2. Validate a contract", "Raise a clear exception when an input violates your function's contract. Catch only errors you know how to handle. Do not silently swallow every exception; that can hide bugs.", '''
        def divide_bill(total, people):
            if people <= 0:
                raise ValueError("people must be positive")
            return total / people

        try:
            print(divide_bill(100, 0))
        except ValueError as error:
            print("Please correct the input:", error)
        assert divide_bill(100, 4) == 25
    ''', "Change people to 2. Which branch runs?"),
    lesson("3. Debug a logic error", "A logic bug can return the wrong value without raising an exception. Reduce the problem to a tiny input with a known answer. Inspect intermediate values before changing code.", '''
        def buggy_average(values):
            return sum(values) / (len(values) + 1)

        sample = [10, 20]
        print("Observed:", buggy_average(sample), "Expected:", 15)
        print("Sum:", sum(sample), "Count:", len(sample))
        # In an interactive session, uncomment breakpoint() to inspect state.
        # breakpoint()
    ''', "Fix the denominator in a new function. Decide what an empty input should do.")], [
    exercise("Safe integer parsing", "Return int(text), or None if text is not valid integer text. Inputs are strings.", 'def parse_int(text):\n    pass', 'assert parse_int("42") == 42\nassert parse_int("oops") is None\nassert parse_int("-2") == -2', 'def parse_int(text):\n    try:\n        return int(text)\n    except ValueError:\n        return None', "Catch ValueError, not every possible error."),
    exercise("Correct average", "Return the arithmetic mean; raise ValueError for an empty list.", 'def average(values):\n    pass', 'assert average([10, 20]) == 15\nassert average([0]) == 0\ntry:\n    average([])\nexcept ValueError:\n    pass\nelse:\n    raise AssertionError("Empty input must raise ValueError")', 'def average(values):\n    if not values:\n        raise ValueError("values must not be empty")\n    return sum(values) / len(values)', "Check emptiness before dividing.")],
    "Write a debugging diary: record one failure, its smallest reproducing input, expected result, actual result, cause, and fix. Add a check that prevents the same bug returning.",
    "Use explicit validation for user input. assert is for development checks and can be disabled by Python's optimization option.")

add("07_files_csv_and_json", "Files, paths, CSV, and JSON", "Intermediate",
    ["Read and write UTF-8 text", "Use context managers for file cleanup", "Round-trip CSV and JSON data"], [
    lesson("1. Paths and text files", "Path represents a filesystem path. Use explicit UTF-8 encoding for portable text. We use temporary directories so running examples never overwrites your own documents. Files disappear when the with block exits.", '''
        from pathlib import Path
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as folder:
            path = Path(folder) / "notes.txt"
            path.write_text("Learn\\nPractice\\nReview\\n", encoding="utf-8")
            print(path.read_text(encoding="utf-8"))
            with path.open(encoding="utf-8") as handle:
                lines = [line.strip() for line in handle]
        assert lines == ["Learn", "Practice", "Review"]
    ''', "Write one extra line. Compare read_text() with reading line by line."),
    lesson("2. JSON", "JSON stores objects, arrays, text, numbers, booleans, and null. Python dictionaries and lists map naturally to it. dumps/loads work on strings; dump/load work with file handles. Dates and sets need explicit conversion.", '''
        import json
        profile = {"name": "Mira", "topics": ["files", "json"], "active": True}
        encoded = json.dumps(profile, indent=2)
        print(encoded)
        restored = json.loads(encoded)
        assert restored == profile
    ''', "Add a numeric progress field and round-trip the updated dictionary."),
    lesson("3. CSV", "CSV is tabular text. DictReader uses the header row as dictionary keys. Values arrive as strings and need conversion. Use newline='' when opening CSV files so the csv module controls line endings.", '''
        import csv
        import io
        source = io.StringIO('item,quantity,price\\npen,2,10\\n"book, ruled",1,80\\n')
        rows = list(csv.DictReader(source))
        total = sum(int(row["quantity"]) * int(row["price"]) for row in rows)
        print(rows)
        print("Total:", total)
        assert total == 100
    ''', "Notice the quoted comma in a product name. Explain why split(',') would fail.")], [
    exercise("JSON summary", "Parse payload and sum its numbers into total.", 'payload = \'{"numbers": [2, 4, 6]}\'\ntotal = None', 'assert total == 12', 'import json\npayload = \'{"numbers": [2, 4, 6]}\'\ntotal = sum(json.loads(payload)["numbers"])', "json.loads(payload) returns a dictionary."),
    exercise("Choose Python files", "Given names, create a sorted list containing only names whose suffix is .py. Treat suffixes case-sensitively.", 'names = ["main.py", "notes.txt", "test_app.py", "data.csv"]\npython_files = None', 'assert python_files == ["main.py", "test_app.py"]', 'from pathlib import Path\nnames = ["main.py", "notes.txt", "test_app.py", "data.csv"]\npython_files = sorted(name for name in names if Path(name).suffix == ".py")', "Use Path(name).suffix or name.endswith('.py').")],
    "Inside a TemporaryDirectory, save three expenses as JSON, load them again, and export them with csv.DictWriter. Assert that the loaded records equal the originals.",
    "Relative paths depend on the current working directory. Opening with 'w' replaces an existing file. Avoid pickle for untrusted input because loading it can execute code.")

add("08_modules_and_environments", "Modules, packages, and reproducible environments", "Intermediate",
    ["Import standard-library tools", "Create and run a module", "Distinguish terminal commands from Python code"], [
    lesson("1. Use the standard library", "A module is a Python file or another importable unit. A package groups modules. Python ships with the standard library; third-party packages are installed into an environment. Importing does not install a package.", '''
        import math
        from statistics import median
        from collections import Counter
        print(math.sqrt(81))
        print(median([1, 100, 3]))
        print(Counter("banana"))
    ''', "Use math.ceil(2.1) and math.floor(2.9). Compare mean and median with an outlier."),
    lesson("2. A module that is also a script", "The __name__ guard runs a demonstration only when the file is executed as a script. This example creates a module in a temporary folder and uses the current Python interpreter to run it. subprocess.run receives an argument list, without shell string construction.", '''
        from pathlib import Path
        from tempfile import TemporaryDirectory
        import subprocess
        import sys

        module_source = 'def square(n):\\n    return n * n\\n\\nif __name__ == "__main__":\\n    print(square(7))\\n'
        with TemporaryDirectory() as folder:
            module_path = Path(folder) / "math_helpers.py"
            module_path.write_text(module_source, encoding="utf-8")
            result = subprocess.run([sys.executable, str(module_path)],
                                    capture_output=True, text=True, check=True)
            print(result.stdout.strip())
        assert result.stdout.strip() == "49"
    ''', "Change the demonstration input to 8 and rerun."),
    lesson("3. Know which interpreter runs", "An environment keeps a project's installed packages separate. The README contains PowerShell setup commands. Commands such as python -m pip install belong in a terminal, not an ordinary Python cell. In notebooks, %pip targets the current kernel, but you may need to restart it after installation.", '''
        import sys
        import importlib.metadata
        print("Kernel interpreter:", sys.executable)
        print("ipykernel version:", importlib.metadata.version("ipykernel"))
    ''', "Compare the kernel interpreter with the .venv path shown in README.md.")], [
    exercise("Word frequencies", "Use Counter on words.split() and store the result in counts.", 'words = "code read code test read code"\ncounts = None', 'assert counts["code"] == 3\nassert counts["read"] == 2\nassert counts["missing"] == 0', 'from collections import Counter\nwords = "code read code test read code"\ncounts = Counter(words.split())', "Counter returns zero for missing keys."),
    exercise("Hypotenuse", "Implement hypotenuse(a, b) with math.hypot.", 'def hypotenuse(a, b):\n    pass', 'assert hypotenuse(3, 4) == 5\nassert hypotenuse(0, 0) == 0', 'import math\ndef hypotenuse(a, b):\n    return math.hypot(a, b)', "Import math before calling math.hypot.")],
    "Create a small helpers.py in your own practice folder and import one function into a notebook. Add a __name__ guard. Restart the kernel after editing the module, then reimport and verify the change.",
    "Do not name your files json.py, csv.py, or another library name: they can shadow the real modules. Imports are cached within a process.")

add("09_object_oriented_python", "Objects, classes, and composition", "Intermediate",
    ["Model state and behavior together", "Protect an object's invariants", "Use composition and a simple special method"], [
    lesson("1. Define a class", "A class describes objects with related data and behavior. __init__ initializes each instance. self refers to that instance. Each BankAccount below has its own balance, represented in integer minor units to avoid float rounding.", '''
        class BankAccount:
            def __init__(self, owner, balance=0):
                if balance < 0:
                    raise ValueError("balance cannot be negative")
                self.owner = owner
                self._balance = balance

            @property
            def balance(self):
                return self._balance

            def deposit(self, amount):
                if amount <= 0:
                    raise ValueError("deposit must be positive")
                self._balance += amount

            def __repr__(self):
                return f"BankAccount({self.owner!r}, balance={self.balance})"

        account = BankAccount("Mira", 1000)
        account.deposit(500)
        print(account)
        assert account.balance == 1500
    ''', "Create a second account. Check that deposits in one do not affect the other."),
    lesson("2. Compose objects", "Composition means an object uses another object. This often keeps responsibilities clearer than a deep inheritance tree. A Wallet delegates storage and validation to an account instead of reimplementing it.", '''
        class Wallet:
            def __init__(self, account):
                self.account = account

            def summary(self):
                return f"{self.account.owner}: {self.account.balance} minor units"

        wallet = Wallet(account)
        print(wallet.summary())
    ''', "Pass a different account to a new wallet. Explain which object owns the balance."),
    lesson("3. Inherit only for a useful relationship", "Inheritance can specialize behavior when the new type can stand in for the original. Python also supports duck typing: code can work with any object providing the operations it needs, regardless of inheritance.", '''
        class Animal:
            def speak(self):
                return "sound"

        class Dog(Animal):
            def speak(self):
                return "woof"

        def announce(animal):
            return animal.speak().upper()

        print(announce(Dog()))
        assert isinstance(Dog(), Animal)
    ''', "Add a Cat subclass and pass it to announce().")], [
    exercise("A counter object", "Implement CounterBox with instance attribute value starting at 0 and increment() increasing it by one.", 'class CounterBox:\n    def __init__(self):\n        pass\n\n    def increment(self):\n        pass', 'a, b = CounterBox(), CounterBox()\na.increment()\na.increment()\nassert a.value == 2\nassert b.value == 0', 'class CounterBox:\n    def __init__(self):\n        self.value = 0\n\n    def increment(self):\n        self.value += 1', "Initialize self.value, not a shared class-level counter."),
    exercise("A rectangle object", "Implement Rectangle(width, height) and area() returning width * height. Assume nonnegative dimensions.", 'class Rectangle:\n    def __init__(self, width, height):\n        pass\n\n    def area(self):\n        pass', 'assert Rectangle(4, 3).area() == 12\nassert Rectangle(0, 3).area() == 0', 'class Rectangle:\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n\n    def area(self):\n        return self.width * self.height', "Store both dimensions on self.")],
    "Extend BankAccount with withdraw(amount). Reject nonpositive withdrawals and overdrafts. Verify that a failed withdrawal leaves the balance unchanged. Decide whether a class is useful compared with plain functions and data.",
    "A leading underscore is a convention, not enforced privacy. This demonstration validates sign, but a production money class should also enforce types, units, and currency rules.")

add("10_testing_and_quality", "Testing behavior and preventing regressions", "Intermediate",
    ["Test normal, boundary, and invalid inputs", "Run unittest inside a notebook", "Inject a dependency for deterministic tests"], [
    lesson("1. A function with a contract", "A good test checks observable behavior against an independently known result. Include boundaries and invalid inputs. Keep production validation explicit, and use assertions in tests.", '''
        def shipping_cost(total):
            """Return shipping in whole currency units; free at 500 or above."""
            if total < 0:
                raise ValueError("total cannot be negative")
            return 0 if total >= 500 else 40

        assert shipping_cost(0) == 40
        assert shipping_cost(499) == 40
        assert shipping_cost(500) == 0
    ''', "Predict what would break if >= became >. Which test catches it?"),
    lesson("2. A small test suite", "unittest is built into Python. Each test method describes one behavior. The explicit runner works inside notebooks without unittest.main() consuming Jupyter's command-line arguments.", '''
        import unittest

        class ShippingTests(unittest.TestCase):
            def test_threshold(self):
                self.assertEqual(shipping_cost(500), 0)

            def test_below_threshold(self):
                self.assertEqual(shipping_cost(499), 40)

            def test_negative_rejected(self):
                with self.assertRaises(ValueError):
                    shipping_cost(-1)

        suite = unittest.defaultTestLoader.loadTestsFromTestCase(ShippingTests)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        assert result.wasSuccessful()
    ''', "Temporarily introduce the >= to > bug, run the suite, then restore it."),
    lesson("3. Test changing external inputs", "Passing a dependency as an argument makes a function easier to test. Here the caller supplies a clock, so a test never depends on the actual day. Similar techniques work for HTTP clients and file readers.", '''
        from datetime import date

        def greeting_for_today(name, today):
            return f"Hello {name}, today is {today().isoformat()}"

        def fixed_day():
            return date(2025, 1, 2)

        assert greeting_for_today("Mira", fixed_day) == "Hello Mira, today is 2025-01-02"
        print(greeting_for_today("Mira", fixed_day))
    ''', "Use a second fixed date and verify the new expected string.")], [
    exercise("Test and fix the boundary", "Fix is_adult: it should return True from age 18 onward and False below 18. Inputs are nonnegative integers.", 'def is_adult(age):\n    return age > 18  # Find and fix the boundary bug.', 'assert is_adult(17) is False\nassert is_adult(18) is True\nassert is_adult(19) is True', 'def is_adult(age):\n    return age >= 18', "The boundary belongs in the accepted range."),
    exercise("Implement a tested slug", "Implement slug(text): strip whitespace, lowercase, split on whitespace, and join words with '-'. Punctuation is preserved in this simplified contract.", 'def slug(text):\n    pass', 'assert slug("  Learn PYTHON  ") == "learn-python"\nassert slug("") == ""\nassert slug("one   two") == "one-two"\nassert slug("Hi!") == "hi!"', 'def slug(text):\n    return "-".join(text.lower().split())', "split() without arguments handles both outer and repeated spaces.")],
    "Write five tests for the withdraw method from notebook 09 in this notebook, copying your class here to keep it independent. Cover success, zero, negative, overdraft, and unchanged state after rejection.",
    "A passing test suite only establishes the cases and properties it checks. Avoid tests that merely repeat the implementation's expression as the expected result.")

add("11_comprehensions_iterators_generators", "Comprehensions, iterators, and lazy pipelines", "Advanced",
    ["Transform collections clearly", "Recognize iterator exhaustion", "Process values lazily with yield"], [
    lesson("1. Comprehensions", "A comprehension is a compact transformation, optionally with a filter. Prefer an ordinary loop if nesting or side effects make the expression hard to read.", '''
        numbers = range(1, 7)
        squares = [n * n for n in numbers if n % 2 == 0]
        lengths = {word: len(word) for word in ["code", "practice"]}
        print(squares, lengths)
        assert squares == [4, 16, 36]
    ''', "Rewrite the list comprehension as a for loop and compare results."),
    lesson("2. Iterator protocol", "An iterable can produce an iterator. next() consumes one item; an exhausted iterator stays exhausted. The optional default avoids StopIteration. A list is reusable; a particular iterator over it is consumed.", '''
        values = [10, 20]
        iterator = iter(values)
        print(next(iterator), next(iterator))
        print(next(iterator, "finished"))
        print(list(iterator), list(values))
    ''', "Create a fresh iter(values), then consume only one item before calling list()."),
    lesson("3. yield and streaming", "A generator function pauses at yield and resumes on the next request. Lazy pipelines avoid materializing all intermediate values. They still do work when consumed, and are normally single-use.", '''
        def running_totals(values):
            total = 0
            for value in values:
                total += value
                yield total

        totals = running_totals([3, 4, 5])
        print(next(totals))
        print(list(totals))
        print(sum(n * n for n in range(100)))
        assert list(running_totals([])) == []
    ''', "Predict list(totals) if you run it again without rebuilding the generator.")], [
    exercise("Filter a mapping", "Create adults mapping names to ages for people aged at least 18.", 'ages = {"Asha": 17, "Mira": 24, "Dev": 18}\nadults = None', 'assert adults == {"Mira": 24, "Dev": 18}', 'ages = {"Asha": 17, "Mira": 24, "Dev": 18}\nadults = {name: age for name, age in ages.items() if age >= 18}', "Iterate over ages.items()."),
    exercise("Generate chunks", "Implement chunks(items, size), yielding list slices of at most size elements. Raise ValueError if size <= 0. Assume items is a list and size an integer.", 'def chunks(items, size):\n    pass', 'assert list(chunks([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]\nassert list(chunks([], 2)) == []\ntry:\n    list(chunks([1], 0))\nexcept ValueError:\n    pass\nelse:\n    raise AssertionError("size=0 must fail")', 'def chunks(items, size):\n    if size <= 0:\n        raise ValueError("size must be positive")\n    for start in range(0, len(items), size):\n        yield items[start:start + size]', "Use range(start, stop, step) and slicing. Generator errors occur when consumed.")],
    "Create a generator pipeline over a list of log lines: strip lines, skip empty lines, select ERROR lines, and count them. Explain where memory is saved and where it is not.",
    "Printing a generator does not show its values. list(generator) consumes it and allocates memory for every result; use that deliberately.")

add("12_decorators_and_context_managers", "Decorators and context managers", "Advanced",
    ["Treat functions as values", "Wrap behavior while preserving metadata", "Guarantee cleanup with try/finally"], [
    lesson("1. Closures", "A closure is a function that remembers names from an enclosing scope. Functions are objects, so they can be returned and passed around. This creates configured behavior without global variables.", '''
        def make_multiplier(factor):
            def multiply(value):
                return value * factor
            return multiply

        double = make_multiplier(2)
        triple = make_multiplier(3)
        print(double(5), triple(5))
    ''', "Create a multiplier for 10. Explain which factor each function remembers."),
    lesson("2. Decorators", "A decorator receives a function and returns a replacement. @trace is shorthand for add = trace(add). *args and **kwargs forward positional and keyword arguments; wraps preserves metadata for documentation and debugging.", '''
        from functools import wraps

        def trace(function):
            @wraps(function)
            def wrapper(*args, **kwargs):
                print("Calling", function.__name__)
                return function(*args, **kwargs)
            return wrapper

        @trace
        def add(a, b):
            """Add two values."""
            return a + b

        assert add(2, b=3) == 5
        print(add.__name__, add.__doc__)
    ''', "Decorate another function. Verify that its return value is preserved."),
    lesson("3. Cleanup even on failure", "A context manager controls entry and exit around a with block. In a contextmanager generator, code before yield acquires a resource and finally releases it. finally runs even if the block raises.", '''
        from contextlib import contextmanager

        @contextmanager
        def recorded_session(events):
            events.append("open")
            try:
                yield events
            finally:
                events.append("close")

        events = []
        try:
            with recorded_session(events):
                events.append("work")
                raise ValueError("demonstration")
        except ValueError:
            pass
        print(events)
        assert events == ["open", "work", "close"]
    ''', "Remove the deliberate error and compare the event sequence.")], [
    exercise("Configured addition", "Implement make_adder(amount), returning a function that adds amount to its input.", 'def make_adder(amount):\n    pass', 'assert make_adder(5)(3) == 8\nassert make_adder(-1)(1) == 0', 'def make_adder(amount):\n    def add(value):\n        return value + amount\n    return add', "Return the inner function without calling it."),
    exercise("Uppercase decorator", "Implement uppercase_result(function) that uppercases the returned string, forwards arguments, and preserves metadata with wraps.", 'def uppercase_result(function):\n    pass', 'def greet(name="world"):\n    return f"Hello {name}"\nwrapped = uppercase_result(greet)\nassert wrapped(name="Mira") == "HELLO MIRA"\nassert wrapped.__name__ == "greet"', 'from functools import wraps\ndef uppercase_result(function):\n    @wraps(function)\n    def wrapper(*args, **kwargs):\n        return function(*args, **kwargs).upper()\n    return wrapper', "Modify the returned value inside a wrapper.")],
    "Create a timing context manager using time.perf_counter(). Ensure it reports elapsed time even when the block raises. Compare three runs; do not expect identical timings.",
    "A wrapper that forgets return silently changes behavior to return None. Context managers should not suppress failures unless that is an explicit part of their contract.")

add("13_types_dataclasses_and_protocols", "Type hints, dataclasses, and interfaces", "Advanced",
    ["Describe data with type hints", "Use dataclasses for records", "Separate an interface from an implementation"], [
    lesson("1. Hints describe a contract", "Annotations help readers and static analyzers. Python does not enforce them automatically. Use explicit checks for runtime validation. The union syntax X | None represents an optional value.", '''
        def first_long_word(words: list[str], minimum: int = 5) -> str | None:
            for word in words:
                if len(word) >= minimum:
                    return word
            return None

        print(first_long_word(["a", "python", "code"]))
        assert first_long_word([]) is None
        print(first_long_word.__annotations__)
    ''', "Change minimum to 7. Explain why the return type includes None."),
    lesson("2. Dataclasses", "A dataclass generates initialization, representation, and equality methods. frozen=True prevents ordinary attribute reassignment; it does not deeply freeze nested data. default_factory creates a fresh mutable container for each instance.", '''
        from dataclasses import dataclass, field

        @dataclass(frozen=True)
        class Product:
            name: str
            price_minor: int

            def __post_init__(self):
                if self.price_minor < 0:
                    raise ValueError("price cannot be negative")

        @dataclass
        class Basket:
            products: list[Product] = field(default_factory=list)

        a, b = Basket(), Basket()
        a.products.append(Product("Pen", 1000))
        print(a, b)
        assert b.products == []
    ''', "Try Product('Pen', -1) inside try/except. Discuss why validation is explicit."),
    lesson("3. Structural interfaces", "A Protocol describes operations a consumer needs. Implementations need not inherit from it. A static type checker can compare a class to this interface; these annotations alone do not run such a checker.", '''
        from typing import Protocol

        class Sender(Protocol):
            def send(self, message: str) -> str: ...

        class PreviewSender:
            def send(self, message: str) -> str:
                return f"Preview: {message}"

        def notify(sender: Sender, message: str) -> str:
            return sender.send(message)

        print(notify(PreviewSender(), "Practice complete"))
    ''', "Add a second implementation that records messages in a list. No messages are actually sent externally.")], [
    exercise("Typed record", "Create a frozen dataclass Point with float fields x and y, plus method distance_squared() returning x*x + y*y.", '# Define Point here.', 'point = Point(3.0, 4.0)\nassert point.distance_squared() == 25.0\nassert Point(1, 2) == Point(1, 2)\nfrom dataclasses import FrozenInstanceError\ntry:\n    point.x = 0\nexcept FrozenInstanceError:\n    pass\nelse:\n    raise AssertionError("Point should be frozen")', 'from dataclasses import dataclass\n@dataclass(frozen=True)\nclass Point:\n    x: float\n    y: float\n\n    def distance_squared(self) -> float:\n        return self.x * self.x + self.y * self.y', "Use @dataclass(frozen=True)."),
    exercise("Optional lookup", "Implement lookup_price(prices: dict[str, int], name: str) -> int | None, returning None for missing names.", 'def lookup_price(prices: dict[str, int], name: str) -> int | None:\n    pass', 'assert lookup_price({"pen": 10}, "pen") == 10\nassert lookup_price({}, "pen") is None\nassert lookup_price({"free": 0}, "free") == 0', 'def lookup_price(prices: dict[str, int], name: str) -> int | None:\n    return prices.get(name)', "A missing value and a valid zero must stay distinct.")],
    "Model a reading list with Book dataclasses and a Repository Protocol. Write an in-memory implementation, then test a service using it. Optional: install and run a static checker in this project environment.",
    "Annotations are not input validation. Protocols describe a dependency's required behavior; avoid adding methods the consumer never uses.")

add("14_standard_library_toolkit", "Dates, exact decimals, regular expressions, and collections", "Intermediate to advanced",
    ["Work with dates and explicit timezones", "Use Decimal for exact decimal arithmetic", "Apply focused text patterns and collection tools"], [
    lesson("1. Dates and aware times", "date models calendar dates; timedelta models durations. Use timezone-aware datetimes for instants. A fixed +05:30 offset below needs no timezone database; geographic timezones with daylight-saving changes need zoneinfo and appropriate timezone data.", '''
        from datetime import date, datetime, timedelta, timezone
        start = date(2025, 1, 1)
        print("One week later:", start + timedelta(days=7))
        utc_time = datetime(2025, 1, 1, 12, tzinfo=timezone.utc)
        india_offset = timezone(timedelta(hours=5, minutes=30))
        print(utc_time.astimezone(india_offset).isoformat())
    ''', "Convert 22:00 UTC and observe whether the calendar date changes."),
    lesson("2. Decimal from text", "Decimal constructed from a string preserves the intended decimal value. Constructing it from a float also preserves that float's approximation. Choose a rounding rule explicitly when reducing precision.", '''
        from decimal import Decimal, ROUND_HALF_UP
        price = Decimal("19.99")
        total = (price * 3 * Decimal("1.05")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        print(total)
        assert Decimal("0.1") + Decimal("0.2") == Decimal("0.3")
        assert total == Decimal("62.97")
    ''', "Compare Decimal('0.1') with Decimal(0.1)."),
    lesson("3. Focused patterns and queues", "Regular expressions match text patterns. Use raw strings for patterns with backslashes. fullmatch requires the entire string to fit. A deque efficiently adds and removes items at both ends.", '''
        import re
        from collections import deque, defaultdict
        pattern = re.compile(r"TASK-[0-9]{3}")
        print(bool(pattern.fullmatch("TASK-042")))
        print(bool(pattern.fullmatch("xTASK-042")))
        queue = deque(["read", "code"])
        queue.append("review")
        print(queue.popleft(), list(queue))
        grouped = defaultdict(list)
        for category, item in [("food", "rice"), ("tools", "pen"), ("food", "tea")]:
            grouped[category].append(item)
        print(dict(grouped))
    ''', "Change the pattern to accept exactly four digits.")], [
    exercise("Days between dates", "Implement days_between(start, end) for ISO YYYY-MM-DD strings, returning (end - start).days.", 'def days_between(start, end):\n    pass', 'assert days_between("2024-02-28", "2024-03-01") == 2\nassert days_between("2025-01-01", "2025-01-01") == 0', 'from datetime import date\ndef days_between(start, end):\n    return (date.fromisoformat(end) - date.fromisoformat(start)).days', "Parse both strings with date.fromisoformat()."),
    exercise("Product-code validation", "Return True only for two uppercase ASCII letters, a hyphen, and exactly four ASCII digits, such as AB-1234.", 'def valid_code(text):\n    pass', 'assert valid_code("AB-1234") is True\nassert valid_code("ab-1234") is False\nassert valid_code("AB-12345") is False\nassert valid_code("prefix AB-1234") is False', 'import re\ndef valid_code(text):\n    return re.fullmatch(r"[A-Z]{2}-[0-9]{4}", text) is not None', "Use fullmatch, [A-Z], and [0-9].")],
    "Parse dated expense records, total their string amounts with Decimal, and group them by month. Include February 29 in a leap year and one invalid date in your checks.",
    "Regex is not a universal parser. Use dedicated parsers for JSON and CSV. Naive and aware datetimes are different kinds of values and should not be mixed casually.")

add("15_algorithms_and_complexity", "Algorithms, recursion, and complexity", "Advanced",
    ["Explain time and space tradeoffs", "Implement binary search", "Use caching on repeated subproblems"], [
    lesson("1. Count work before timing", "Big-O describes how work grows with input size; it is not an exact stopwatch prediction. A list scan is O(n), while set membership is expected O(1) after building the set. Constructing the set costs O(n) time and additional memory.", '''
        def linear_find(items, target):
            comparisons = 0
            for index, item in enumerate(items):
                comparisons += 1
                if item == target:
                    return index, comparisons
            return -1, comparisons

        print(linear_find(list(range(10)), 9))
        print(linear_find(list(range(100)), 99))
    ''', "Compare a match at the beginning with a missing target."),
    lesson("2. Binary search", "For sorted random-access data, binary search halves the remaining interval each step: O(log n) comparisons. Sorting first costs O(n log n), so it may not pay off for a single lookup. This version returns any matching index or -1.", '''
        def binary_search(items, target):
            low, high = 0, len(items) - 1
            while low <= high:
                middle = (low + high) // 2
                if items[middle] == target:
                    return middle
                if items[middle] < target:
                    low = middle + 1
                else:
                    high = middle - 1
            return -1

        assert binary_search([2, 4, 6, 8], 6) == 2
        assert binary_search([], 6) == -1
        assert binary_search([2, 4], 3) == -1
        print(binary_search([2, 4, 6, 8], 8))
    ''', "Trace low, high, and middle on paper for target 3."),
    lesson("3. Recursion and memoization", "Recursive functions solve smaller versions of a problem and need a base case. Caching avoids recomputing the same input. This Fibonacci version has O(n) distinct subproblems, though recursion depth still limits large n. An iterative approach avoids recursive stack growth.", '''
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def fibonacci(n):
            if n < 0:
                raise ValueError("n must be nonnegative")
            if n < 2:
                return n
            return fibonacci(n - 1) + fibonacci(n - 2)

        print(fibonacci(20))
        print(fibonacci.cache_info())
        assert fibonacci(10) == 55
    ''', "Call fibonacci(20) again and inspect the hit count.")], [
    exercise("Stable deduplication", "Return a new list with duplicates removed while preserving first-seen order. Inputs contain hashable values. Aim for expected O(n) time.", 'def unique_in_order(items):\n    pass', 'assert unique_in_order([3, 1, 3, 2, 1]) == [3, 1, 2]\nassert unique_in_order([]) == []', 'def unique_in_order(items):\n    seen = set()\n    result = []\n    for item in items:\n        if item not in seen:\n            seen.add(item)\n            result.append(item)\n    return result', "Use a set for membership and a list for output order."),
    exercise("Iterative factorial", "Compute n! for a nonnegative integer using a loop. Return 1 for n=0; raise ValueError for negative n.", 'def factorial(n):\n    pass', 'assert factorial(0) == 1\nassert factorial(5) == 120\ntry:\n    factorial(-1)\nexcept ValueError:\n    pass\nelse:\n    raise AssertionError("negative n must fail")', 'def factorial(n):\n    if n < 0:\n        raise ValueError("n must be nonnegative")\n    result = 1\n    for value in range(2, n + 1):\n        result *= value\n    return result', "Start the accumulator at 1, not 0.")],
    "Implement two-sum: return indexes of two distinct items whose values add to a target, or None. First use nested loops; then use a dictionary for expected O(n) time. Test duplicates, negatives, and no match.",
    "Binary search requires sorted data. Recursive elegance does not eliminate stack limits. Caches consume memory and require hashable arguments.")

add("16_sqlite_and_persistence", "SQLite: query and persist structured data", "Advanced",
    ["Create tables and parameterized queries", "Aggregate with SQL", "Use transactions and close connections"], [
    lesson("1. A database lifecycle", "SQLite is included with Python. ':memory:' creates a temporary database; a filename creates a persistent one. A connection's with block handles transactions but does not close it. closing() ensures cleanup.", '''
        import sqlite3
        from contextlib import closing

        with closing(sqlite3.connect(":memory:")) as connection:
            connection.row_factory = sqlite3.Row
            with connection:
                connection.execute("CREATE TABLE expenses (id INTEGER PRIMARY KEY, category TEXT NOT NULL, amount INTEGER CHECK(amount > 0))")
                connection.executemany("INSERT INTO expenses(category, amount) VALUES (?, ?)",
                                       [("food", 120), ("travel", 80), ("food", 50)])
            rows = connection.execute("SELECT category, SUM(amount) AS total FROM expenses GROUP BY category ORDER BY category").fetchall()
            totals = {row["category"]: row["total"] for row in rows}
        print(totals)
        assert totals == {"food": 170, "travel": 80}
    ''', "Add an expense to the input rows and predict the new totals."),
    lesson("2. Parameters are data", "Use ? placeholders for values. Concatenating user values into SQL can change the query's meaning. Parameters do not stand in for table or column names; those need a trusted allowlist if dynamic.", '''
        with closing(sqlite3.connect(":memory:")) as connection:
            connection.execute("CREATE TABLE users (name TEXT)")
            connection.executemany("INSERT INTO users VALUES (?)", [("Mira",), ("Dev",)])
            entered_name = "' OR 1=1 --"
            matches = connection.execute("SELECT name FROM users WHERE name = ?", (entered_name,)).fetchall()
        print("Matches:", matches)
        assert matches == []
    ''', "Set entered_name to Mira. Observe the result without changing the SQL."),
    lesson("3. Roll back a failed transaction", "A transaction groups changes that should succeed or fail together. An exception escaping the connection's with block rolls back the transaction. Here one invalid row prevents both inserts from being committed.", '''
        with closing(sqlite3.connect(":memory:")) as connection:
            connection.execute("CREATE TABLE numbers (value INTEGER CHECK(value > 0))")
            try:
                with connection:
                    connection.execute("INSERT INTO numbers VALUES (?)", (5,))
                    connection.execute("INSERT INTO numbers VALUES (?)", (-1,))
            except sqlite3.IntegrityError:
                print("Both inserts rolled back")
            count = connection.execute("SELECT COUNT(*) FROM numbers").fetchone()[0]
        assert count == 0
    ''', "Use 1 instead of -1 and predict count. Update the expected assertion for that experiment.")], [
    exercise("Filter with SQL", "Implement expensive_items(connection, minimum) to return (name, price) rows with price >= minimum, ordered by price then name. The items table already exists in the checks.", 'def expensive_items(connection, minimum):\n    pass', 'with closing(sqlite3.connect(":memory:")) as db:\n    db.execute("CREATE TABLE items (name TEXT, price INTEGER)")\n    db.executemany("INSERT INTO items VALUES (?, ?)", [("pen", 10), ("book", 80), ("bag", 200)])\n    assert expensive_items(db, 80) == [("book", 80), ("bag", 200)]\n    assert expensive_items(db, 999) == []', 'def expensive_items(connection, minimum):\n    return connection.execute("SELECT name, price FROM items WHERE price >= ? ORDER BY price, name", (minimum,)).fetchall()', "Use a one-element tuple (minimum,) for the parameter."),
    exercise("Insert one row", "Implement add_item(connection, name, price) with a parameterized INSERT into items(name, price). The caller controls committing.", 'def add_item(connection, name, price):\n    pass', 'with closing(sqlite3.connect(":memory:")) as db:\n    db.execute("CREATE TABLE items (name TEXT, price INTEGER)")\n    add_item(db, "Mira\'s book", 90)\n    assert db.execute("SELECT name, price FROM items").fetchall() == [("Mira\'s book", 90)]', 'def add_item(connection, name, price):\n    connection.execute("INSERT INTO items(name, price) VALUES (?, ?)", (name, price))', "An apostrophe in a value should work without manual escaping.")],
    "Build a task table with id, title, and done. Insert three tasks, mark one complete with UPDATE, and query unfinished tasks. Use a temporary file database and reopen it to demonstrate persistence.",
    "SQL row order is unspecified without ORDER BY. Remember to commit writes intended to persist. A real application also needs schema migrations and a backup plan.")

add("17_http_apis_and_json", "HTTP APIs with a local practice server", "Advanced",
    ["Make a real HTTP request with a timeout", "Decode JSON and inspect status errors", "Separate response parsing from transport"], [
    lesson("1. The request-response model", "An HTTP client sends a method and URL; a server responds with a status, headers, and body. GET normally retrieves data. This tiny server listens only on your computer and serves fixed practice data, so no account or internet connection is needed. It shuts down after the demonstration.", '''
        import json
        from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
        from threading import Thread
        from urllib.request import urlopen
        from urllib.error import HTTPError

        class PracticeHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path == "/tasks":
                    status = 200
                    payload = {"tasks": [{"id": 1, "title": "Practice", "done": False}]}
                else:
                    status = 404
                    payload = {"error": "not found"}
                body = json.dumps(payload).encode("utf-8")
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, format, *args):
                pass  # Keep the educational output focused.

        server = ThreadingHTTPServer(("127.0.0.1", 0), PracticeHandler)
        worker = Thread(target=server.serve_forever, daemon=True)
        worker.start()
        base_url = f"http://127.0.0.1:{server.server_port}"
        try:
            with urlopen(base_url + "/tasks", timeout=2) as response:
                print("Status:", response.status)
                payload = json.loads(response.read().decode("utf-8"))
                print(payload)
            try:
                urlopen(base_url + "/missing", timeout=2)
            except HTTPError as error:
                print("Expected missing-resource status:", error.code)
                error.close()
        finally:
            server.shutdown()
            server.server_close()
            worker.join(timeout=2)
        assert payload["tasks"][0]["title"] == "Practice"
    ''', "Change the task title in the handler and rerun the whole cell."),
    lesson("2. Build query strings", "Query parameters belong in the URL after ?. urlencode handles reserved characters and spaces. Avoid manually joining unescaped user text into a URL.", '''
        from urllib.parse import urlencode, parse_qs
        params = {"search": "python & data", "page": 2}
        query = urlencode(params)
        print("https://example.com/tasks?" + query)
        assert parse_qs(query)["search"] == ["python & data"]
    ''', "Try a search containing + or a non-ASCII character."),
    lesson("3. Validate the shape", "Valid JSON is not necessarily the expected schema. Validate fields at a boundary before processing them. Real clients also distinguish transport failures, invalid JSON, authentication failures, rate limits, and server errors. Retry only when the operation and error make retrying appropriate.", '''
        def task_titles(payload):
            if not isinstance(payload, dict) or not isinstance(payload.get("tasks"), list):
                raise ValueError("expected an object containing a tasks list")
            titles = []
            for task in payload["tasks"]:
                if not isinstance(task, dict) or not isinstance(task.get("title"), str):
                    raise ValueError("each task needs a string title")
                titles.append(task["title"])
            return titles

        assert task_titles({"tasks": [{"title": "Read"}]}) == ["Read"]
        assert task_titles({"tasks": []}) == []
        print(task_titles(payload))
    ''', "Pass {'tasks': [42]} inside try/except and inspect the error.")], [
    exercise("Select completed tasks", "Return titles of tasks whose done field is True. Assume tasks have valid title and boolean done fields.", 'def completed_titles(tasks):\n    pass', 'assert completed_titles([{"title": "Read", "done": True}, {"title": "Code", "done": False}]) == ["Read"]\nassert completed_titles([]) == []', 'def completed_titles(tasks):\n    return [task["title"] for task in tasks if task["done"]]', "Filter before extracting titles."),
    exercise("Flatten pages", "Each response page contains an items list. Return all items in page order; treat a missing items field as an empty list.", 'def collect_items(pages):\n    pass', 'assert collect_items([{"items": [1, 2]}, {}, {"items": [3]}]) == [1, 2, 3]\nassert collect_items([]) == []', 'def collect_items(pages):\n    result = []\n    for page in pages:\n        result.extend(page.get("items", []))\n    return result', "extend adds the elements; append would add the list itself.")],
    "Extend the local server with a /health route and test both success and 404 responses. Then design a paginated response with a next-page field. Keep credentials out of notebook cells and saved outputs if you later try an authenticated API.",
    "Never assume every response is successful JSON. This local HTTP demo is for practice; external services should use HTTPS and their documented authentication and usage rules.")

add("18_concurrency_threads_and_async", "Concurrency: threads and asyncio", "Advanced",
    ["Distinguish concurrency from parallelism", "Use a thread pool for waiting tasks", "Run bounded asynchronous work in Jupyter"], [
    lesson("1. Overlap waiting with threads", "Concurrency lets tasks make progress during each other's waits. This mock I/O uses sleep instead of external services. Thread pools often help blocking I/O. In a typical GIL-enabled CPython build, threads do not normally speed up CPU-bound Python loops; processes are one option for those workloads.", '''
        from concurrent.futures import ThreadPoolExecutor
        import time

        def fetch_mock(item):
            time.sleep(0.03)
            return f"item-{item}"

        started = time.perf_counter()
        with ThreadPoolExecutor(max_workers=3) as pool:
            results = list(pool.map(fetch_mock, range(6)))
        print(results)
        print(f"Elapsed: {time.perf_counter() - started:.3f}s")
        assert results == [f"item-{n}" for n in range(6)]
    ''', "Compare max_workers=1 and 3. Timing varies, so do not assert an exact speedup."),
    lesson("2. Async functions cooperate", "An async function returns a coroutine. await pauses it until an awaitable completes, allowing other work to run. Jupyter supports top-level await because it already runs an event loop; use asyncio.run(main()) at the entry point of a normal script instead.", '''
        import asyncio

        async def fetch_async(item):
            await asyncio.sleep(0.03)
            return item * 2

        async_results = await asyncio.gather(*(fetch_async(n) for n in range(4)))
        print(async_results)
        assert async_results == [0, 2, 4, 6]
    ''', "Replace gather with a loop that awaits one task at a time and compare elapsed time."),
    lesson("3. Bound concurrency and timeouts", "A semaphore limits simultaneous work. Use timeouts so stalled operations cannot wait indefinitely. Cleanup belongs in finally or context managers; cancellation is part of a task's lifecycle.", '''
        async def run_bounded():
            semaphore = asyncio.Semaphore(2)

            async def limited(item):
                async with semaphore:
                    return await fetch_async(item)

            return await asyncio.wait_for(
                asyncio.gather(*(limited(n) for n in range(5))), timeout=2
            )

        bounded_results = await run_bounded()
        print(bounded_results)
        assert bounded_results == [0, 2, 4, 6, 8]
    ''', "Set the limit to 1, then 5. Explain why the output order remains unchanged.")], [
    exercise("Threaded transformation", "Implement threaded_lengths(words) with ThreadPoolExecutor.map and return lengths in input order. This is API practice, not a speed optimization for such a small CPU task.", 'def threaded_lengths(words):\n    pass', 'assert threaded_lengths(["a", "python", "code"]) == [1, 6, 4]\nassert threaded_lengths([]) == []', 'from concurrent.futures import ThreadPoolExecutor\ndef threaded_lengths(words):\n    with ThreadPoolExecutor(max_workers=2) as pool:\n        return list(pool.map(len, words))', "map preserves the order of inputs."),
    exercise("An async function", "Implement async_square(n): await asyncio.sleep(0), then return n*n. sleep(0) explicitly yields control without a positive delay.", 'async def async_square(n):\n    pass', 'assert await async_square(3) == 9\nassert await asyncio.gather(async_square(0), async_square(-2)) == [0, 4]', 'import asyncio\nasync def async_square(n):\n    await asyncio.sleep(0)\n    return n * n', "Use async def and await inside it.")],
    "Simulate ten downloads with a concurrency limit of three, record their start and finish events, and verify that no more than three are active at once. Add a failing operation and decide how callers should receive its error.",
    "time.sleep blocks the event-loop thread; asyncio.sleep yields control. Shared mutable state needs coordination. For process pools on Windows, put worker functions in an importable .py file and protect script startup with a __name__ guard.")

add("19_numpy_numerical_python", "NumPy: numerical arrays", "Applied Python",
    ["Understand array shape and dtype", "Use vectorized operations and broadcasting", "Recognize views and copies"], [
    lesson("1. Arrays and vectorization", "NumPy arrays store values of a common dtype and support elementwise operations. Multiplying a Python list repeats it; multiplying an array multiplies its elements. shape gives the length of each dimension.", '''
        import numpy as np
        prices = np.array([10.0, 20.0, 30.0])
        print("List:", [1, 2] * 2)
        print("Array:", np.array([1, 2]) * 2)
        print(prices.shape, prices.dtype)
        discounted = prices * 0.9
        print(discounted)
        np.testing.assert_allclose(discounted, [9, 18, 27])
    ''', "Compute a 15% discount without a Python for loop."),
    lesson("2. Axes and broadcasting", "For a two-dimensional array, axis=0 reduces over rows, leaving one value per column; axis=1 reduces over columns. Broadcasting aligns trailing dimensions when sizes match or one size is 1. @ performs matrix multiplication, while * multiplies elementwise.", '''
        scores = np.array([[70, 80, 90], [60, 75, 85]])
        print("Shape:", scores.shape)
        print("Subject means:", scores.mean(axis=0))
        print("Student means:", scores.mean(axis=1))
        bonus = np.array([5, 0, 2])
        print("Adjusted:\\n", scores + bonus)
        weights = np.array([0.2, 0.3, 0.5])
        print("Weighted scores:", scores @ weights)
    ''', "Predict the output shape before each calculation."),
    lesson("3. Masks, views, and copies", "A boolean mask selects matching values. Basic slicing often produces a view sharing memory with the original. Use copy() when you need independent storage. Boolean indexing produces a new array.", '''
        values = np.array([1, 2, 3, 4])
        view = values[1:3]
        view[0] = 99
        print(values)
        independent = values.copy()
        independent[0] = -1
        print("Selected:", values[values > 3])
        assert values[0] == 1
        assert np.shares_memory(values, view)
    ''', "Replace the slice with values[1:3].copy() and compare the mutation.")], [
    exercise("Normalize an array", "Implement minmax(values) returning float values scaled to [0, 1]. For a constant, nonempty one-dimensional numeric input return zeros of the same shape.", 'def minmax(values):\n    pass', 'np.testing.assert_allclose(minmax([10, 20, 30]), [0, 0.5, 1])\nnp.testing.assert_allclose(minmax([5, 5]), [0, 0])', 'def minmax(values):\n    array = np.asarray(values, dtype=float)\n    span = array.max() - array.min()\n    if span == 0:\n        return np.zeros_like(array)\n    return (array - array.min()) / span', "Handle a zero range before dividing."),
    exercise("Column totals", "Implement column_totals(matrix) returning the sum of each column of a two-dimensional numeric array.", 'def column_totals(matrix):\n    pass', 'np.testing.assert_array_equal(column_totals([[1, 2], [3, 4]]), [4, 6])\nnp.testing.assert_array_equal(column_totals([[5, 6, 7]]), [5, 6, 7])', 'def column_totals(matrix):\n    return np.asarray(matrix).sum(axis=0)', "Reduce axis=0.")],
    "Create a 7-day by 3-city temperature array. Find each city's average, each day's maximum, and a boolean mask of temperatures above 30. Explain the shape of every result. Optional: add missing values and compare mean with nanmean.",
    "Vectorization can still allocate large intermediate arrays. Integer arrays may overflow. NumPy float values have the same approximate-decimal concerns as Python floats.")

add("20_pandas_data_analysis", "pandas: clean, group, and join data", "Applied Python",
    ["Inspect a DataFrame and its dtypes", "Handle missing and invalid values explicitly", "Aggregate and validate joins"], [
    lesson("1. Load a small messy dataset", "A DataFrame is a labeled table; each column is a Series. Inspect shape, dtypes, and missing values before calculating. This fixture is embedded so the notebook runs without downloading data.", '''
        import pandas as pd
        from io import StringIO

        raw_csv = "date,category,amount\\n2025-01-01, Food ,120\\n2025-01-02,travel,80\\n2025-01-03,food,50\\n2025-01-04,books,\\n2025-01-05,travel,oops\\n"
        raw = pd.read_csv(StringIO(raw_csv))
        print(raw)
        print(raw.dtypes)
        print("Missing per column:\\n", raw.isna().sum())
    ''', "Add a malformed date to the fixture and inspect it before cleaning."),
    lesson("2. Clean with an explicit policy", "Normalize category text, parse dates, and coerce invalid amounts to missing. Here we quarantine rows with missing, invalid, or negative amounts, rather than silently turning them into zero. Choose a policy that matches the real meaning of your data.", '''
        cleaned = raw.copy()
        cleaned["category"] = cleaned["category"].str.strip().str.lower()
        cleaned["date"] = pd.to_datetime(cleaned["date"], errors="coerce")
        cleaned["amount"] = pd.to_numeric(cleaned["amount"], errors="coerce")
        valid = cleaned["date"].notna() & cleaned["category"].notna() & cleaned["category"].ne("") & cleaned["amount"].notna() & cleaned["amount"].ge(0)
        rejected = cleaned.loc[~valid].copy()
        accepted = cleaned.loc[valid].copy()
        print("Accepted:\\n", accepted)
        print("Rejected:\\n", rejected)
        assert len(accepted) == 3 and len(rejected) == 2
    ''', "Explain why filling a missing expense with zero might bias an analysis."),
    lesson("3. Aggregate and join", "groupby splits rows into groups and aggregates them. A merge joins tables by keys. validate='many_to_one' rejects duplicate keys on the budget side, preventing unexpected multiplication of expense rows.", '''
        totals = accepted.groupby("category", as_index=False)["amount"].sum()
        budgets = pd.DataFrame({"category": ["food", "travel"], "budget": [200, 100]})
        report = totals.merge(budgets, on="category", how="left", validate="many_to_one")
        report["remaining"] = report["budget"] - report["amount"]
        print(report)
        assert report.set_index("category").loc["food", "remaining"] == 30
    ''', "Add a duplicate food budget and observe the merge validation failure, then restore the data.")], [
    exercise("Top categories", "Implement category_totals(frame): return a Series summing amount by category, sorted by category name.", 'def category_totals(frame):\n    pass', 'sample = pd.DataFrame({"category": ["b", "a", "b"], "amount": [2, 3, 4]})\nassert category_totals(sample).to_dict() == {"a": 3, "b": 6}\nassert list(category_totals(sample).index) == ["a", "b"]', 'def category_totals(frame):\n    return frame.groupby("category")["amount"].sum().sort_index()', "Group by category, select amount, sum, then sort_index()."),
    exercise("Select expensive rows", "Return a copy containing rows with amount >= minimum, preserving row order and all columns.", 'def select_expensive(frame, minimum):\n    pass', 'sample = pd.DataFrame({"amount": [10, 50, 100], "label": ["a", "b", "c"]})\nselected = select_expensive(sample, 50)\nassert selected["label"].tolist() == ["b", "c"]\nselected.loc[1, "amount"] = 999\nassert sample.loc[1, "amount"] == 50', 'def select_expensive(frame, minimum):\n    return frame.loc[frame["amount"] >= minimum].copy()', "Use .loc[mask].copy().")],
    "Analyze a month of invented expenses. Produce a rejected-row table, category totals, and weekly totals. Check that category totals sum to the accepted grand total, and write three findings supported by values.",
    "Avoid chained assignment; use .loc for explicit updates. Missing is not the same as zero. Floating-point currency is used here for teaching; use integer minor units or a suitable decimal approach for exact accounting.")

add("21_matplotlib_visualization", "Visualize data and explain the result", "Applied Python",
    ["Choose a chart for a question", "Label axes and units", "Create and inspect a multi-panel figure"], [
    lesson("1. Compare categories", "Use a bar chart to compare categories. Name the measure and its units. A zero baseline makes bar lengths interpretable. The object-oriented matplotlib API keeps each axis explicit.", '''
        import matplotlib.pyplot as plt
        categories = ["Food", "Travel", "Books"]
        amounts = [170, 80, 120]
        fig, ax = plt.subplots(figsize=(7, 4), layout="constrained")
        bars = ax.bar(categories, amounts, color=["#2563eb", "#0891b2", "#7c3aed"])
        ax.bar_label(bars, padding=3)
        ax.set(title="Practice expenses by category", ylabel="Amount (currency units)")
        ax.set_ylim(0, 210)
        ax.spines[["top", "right"]].set_visible(False)
        plt.show()
    ''', "Change one value. Update the y limit if necessary so labels stay inside the figure."),
    lesson("2. Change over time and distributions", "A line chart shows ordered change; a histogram shows a distribution. These answer different questions. Histogram bins affect the appearance, and a small dataset does not justify strong general conclusions.", '''
        days = [1, 2, 3, 4, 5, 6, 7]
        minutes = [20, 35, 25, 45, 30, 60, 40]
        fig, axes = plt.subplots(1, 2, figsize=(10, 4), layout="constrained")
        axes[0].plot(days, minutes, marker="o", color="#2563eb")
        axes[0].set(title="Daily practice", xlabel="Day", ylabel="Minutes", ylim=(0, 70))
        axes[0].grid(alpha=0.2)
        axes[1].hist(minutes, bins=[0, 20, 40, 60, 80], edgecolor="white", color="#0891b2")
        axes[1].set(title="Practice duration distribution", xlabel="Minutes per day", ylabel="Number of days")
        plt.show()
    ''', "Compare different bin widths. Write one claim supported by the line chart."),
    lesson("3. Export a figure", "Save the figure object before closing it. Here a temporary PNG verifies the export without leaving generated files around. For your own report, choose a path under a practice_output folder and inspect the saved image.", '''
        from pathlib import Path
        from tempfile import TemporaryDirectory
        fig, ax = plt.subplots(figsize=(5, 3), layout="constrained")
        ax.scatter([1, 2, 3, 4], [2, 3, 5, 7], color="#7c3aed")
        ax.set(title="Illustrative relationship", xlabel="Practice sessions", ylabel="Tasks completed")
        with TemporaryDirectory() as folder:
            image_path = Path(folder) / "practice.png"
            fig.savefig(image_path, dpi=150)
            print("PNG export created:", image_path.stat().st_size > 0)
        plt.show()
        plt.close(fig)
    ''', "Explain why this invented scatter plot cannot establish that practice caused the outcome.")], [
    exercise("Cumulative values", "Implement cumulative(values) returning running totals for a line chart.", 'def cumulative(values):\n    pass', 'assert cumulative([2, 3, 5]) == [2, 5, 10]\nassert cumulative([]) == []', 'def cumulative(values):\n    result = []\n    total = 0\n    for value in values:\n        total += value\n        result.append(total)\n    return result', "Accumulate and append at each step."),
    exercise("A labeled chart function", "Implement make_bar_chart(labels, values) returning (fig, ax), with a bar for each value, title 'Expense comparison', and y-label 'Amount'. Do not call show() inside the function.", 'def make_bar_chart(labels, values):\n    pass', 'test_fig, test_ax = make_bar_chart(["A", "B"], [10, 20])\nassert test_ax.get_title() == "Expense comparison"\nassert test_ax.get_ylabel() == "Amount"\nassert [bar.get_height() for bar in test_ax.patches] == [10, 20]\nplt.close(test_fig)', 'def make_bar_chart(labels, values):\n    fig, ax = plt.subplots(figsize=(6, 4), layout="constrained")\n    ax.bar(labels, values)\n    ax.set(title="Expense comparison", ylabel="Amount")\n    return fig, ax', "Use plt.subplots(), ax.bar(), and ax.set().")],
    "Make a two-chart practice dashboard: daily minutes and cumulative minutes. Label units, use readable text, export a PNG, and write two observations plus one limitation. Inspect the image at its actual display size.",
    "A beautiful chart can still mislead. Avoid distorted bar baselines, missing units, and claims stronger than the data. Close figures when generating many plots in a loop.")

add("22_performance_and_software_design", "Expert practice: measurement, design, and observability", "Expert practice",
    ["Measure before optimizing", "Profile a repeatable workload", "Separate pure logic from I/O and inject dependencies"], [
    lesson("1. Compare equivalent work", "Timing depends on hardware, interpreter, input size, and background activity. Compare equal results and include relevant setup costs. timeit repeats work; do not turn a timing ratio into a universal rule.", '''
        import timeit
        numbers = list(range(5000))
        targets = list(range(4900, 5000))

        def list_lookups():
            return sum(target in numbers for target in targets)

        def set_lookups():
            indexed = set(numbers)  # Include construction in this comparison.
            return sum(target in indexed for target in targets)

        assert list_lookups() == set_lookups() == 100
        for function in [list_lookups, set_lookups]:
            seconds = min(timeit.repeat(function, number=3, repeat=3)) / 3
            print(function.__name__, f"{seconds:.6f} seconds per call (best sample)")
    ''', "Try one lookup instead of 100. Does building a set still help?"),
    lesson("2. Find where time goes", "A profiler attributes time to functions. Use a representative workload before choosing an optimization. cProfile adds overhead, so use it to locate work; use focused timing to compare a proposed change.", '''
        import cProfile
        import pstats
        import io

        def workload():
            return sum(sum(n * n for n in range(1000)) for _ in range(20))

        profiler = cProfile.Profile()
        profiler.runcall(workload)
        report = io.StringIO()
        pstats.Stats(profiler, stream=report).strip_dirs().sort_stats("cumulative").print_stats(5)
        print(report.getvalue())
    ''', "Replace the inner generator with another correct implementation. Check equality before timing."),
    lesson("3. Pure core, explicit boundaries", "Keep calculations separate from loading and saving. Passing a loader makes the workflow testable without a real filesystem or API. Log useful events without including sensitive records. Configure an isolated logger to avoid duplicate notebook handlers.", '''
        import logging
        import io

        def summarize(records):
            return {"count": len(records), "total": sum(record["amount"] for record in records)}

        def build_report(load_records, logger):
            records = load_records()
            logger.info("Loaded %d records", len(records))
            return summarize(records)

        log_output = io.StringIO()
        logger = logging.Logger("course_report", level=logging.INFO)
        handler = logging.StreamHandler(log_output)
        logger.addHandler(handler)
        try:
            report = build_report(lambda: [{"amount": 10}, {"amount": 20}], logger)
            print(report)
            print(log_output.getvalue().strip())
        finally:
            logger.removeHandler(handler)
            handler.close()
        assert report == {"count": 2, "total": 30}
    ''', "Use an empty loader and verify the summary. Decide which failures belong at the loading boundary.")], [
    exercise("Index once", "Implement index_by_id(records) returning a dict keyed by id. Raise ValueError for duplicate IDs instead of silently overwriting them. Each record has a hashable id.", 'def index_by_id(records):\n    pass', 'assert index_by_id([{"id": 1, "name": "A"}])[1]["name"] == "A"\nassert index_by_id([]) == {}\ntry:\n    index_by_id([{"id": 1}, {"id": 1}])\nexcept ValueError:\n    pass\nelse:\n    raise AssertionError("duplicate IDs must fail")', 'def index_by_id(records):\n    index = {}\n    for record in records:\n        key = record["id"]\n        if key in index:\n            raise ValueError(f"duplicate id: {key}")\n        index[key] = record\n    return index', "Check membership before inserting."),
    exercise("Inject a loader", "Implement total_from_loader(loader): call loader exactly once, then sum amount from its records. Return 0 for no records.", 'def total_from_loader(loader):\n    pass', 'calls = []\ndef fake_loader():\n    calls.append("called")\n    return [{"amount": 3}, {"amount": 4}]\nassert total_from_loader(fake_loader) == 7\nassert calls == ["called"]\nassert total_from_loader(lambda: []) == 0', 'def total_from_loader(loader):\n    records = loader()\n    return sum(record["amount"] for record in records)', "Keep the data source outside the calculation.")],
    "Refactor one earlier mini-project into validation, pure calculations, and I/O. Add behavior tests, a representative benchmark, and a short tradeoff note covering complexity, memory, readability, and failure handling.",
    "Expertise is not a list of syntax features. Practice making justified tradeoffs, testing failure paths, reading existing code, and revisiting decisions with evidence. These notebooks are a foundation for that ongoing work.")

add("23_capstone_expense_tracker", "Capstone: a validated expense pipeline", "Capstone",
    ["Validate and quarantine malformed records", "Persist exact amounts to SQLite", "Produce and test a report from reopened data"], [
    lesson("1. Define the domain and validate input", "Build a complete small pipeline: CSV → validated records → SQLite → category report → CSV export. Store amounts as integer minor units: 12.50 becomes 1250. Invalid records should have a clear reason and must not enter storage. The fixture includes two invalid rows.", '''
        from dataclasses import dataclass
        from datetime import date
        from decimal import Decimal, InvalidOperation
        import csv
        import io

        @dataclass(frozen=True)
        class Expense:
            day: date
            category: str
            amount_minor: int

        def parse_expense(row):
            try:
                day = date.fromisoformat(row["date"])
                category = row["category"].strip().lower()
                amount = Decimal(row["amount"])
            except (KeyError, TypeError, AttributeError, ValueError, InvalidOperation) as error:
                raise ValueError("missing or malformed field") from error
            if not category:
                raise ValueError("category must not be empty")
            if not amount.is_finite() or amount <= 0 or amount > Decimal("1000000000"):
                raise ValueError("amount must be finite, positive, and at most 1 billion")
            minor = amount * 100
            if minor != minor.to_integral_value():
                raise ValueError("amount must have at most two decimal places")
            return Expense(day, category, int(minor))

        def load_expenses(csv_text):
            accepted, rejected = [], []
            for row_number, row in enumerate(csv.DictReader(io.StringIO(csv_text)), start=2):
                try:
                    accepted.append(parse_expense(row))
                except ValueError as error:
                    rejected.append({"row": row_number, "reason": str(error)})
            return accepted, rejected

        csv_text = "date,category,amount\\n2025-01-02, Food ,120.50\\n2025-01-03,travel,80.00\\n2025-01-04,food,49.50\\n2025-02-01,books,200.00\\ninvalid,food,10\\n2025-01-06,food,-5\\n"
        expenses, rejected = load_expenses(csv_text)
        print("Accepted:", expenses)
        print("Rejected:", rejected)
        assert len(expenses) == 4 and len(rejected) == 2
    ''', "Add an amount of 1.005 and observe rejection. Why not silently round it?"),
    lesson("2. Persist and reopen", "Create a real temporary SQLite file, insert the validated rows in one transaction, close it, then reopen for the report. This demonstrates persistence across connections. Each run gets a new database, so rerunning does not duplicate the sample records.", '''
        import sqlite3
        from contextlib import closing
        from pathlib import Path
        from tempfile import TemporaryDirectory

        def save_expenses(connection, records):
            connection.execute("CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, day TEXT NOT NULL, category TEXT NOT NULL, amount_minor INTEGER NOT NULL CHECK(amount_minor > 0))")
            with connection:
                connection.executemany(
                    "INSERT INTO expenses(day, category, amount_minor) VALUES (?, ?, ?)",
                    [(record.day.isoformat(), record.category, record.amount_minor) for record in records],
                )

        def category_report(connection):
            return connection.execute("SELECT category, SUM(amount_minor) FROM expenses GROUP BY category ORDER BY category").fetchall()

        with TemporaryDirectory() as folder:
            database_path = Path(folder) / "expenses.sqlite"
            with closing(sqlite3.connect(database_path)) as connection:
                save_expenses(connection, expenses)
            with closing(sqlite3.connect(database_path)) as connection:
                report_rows = category_report(connection)
        print(report_rows)
        assert dict(report_rows) == {"books": 20000, "food": 17000, "travel": 8000}
    ''', "Add another valid expense to the CSV and verify the category report changes correctly."),
    lesson("3. Export and test failure paths", "Export formatted amounts with Decimal to preserve exact decimal values. Test malformed input as well as totals. This project is deliberately small: before turning it into a long-lived application, add duplicate-import handling, schema migration, and a clear currency policy.", '''
        def export_report(rows):
            output = io.StringIO(newline="")
            writer = csv.writer(output)
            writer.writerow(["category", "amount"])
            for category, minor in rows:
                writer.writerow([category, f"{Decimal(minor) / 100:.2f}"])
            return output.getvalue()

        exported = export_report(report_rows)
        print(exported)
        assert sum(record.amount_minor for record in expenses) == 45000
        assert list(csv.DictReader(io.StringIO(exported)))[0] == {"category": "books", "amount": "200.00"}
        for bad_amount in ["NaN", "Infinity", "0", "-1", "1.005", "oops"]:
            try:
                parse_expense({"date": "2025-01-01", "category": "food", "amount": bad_amount})
            except ValueError:
                pass
            else:
                raise AssertionError(f"should reject {bad_amount}")
        print("Capstone validation checks passed")
    ''', "Add missing-field, empty-category, and invalid-date cases to the checks.")], [
    exercise("Monthly totals", "Implement monthly_totals(records) returning a dictionary from YYYY-MM to total integer minor units. Accept Expense objects.", 'def monthly_totals(records):\n    pass', 'assert monthly_totals(expenses) == {"2025-01": 25000, "2025-02": 20000}\nassert monthly_totals([]) == {}', 'def monthly_totals(records):\n    totals = {}\n    for record in records:\n        month = record.day.strftime("%Y-%m")\n        totals[month] = totals.get(month, 0) + record.amount_minor\n    return totals', "Use the date's strftime('%Y-%m') as the grouping key."),
    exercise("Budget alerts", "Implement over_budget(totals, budgets). Return sorted categories where spending is strictly greater than the known budget. Ignore categories without a budget; equality is allowed.", 'def over_budget(totals, budgets):\n    pass', 'assert over_budget({"food": 17000, "books": 20000, "travel": 8000}, {"food": 15000, "books": 20000}) == ["food"]\nassert over_budget({}, {}) == []\nassert over_budget({"b": 2, "a": 3}, {"b": 1, "a": 1}) == ["a", "b"]', 'def over_budget(totals, budgets):\n    return sorted(category for category, amount in totals.items()\n                  if category in budgets and amount > budgets[category])', "Require both a known budget and amount > budget.")],
    "Finish your own version: add a monthly report, budget alerts, a chart, and a rejected-row CSV. Then move domain logic into .py modules and add a command-line interface. Acceptance criteria: 4 accepted and 2 rejected fixture rows; total 450.00; exact category totals; no invalid row stored; parameterized queries; tests pass after a fresh restart. Stretch: prevent duplicate imports using a documented record ID strategy, and explain your tradeoffs.",
    "The database constraint protects positive stored amounts, while the parser enforces the richer input contract. Calling save_expenses twice appends twice: a real import workflow needs an explicit duplicate policy. Completing the course starts your expert practice; build and review larger projects to deepen it.")


def cell(kind, source, tags=()):
    result = {"cell_type": kind, "metadata": {"tags": list(tags)} if tags else {},
              "source": clean(source).splitlines(keepends=True)}
    if kind == "code":
        result.update(execution_count=None, outputs=[])
    return result


def make_notebook(index, course, solution=False):
    slug = course["slug"]
    prefix = "Worked solutions — " if solution else ""
    prereq = "None; start here." if index == 0 else f"Concepts from notebooks 00–{index - 1:02d}. No variables or files from other notebooks are required."
    cells = [cell("markdown", f"# {prefix}{course['title']}\n\n"
                  f"**Stage:** {course['level']} · **Suggested time:** 45–90 minutes (capstone: several sessions)\n\n"
                  f"**Prerequisites:** {prereq}\n\n"
                  "## What you will learn\n\n" + "\n".join(f"- {goal}" for goal in course["goals"]))]
    if solution:
        cells.append(cell("markdown", "This notebook contains complete worked answers. Try the corresponding learning notebook first. These are possible solutions, not the only correct approaches. Run from the top so all examples and answer checks execute."))
    else:
        cells.append(cell("markdown", "## Your learning loop\n\n"
            "1. Read the explanation and predict the next output.\n"
            "2. Run the example with **Shift+Enter**.\n"
            "3. Follow **Try a change**; explain the result in your own words.\n"
            "4. Complete both exercises and enable their checks.\n"
            "5. Build the mini-project, then use **Restart Kernel and Run All**.\n\n"
            "Examples run as provided. Exercise starters are deliberately unfinished; their checks are disabled until you enable them. A successful Run All with checks disabled does **not** mean the exercises are complete.\n\n"
            "Save a copy before extensive experiments. Use one notebook at a time to avoid mixing kernel state."))
    for title, explanation, code, experiment in course["lessons"]:
        cells.extend([cell("markdown", f"## {title}\n\n{explanation}"),
                      cell("code", code, ("example",)),
                      cell("markdown", f"**Try a change:** {experiment}")])
    cells.append(cell("markdown", "## Practice: solve before looking at the answers\n\n"
        "Replace the starter code with your implementation. Run it, then change that exercise's `exercise_N_ready` flag to `True` and run its check cell. A failed assertion is feedback: compare the expected value with your result. Add at least one test of your own."))
    for number, (title, prompt, starter, checks, answer, hint) in enumerate(course["exercises"], 1):
        cells.append(cell("markdown", f"### Exercise {number}: {title}\n\n{prompt}\n\n<details>\n<summary>Show a hint</summary>\n\n{hint}\n\n</details>"))
        cells.append(cell("code", answer if solution else starter, ("solution" if solution else "exercise",)))
        enabled = "True" if solution else "False"
        code = f"exercise_{number}_ready = {enabled}  # Set True when your implementation is ready.\n"
        code += f"if exercise_{number}_ready:\n"
        code += textwrap.indent(clean(checks), "    ")
        code += f'    print("Exercise {number}: supplied checks passed. Add your own edge cases!")\n'
        code += f'else:\n    print("Exercise {number}: not checked yet. Complete the code, then set exercise_{number}_ready = True.")\n'
        cells.append(cell("code", code, ("exercise-check",)))
    cells.extend([
        cell("markdown", f"## Build it yourself\n\n{course['project']}\n\nThis open-ended extension has no single supplied solution. Record your design choices and test your result."),
        cell("code", "# Your mini-project workspace. Add more cells as needed.\n", ("project",)),
        cell("markdown", f"## Common mistakes and limits\n\n{course['pitfalls']}"),
        cell("markdown", "## Before you move on\n\n"
            "- [ ] I can explain the examples without reading the code.\n"
            "- [ ] I changed at least two inputs and predicted the results.\n"
            "- [ ] I completed both exercises and enabled their checks.\n"
            "- [ ] I added a boundary or failure case of my own.\n"
            "- [ ] I attempted the mini-project and recorded one lesson learned.\n\n"
            "**Reflection:** What surprised you? What would you try next? Edit this Markdown cell with your notes."),
    ])
    nav = ["[Course guide](../README.md)"]
    if not solution:
        nav.append(f"[Worked solutions](../solutions/{slug}_solutions.ipynb)")
        if index > 0:
            nav.append(f"[Previous notebook]({COURSE[index - 1]['slug']}.ipynb)")
        if index + 1 < len(COURSE):
            nav.append(f"[Next notebook]({COURSE[index + 1]['slug']}.ipynb)")
    else:
        nav.append(f"[Back to learning notebook](../notebooks/{slug}.ipynb)")
    cells.append(cell("markdown", " · ".join(nav)))
    for i, item in enumerate(cells):
        item["id"] = uuid.uuid5(uuid.NAMESPACE_URL, f"python-practical/{slug}/{solution}/{i}").hex[:12]
    return {"cells": cells, "metadata": {
        "kernelspec": {"display_name": "Python 3 (ipykernel)", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.13", "file_extension": ".py", "mimetype": "text/x-python", "pygments_lexer": "ipython3"},
        "course": {"level": course["level"], "solution": solution, "sequence": index},
    }, "nbformat": 4, "nbformat_minor": 5}


def build():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing notebooks, including learner edits.")
    args = parser.parse_args()
    existing = list((ROOT / "notebooks").glob("*.ipynb")) + list((ROOT / "solutions").glob("*.ipynb"))
    if existing and not args.overwrite:
        parser.error("Notebooks already exist. Back up your work, then use --overwrite only if you intend to replace them.")
    for directory in ["notebooks", "solutions"]:
        (ROOT / directory).mkdir(exist_ok=True)
    for index, course in enumerate(COURSE):
        for solution in [False, True]:
            directory = "solutions" if solution else "notebooks"
            suffix = "_solutions" if solution else ""
            destination = ROOT / directory / f"{course['slug']}{suffix}.ipynb"
            destination.write_text(json.dumps(make_notebook(index, course, solution), indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    rows = []
    for index, course in enumerate(COURSE):
        rows.append(f"| {index:02d} | [{course['title']}](notebooks/{course['slug']}.ipynb) | {course['level']} | [Answers](solutions/{course['slug']}_solutions.ipynb) |")
    readme = (ROOT / "tools" / "guide_template.md").read_text(encoding="utf-8")
    (ROOT / "README.md").write_text(readme.replace("<!-- COURSE_TABLE -->", "\n".join(rows)), encoding="utf-8")
    progress = ["# My Python practice tracker", "", "Mark a notebook complete after doing its exercises with checks enabled. Revisit difficult topics.", "", "| Notebook | Examples changed | Exercises passed | Project attempted | Notes / date |", "|---|---|---|---|---|"]
    progress += [f"| {item['slug']} | [ ] | [ ] | [ ] | |" for item in COURSE]
    (ROOT / "PROGRESS.md").write_text("\n".join(progress) + "\n", encoding="utf-8")
    print(f"Created {len(COURSE)} learning notebooks and {len(COURSE)} solution notebooks.")


if __name__ == "__main__":
    build()
