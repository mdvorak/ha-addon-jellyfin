import re

with open('/tmp/pr_body.txt') as f:
    body = f.read()
with open('/tmp/jellyfin_notes.md') as f:
    notes = f.read().strip()

div_id = 'jellyfin-server-footer'
new_footer = f'<div id="{div_id}">\n\n{notes}\n\n</div>'
pattern = re.compile(
    r'<div\s+id=["\']' + re.escape(div_id) + r'["\']>.*?</div>',
    re.DOTALL
)
if pattern.search(body):
    updated = pattern.sub(new_footer, body)
    print('Replaced footer div.')
else:
    updated = body.rstrip() + '\n\n' + new_footer + '\n'
    print('Appended footer div.')

with open('/tmp/pr_body_new.txt', 'w') as f:
    f.write(updated)
