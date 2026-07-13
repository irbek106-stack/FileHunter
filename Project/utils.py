from pathlib import Path
from datetime import datetime

def format_size(bytes):
    for u in ['Б','КБ','МБ','ГБ','ТБ']:
        if bytes < 1024: return f"{bytes:.2f} {u}"
        bytes /= 1024
    return f"{bytes:.2f} ПБ"

def load_bad_words(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return [w.strip().lower() for w in f if w.strip() and not w.startswith('#')]
    except:
        with open(path, 'w', encoding='utf-8') as f:
            f.write("# мат\nмат\nоскорбление\nглупый\n")
        return ["мат","оскорбление","глупый"]

def age_str(mtime):
    d = (datetime.now() - mtime).days
    return f"{d} дн." if d > 0 else "сегодня"