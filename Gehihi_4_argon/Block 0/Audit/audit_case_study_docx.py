import sys, os, docx
sys.stdout.reconfigure(encoding='utf-8')
root = r'D:\Tài liệu học tập\Kỳ 2026.1\Thiết Kế TĐĐ\Project'

# check Case_study.docx
p_docx = os.path.join(root, 'Case study', 'Case_study.docx')
doc = docx.Document(p_docx)
print('=== Case_study.docx Sample ===')
for i, p in enumerate(doc.paragraphs):
    if any(k in p.text.lower() for k in ['ma sát', 'cản lăn', 'mu =', 'μ', 'công suất', 'bánh xe', 'hệ số']):
        print(f'P{i+1}: {p.text.strip()}')

# check 04_tong_hop_so_sanh.md
p_md = os.path.join(root, 'Case study', '04_tong_hop_so_sanh.md')
if os.path.exists(p_md):
    with open(p_md, 'r', encoding='utf-8') as f:
        print('=== 04_tong_hop_so_sanh.md (first 1000 chars) ===')
        print(f.read()[:1000])
