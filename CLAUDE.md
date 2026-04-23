# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

Personal LeetCode solutions repository. All solutions are written in Python using the `class Solution` pattern that LeetCode expects.

## Running Solutions

Run any solution directly with Python:
```
python "1. Two sum.py"
```

Solutions don't include test harnesses by default — add a `if __name__ == "__main__":` block with test cases when debugging.

## File Naming Convention

Files are named `<problem_number>. <problem_title>.py` (e.g., `1. Two sum.py`, `347. Top K Frequent Elements.py`).

## Code Style

- Each file contains a single `class Solution` with the method signature matching LeetCode's interface
- Solutions import only what's needed (`from typing import List` is implicit on LeetCode but must be added locally to run)
- Prefer hash maps and two-pointer techniques for array/string problems
- Use `heapq` for heap-based solutions
