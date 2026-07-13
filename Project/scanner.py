from pathlib import Path
from datetime import datetime

def scan_files(dir):
    files = []
    p = Path(dir)
    if not p.exists(): return []
    for f in p.rglob("*"):
        if f.is_file():
            try:
                s = f.stat()
                files.append({"path":f,"name":f.name,"size_mb":s.st_size/1048576,
                             "size_bytes":s.st_size,"mtime":datetime.fromtimestamp(s.st_mtime)})
            except: continue
    return files

def select_dir():
    print("\n📁 ВЫБОР ДИРЕКТОРИИ\n1. Текущая\n2. Вручную\n3. Типовые")
    c = input("Выбор: ")
    if c=='1': return Path(".")
    if c=='2':
        p = input("Путь: ").strip()
        return Path(p) if p else Path(".")
    if c=='3':
        dirs = [("Домашняя",Path.home()), ("Загрузки",Path.home()/"Downloads"),
                ("Документы",Path.home()/"Documents"), ("Рабочий стол",Path.home()/"Desktop")]
        for i,(n,p) in enumerate(dirs,1):
            print(f"{i}. {n} - {p}")
        try:
            idx = int(input("Выберите: "))-1
            return dirs[idx][1] if 0<=idx<len(dirs) else Path(".")
        except: return Path(".")
    return Path(".")