
download-data:
	aocd > "aoc/inputs/day$(shell date +"%d").txt"

create-scripts:
	python aoc/generate_scripts.py

run:
	python aoc/runner.py

lint:
	black aoc tests --exclude=aoc/templates
	flake8 aoc tests

test:
	pytest .
