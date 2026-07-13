found = []
counter = 0

def add_files(items, label=""):
    global counter
    for f in items:
        counter += 1
        found.append({"id":counter,"path":f["path"],"name":f["name"],
                     "size_mb":f["size_mb"],"mtime":f["mtime"],
                     "label":label,"selected":False})

def clear_files():
    global found, counter
    found = []; counter = 0

def show_files():
    if not found: print("\n✅ Список пуст."); return
    print(f"\n📋 ВСЕ ФАЙЛЫ ({len(found)})")
    for f in found:
        sel = "✓" if f.get("selected") else " "
        print(f"[{sel}][{f['id']:>3}] {f['path']} ({f['size_mb']:.2f} МБ)")

def delete_selected():
    sel = [f for f in found if f.get("selected")]
    if not sel: print("❌ Нет выбранных!"); return
    print(f"\n🗑️ УДАЛЕНИЕ ({len(sel)} файлов)")
    for f in sel: print(f"  • {f['path']}")
    if input("Удалить? (y/n): ").lower() != 'y': print("Отмена"); return
    ok = err = 0
    for f in sel:
        try: f["path"].unlink(); ok+=1
        except: err+=1
    found = [f for f in found if not f.get("selected")]
    print(f"✅ Удалено: {ok}, ошибок: {err}")

def select_files():
    if not found: print("❌ Нет файлов!"); return
    show_files()
    print("\nКоманды: номера (1,3,5), диапазон (1-5), all, clear, delete, back")
    while True:
        cmd = input("> ").lower()
        if cmd=='back': break
        elif cmd=='all':
            for f in found: f["selected"]=True
            print(f"✅ Выбрано {len(found)}")
        elif cmd=='clear':
            for f in found: f["selected"]=False
            print("✅ Сброшено")
        elif cmd=='delete':
            delete_selected()
            if not found: break
        elif cmd=='show':
            show_files()
        else:
            try:
                ids=set()
                for p in cmd.split(','):
                    if '-' in p:
                        a,b=map(int,p.split('-'))
                        ids.update(range(a,b+1))
                    elif p:
                        ids.add(int(p))
                for f in found:
                    if f["id"] in ids: f["selected"]=True
                print(f"✅ Выбрано {len(ids)}")
            except: print("❌ Неверно")