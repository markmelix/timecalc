#!/usr/bin/env python3

import sys
import pyparsing as pp
from typing import List
from datetime import timedelta
from pytimeparse.timeparse import timeparse


def parse_problem(string: str) -> pp.ParseResults:
    integer = pp.Word(pp.nums)
    timeobj = pp.Combine(integer + pp.Char(":") + integer)
    problem = pp.infixNotation(
        timeobj,
        [
            # leading sign
            (
                pp.oneOf("+ -"),
                1,
                pp.opAssoc.RIGHT,
            ),
            # multiplication and division
            (
                pp.oneOf("* /"),
                2,
                pp.opAssoc.LEFT,
            ),
            # addition and subtraction
            (
                pp.oneOf("+ -"),
                2,
                pp.opAssoc.LEFT,
            ),
        ],
    )
    return problem.parse_string(string)


def solve_problem(parts: List[str]) -> str:
    length = len(parts)

    match length:
        case 0:
            return ""
        case 1:
            return parts[0]
        case 2:
            return f"{parts[0]}{parts[1]}"
        case 3:
            op = parts[1]
            t1 = parts[0] if isinstance(parts[0], str) else solve_problem(parts[0])
            t2 = parts[2] if isinstance(parts[2], str) else solve_problem(parts[2])

            secs = eval(f"{timeparse(t1)}{op}{timeparse(t2)}")

            if secs != 0 and secs < 60:
                return f"{secs}s"

            mins = secs % 60
            hours = (secs - mins) // 60

            return f"{hours:02}:{mins:02}"

    if length % 2 != 0:
        return solve_problem(
            [
                solve_problem(parts[:-2]),
            ]
            + parts[-2:]
        )

    return ""


if __name__ == "__main__":
    a = " ".join(sys.argv[1:]).replace("_", ":")
    b = parse_problem(a).asList()[0]
    c = solve_problem(b)
    print(c)
