import sys, os, fitz, docx
sys.stdout.reconfigure(encoding='utf-8')
root = r'D:\Tài liệu học tập\Kỳ 2026.1\Thiết Kế TĐĐ\Project'
case_dir = os.path.join(root, 'Case study')

for fname in sorted(os.listdir(case_dir)):
    p = os.path.join(case_dir, fname)
    if fname == 'tcvn-4244-2005.pdf':
        continue
    if fname.lower().endswith('.pdf'):
        try:
            doc = fitz.open(p)
            num_pages = len(doc)
            sample_text = ''
            for i in range(min(5, num_pages)):
                sample_text += doc[i].get_text() + ' '
            status = 'Text OK' if len(sample_text.strip()) > 200 else ('Scan/Little text' if len(sample_text.strip()) < 50 else 'Partial')
            print(f'=== {fname} ({num_pages} pages, status={status}) ===')
            # Look for keywords across all pages
            hits = {}
            for i, page in enumerate(doc):
                t = page.get_text()
                for kw in ['trolley', 'crab', 'xe con', 'speed', 'tốc độ', 'velocity', 'motor', 'động cơ', 'power', 'công suất', 'mass', 'weight', 'khối lượng', 'wheel', 'bánh xe', 'friction', 'ma sát', 'cản lăn']:
                    if kw in t.lower() and kw not in hits:
                        hits[kw] = (i+1, t[:300].replace('\n', ' '))
            print('  Keywords found on pages:', {k: v[0] for k, v in hits.items()})
        except Exception as e:
            print(f'=== {fname}: Error {e} ===')
    elif fname.lower().endswith('.docx'):
        try:
            d = docx.Document(p)
            text = ' '.join([para.text for para in d.paragraphs])
            print(f'=== {fname} (DOCX, len={len(text)} chars) ===')
            print('  Sample:', text[:300])
        except Exception as e:
            print(f'=== {fname}: Error {e} ===')
