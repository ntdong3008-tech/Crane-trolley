import sys, os, fitz
sys.stdout.reconfigure(encoding='utf-8')
root = r'D:\Tài liệu học tập\Kỳ 2026.1\Thiết Kế TĐĐ\Project'

for fname, code in [
    ('Tai_lieu_du_an\\PRD .pdf', 'R6'),
    ('Tai_lieu_du_an\\SOW_HungNB.docx.pdf', 'R7'),
    ('Tai_lieu_du_an\\BTL-TKTDD-Nhóm-4.pdf', 'R8')
]:
    p = os.path.join(root, fname)
    if os.path.exists(p):
        doc = fitz.open(p)
        print(f'=== {code}: {fname} ({len(doc)} pages) ===')
        for i in range(min(5, len(doc))):
            t = doc[i].get_text().strip().replace('\n', ' ')
            print(f'  p{i+1}: {t[:150]}')
