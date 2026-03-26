class SpaceSection:
    def __init__(self, name, oxygen, temperature, pressure, access_code):
        self.name = name
        self.__oxygen_level = oxygen
        self.__temperature = temperature
        self.__pressure = pressure
        self.__access_code = str(access_code)
        self.__captain_password = "admin123"

    @property
    def oxygen(self):
        return self.__oxygen_level

    @oxygen.setter
    def oxygen(self, level):
        if 0 <= level <= 100:
            self.__oxygen_level = level
            print(f"✅ [СИСТЕМА] Уровень кислорода в '{self.name}' изменен на {level}%")
        else:
            print("❌ [ОШИБКА] Уровень кислорода должен быть от 0 до 100!")

    @oxygen.deleter
    def oxygen(self):
        print(f"🛑 [БЛОКИРОВКА] Критическая ошибка! Нельзя удалить систему жизнеобеспечения в '{self.name}'!")

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, temp):
        if -50 <= temp <= 50:
            self.__temperature = temp
            print(f"✅ [СИСТЕМА] Температура в '{self.name}' изменена на {temp}°C")
        else:
            print("❌ [ОШИБКА] Температура должна быть от -50 до +50°C!")

    @temperature.deleter
    def temperature(self):
        print(f"🛑 [БЛОКИРОВКА] Нельзя удалить климат-контроль в '{self.name}'!")

    @property
    def pressure(self):
        return self.__pressure

    @pressure.setter
    def pressure(self, value):
        if 0 <= value <= 200:
            self.__pressure = value
            print(f"✅ [СИСТЕМА] Давление в '{self.name}' изменен на {value} кПа")
        else:
            print("❌ [ОШИБКА] Давление должно быть от 0 до 200 кПа!")

    @pressure.deleter
    def pressure(self):
        print(f"🛑 [БЛОКИРОВКА] Нельзя разгерметизировать отсек '{self.name}' через удаление!")

    @property
    def access_code(self):
        return "🔒 Доступ закрыт! Используйте метод чтения с паролем капитана."

    def get_secure_access_code(self, password):
        if password == self.__captain_password:
            return f"🔑 Код доступа к '{self.name}': {self.__access_code}"
        return "❌ [ОТКАЗ] Неверный пароль капитана!"

    def change_access_code(self, old_code, new_code):
        if str(old_code) == self.__access_code:
            if len(str(new_code)) == 4 and str(new_code).isdigit():
                self.__access_code = str(new_code)
                print(f"✅ [СИСТЕМА] Код доступа к '{self.name}' успешно изменен")
                return True
            print("❌ [ОШИБКА] Новый код должен состоять из 4 цифр!")
        else:
            print("❌ [ОШИБКА] Неверный текущий код доступа!")
        return False

    def emergency_report(self, password):
        if password == self.__captain_password:
            print("\n" + "="*40)
            print(f"🚨 АВАРИЙНЫЙ ОТЧЕТ: {self.name}")
            print(f"Кислород: {self.oxygen}%")
            print(f"Температура: {self.temperature}°C")
            print(f"Давление: {self.pressure} кПа")
            print(f"Код доступа: {self.__access_code}")
            print("="*40)
        else:
            print("❌ [ОТКАЗ] Только капитан может просматривать аварийные отчеты!")


class Spaceship:
    def __init__(self):
        self.sections = [
            SpaceSection("Жилой отсек", 75, 22, 101, "1111"),
            SpaceSection("Двигательный отсек", 85, 45, 150, "2222"),
            SpaceSection("Научный отсек", 70, 18, 98, "3333")
        ]

    def check_all_systems(self):
        print("\n" + "=" * 50)
        print("🛰️ ПРОВЕРКА ВСЕХ СИСТЕМ КОРАБЛЯ")
        print("=" * 50)
        for section in self.sections:
            print(f"\n--- {section.name} ---")
            print(f"Уровень кислорода: {section.oxygen}%")
            print(f"Температура: {section.temperature}°C")
            print(f"Давление: {section.pressure} кПа")
        print("=" * 50)


def interactive_menu():
    ship = Spaceship()
    
    while True:
        print("\n" + "="*50)
        print("🛸 ГЛАВНЫЙ МОСТИК КОРАБЛЯ 'ПИТОН-1'")
        print("="*50)
        print("1. Показать состояние всего корабля")
        print("2. Управление конкретным отсеком")
        print("0. Выход из системы")
        
        choice = input("\nВыберите действие: ").strip()

        if choice == "0":
            print("\n👋 Отключение систем безопасности корабля. До связи!")
            break

        elif choice == "1":
            ship.check_all_systems()

        elif choice == "2":
            print("\nДоступные отсеки:")
            for i, sec in enumerate(ship.sections):
                print(f"{i + 1}. {sec.name}")
            
            try:
                sec_choice = int(input("Выберите номер отсека: ")) - 1
                if 0 <= sec_choice < len(ship.sections):
                    active_sec = ship.sections[sec_choice]
                    
                    while True:
                        print(f"\n⚙️ УПРАВЛЕНИЕ: {active_sec.name}")
                        print("1. Изменить уровень кислорода")
                        print("2. Изменить температуру")
                        print("3. Изменить давление")
                        print("4. Сменить код доступа")
                        print("5. Аварийный отчет (пароль капитана)")
                        print("6. Попробовать удалить параметры (Тест deleter)")
                        print("0. Вернуться назад")
                        
                        action = input("\nВыберите действие: ").strip()

                        if action == "0":
                            break
                        elif action == "1":
                            level = int(input("Введите новый уровень кислорода (0-100): "))
                            active_sec.oxygen = level
                        elif action == "2":
                            temp = int(input("Введите новую температуру (-50 до 50): "))
                            active_sec.temperature = temp
                        elif action == "3":
                            pres = int(input("Введите новое давление (0-200): "))
                            active_sec.pressure = pres
                        elif action == "4":
                            old_c = input("Введите старый код доступа: ")
                            new_c = input("Введите новый 4-значный код: ")
                            active_sec.change_access_code(old_c, new_c)
                        elif action == "5":
                            pwd = input("Введите пароль капитана: ")
                            active_sec.emergency_report(pwd)
                        elif action == "6":
                            print("\n--- ТЕСТ DELETER ---")
                            del active_sec.oxygen
                            del active_sec.temperature
                            del active_sec.pressure
                else:
                    print("❌ Неверный номер отсека.")
            except ValueError:
                print("❌ Ошибка ввода. Введите число.")


if __name__ == "__main__":
    interactive_menu()
