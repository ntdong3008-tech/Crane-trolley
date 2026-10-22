import sys, os, fitz, docx
sys.stdout.reconfigure(encoding='utf-8')
root = r'D:\Tài liệu học tập\Kỳ 2026.1\Thiết Kế TĐĐ\Project'
case_dir = os.path.join(root, 'Case study')

for fname in sorted(os.listdir(case_dir)):
    p = os.path.join(case_dir, fname)
    if fname == 'tcvn-4244-2005.pdf':
        continue
    print(f'==============================')
    print(f'FILE: {fname}')
    if fname.lower().endswith('.pdf'):
        try:
            doc = fitz.open(p)
            print(f'Pages: {len(doc)}')
            for i in range(min(2, len(doc))):
                t = doc[i].get_text().strip()
                lines = [l.strip() for l in t.split('\n') if l.strip()]
                print(f'-- Page {i+1} lines (first 5): {lines[:5]}')
        except Exception as e:
            print(f'Error reading PDF: {e}')
    elif fname.lower().endswith('.docx'):
        try:
            d = docx.Document(p)
            print(f'DOCX paragraphs: {len(d.paragraphs)}')
            for p_idx, para in enumerate(d.paragraphs[:5]):
                if para.text.strip():
                    print(f'-- Para {p_idx+1}: {para.text.strip()}')
        except Exception as e:
            print(f'Error reading DOCX: {e}')
