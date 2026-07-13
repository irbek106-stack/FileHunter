from config import *
from utils import load_bad_words, format_size
from scanner import scan_files, select_dir
from filters import filter_big, filter_old, filter_bad
from duplicates import find_dup, dup_summary
from files import found, add_files, clear_files, show_files, select_files, delete_selected
from printer import print_res, print_stats

# ==================== ASCII-АРТ ====================
def show_logo():
    print("""
██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ ███████╗██╗██╗     ███████╗
██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝██║██║     ██╔════╝
███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝█████╗  ██║██║     █████╗  
██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗██╔══╝  ██║██║     ██╔══╝  
██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║██║     ██║███████╗███████╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄██████▄▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄██████████████▄▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░▄████▀▀░░░░░░░░▀▀████▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░▄███▀░░░░░░░░░░░░░░▀███▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░▄███░░░░░░░░░░░░░░░░░░███▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░███░░░░░▄▄▄████▄▄▄░░░░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░███░░▄█████░░░░█████▄░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░███░░▀█████░░░░█████▀░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░███░░░░░▀▀▀████▀▀▀░░░░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░▀███░░░░░░░░░░░░░░░░░░███▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░▀███▄░░░░░░░░░░░░░░▄███▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░▀████▄▄░░░░░░░░▄▄████░░▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀██████████████▀░░▄███▄░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀██████▀▀░░░░▀██████▄░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀███████▄░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀███████▄░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█████████▄░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀████████▄░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀███████░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░░░░░░░░░░░░░░░░
    """)
    print("="*60)
    print("   🚀 ФАЙЛОВЫЙ СКАНЕР HUNTERfile")
    print("="*60)
    print(f"   📂 Папка: {SCAN_DIR.absolute()}")
    print(f"   ⚙️  Размер: ≥{MIN_SIZE_MB} МБ, Возраст: >{MAX_AGE_DAYS} дн.")
    if found:
        print(f"   📋 Найдено файлов: {len(found)} (готово к удалению)")
    print("="*60)

# ==================== ОСНОВНЫЕ ФУНКЦИИ ====================

def full_scan():
    clear_files()
    print("\n🔍 ПОЛНОЕ СКАНИРОВАНИЕ")
    print(f"📂 {SCAN_DIR.absolute()}")
    all_f = scan_files(SCAN_DIR)
    if not all_f: print("❌ Нет файлов!"); return
    print(f"✅ {len(all_f)} файлов")
    bad = load_bad_words(BAD_WORDS_FILE)
    big = filter_big(all_f, MIN_SIZE_MB)
    old = filter_old(all_f, MAX_AGE_DAYS)
    bad_f = filter_bad(all_f, bad)
    dups = find_dup(all_f)
    dup_f = [f for g in dups.values() for f in g]
    add_files(big, "Большие"); add_files(old, "Старые")
    add_files(bad_f, "Плохие"); add_files(dup_f, "Дубликаты")
    print_res("БОЛЬШИЕ", big)
    print_res("СТАРЫЕ", old)
    print_res("ПЛОХИЕ", bad_f)
    print_res("ДУБЛИКАТЫ", dups, 5)
    print_stats(all_f, big, old, bad_f, dups)
    print(f"\n📊 Найдено: {len(found)} файлов")
    if found and input("Выбрать для удаления? (y/n): ").lower()=='y':
        select_files()

def combined():
    clear_files()
    print("\n🔍 КОМБИНИРОВАННЫЙ ПОИСК")
    all_f = scan_files(SCAN_DIR)
    if not all_f: print("❌ Нет файлов!"); return
    print(f"✅ {len(all_f)} файлов")
    print("\nКритерии:\n1. Большие\n2. Старые\n3. Плохие\n4. Дубликаты\n5. Все")
    c = input("Номера (1,2,3,4,5): ")
    crit = []
    if '5' in c or not c: crit=['big','old','bad','dup']
    else:
        if '1' in c: crit.append('big')
        if '2' in c: crit.append('old')
        if '3' in c: crit.append('bad')
        if '4' in c: crit.append('dup')
    if not crit: print("❌ Нет критериев!"); return
    bad = load_bad_words(BAD_WORDS_FILE)
    if 'big' in crit:
        r=filter_big(all_f, MIN_SIZE_MB); add_files(r,"Большие"); print(f"  Большие: {len(r)}")
    if 'old' in crit:
        r=filter_old(all_f, MAX_AGE_DAYS); add_files(r,"Старые"); print(f"  Старые: {len(r)}")
    if 'bad' in crit:
        r=filter_bad(all_f, bad); add_files(r,"Плохие"); print(f"  Плохие: {len(r)}")
    if 'dup' in crit:
        print("⏳ Поиск дубликатов...")
        dups=find_dup(all_f); r=[f for g in dups.values() for f in g]
        add_files(r,"Дубликаты"); print(f"  Дубликаты: {len(r)}")
    if not found: print("✅ Ничего нет"); return
    print(f"\n📊 Найдено: {len(found)}, {format_size(sum(f['size_mb'] for f in found)*1048576)}")
    select_files()

