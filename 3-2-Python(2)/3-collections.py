from typing import (
    Dict, List,
    Callable,
    Generic,
    TypeVar,
    Hashable
)


K = TypeVar("K", bound=Hashable)
V = TypeVar("V")

class defaultdict(Dict[K, V], Generic[K, V]):
    def __init__(self, default_factory: Callable[[], V]):
        super().__init__()
        self.default_factory = default_factory

    def __missing__(self, key: K) -> V:
        if self.default_factory is None:
            raise KeyError(key)
        self[key] = value = self.default_factory()
        return value

    def __getitem__(self, key: K) -> V:
        try:
            return super().__getitem__(key)
        except KeyError:
            return self.__missing__(key)

    def __repr__(self) -> str:
        return f"defaultdict({self.default_factory.__name__}, {super().__repr__()})"


if __name__ == "__main__":
    test_keys = ["asdf", 892340, 3+4j, -2345, (4, 2, "a")]

    try:
        test_dict_1: defaultdict[Hashable, int] = defaultdict(int)
        for key in test_keys:
            assert test_dict_1[key] == 0
            test_dict_1[key] += 5
            assert test_dict_1[key] == 5

        test_dict_2: defaultdict[Hashable, Dict[str, int]] = defaultdict(dict)
        for key in test_keys:
            assert len(test_dict_2[key]) == 0
            test_dict_2[key]["a"] = 1
            test_dict_2[key]["b"] = 2
            assert str(test_dict_2[key]) == "{'a': 1, 'b': 2}"

        test_dict_3: defaultdict[Hashable, List[int]] = defaultdict(lambda: [0, 1])
        for key in test_keys:
            assert len(test_dict_3[key]) == 2
            test_dict_3[key].append(2)
            assert str(test_dict_3[key] + [3, 4]) == '[0, 1, 2, 3, 4]'

    except Exception as e:
        print("something's wrong...", e.__class__.__name__)
    else:
        print("well done!")
    finally:
        print("goodbye!")