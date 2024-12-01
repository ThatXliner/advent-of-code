import sys
from dataclasses import dataclass
from collections import Counter
from functools import cache

card_strength = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def _get_type(t: str) -> int:
    co = Counter(t)
    c = co.most_common(1)[0][1]
    # 5 of a kind
    if c == 5:
        return 7
    # 4 of a kind
    if c == 4:
        return 6
    if c == 3:
        # full house
        if (x := t.replace(co.most_common(1)[0][0], ""))[0] == x[1]:
            return 5
        # 3 of a kind
        return 4
    # 2 pair
    e = co.most_common(2)
    if e[0][1] == e[1][1] == 2:
        return 3
    # 1 pair
    if c == 2:
        return 2
    return 1


@dataclass(order=False, frozen=True)
class Hand:
    # 5 cards
    raw: str

    @cache
    def get_type(self) -> int:
        print("Type of ", self.raw, end=" ")
        if "J" in self.raw:
            e = 0
            for x in card_strength[:-1]:
                e = max(e, _get_type(self.raw.replace("J", x)))
            print(e - 1)
            return e - 1
        print(_get_type(self.raw) - 1)
        return _get_type(self.raw) - 1

    def __lt__(self, other):
        if self.get_type() == other.get_type():
            for x in range(5):
                first_a = card_strength.index(self.raw[x])
                first_b = card_strength.index(other.raw[x])
                if first_a == first_b:
                    continue
                return first_a > first_b
            assert False
        return self.get_type() < other.get_type()


o = list(
    map(
        lambda x: x[0] * x[1][1],
        enumerate(
            sorted(
                list(
                    map(
                        lambda x: (Hand((_ := x.split())[0]), int(_[1])),
                        sys.stdin.read().splitlines(),
                    )
                ),
                key=lambda x: x[0],
            ),
            start=1,
        ),
    )
)
print(sum(o))
