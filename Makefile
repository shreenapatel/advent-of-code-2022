
download-data:
	aocd > "aoc/inputs/day$(shell date +"%d").txt"

run:
	python aoc/runner.py

lint:
	black aoc
	flake8 aoc

test:
	pytest .
