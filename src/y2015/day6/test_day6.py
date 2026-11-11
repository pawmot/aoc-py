import os
from dataclasses import dataclass
from enum import StrEnum

from parsy import regex, seq, string


def solve_a(data):
    instructions = parse_instructions(data)
    res = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            point = Point(x, y)
            on = False
            for i in instructions:
                if i.rect.contains(point):
                    if i.type == InstructionType.TurnOn:
                        on = True
                    elif i.type == InstructionType.TurnOff:
                        on = False
                    elif i.type == InstructionType.Toggle:
                        on = not on
            if on:
                res += 1
    return res


def solve_b(data):
    instructions = parse_instructions(data)
    res = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            point = Point(x, y)
            brightness = 0
            for i in instructions:
                if i.rect.contains(point):
                    if i.type == InstructionType.TurnOn:
                        brightness += 1
                    elif i.type == InstructionType.TurnOff:
                        brightness = max(brightness - 1, 0)
                    elif i.type == InstructionType.Toggle:
                        brightness += 2
            res += brightness
    return res


def test_a_sample():
    data = load_data('sample')
    assert solve_a(data) == 998996


def test_a_full():
    data = load_data('full')
    assert solve_a(data) == 543903


def test_b_sample():
    data = load_data('sample')
    assert solve_b(data) == 1001996


def test_b_full():
    data = load_data('full')
    assert solve_b(data) == 14687245


def load_data(set: str):
    with open(os.path.dirname(__file__) + f'/{set}.txt') as f:
        lines = f.read().splitlines()
    return lines

# turn on 0,0 through 999,999
# toggle 0,0 through 999,0
# turn off 499,499 through 500,500

@dataclass
class Point:
    x: int
    y: int

class Rect:
    def __init__(self, a: Point, b: Point):
        min_x = min(a.x, b.x)
        min_y = min(a.y, b.y)
        max_x = max(a.x, b.x)
        max_y = max(a.y, b.y)

        self.a = Point(min_x, min_y)
        self.b = Point(max_x, max_y)

    def contains(self, point: Point) -> bool:
        return point.x >= self.a.x and point.x <= self.b.x and point.y >= self.a.y and point.y <= self.b.y


class InstructionType(StrEnum):
    TurnOn = 'turn on'
    TurnOff = 'turn off'
    Toggle = 'toggle'

@dataclass
class Instruction:
    type: InstructionType
    rect: Rect

    def __str__(self):
        return f'{self.type.__str__()} - ({self.rect.a}, {self.rect.b})'

def parse_instructions(lines: list[str]) -> list[Instruction]:
    number = regex(r'[0-9]+').map(int)
    comma = string(',')
    point = seq(x=number, _=comma, y=number).combine_dict(Point)
    rect = seq(a=point, _=string(' through '), b = point).combine_dict(Rect)
    turn_on = string('turn on').map(InstructionType)
    turn_off = string('turn off').map(InstructionType)
    toggle = string('toggle').map(InstructionType)
    instruction_type = turn_on | turn_off | toggle
    instruction = seq(type=instruction_type, _=string(' '), rect = rect).combine_dict(Instruction)
    return [instruction.parse(l) for l in lines]
