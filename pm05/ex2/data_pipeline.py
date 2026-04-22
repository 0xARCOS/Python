from abc import ABC, abstractmethod
from typing import Any, List, Union, Dict, Protocol


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class DataStream:
    def __init__(self) -> None:
        self._processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: List[Any]) -> None:
        for element in stream:
            found = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    found = True
                    break
            if not found:
                print(
                    f"DataStream error - Can't process element in stream: "
                    f"{element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data\n")
            return

        for proc in self._processors:
            name = proc.__class__.__name__
            processed = proc._count + len(proc._storage)
            remaining = len(proc._storage)
            print(
                f"{name}: total {processed} items processed, "
                f"remaining {remaining} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            collected: list[tuple[int, str]] = []
            for _ in range(nb):
                if proc._storage:
                    collected.append(proc.output())
            if collected:
                plugin.process_output(collected)


class CSVExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [item[1] for item in data]
        print("CSV Output:")
        print(",".join(values))


class JSONExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pairs = ", ".join(
            f'"item_{item[0]}": "{item[1]}"' for item in data
        )
        print("JSON Output:")
        print("{" + pairs + "}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")

    stream = DataStream()
    print("Initialize Data Stream...")
    stream.print_processors_stats()

    print("Registering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch1 = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
             'log_message': 'User wil is connected'}
        ],
        42,
        ['Hi', 'five']
    ]
    print(f"Send first batch of data on stream: {batch1}")
    stream.process_stream(batch1)
    stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExport())
    stream.print_processors_stats()

    batch2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR',
             'log_message': '500 server crash'},
            {'log_level': 'NOTICE',
             'log_message': 'Certificate expires in 10 days'}
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print(f"Send another batch of data: {batch2}")
    stream.process_stream(batch2)
    stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExport())
    stream.print_processors_stats()
