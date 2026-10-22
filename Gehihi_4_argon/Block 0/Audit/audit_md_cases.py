import sys, os
sys.stdout.reconfigure(encoding='utf-8')
root = r'D:\Tài liệu học tập\Kỳ 2026.1\Thiết Kế TĐĐ\Project'
case_dir = os.path.join(root, 'Case study')

for fname in ['01_bai1_nhat_ban.md', '02_bai2_indonesia.md', '03_bai3_tho_nhi_ky.md', '05_bai4_A54_ieee2024.md', '06_bai5_SM2693_fuzzy_vision.md', '07_bai6_shevchenko_kpi2024.md']:
    p = os.path.join(case_dir, fname)
    if os.path.exists(p):
        print(f'=== {fname} ===')
        with open(p, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # print lines containing numbers or parameters
            for line in lines[:35]:
                print(line.rstrip())
