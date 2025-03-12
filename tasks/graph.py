from typing import TypeVar, Generic
from collections import deque

__all__ = ("Node", "Graph")


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

        self.outbound: list[Node] = []
        self.inbound: list[Node] = []

    @property
    def value(self) -> T:
        return self._value

    def point_to(self, other: "Node") -> None:
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        return f"Node({repr(self._value)})"

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node) -> None:
        self._root = root

    def dfs(self) -> list[Node]:
        visited = set()
        stack = [self._root]
        result = []

        while stack:
            current_node = stack.pop()
            if current_node not in visited:
                visited.add(current_node)
                result.append(current_node)
                stack.extend(reversed([
                    neighbor
                    for neighbor in current_node.outbound
                    if neighbor not in visited
                ]))
        return result

    def bfs(self) -> list[Node]:
        visited = set()
        queue = deque([self._root])
        result = []

        while queue:
            current_node = queue.popleft()
            if current_node not in visited:
                visited.add(current_node)
                result.append(current_node)
                queue.extend([
                    neighbor
                    for neighbor in current_node.outbound
                    if neighbor not in visited
                ])
        return result
