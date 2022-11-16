# Select which item
from typing import List, Tuple
from copy import copy
import random


def selector(member_list: List[str]) -> List[Tuple[str, str]]:
    max_counter = 100
    ok_flag = False
    while not ok_flag:
        max_counter -= 1
        if max_counter < 0:
            raise OverflowError
        target_list = copy(member_list)
        result = []
        for member in member_list:
            target = random.choice(target_list)
            if target == member:
                break
            result.append((member, target))
            target_list.remove(target)
        else:
            ok_flag = True
    return result
