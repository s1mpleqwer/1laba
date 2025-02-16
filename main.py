class Car:
    """
    Базовый класс для автомобилей.

    Attributes:
        make (str): Производитель автомобиля.
        model (str): Модель автомобиля.
        year (int): Год выпуска автомобиля.
        _engine_power (float): Мощность двигателя (в лошадиных силах).
            Инкапсулирован для защиты от прямого изменения извне.
    """

    def __init__(self, make: str, model: str, year: int, engine_power: float) -> None:
        """
        Инициализирует объект автомобиля.

        Args:
            make (str): Производитель.
            model (str): Модель.
            year (int): Год выпуска.
            engine_power (float): Мощность двигателя.
        """
        self.make: str = make
        self.model: str = model
        self.year: int = year
        self._engine_power: float = engine_power

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта автомобиля.

        Returns:
            str: Строка с описанием автомобиля.
        """
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта автомобиля.

        Returns:
            str: Официальное представление автомобиля.
        """
        return (f"Car(make='{self.make}', model='{self.model}', "
                f"year={self.year}, engine_power={self._engine_power})")

    def drive(self, distance: float) -> None:
        """
        Имитация движения автомобиля.

        Args:
            distance (float): Пройденное расстояние в километрах.
        """
        print(f"{self} проехал(а) {distance} км.")

    def calculate_efficiency(self, distance: float, fuel_used: float) -> float:
        """
        Рассчитывает топливную эффективность (километров на литр).

        Args:
            distance (float): Пройденное расстояние в километрах.
            fuel_used (float): Количество использованного топлива в литрах.

        Returns:
            float: Топливная эффективность (км/л). Если топливо не потрачено, возвращает 0.0.
        """
        if fuel_used == 0:
            return 0.0
        return distance / fuel_used


class Truck(Car):
    """
    Дочерний класс для грузовых автомобилей, наследующий функциональность от базового класса Car.

    Attributes:
        max_load (float): Максимальная грузоподъемность грузовика в тоннах.
    """

    def __init__(self, make: str, model: str, year: int, engine_power: float, max_load: float) -> None:
        """
        Инициализирует объект грузовика.

        Args:
            make (str): Производитель.
            model (str): Модель.
            year (int): Год выпуска.
            engine_power (float): Мощность двигателя.
            max_load (float): Максимальная грузоподъемность грузовика.
        """
        super().__init__(make, model, year, engine_power)
        self.max_load: float = max_load

    def __str__(self) -> str:
        """
        Возвращает строковое представление грузовика с указанием его грузоподъемности.

        Returns:
            str: Строка с описанием грузовика.
        """
        return f"{super().__str__()} (Грузоподъемность: {self.max_load} т)"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление грузовика.

        Returns:
            str: Официальное представление грузовика.
        """
        return (f"Truck(make='{self.make}', model='{self.model}', year={self.year}, "
                f"engine_power={self._engine_power}, max_load={self.max_load})")

    def drive(self, distance: float) -> None:
        """
        Переопределяет метод drive для грузового автомобиля.

        Причина перегрузки: у грузовиков могут быть особенности при движении, связанные с нагрузкой
        (например, повышенные требования к торможению или ускорению), что требует модификации поведения
        метода drive по сравнению с легковыми автомобилями.

        Args:
            distance (float): Пройденное расстояние в километрах.
        """
        # Здесь можно добавить дополнительные расчёты с учетом грузоподъемности.
        print(f"{self} (с учетом груза) проехал(а) {distance} км.")


if __name__ == "__main__":
    # Создаем экземпляр легкового автомобиля
    car: Car = Car("Toyota", "Corolla", 2020, 132)
    print(car)  # Вывод: 2020 Toyota Corolla
    print(repr(car))  # Вывод: Car(make='Toyota', model='Corolla', year=2020, engine_power=132)
    car.drive(150)  # Имитация движения автомобиля
    efficiency_car: float = car.calculate_efficiency(150, 10)
    print(f"Эффективность автомобиля: {efficiency_car:.2f} км/л\n")

    # Создаем экземпляр грузового автомобиля
    truck: Truck = Truck("Volvo", "FH16", 2018, 540, 25)
    print(truck)  # Вывод: 2018 Volvo FH16 (Грузоподъемность: 25 т)
    print(repr(truck))  # Вывод: Truck(make='Volvo', model='FH16', year=2018, engine_power=540, max_load=25)
    truck.drive(80)  # Имитация движения грузовика с учетом особенностей груза
    efficiency_truck: float = truck.calculate_efficiency(80, 15)
    print(f"Эффективность грузовика: {efficiency_truck:.2f} км/л")
