import os, sys, fitz
sys.stdout.reconfigure(encoding='utf-8')

root = r'D:\Tài liệu học tập\Kỳ 2026.1\Thiết Kế TĐĐ\Project'
nasa_path = os.path.join(root, r'Tai_lieu_tham_khao\NASA_SP-2007-6105_Rev_1.pdf')
doc = fitz.open(nasa_path)

# Let's inspect TOC pages (pages 5 to 15)
for i in range(5, 16):
    text = doc[i].get_text()
    if 'Table of Contents' in text or 'Stakeholder' in text or 'Requirements' in text:
        print(f'=== PDF Page {i+1} ===')
        print(text[:1500])
