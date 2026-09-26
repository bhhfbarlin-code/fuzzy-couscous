mod made by seraph

```python
# -*- coding: utf-8 -*-
# ============================================================
#  MARCO X CARLO
#  Комбинированный инструмент для Free Fire (легальные функции)
#  Создатель: Prime X Karlo
#  Команда: BLACK HAT HACKERS FORCE
#  Версия: 1.0
#  Только легальные модули: сравнение оружия, генератор
#  чувствительности, генератор карт кастомных комнат,
#  генератор имён, трекер гильдий/турниров, проверка
#  промокодов. Никакого взлома аккаунтов.
# ============================================================

import os
import sys
import random
import json
import string
from datetime import datetime

# ---------- Цвета для Termux/Linux ----------
class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    WHITE = "\033[97m"

# ---------- Баннер ----------
def banner():
    os.system("clear" if os.name != "nt" else "cls")
    print(f"""{C.RED}{C.BOLD}
    ███╗   ███╗ █████╗ ██████╗  ██████╗ ██████╗
    ████╗ ████║██╔══██╗██╔══██╗██╔════╝██╔═══██╗
    ██╔████╔██║███████║██████╔╝██║     ██║   ██║
    ██║╚██╔╝██║██╔══██║██╔══██╗██║     ██║   ██║
    ██║ ╚═╝ ██║██║  ██║██║  ██║╚██████╗╚██████╔╝
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝
{C.RESET}{C.WHITE}{C.BOLD}            MARCO X CARLO{C.RESET}
{C.YELLOW}   ──────────────────────────────────────────{C.RESET}
{C.MAGENTA}      Создатель : {C.BOLD}Prime X Karlo{C.RESET}
{C.GREEN}      Команда   : {C.BOLD}BLACK HAT HACKERS FORCE{C.RESET}
{C.GREEN}      Версия    : {C.BOLD}1.0{C.RESET}
{C.YELLOW}   ──────────────────────────────────────────{C.RESET}
""")

# ---------- Меню ----------
def menu():
    print(f"""{C.CYAN}{C.BOLD}  ┌─────────────── ГЛАВНОЕ МЕНЮ ───────────────┐{C.RESET}
{C.WHITE}  │                                            │
  │  {C.GREEN}[1]{C.WHITE}  Сравнение оружия                        │
  │  {C.GREEN}[2]{C.WHITE}  Генератор чувствительности              │
  │  {C.GREEN}[3]{C.WHITE}  Генератор карт кастомных комнат         │
  │  {C.GREEN}[4]{C.WHITE}  Генератор имён                         │
  │  {C.GREEN}[5]{C.WHITE}  Трекер гильдий / турниров              │
  │  {C.GREEN}[6]{C.WHITE}  Проверка промокодов                    │
  │                                            │
  │  {C.RED}[0]{C.WHITE}  Выход                                 │
  │                                            │
  └────────────────────────────────────────────┘{C.RESET}
""")

# ============================================================
# МОДУЛЬ 1: СРАВНЕНИЕ ОРУЖИЯ
# ============================================================
WEAPONS = {
    "M4A1":   {"урон": 48, "скорострельность": 72, "дальность": 65, "точность": 70},
    "AK47":   {"урон": 53, "скорострельность": 60, "дальность": 68, "точность": 62},
    "MP40":   {"урон": 35, "скорострельность": 85, "дальность": 40, "точность": 55},
    "UMP":    {"урон": 42, "скорострельность": 78, "дальность": 50, "точность": 65},
    "SCAR":   {"урон": 50, "скорострельность": 68, "дальность": 66, "точность": 68},
    "AWM":    {"урон": 90, "скорострельность": 20, "дальность": 95, "точность": 92},
    "M1014":  {"урон": 80, "скорострельность": 30, "дальность": 25, "точность": 40},
    "MP5":    {"урон": 38, "скорострельность": 82, "дальность": 45, "точность": 60},
}

def compare_weapons():
    print(f"\n{C.YELLOW}═══ СРАВНЕНИЕ ОРУЖИЯ ═══{C.RESET}\n")
    print(f"{C.WHITE}Доступное оружие:{C.RESET}")
    for i, w in enumerate(WEAPONS.keys(), 1):
        print(f"  {C.GREEN}{i}.{C.RESET} {w}")
    print()
    try:
        a = int(input(f"{C.CYAN}[?]{C.RESET} Номер первого оружия: "))
        b = int(input(f"{C.CYAN}[?]{C.RESET} Номер второго оружия: "))
    except ValueError:
        print(f"{C.RED}[!]{C.RESET} Введите числа.")
        return
    names = list(WEAPONS.keys())
    if not (1 <= a <= len(names) and 1 <= b <= len(names)):
        print(f"{C.RED}[!]{C.RESET} Неверный номер.")
        return
    w1 = names[a-1]
    w2 = names[b-1]
    print(f"\n{C.YELLOW}── {w1} vs {w2} ──{C.RESET}\n")
    for key in ["урон", "скорострельность", "дальность", "точность"]:
        v1 = WEAPONS[w1][key]
        v2 = WEAPONS[w2][key]
        if v1 > v2:
            mark = f"{C.GREEN}◀ {w1}{C.RESET}"
        elif v2 > v1:
            mark = f"{C.GREEN}▶ {w2}{C.RESET}"
        else:
            mark = f"{C.YELLOW}равно{C.RESET}"
        print(f"  {C.CYAN}{key:>18}:{C.RESET} {v1:>3}  vs  {v2:<3}  {mark}")
    print()

# ============================================================
# МОДУЛЬ 2: ГЕНЕРАТОР ЧУВСТВИТЕЛЬНОСТИ
# ============================================================
def sensitivity_generator():
    print(f"\n{C.YELLOW}═══ ГЕНЕРАТОР ЧУВСТВИТЕЛЬНОСТИ ═══{C.RESET}\n")
    print(f"{C.WHITE}Выберите стиль игры:{C.RESET}")
    print(f"  {C.GREEN}1.{C.RESET} Ближний бой (близко)")
    print(f"  {C.GREEN}2.{C.RESET} Средний бой")
    print(f"  {C.GREEN}3.{C.RESET} Дальний бой (снайпер)")
    try:
        style = int(input(f"{C.CYAN}[?]{C.RESET} Номер стиля: "))
    except ValueError:
        print(f"{C.RED}[!]{C.RESET} Введите число.")
        return
    if style == 1:
        sens = {"Общий": 95, "Красная точка": 90, "2x прицел": 85, "4x прицел": 75, "AWM": 50, "Свободный взгляд": 80}
    elif style == 2:
        sens = {"Общий": 80, "Красная точка": 75, "2x прицел": 70, "4x прицел": 60, "AWM": 40, "Свободный взгляд": 65}
    elif style == 3:
        sens = {"Общий": 60, "Красная точка": 55, "2x прицел": 50, "4x прицел": 45, "AWM": 30, "Свободный взгляд": 50}
    else:
        print(f"{C.RED}[!]{C.RESET} Неверный выбор.")
        return
    print(f"\n{C.GREEN}Рекомендуемая чувствительность:{C.RESET}")
    for k, v in sens.items():
        print(f"  {C.CYAN}{k:>18}:{C.RESET} {v}")
    print(f"\n{C.YELLOW}Совет: настройте под себя, это базовая рекомендация.{C.RESET}\n")

# ============================================================
# МОДУЛЬ 3: ГЕНЕРАТОР КАРТ КАСТОМНЫХ КОМНАТ
# ============================================================
def custom_room_generator():
    print(f"\n{C.YELLOW}═══ ГЕНЕРАТОР КАРТ КАСТОМНЫХ КОМНАТ ═══{C.RESET}\n")
    mode = input(f"{C.CYAN}[?]{C.RESET} Режим (BR/CS/Clash Squad): ").strip().upper()
    if mode not in ("BR", "CS", "CLASH SQUAD"):
        print(f"{C.RED}[!]{C.RESET} Неверный режим.")
        return
    map_name = input(f"{C.CYAN}[?]{C.RESET} Карта (Bermuda/Purgatory/Kalahari/Alpine): ").strip()
    players = input(f"{C.CYAN}[?]{C.RESET} Количество игроков: ").strip()
    print(f"\n{C.GREEN}── Карта создана ──{C.RESET}")
    print(f"  {C.CYAN}Режим   :{C.RESET} {mode}")
    print(f"  {C.CYAN}Карта   :{C.RESET} {map_name}")
    print(f"  {C.CYAN}Игроки  :{C.RESET} {players}")
    print(f"  {C.CYAN}ID комнаты:{C.RESET} {random.randint(100000, 999999)}")
    print(f"  {C.CYAN}Пароль  :{C.RESET} {''.join(random.choices(string.ascii_uppercase + string.digits, k=6))}")
    print()

# ============================================================
# МОДУЛЬ 4: ГЕНЕРАТОР ИМЁН
# ============================================================
def name_generator():
    print(f"\n{C.YELLOW}═══ ГЕНЕРАТОР ИМЁН ═══{C.RESET}\n")
    prefixes = ["Pro", "Dark", "Fire", "Ghost", "King", "Lord", "Noob", "Sniper", "Alpha", "Toxic"]
    suffixes = ["Killer", "Master", "Legend", "Hunter", "Slayer", "Warrior", "God", "Boss", "X", "OP"]
    try:
        count = int(input(f"{C.CYAN}[?]{C.RESET} Сколько имён сгенерировать? (1-20): "))
        if not 1 <= count <= 20:
            count = 5
    except ValueError:
        count = 5
    print(f"\n{C.GREEN}Сгенерированные имена:{C.RESET}")
    for i in range(1, count+1):
        style = random.choice([1,2,3])
        if style == 1:
            name = random.choice(prefixes) + random.choice(suffixes)
        elif style == 2:
            name = random.choice(prefixes) + str(random.randint(1,999))
        else:
            name = random.choice(prefixes) + "_" + random.choice(suffixes)
        print(f"  {C.CYAN}{i:02d}.{C.RESET} {name}")
    print()

# ============================================================
# МОДУЛЬ 5: ТРЕКЕР ГИЛЬДИЙ / ТУРНИРОВ
# ============================================================
GUILD_FILE = "guild_data.json"

def load_guilds():
    if os.path.exists(GUILD_FILE):
        with open(GUILD_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_guilds(data):
    with open(GUILD_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def guild_tracker():
    print(f"\n{C.YELLOW}═══ ТРЕКЕР ГИЛЬДИЙ / ТУРНИРОВ ═══{C.RESET}\n")
    data = load_guilds()
    while True:
        print(f"{C.WHITE}1. Добавить запись{C.RESET}")
        print(f"{C.WHITE}2. Показать все{C.RESET}")
        print(f"{C.WHITE}3. Удалить запись{C.RESET}")
        print(f"{C.WHITE}0. Назад{C.RESET}")
        ch = input(f"{C.CYAN}[?]{C.RESET} Выбор: ").strip()
        if ch == "1":
            name = input(f"{C.CYAN}[?]{C.RESET} Название гильдии/турнира: ").strip()
            date = input(f"{C.CYAN}[?]{C.RESET} Дата (ГГГГ-ММ-ДД): ").strip()
            result = input(f"{C.CYAN}[?]{C.RESET} Результат: ").strip()
            data.append({"name": name, "date": date, "result": result})
            save_guilds(data)
            print(f"{C.GREEN}[OK]{C.RESET} Запись добавлена.")
        elif ch == "2":
            if not data:
                print(f"{C.YELLOW}Список пуст.{C.RESET}")
            else:
                for i, item in enumerate(data, 1):
                    print(f"  {C.CYAN}{i}.{C.RESET} {item['name']} | {item['date']} | {item['result']}")
        elif ch == "3":
            if not data:
                print(f"{C.YELLOW}Список пуст.{C.RESET}")
            else:
                for i, item in enumerate(data, 1):
                    print(f"  {C.CYAN}{i}.{C.RESET} {item['name']}")
                try:
                    idx = int(input(f"{C.CYAN}[?]{C.RESET} Номер для удаления: ")) - 1
                    if 0 <= idx < len(data):
                        data.pop(idx)
                        save_guilds(data)
                        print(f"{C.GREEN}[OK]{C.RESET} Удалено.")
                    else:
                        print(f"{C.RED}[!]{C.RESET} Неверный номер.")
                except ValueError:
                    print(f"{C.RED}[!]{C.RESET} Введите число.")
        elif ch == "0":
            break
        else:
            print(f"{C.RED}[!]{C.RESET} Неверный выбор.")
    print()

# ============================================================
# МОДУЛЬ 6: ПРОВЕРКА ПРОМОКОДОВ
# ============================================================
# Статический список известных промокодов (только для примера).
# В реальности нужно обновлять вручную или через API, если появится.
KNOWN_CODES = {
    "FF9MJ31CXKRG": "Скин оружия",
    "FFICJGW9NKYT": "Скин персонажа",
    "FF9MJ34CXKRG": "Алмазы",
    "FFAC2BK8QZ": "Питомец",
}

def redeem_checker():
    print(f"\n{C.YELLOW}═══ ПРОВЕРКА ПРОМОКОДОВ ═══{C.RESET}\n")
    code = input(f"{C.CYAN}[?]{C.RESET} Введите промокод: ").strip().upper()
    if code in KNOWN_CODES:
        print(f"{C.GREEN}[OK]{C.RESET} Код действителен: {KNOWN_CODES[code]}")
        print(f"{C.YELLOW}Активируйте его в официальном центре награды Free Fire.{C.RESET}")
    else:
        print(f"{C.RED}[!]{C.RESET} Код не найден в базе. Возможно, он недействителен или истёк.")
    print()

# ============================================================
# ГЛАВНЫЙ ЦИКЛ
# ============================================================
def main():
    banner()
    actions = {
        "1": ("Сравнение оружия", compare_weapons),
        "2": ("Генератор чувствительности", sensitivity_generator),
        "3": ("Генератор карт кастомных комнат", custom_room_generator),
        "4": ("Генератор имён", name_generator),
        "5": ("Трекер гильдий / турниров", guild_tracker),
        "6": ("Проверка промокодов", redeem_checker),
    }
    while True:
        menu()
        choice = input(f"{C.CYAN}[?]{C.RESET} Выберите пункт: ").strip()
        if choice == "0":
            print(f"\n{C.MAGENTA}  MARCO X CARLO | Prime X Karlo | BLACK HAT HACKERS FORCE{C.RESET}")
            print(f"{C.YELLOW}  Выход.{C.RESET}\n")
            sys.exit(0)
        if choice in actions:
            name, func = actions[choice]
            func()
            input(f"\n{C.YELLOW}Нажмите Enter для возврата в меню...{C.RESET}")
            banner()
        else:
            print(f"{C.RED}[!]{C.RESET} Неверный пункт. Попробуйте 0-6.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.RED}[!]{C.RESET} Прервано пользователем.")
        sys.exit(0)
```