import hashlib
from collections import defaultdict

def md5(path):
    try:
        h = hashlib.md5()
        with open(path,"rb") as f:
            for c in iter(lambda: f.read(8192), b""): h.update(c)
        return h.hexdigest()
    except: return None

def find_dup(files):
    if not files: return {}
    by_size = defaultdict(list)
    for f in files: by_size[f["size_bytes"]].append(f)
    res = defaultdict(list)
    for g in by_size.values():
        if len(g)>1:
            for f in g:
                h = md5(f["path"])
                if h: res[h].append(f)
    return {h:g for h,g in res.items() if len(g)>1}

def dup_summary(dups):
    if not dups: return {"groups":0,"files":0,"size_mb":0}
    return {"groups":len(dups),"files":sum(len(g) for g in dups.values()),
            "size_mb":sum(sum(f["size_mb"] for f in g) for g in dups.values())}