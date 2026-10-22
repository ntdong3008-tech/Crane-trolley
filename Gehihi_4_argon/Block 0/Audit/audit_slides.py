import sys, os, fitz
sys.stdout.reconfigure(encoding='utf-8')
root = r'D:\Tài liệu học tập\Kỳ 2026.1\Thiết Kế TĐĐ\Project'
thay_dinh = os.path.join(root, 'Thầy Đỉnh')

for fname in ['Bài 3.pdf', 'Bài 4.pdf']:
    doc = fitz.open(os.path.join(thay_dinh, fname))
    print(f'=== Hits in {fname} ===')
    for pno in range(len(doc)):
        t = doc[pno].get_text()
        for kw in ['cầu trục', 'xe con', 'di chuyển', 'lăn', 'ma sát', 'bánh xe', 'cản', 's3']:
            if kw in t.lower():
                print(f'  Page {pno+1}: contains "{kw}"')
                for line in t.split('\n'):
                    if kw in line.lower():
                        print(f'    {line.strip()[:100]}')
                break
