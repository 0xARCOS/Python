from abc import ABC, abstractmethod
from typing import Any, List, Union, Dict


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: List[str] = []
        self._count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Determina si los datos son compatibles."""
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Procesa y guarda los datos."""
        pass

    def output(self) -> tuple[int, str]:
        """
        Extrae el dato más antiguo (FIFO) y lo devuelve.
        """
        if not self._storage:
            raise IndexError("No data available")

        rank = self._count
        self._count += 1
        return (rank, self._storage.pop(0))


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._storage.append(str(item))
        else:
            self._storage.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: Union[str, List[str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")

        if isinstance(data, list):
            self._storage.extend(data)
        else:
            self._storage.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_log(d: Any) -> bool:
            if not isinstance(d, dict):
                return False
            has_keys = "log_level" in d and "log_message" in d
            if not has_keys:
                return False
            return all(isinstance(k, str) and isinstance(v, str)
                       for k, v in d.items())

        if is_log(data):
            return True
        if isinstance(data, list) and data:
            return all(is_log(x) for x in data)
        return False

    def ingest(self,
               data: Union[Dict[str, str], List[Dict[str, str]]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")

        def format_log(d: Dict[str, str]) -> str:
            return f"{d['log_level']}: {d['log_message']}"

        if isinstance(data, list):
            for item in data:
                self._storage.append(format_log(item))
        else:
            self._storage.append(format_log(data))


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    # --- Testing Numeric Processor ---
    print("Testing Numeric Processor...")
    num = NumericProcessor()
    print(f"Trying to validate input '42': {num.validate(42)}")
    print(f"Trying to validate input 'Hello': {num.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num.ingest("foo")  # type: ignore
    except TypeError as e:
        print(f"Got exception: {e}")
    data: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    num.ingest(data)
    print("Extracting 3 values...")
    for _ in range(3):
        r, v = num.output()
        print(f"Numeric value {r}: {v}")

    # --- Testing Text Processor ---
    print("\nTesting Text Processor...")
    txt = TextProcessor()
    print(f"Trying to validate input '42': {txt.validate(42)}")
    words = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {words}")
    txt.ingest(words)
    print("Extracting 1 value...")
    r, v = txt.output()
    print(f"Text value {r}: {v}")

    # --- Testing Log Processor ---
    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    logs = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {logs}")
    log.ingest(logs)
    print("Extracting 2 values...")
    for _ in range(2):
        r, v = log.output()
        print(f"Log entry {r}: {v}")
