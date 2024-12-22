class Table:
    """
    Класс, описывающий стол.

    Атрибуты:
        material (str): Материал, из которого изготовлен стол.
        legs_count (int): Количество ножек стола.
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

    def assemble(self, tools: list[str], time: int) -> bool:
        """
        Собрать стол с использованием заданных инструментов за указанное время.

        Args:
            tools (list[str]): Список инструментов, необходимых для сборки.
            time (int): Время, отведенное на сборку в минутах.

        Returns:
            bool: Успешно ли завершена сборка.

        Raises:
            ValueError: Если время меньше или равно 0.
            TypeError: Если инструменты не переданы в виде списка строк.

        Example:
            >>> table = Table("wood", 4)
            >>> table.assemble(["hammer", "screwdriver"], 30)
            True
        """
        if not isinstance(tools, list) or not all(isinstance(tool, str) for tool in tools):
            raise TypeError("Инструменты должны быть списком строк.")
        if not isinstance(time, int) or time <= 0:
            raise ValueError("Время должно быть положительным целым числом.")
        return True

    def clean(self, detergent: str, effort: int) -> bool:
        """
        Очистить поверхность стола с использованием чистящего средства.

        Args:
            detergent (str): Чистящее средство.
            effort (int): Усилие, приложенное к очистке (в условных единицах).

        Returns:
            bool: Успешно ли завершена очистка.

        Raises:
            TypeError: Если параметры имеют неверный тип.
            ValueError: Если усилие меньше 1.

        Example:
            >>> table = Table("metal", 3)
            >>> table.clean("soap", 5)
            True
        """
        if not isinstance(detergent, str):
            raise TypeError("Чистящее средство должно быть строкой.")
        if not isinstance(effort, int):
            raise TypeError("Усилие должно быть целым числом.")
        if effort < 1:
            raise ValueError("Усилие должно быть не меньше 1.")
        return True

    def move(self, new_location: str, safety_checks: bool) -> bool:
        """
        Переместить стол в новое место с проверкой безопасности.

        Args:
            new_location (str): Новое место для стола.
            safety_checks (bool): Флаг выполнения проверок безопасности.

        Returns:
            bool: Успешно ли выполнено перемещение.

        Raises:
            TypeError: Если `new_location` не строка или `safety_checks` не булевое значение.
            ValueError: Если `new_location` является пустой строкой.

        Example:
            >>> table = Table("wood", 4)
            >>> table.move("Living Room", True)
            True
        """
        if not isinstance(new_location, str):
            raise TypeError("Новое место должно быть строкой.")
        if not new_location.strip():
            raise ValueError("Новое место не может быть пустой строкой.")
        if not isinstance(safety_checks, bool):
            raise TypeError("Проверки безопасности должны быть булевым значением.")

        # Предположим, что здесь выполняются действия по перемещению стола.
        return True


class Tree:
    """
    Класс, описывающий дерево.

    Атрибуты:
        species (str): Вид дерева.
        age (int): Возраст дерева в годах.
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

    def photosynthesize(self):
        """
        Запустить процесс фотосинтеза.
        """
        ...

    def grow(self, years: int):
        """
        Увеличить возраст дерева.

        Args:
            years (int): Количество лет, на которое увеличивается возраст.

        Raises:
            ValueError: Если количество лет меньше 0.
        """
        if not isinstance(years, int):
            raise TypeError("Количество лет должно быть целым числом.")
        if years < 0:
            raise ValueError("Количество лет не может быть отрицательным.")
        ...

    def shed_leaves(self):
        """
        Сбрасывать листья.
        """
        ...


class Stack:
    """
    Класс, описывающий стек.

    Атрибуты:
        max_size (int): Максимальный размер стека.
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

    def push(self, item: int):
        """
        Добавить элемент в стек.

        Args:
            item (int): Элемент для добавления.

        Raises:
            OverflowError: Если стек уже заполнен.
            TypeError: Если элемент не является целым числом.
        """
        if not isinstance(item, int):
            raise TypeError("Элемент должен быть целым числом.")
        if len(self.items) >= self.max_size:
            raise OverflowError("Стек переполнен.")
        self.items.append(item)

    def pop(self) -> int:
        """
        Удалить и вернуть верхний элемент из стека.

        Returns:
            int: Удаленный элемент.

        Raises:
            IndexError: Если стек пуст.
        """
        if not self.items:
            raise IndexError("Стек пуст.")
        return self.items.pop()

    def peek(self) -> int:
        """
        Посмотреть верхний элемент стека без удаления.

        Returns:
            int: Верхний элемент.

        Raises:
            IndexError: Если стек пуст.
        """
        if not self.items:
            raise IndexError("Стек пуст.")
        return self.items[-1]

if __name__ == "__main__":
    import doctest

    doctest.testmod()
