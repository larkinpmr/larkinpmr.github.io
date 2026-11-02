"""Keep the public saved copy (data/snapshot.json) free of private data.

data/snapshot.json is served publicly by GitHub Pages, so it holds only content that is fine for anyone to read:
the academic year, the rotation list (names, codes, groups; no guide text), the note templates and the
"read this first" note. Residents, schedules, didactics, contacts, links, guide and policy text all come from
Google after sign-in (and are cached on each signed-in device).

Run directly to trim the file in place:  python3 tools/trim_snapshot.py
The other tools call trim() before they write, so private data can't creep back in.
"""
import json, os

ROT_KEEP = ('id', 'title', 'short', 'codes', 'handbookMatch', 'category', 'pgy', 'type', 'location')
POL_KEEP = ('id', 'title', 'handbookMatch')


def trim(snap):
    out = {k: snap[k] for k in ('academicYear', 'builtFrom', 'builtAt', 'months', 'readinessHtml', 'templates') if k in snap}
    out['rotations'] = [dict({k: r[k] for k in ROT_KEEP if k in r}, html='', handbookHtml='', attachments=[], source='handbook') for r in snap.get('rotations', [])]
    out['policies'] = [dict({k: p[k] for k in POL_KEEP if k in p}, html='', source='handbook', attachments=[]) for p in snap.get('policies', [])]
    out.update(guides=[], residents=[], didactics=[], contacts=[], links=[], announcements=[], subpages=[], public=True)
    return out


if __name__ == '__main__':
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'snapshot.json')
    snap = json.load(open(path, encoding='utf-8'))
    before = os.path.getsize(path)
    json.dump(trim(snap), open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'trimmed {path}: {before // 1024} KB -> {os.path.getsize(path) // 1024} KB')
