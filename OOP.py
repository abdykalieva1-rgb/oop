class SmartDevice:
    def __init__(self, brand, model, battery_level, is_on):
        self.brand = brand
        self.model = model

        # Приватные атрибуты
        self.__battery_level = self.__validate_battery(battery_level)
        self.__is_on = self.__validate_power(is_on)

    def __validate_battery(self, value):
        if value < 0:
            return 0
        elif value > 100:
            return 100
        return value

    def __validate_power(self, value):
        return bool(value)

    def turn_on(self):
        if self.__battery_level == 0:
            print("❌ Нельзя включить: заряд 0%")
            return
        self.__is_on = True
        print("✅ Устройство включено")

    def turn_off(self):
        self.__is_on = False
        print("🔌 Устройство выключено")

    def charge(self, amount):
        if amount <= 0:
            print("❌ Заряд должен быть положительным")
            return

        self.__battery_level += amount
        if self.__battery_level > 100:
            self.__battery_level = 100

        print(f"🔋 Заряд увеличен. Текущий уровень: {self.__battery_level}%")

    def use(self, minutes):
        if not self.__is_on:
            print("❌ Устройство выключено")
            return

        required = minutes  # 1 минута = 1%

        if self.__battery_level >= required:
            self.__battery_level -= required
            print(f"⚡ Использовано {minutes} мин. Осталось {self.__battery_level}%")
        else:
            print("⚠️ Недостаточно заряда. Устройство выключено")
            self.__battery_level = 0
            self.__is_on = False

    def get_status(self):
        power = "Да" if self.__is_on else "Нет"
        return f"Устройство: {self.brand} {self.model} | Включено: {power} | Заряд: {self.__battery_level}%"

device = SmartDevice("Samsung", "Galaxy", 120, True)

print(device.get_status())

device.use(30)

print(device.get_status())

device.charge(20)

device.turn_off()
device.use(10)

device.turn_on()
device.use(100)

print(device.get_status())
