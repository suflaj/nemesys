from typing import Any, Iterable, Optional

from nemesys.modelling.blocks.block import Block

class Store:
    @property
    def blocks(self) -> Iterable[Block]: ...
    @staticmethod
    def init_from(content: Any, method: Optional[str]) -> "Store": ...
    def append(self, content: Block): ...
    def get_all(self) -> Iterable[Block]: ...
    def get_one(self, key: Any) -> Block: ...
    def get_some(self, keys: Iterable[Any]) -> Iterable[Block]: ...
    def remove_all(self): ...
    def remove_one(self, key: Any): ...
    def remove_some(self, keys: Iterable[Any]): ...
    def set_all(self, content: Iterable[Block]): ...
    def set_one(self, key: Any, content: Block): ...
    def set_some(self, keys: Iterable[Any], contents: Iterable[Block]): ...
