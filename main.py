
from abc import ABC, abstractmethod


class Table(ABC):
    """
    Абстрактный класс, описывающий стол.

    Атрибуты:
        material (str): Материал, из которого изготовлен стол (например, "дерево", "металл").
        legs_count (int): Количество ножек стола. Должно быть больше 0.
    """

    def __init__(self, material: str, legs_count: int):
        """
        Конструктор класса Table.

        Args:
            material (str): Материал стола.
            legs_count (int): Количество ножек.

        Raises:
            ValueError: Если количество ножек меньше или равно 0.
            TypeError: Если типы переданных аргументов некорректны.
        """
        if not isinstance(material, str):
            raise TypeError("Материал стола должен быть строкой.")
        if not isinstance(legs_count, int):
            raise TypeError("Количество ножек должно быть целым числом.")
        if legs_count <= 0:
            raise ValueError("Количество ножек стола должно быть больше 0.")

        self.material = material
        self.legs_count = legs_count

    @abstractmethod
    def assemble(self, tools: list[str], time: int) -> bool:
        """
        Собрать стол с использованием заданных инструментов за указанное время.

        Args:
            tools (list[str]): Список инструментов для сборки.
            time (int): Время в минутах, отведенное на сборку.

        Returns:
            bool: Успешно ли была завершена сборка.
        """
        ...

    @abstractmethod
    def clean(self, detergent: str, effort: int) -> bool:
        """
        Очистить поверхность стола с использованием чистящего средства.

        Args:
            detergent (str): Тип чистящего средства.
            effort (int): Уровень усилия от 1 до 10.

        Returns:
            bool: Успешно ли выполнена очистка.
        """
        ...

    @abstractmethod
    def move(self, new_location: str, safety_checks: bool) -> bool:
        """
        Переместить стол в новое место с проверкой безопасности.

        Args:
            new_location (str): Новое место для стола.
            safety_checks (bool): Учитывать ли меры предосторожности при перемещении.

        Returns:
            bool: Успешно ли выполнено перемещение.
        """
        ...


class Tree(ABC):
    """
    Абстрактный класс, описывающий дерево.

    Атрибуты:
        species (str): Вид дерева (например, "дуб", "ель").
        age (int): Возраст дерева в годах. Не может быть отрицательным.
    """

    def __init__(self, species: str, age: int):
        """
        Конструктор класса Tree.

        Args:
            species (str): Вид дерева.
            age (int): Возраст дерева.

        Raises:
            ValueError: Если возраст меньше 0.
            TypeError: Если типы переданных аргументов некорректны.
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой.")
        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть целым числом.")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")

        self.species = species
        self.age = age

    @abstractmethod
    def photosynthesize(self, sunlight: float, water: float) -> float:
        """
        Запустить процесс фотосинтеза с учетом количества света и воды.

        Args:
            sunlight (float): Количество света в люксах.
            water (float): Количество воды в литрах.

        Returns:
            float: Количество произведенного кислорода в граммах.
        """
        ...

    @abstractmethod
    def grow(self, years: int, nutrients: float) -> int:
        """
        Увеличить возраст дерева с учетом наличия питательных веществ.

        Args:
            years (int): Количество лет, на которое увеличивается возраст.
            nutrients (float): Количество доступных питательных веществ в килограммах.

        Returns:
            int: Новый возраст дерева.
        """
        ...

    @abstractmethod
    def shed_leaves(self, season: str) -> bool:
        """
        Сбрасывать листья в зависимости от сезона.

        Args:
            season (str): Текущий сезон (например, "осень").

        Returns:
            bool: Произошло ли опадение листьев.
        """
        ...


class Stack(ABC):
    """
    Абстрактный класс, описывающий стек.

    Атрибуты:
        max_size (int): Максимальный размер стека. Должен быть больше 0.
        items (list[int]): Список элементов в стеке.
    """

    def __init__(self, max_size: int):
        """
        Конструктор класса Stack.

        Args:
            max_size (int): Максимальный размер стека.

        Raises:
            ValueError: Если максимальный размер меньше или равен 0.
            TypeError: Если тип переданного аргумента некорректен.
        """
        if not isinstance(max_size, int):
            raise TypeError("Максимальный размер стека должен быть целым числом.")
        if max_size <= 0:
            raise ValueError("Максимальный размер стека должен быть больше 0.")

        self.max_size = max_size
        self.items = []

    @abstractmethod
    def push(self, item: int, priority: int) -> None:
        """
        Добавить элемент в стек с учетом приоритета.

        Args:
            item (int): Элемент для добавления.
            priority (int): Приоритет добавления элемента.

        Raises:
            OverflowError: Если стек уже заполнен.
        """
        ...

    @abstractmethod
    def pop(self, count: int = 1) -> list[int]:
        """
        Удалить и вернуть один или несколько элементов из стека.

        Args:
            count (int): Количество элементов для удаления.

        Returns:
            list[int]: Список удаленных элементов.

        Raises:
            IndexError: Если в стеке недостаточно элементов.
        """
        ...

    @abstractmethod
    def peek(self, depth: int = 1) -> list[int]:
        """
        Посмотреть верхние элементы стека без удаления.

        Args:
            depth (int): Количество элементов для просмотра с вершины стека.

        Returns:
            list[int]: Список верхних элементов.

        Raises:
            IndexError: Если в стеке недостаточно элементов.
        """
        ...


if __name__ == "__main__":
    import doctest

    class SimpleTable(Table):
        def assemble(self, tools: list[str], time: int) -> bool:
            print("Стол собран.")
            return True

        def clean(self, detergent: str, effort: int) -> bool:
            print("Стол очищен.")
            return True

        def move(self, new_location: str, safety_checks: bool) -> bool:
            print(f"Стол перемещен в {new_location}.")
            return True

    class SimpleTree(Tree):
        def photosynthesize(self, sunlight: float, water: float) -> float:
            print("Фотосинтез начался.")
            return 10.0

        def grow(self, years: int, nutrients: float) -> int:
            self.age += years
            print(f"Дерево выросло на {years} лет.")
            return self.age

        def shed_leaves(self, season: str) -> bool:
            print("Листья опали.")
            return season.lower() == "осень"

    class SimpleStack(Stack):
        def push(self, item: int, priority: int) -> None:
            if len(self.items) >= self.max_size:
                raise OverflowError("Стек переполнен.")
            self.items.append(item)

        def pop(self, count: int = 1) -> list[int]:
            if len(self.items) < count:
                raise IndexError("Стек пуст.")
            popped_items = self.items[-count:]
            self.items = self.items[:-count]
            return popped_items

        def peek(self, depth: int = 1) -> list[int]:
            if len(self.items) < depth:
                raise IndexError("Недостаточно элементов в стеке.")
            return self.items[-depth:]

    doctest.testmod()
