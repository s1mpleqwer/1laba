from abc import ABC, abstractmethod


class Table(ABC):
    """
    Абстрактный класс, описывающий стол.
    """

    def __init__(self, material: str, legs_count: int):
        if legs_count <= 0:
            raise ValueError("Количество ножек стола должно быть больше 0.")
        self.material = material
        self.legs_count = legs_count

    @abstractmethod
    def assemble(self) -> None:
        """
        Собрать стол.
        """
        ...

    @abstractmethod
    def clean(self) -> None:
        """
        Очистить поверхность стола.
        """
        ...

    @abstractmethod
    def move(self, new_location: str) -> None:
        """
        Переместить стол в новое место.

        Args:
            new_location (str): Новое место для стола.
        """
        ...


class Tree(ABC):
    """
    Абстрактный класс, описывающий дерево.
    """

    def __init__(self, species: str, age: int):
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")
        self.species = species
        self.age = age

    @abstractmethod
    def photosynthesize(self) -> None:
        """
        Запустить процесс фотосинтеза.
        """
        ...

    @abstractmethod
    def grow(self, years: int) -> None:
        """
        Увеличить возраст дерева.

        Args:
            years (int): Количество лет, на которое увеличивается возраст.
        """
        ...

    @abstractmethod
    def shed_leaves(self) -> None:
        """
        Сбрасывать листья.
        """
        ...


class Stack(ABC):
    """
    Абстрактный класс, описывающий стек.
    """

    def __init__(self, max_size: int):
        if max_size <= 0:
            raise ValueError("Максимальный размер стека должен быть больше 0.")
        self.max_size = max_size
        self.items = []

    @abstractmethod
    def push(self, item: int) -> None:
        """
        Добавить элемент в стек.

        Args:
            item (int): Элемент для добавления.

        Raises:
            OverflowError: Если стек уже заполнен.
        """
        ...

    @abstractmethod
    def pop(self) -> int:
        """
        Удалить и вернуть элемент из стека.

        Returns:
            int: Удаленный элемент.

        Raises:
            IndexError: Если стек пуст.
        """
        ...

    @abstractmethod
    def peek(self) -> int:
        """
        Посмотреть верхний элемент стека без удаления.

        Returns:
            int: Верхний элемент стека.

        Raises:
            IndexError: Если стек пуст.
        """
        ...


if __name__ == "__main__":
    import doctest


    class SimpleTable(Table):
        def assemble(self) -> None:
            """Пример реализации"""
            print("Стол собран.")

        def clean(self) -> None:
            """Пример реализации"""
            print("Стол очищен.")

        def move(self, new_location: str) -> None:
            """Пример реализации"""
            print(f"Стол перемещен в {new_location}.")


    class SimpleTree(Tree):
        def photosynthesize(self) -> None:
            """Пример реализации"""
            print("Фотосинтез начался.")

        def grow(self, years: int) -> None:
            """Пример реализации"""
            self.age += years
            print(f"Дерево выросло на {years} лет.")

        def shed_leaves(self) -> None:
            """Пример реализации"""
            print("Листья опали.")


    class SimpleStack(Stack):
        def push(self, item: int) -> None:
            """Пример реализации"""
            if len(self.items) >= self.max_size:
                raise OverflowError("Стек переполнен.")
            self.items.append(item)

        def pop(self) -> int:
            """Пример реализации"""
            if not self.items:
                raise IndexError("Стек пуст.")
            return self.items.pop()

        def peek(self) -> int:
            """Пример реализации"""
            if not self.items:
                raise IndexError("Стек пуст.")
            return self.items[-1]


    doctest.testmod()
