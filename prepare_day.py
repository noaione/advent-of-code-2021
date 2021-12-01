import configparser
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

current = Path(__file__).parent.absolute()

config = configparser.ConfigParser()
config.read("aoc.ini")

secret_cookies = config["AoC"]["SESSION_COOKIES"]

session = requests.Session()
session.headers.update({
    "Cookie": f"session={secret_cookies}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",  # noqa: E501
})

wib_tz = timezone(timedelta(hours=7))
current_time = datetime.now(tz=wib_tz)
print(f"[*] Current Time: {current_time.strftime('%d %b %Y %H:%M:%S')}")

# AOC New Day started at 12:00PM my time
if current_time.hour >= 12:
    current_day = current_time.day
else:
    current_day = current_time.day - 1

dayf = str(current_day).zfill(2)

day_folder = current / "src" / f"day{dayf}"

if day_folder.exists():
    print(f"[!] Day {dayf} already initialized.")
    exit(1)

wait_for = input(f"[*] This will prepare day {dayf}, type `c` to cancel")
if wait_for.lower().strip() == "c":
    exit(0)

day_folder.mkdir(parents=True, exist_ok=True)

PYTHON_INIT = """import typing as t

in_data = [num.rstrip() for num in open("input", "r).readlines() if num]

# Part A
print(f"Part A: ")

# Part B
print(f"Part B: ")

# if __name__ == "__main__":
#     pass
#     in_data = [num.rstrip() for num in open("input", "r").readlines() if num]
#     print(f"Part A: {solve(in_data, 2)}")
#     print(f"Part B: {solve(in_data, 3)}")
"""

print(f"[*] Downloading input day {dayf}")
req_input = session.get(f"https://adventofcode.com/2021/day/{current_day}/input")
with open(day_folder / "input", "w") as fp:
    fp.write(req_input.text)

print("[*] Generating solution template...")
with open(day_folder / "solution.py", "w") as fp:
    fp.write(PYTHON_INIT)

print("[*] Done!")
