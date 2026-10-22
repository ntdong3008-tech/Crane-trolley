import sys, os, fitz
sys.stdout.reconfigure(encoding='utf-8')
root = r'D:\Tài liệu học tập\Kỳ 2026.1\Thiết Kế TĐĐ\Project'
case_dir = os.path.join(root, 'Case study')

# find demag pdf
for fname in os.listdir(case_dir):
    if 'đức' in fname.lower() or 'duc' in fname.lower() or 'demag' in fname.lower():
        p = os.path.join(case_dir, fname)
        doc = fitz.open(p)
        print(f'Demag file: {fname}, pages={len(doc)}')
        for pno in [3, 4, 5, 8, 9, 13]:
            if pno <= len(doc):
                print(f'=== Page {pno} (index {pno-1}) ===')
                print(doc[pno-1].get_text()[:1200])
