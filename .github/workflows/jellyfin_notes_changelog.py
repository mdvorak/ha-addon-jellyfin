import re

with open('CHANGELOG.md') as f:
    content = f.read()
with open('/tmp/jellyfin_notes.md') as f:
    notes = f.read().strip()

# Insert after the first version entry, before the second
entries = list(re.finditer(r'^#{1,2} \[', content, re.MULTILINE))
if len(entries) >= 2:
    pos = entries[1].start()
    new_content = content[:pos].rstrip() + '\n\n' + notes + '\n\n' + content[pos:]
else:
    new_content = content.rstrip() + '\n\n' + notes + '\n'

with open('CHANGELOG.md', 'w') as f:
    f.write(new_content)
