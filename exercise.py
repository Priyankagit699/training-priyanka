docs = [
    {"name": "report.pdf", "type": "pdf", "size_kb": 500, "status": "ACTIVE"},
    {"name": "notes.txt", "type": "txt", "size_kb": 20, "status": "ARCHIVED"},
    {"name": "invoice.pdf", "type": "pdf", "size_kb": 150, "status": "ACTIVE"},
    {"name": "photo.png", "type": "png", "size_kb": 900, "status": "ACTIVE"},
]
def active_sorted(docs):
    active=[]
    for doc in docs:
        if doc["status"]=="ACTIVE":
            active.append(doc)
    return sorted(active, key=lambda d: d["size_kb"])

def count_type(docs):
    counts={}
    for doc in docs:
        t=doc["type"]
        counts[t]=counts.get(t,0)+1
    return counts

def sorted_active(docs):
    return sorted([d for d in docs if d["status"]=="ACTIVE"], key=lambda d: d["size_kb"])

#mere exercise me filter simple tha bus check krna tha isliye comprehension thik tha but agar mujhe active, size, type, or log bhi to mai loop use krti

if __name__=="__main__":
    print(active_sorted(docs))
    print(count_type(docs))
    print(sorted_active(docs))

