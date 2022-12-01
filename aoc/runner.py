"""Advent of code puzzle runner"""

import time
import importlib
import math
from typing import Any


def format_filename(day: int):
    return str(day).zfill(2)


def format_runtime(ms):

    # Microseconds
    if ms <= 1:
        return f"{round(ms * 1000)}µs"
    # Milliseconds
    if ms < 1000:
        whole_ms = math.floor(ms)
        rem_ms = ms - whole_ms
        return f"{whole_ms}ms " + format_runtime(rem_ms)
    sec = ms / 1000
    # Seconds
    if sec < 60:
        whole_sec = math.floor(sec)
        rem_ms = ms - whole_sec * 1000
        return f"{whole_sec}s " + format_runtime(rem_ms)
    # Minutes
    return f"{math.floor(sec / 60)}m " + format_runtime((sec % 60) * 1000)


def run_part(part: str, mod: Any, data: str):
    funcname = f"part{part}"

    f = getattr(mod, funcname, None)
    if callable(f):
        print(f"Running Part {part}")

        time_start = time.perf_counter()
        val = f(data)
        time_end = time.perf_counter()

        print(f"Output: {val}")
        run_time = (time_end - time_start) * 1000  # sec -> ms
        print(f"Took {format_runtime(run_time)}\n")
        return run_time
    else:
        print(f"No {funcname} function")
        return 0

    return run_time


def load_data(day: int):

    filename = "day" + format_filename(day) + ".txt"
    try:
        with open(f"aoc/inputs/{filename}", "r") as f:
            data = f.read()
    except Exception as e:
        raise ValueError(f"Unable to read file {filename}") from e

    print(f"Loaded puzzle input from {filename}\n")
    return data


def run(day, year=2022):
    print(f"Advent of Code {year} Day {day}")

    mod = importlib.import_module(f"solutions.day{format_filename(day)}")
    data = load_data(day)

    part1Time = run_part(1, mod, data)
    part2Time = run_part(2, mod, data)
    if part1Time != 0 and part2Time != 0:
        print(f"Total runtime: {format_runtime(part1Time + part2Time)}")


def get_day(max_day=None):
    while True:
        prompt = "Enter day" + (f" (max {max_day})" if max_day else "")
        inp = input(prompt + ": ")
        try:
            day = int(inp)
        except ValueError:
            print("Invalid day")
            continue

        if max_day is not None and day <= max_day:
            return day
        else:
            print(f"Must be at most {max_day}")


if __name__ == "__main__":

    day = get_day(25)
    run(day)
