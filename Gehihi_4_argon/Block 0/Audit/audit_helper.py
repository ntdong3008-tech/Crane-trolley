import os, sys, fitz
sys.stdout.reconfigure(encoding='utf-8')

root = r'D:\Tài liệu học tập\Kỳ 2026.1\Thiết Kế TĐĐ\Project'
nasa_path = os.path.join(root, r'Tai_lieu_tham_khao\NASA_SP-2007-6105_Rev_1.pdf')
doc = fitz.open(nasa_path)
print('Total pages NASA:', len(doc))

queries = [
    '4.1 Stakeholder Expectations Definition',
    '4.2 Technical Requirements Definition',
    'Measures of Effectiveness',
    'Appendix C: How to Write',
    'Technical Performance Measures'
]

for q in queries:
    hits = []
    for i, page in enumerate(doc):
        t = page.get_text()
        if q.lower() in t.lower():
            hits.append(i + 1)
    print(f'Query "{q}": pages {hits[:10]}')
