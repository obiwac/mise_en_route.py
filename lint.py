import pylint.lint as linter

print("Starting linter ...")

LINTER_OPTIONS = [
	"--disable", "C0114", # disable 'missing-module-docstring'
	"--disable", "C0103", # disable 'invalid-name' (pylint thinks 'sum_of_squares' is a constant when, in reality, it isn't)
	"--disable", "W0311", # TIL some dumbasses unironically prefer spaces to tabs 🤮
]

results = linter.Run(["./src"] + LINTER_OPTIONS, do_exit = False)
score = results.linter.stats["global_note"]

if score < 10:
	raise Exception(f"Linter failed, score is {score}")

else:
	exit(0)