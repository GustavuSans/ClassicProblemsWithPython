from typing import TypeVar, Generic, List

T = TypeVar('T')
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    def push(self, item: T) -> None:
        self._container.append(item)
    def pop(self) -> T:
        return self._container.pop()
    def __repr__(self) -> str:
        return repr(self._container)
nDisc : int = 3
towerA : Stack[int] = Stack()
towerB : Stack[int] = Stack()
towerC : Stack[int] = Stack()
for _ in range(1, nDisc + 1):
    towerA.push(_)

def tower(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        tower(begin, temp, end, n - 1)
        tower(begin, end, temp, 1)
        tower(temp, end, begin, n - 1)
if __name__ == "__main__":
    tower(towerA, towerB, towerC, nDisc)
    print(towerA, '\n', towerB, '\n', towerC)