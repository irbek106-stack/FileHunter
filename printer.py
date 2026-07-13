from utils import format_size, age_str

def print_res(title, items, max_items=10):
    print(f"\n📌 {title}\n"+"─"*50)
    if not items: 
        print("  ✅ Ничего нет.")
        return
    
    # Проверяем, является ли items словарём (дубликаты)
    if isinstance(items, dict):
        # Для дубликатов выводим группы
        for i, (hash_val, group) in enumerate(items.items(), 1):
            if i > max_items:
                print(f"  ... и ещё {len(items) - max_items} групп")
                break
            total_size = sum(f["size_mb"] for f in group)
            print(f"  Группа {i} (хэш: {hash_val[:8]}...):")
            print(f"    Файлов: {len(group)}, Размер: {total_size:.2f} МБ")
            for f in group[:3]:
                print(f"      • {f['path']} ({f['size_mb']:.2f} МБ)")
            if len(group) > 3:
                print(f"      ... и ещё {len(group)-3} файлов")
    else:
        # Для списка файлов
        for i, f in enumerate(items[:max_items], 1):
            print(f"  {i}. {f['path']}")
            print(f"     {f['size_mb']:.2f} МБ | {age_str(f['mtime'])}")
        if len(items) > max_items:
            print(f"  ... и ещё {len(items)-max_items}")

def print_stats(all_f, big_f, old_f, bad_f, dups):
    print("\n📊 СТАТИСТИКА\n"+"="*50)
    print(f"📁 Всего: {len(all_f)}")
    print(f"💾 Размер: {format_size(sum(f['size_bytes'] for f in all_f))}")
    print(f"💾 Больших: {len(big_f)}")
    print(f"⏳ Старых: {len(old_f)}")
    print(f"🚫 Плохих: {len(bad_f)}")
    if dups:
        from duplicates import dup_summary
        s = dup_summary(dups)
        print(f"📋 Дубликатов: {s['groups']} групп, {s['files']} файлов")
        print(f"💾 Можно освободить: {format_size(s['size_mb']*1048576)}")