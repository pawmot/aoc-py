import os
from dataclasses import dataclass
from enum import StrEnum
from typing import Self

from parsy import regex, seq, string


def solve_a(data):
    instructions = parse_instructions(data)
    rects = [(Rect(Point(0, 0), Point(999, 999)), False)]
    for i in instructions:
        new_rects = []
        for r in rects:
            if not i.rect.overlaps(r[0]) or i.type == InstructionType.TurnOn and r[1] or i.type == InstructionType.TurnOff and not r[1]:
                new_rects.append(r)
            else:
                x_ranges = []
                y_ranges = []
                overlap = r[0].overlap(i.rect)
                if overlap == None:
                    return None
                # below False means follow old rule, True means follow new rule
                if r[0].a.x < i.rect.a.x:
                    x_ranges.append(((r[0].a.x, overlap.a.x - 1), False))
                x_ranges.append(((overlap.a.x, overlap.b.x), True))
                if r[0].b.x > overlap.b.x:
                    x_ranges.append(((overlap.b.x+1, r[0].b.x), False))
                if r[0].a.y < overlap.a.y:
                    y_ranges.append(((r[0].a.y, overlap.a.y - 1), False))
                y_ranges.append(((overlap.a.y, overlap.b.y), True))
                if r[0].b.y > overlap.b.y:
                    y_ranges.append(((overlap.b.y+1, r[0].b.y), False))

                for xr in x_ranges:
                    if not xr[1]:
                        min_y = y_ranges[0][0][0]
                        max_y = y_ranges[-1][0][1]
                        new_rect = Rect(Point(xr[0][0], min_y), Point(xr[0][1], max_y))
                        new_rects.append((new_rect, r[1]))
                    else:
                        for yr in y_ranges:
                            new_rect = Rect(Point(xr[0][0], yr[0][0]), Point(xr[0][1], yr[0][1]))
                            rule = r[1]
                            # only if both ranges follow new rule the rect follows new rule
                            if yr[1]:
                                if i.type == InstructionType.TurnOn:
                                    rule = True
                                elif i.type == InstructionType.TurnOff:
                                    rule = False
                                elif i.type == InstructionType.Toggle:
                                    rule = not rule
                                new_rects.append((new_rect, rule))
                            else:
                                new_rects.append((new_rect, r[1]))
        rects = new_rects

    res = 0
    for r in rects:
        if r[1]:
            res += r[0].area()
    return res


def solve_b(data):
    instructions = parse_instructions(data)
    rects = [(Rect(Point(0, 0), Point(999, 999)), 0)]
    for i in instructions:
        new_rects = []
        for r in rects:
            if not i.rect.overlaps(r[0]) or i.type == InstructionType.TurnOff and r[1] == 0:
                new_rects.append(r)
            else:
                x_ranges = []
                y_ranges = []
                overlap = r[0].overlap(i.rect)
                if overlap == None:
                    return None
                # below False means follow old rule, True means follow new rule
                if r[0].a.x < i.rect.a.x:
                    x_ranges.append(((r[0].a.x, overlap.a.x - 1), False))
                x_ranges.append(((overlap.a.x, overlap.b.x), True))
                if r[0].b.x > overlap.b.x:
                    x_ranges.append(((overlap.b.x+1, r[0].b.x), False))
                if r[0].a.y < overlap.a.y:
                    y_ranges.append(((r[0].a.y, overlap.a.y - 1), False))
                y_ranges.append(((overlap.a.y, overlap.b.y), True))
                if r[0].b.y > overlap.b.y:
                    y_ranges.append(((overlap.b.y+1, r[0].b.y), False))

                for xr in x_ranges:
                    if not xr[1]:
                        min_y = y_ranges[0][0][0]
                        max_y = y_ranges[-1][0][1]
                        new_rect = Rect(Point(xr[0][0], min_y), Point(xr[0][1], max_y))
                        new_rects.append((new_rect, r[1]))
                    else:
                        for yr in y_ranges:
                            new_rect = Rect(Point(xr[0][0], yr[0][0]), Point(xr[0][1], yr[0][1]))
                            rule = r[1]
                            # only if both ranges follow new rule the rect follows new rule
                            if yr[1]:
                                if i.type == InstructionType.TurnOn:
                                    value = r[1] + 1
                                elif i.type == InstructionType.TurnOff:
                                    value = max(r[1] - 1, 0)
                                else: # i.type == InstructionType.Toggle
                                    value = r[1] + 2
                                new_rects.append((new_rect, value))
                            else:
                                new_rects.append((new_rect, r[1]))
        rects = new_rects

    return sum([r[0].area() * r[1] for r in rects])


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

    def __repr__(self):
        return f'({self.x},{self.y})'

class Rect:
    def __init__(self, a: Point, b: Point):
        min_x = min(a.x, b.x)
        min_y = min(a.y, b.y)
        max_x = max(a.x, b.x)
        max_y = max(a.y, b.y)

        self.a = Point(min_x, min_y)
        self.b = Point(max_x, max_y)

    def overlaps(self, rect: Self) -> bool:
        return self.a.x <= rect.b.x and rect.a.x <= self.b.x and self.a.y <= rect.b.y and rect.a.y <= self.b.y

    def overlap(self, rect: Self) -> "Rect | None":
        if not self.overlaps(rect):
            return None
        x_bl = max(self.a.x, rect.a.x)
        y_bl = max(self.a.y, rect.a.y)
        x_ur = min(self.b.x, rect.b.x)
        y_ur = min(self.b.y, rect.b.y)
        return Rect(Point(x_bl, y_bl), Point(x_ur, y_ur))

    def area(self) -> int:
        return (self.b.x - self.a.x + 1) * (self.b.y - self.a.y + 1)

    def __repr__(self) -> str:
        return f'Rect[{self.a},{self.b}]'


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
