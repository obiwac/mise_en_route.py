import pylint.lint as linter

print("Starting linter ...")

results = linter.Run(["./src"], do_exit = False)
score = results.linter.stats["global_note"]

if score < 10:
	raise Exception(f"Linter failed, score is {score}")

else:
	exit(0)