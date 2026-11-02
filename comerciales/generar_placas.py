# -*- coding: utf-8 -*-
"""Genera los JPG que falten: por cada comerciales/placas/AAAA-MM-DD-HHMM-*.py sin su .jpg en comerciales/posts/."""
import os, re, subprocess, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
PLACAS, POSTS = os.path.join(AQUI, 'placas'), os.path.join(AQUI, 'posts')
hechas = 0
for f in sorted(os.listdir(PLACAS)):
    base, ext = os.path.splitext(f)
    if ext == '.py' and re.match(r'^\d{4}-\d{2}-\d{2}-\d{4}-', base) and not os.path.exists(os.path.join(POSTS, base + '.jpg')):
        subprocess.run([sys.executable, f], cwd=PLACAS, check=True)
        hechas += 1
print(f'Placas generadas: {hechas}')
