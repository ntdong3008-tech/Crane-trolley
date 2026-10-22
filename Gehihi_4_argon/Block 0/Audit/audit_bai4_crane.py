import sys, os, fitz
sys.stdout.reconfigure(encoding='utf-8')
root = r'D:\Tài liệu học tập\Kỳ 2026.1\Thiết Kế TĐĐ\Project'
p = os.path.join(root, 'Thầy Đỉnh', 'Bài 4.pdf')
doc = fitz.open(p)

for pno in range(42, 55):
    print(f'=== Page {pno+1} ===')
    print(doc[pno].get_text())
