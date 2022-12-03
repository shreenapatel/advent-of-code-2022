from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape

day = datetime.today().day
day_str = str(day).zfill(2)

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())

template_solutions = env.get_template("aoc/templates/solutions.py")
template_tests = env.get_template("aoc/templates/tests.py")

render_solutions = template_solutions.render()
render_tests = template_tests.render(day=day, day_str=day_str)

with open(f"aoc/solutions/day{day_str}.py", "w") as f:
    f.write(render_solutions)

with open(f"tests/test_day{day_str}.py", "w") as f:
    f.write(render_tests)
