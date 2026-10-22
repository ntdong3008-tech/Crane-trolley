import sys, os
sys.stdout.reconfigure(encoding='utf-8')
root = r'D:\Tài liệu học tập\Kỳ 2026.1\Thiết Kế TĐĐ\Project'
p = os.path.join(root, 'Case study', '07_bai6_shevchenko_kpi2024.md')

with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

for section in text.split('##'):
    if any(k in section.lower() for k in ['cản', 'lực cản', 'ma sát', 'động cơ', 'công suất', 'bánh xe']):
        print('##' + section[:1200])
        print('='*40)
