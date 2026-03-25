class SpaceSection:
    def __init__(self, name, oxygen, temperature, pressure, access_code):
        self.name = name
        self.__oxygen_level = oxygen
        self.__temperature = temperature
        self.__pressure = pressure # Задание 3: Новый параметр (Давление)
        self.__access_code = str(access_code)
        self.__captain_password = "admin123"

    # --- Геттеры ---
    def get_oxygen(self):
        return f"Уровень кислорода в {self.name}: {self.__oxygen_level}%"

    def get_temperature(self):
        return f"Температура в {self.name}: {self.__temperature}°C"

    def get_pressure(self):
        return f"Давление в {self.name}: {self.__pressure} кПа"

    def get_access_code(self, password):
        if password == self.__captain_password:
            return f"Код доступа к {self.name}: {self.__access_code}"
        return "❌ Доступ запрещен! Неверный пароль капитана!"

    # --- Сеттеры ---
    def set_oxygen(self, level):
        if 0 <= level <= 100:
            self.__oxygen_level = level
            print(f"✅ Уровень кислорода в {self.name} изменен на {level}%")
        else:
            print("❌ Ошибка! Уровень кислорода должен быть от 0 до 100")

    def set_temperature(self, temp):
        if -50 <= temp <= 50:
            self.__temperature = temp
            print(f"✅ Температура в {self.name} изменена на {temp}°C")
        else:
            print("❌ Ошибка! Температура должна быть от -50 до +50")

    def set_pressure(self, pressure):
        if 0 <= pressure <= 200: # Валидация давления (от 0 до 200 кПа)
            self.__pressure = pressure
            print(f"✅ Давление в {self.name} изменено на {pressure} кПа")
        else:
            print("❌ Ошибка! Давление должно быть от 0 до 200 кПа")

    def set_access_code(self, old_code, new_code):
        if str(old_code) == self.__access_code:
            if len(str(new_code)) == 4 and str(new_code).isdigit():
                self.__access_code = str(new_code)
                print(f"✅ Код доступа к {self.name} успешно изменен")
                return True
            else:
                print("❌ Новый код должен состоять из 4 цифр!")
        else:
            print("❌ Неверный текущий код доступа!")
        return False

    def emergency_report(self, password):
        if password == self.__captain_password:
            print("\n" + "="*40)
            print(f"🚨 АВАРИЙНЫЙ ОТЧЕТ: {self.name}")
            print(f"Кислород: {self.__oxygen_level}%")
            print(f"Температура: {self.__temperature}°C")
            print(f"Давление: {self.__pressure} кПа")
            print(f"Код доступа: {self.__access_code}")
            print("="*40)
        else:
            print("❌ Только капитан может просматривать аварийные отчеты!")


class Spaceship:
    def __init__(self):
        # Задание 4: Модификация корабля (добавлено давление)
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
            print(section.get_oxygen())
            print(section.get_temperature())
            print(section.get_pressure())
        print("=" * 50)


# Задание 5: Диалоговая система (меню через input())
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
            print("\n👋 Отключение систем безопасности корабля...")
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
                        print("0. Вернуться назад")
                        
                        action = input("\nВыберите действие: ").strip()

                        if action == "0":
                            break
                        elif action == "1":
                            level = int(input("Введите новый уровень кислорода (0-100): "))
                            active_sec.set_oxygen(level)
                        elif action == "2":
                            temp = int(input("Введите новую температуру (-50 до 50): "))
                            active_sec.set_temperature(temp)
                        elif action == "3":
                            pres = int(input("Введите новое давление (0-200 кПа): "))
                            active_sec.set_pressure(pres)
                        elif action == "4":
                            old_c = input("Введите старый код доступа: ")
                            new_c = input("Введите новый 4-значный код: ")
                            active_sec.set_access_code(old_c, new_c)
                        elif action == "5":
                            pwd = input("Введите пароль капитана: ")
                            active_sec.emergency_report(pwd)
                else:
                    print("❌ Неверный номер отсека.")
            except ValueError:
                print("❌ Ошибка ввода. Введите число.")


if __name__ == "__main__":
    interactive_menu()