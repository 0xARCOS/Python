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


class DataStream:
    def __init__(self) -> None:
        self._processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """
        Añade un procesador a la lista de handlers.
        """
        self._processors.append(proc)

    def process_stream(self, stream: List[Any]) -> None:
        """
        Analiza cada elemento y lo envía al procesador adecuado.
        Usa polimorfismo: llama a validate() sin saber el tipo de proc.
        """
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
        """
        Imprime cuántos items lleva cada procesador.
        """
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


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("Registering Numeric Processor\n")
    num_proc = NumericProcessor()
    ds.register_processor(num_proc)

    batch = [
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

    print("Send first batch of data on stream: " + str(batch))
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("\nRegistering other data processors")
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    print("Send the same batch again")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        ds._processors[0].output()
    for _ in range(2):
        ds._processors[1].output()
    for _ in range(1):
        ds._processors[2].output()

    ds.print_processors_stats()