def find_big():
    all_f=scan_files(SCAN_DIR); r=filter_big(all_f, MIN_SIZE_MB)
    clear_files(); add_files(r,"Большие")
    print_res(f"≥{MIN_SIZE_MB} МБ", r)
    if r and input("Удалить? (y/n): ").lower()=='y': select_files()

def find_old():
    all_f=scan_files(SCAN_DIR); r=filter_old(all_f, MAX_AGE_DAYS)
    clear_files(); add_files(r,"Старые")
    print_res(f"Старше {MAX_AGE_DAYS} дн.", r)
    if r and input("Удалить? (y/n): ").lower()=='y': select_files()

def find_bad():
    bad=load_bad_words(BAD_WORDS_FILE)
    if not bad: print("⚠️ Нет слов!"); return
    all_f=scan_files(SCAN_DIR); r=filter_bad(all_f, bad)
    clear_files(); add_files(r,"Плохие")
    print_res("ПЛОХИЕ ИМЕНА", r)
    if r and input("Удалить? (y/n): ").lower()=='y': select_files()

def find_dup_only():
    all_f=scan_files(SCAN_DIR)
    print("⏳ Вычисление MD5...")
    dups=find_dup(all_f)
    if not dups: print("✅ Дубликатов нет"); return
    s=dup_summary(dups); print(f"📊 {s['groups']} групп, {s['files']} файлов")
    r=[f for g in dups.values() for f in g]
    clear_files(); add_files(r,"Дубликаты")
    if input("Удалить? (y/n): ").lower()=='y': select_files()

def settings():
    global SCAN_DIR, MIN_SIZE_MB, MAX_AGE_DAYS
    print("\n⚙️ НАСТРОЙКИ")
    print(f"1. Размер: {MIN_SIZE_MB} МБ")
    print(f"2. Возраст: {MAX_AGE_DAYS} дн.")
    print(f"3. Папка: {SCAN_DIR}")
    c=input("Выбор (1-4, 4-сброс): ")
    if c=='1':
        n=input(f"Размер [{MIN_SIZE_MB}]: ")
        if n: MIN_SIZE_MB=int(n)
    elif c=='2':
        n=input(f"Возраст [{MAX_AGE_DAYS}]: ")
        if n: MAX_AGE_DAYS=int(n)
    elif c=='3':
        from pathlib import Path
        p=input(f"Путь [{SCAN_DIR}]: ")
        if p and Path(p).exists(): SCAN_DIR=Path(p)
    elif c=='4':
        from pathlib import Path
        MIN_SIZE_MB=100; MAX_AGE_DAYS=30; SCAN_DIR=Path(".")
        print("✅ Сброшено")

def info():
    print("\nℹ️ ИНФОРМАЦИЯ\n"+"="*50)
    print("HUNTERfile - это автоматизированная система для мониторинга файлого мусора и нарушения хранения файлов")
    print("HUNTERfile использует Библиотеки: pathlib, hashlib, re\n")
    print("Функции: большие, старые, плохие имена, дубликаты")
    print("Комбинированный поиск, интерактивное удаление")
    print("Ссылка на картинку лупы https://text-image.ru/news/")
    print("v.3.7.26")
    print(f"\n📁 {SCAN_DIR.absolute()}")
    print(f"⚙️ ≥{MIN_SIZE_MB} МБ, >{MAX_AGE_DAYS} дн.")

def menu():
    show_logo()
    print("\n1. 🔍 Полное сканирование")
    print("2. 🔍 Комбинированный поиск")
    print("3. 📁 Выбрать папку")
    print("4. 💾 Большие файлы")
    print("5. ⏳ Старые файлы")
    print("6. 🚫 Плохие имена")
    print("7. 📋 Дубликаты")
    print("8. 📋 Показать найденные")
    print("9. 🎯 Выбрать для удаления")
    print("10. 🗑️ Удалить выбранные")
    print("11. ⚙️ Настройки")
    print("12. ℹ️ Информация")
    print("0. 🚪 Выход")
    print("="*60)

def main():
    while True:
        menu()
        c=input("\nВыбор (0-12): ")
        if c=='0': print("\n👋 До свидания!"); break
        elif c=='1': full_scan()
        elif c=='2': combined()
        elif c=='3':
            d=select_dir()
            if d and d.exists(): 
                global SCAN_DIR
                SCAN_DIR=d
                print(f"✅ {SCAN_DIR.absolute()}")
        elif c=='4': find_big()
        elif c=='5': find_old()
        elif c=='6': find_bad()
        elif c=='7': find_dup_only()
        elif c=='8': show_files()
        elif c=='9': select_files()
        elif c=='10': delete_selected()
        elif c=='11': settings()
        elif c=='12': info()
        else: print("❌ Неверно")

if __name__ == "__main__":
    main()