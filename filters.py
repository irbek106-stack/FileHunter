from datetime import datetime, timedelta
import re

def filter_big(files, min_mb):
    return [f for f in files if f["size_mb"] >= min_mb]

def filter_old(files, days):
    cutoff = datetime.now() - timedelta(days=days)
    return [f for f in files if f["mtime"] <= cutoff]

def filter_bad(files, words):
    if not words: return []
    p = re.compile(r'\b(' + '|'.join(re.escape(w) for w in words) + r')\b', re.I)
    return [f for f in files if p.search(f["name"])]