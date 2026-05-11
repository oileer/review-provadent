import re

PRODUCT_URL = "https://discord.com/channels/1226995485966073919/1234482277870997536/1503453660162560202"
LINK = f'<strong><a href="{PRODUCT_URL}" style="color:var(--gold);text-decoration:none;" target="_blank" rel="nofollow">ProvaDent</a></strong>'

files = [
    'C:/Users/eulle/Downloads/review-provadent/index.html',
    'C:/Users/eulle/Downloads/review-provadent/provadent-child/page-provadent-review.php'
]

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Restore plain ProvaDent inside <title> tags
    def fix_title(m):
        return m.group().replace(LINK, 'ProvaDent')
    content = re.sub(r'<title>.*?</title>', fix_title, content, flags=re.DOTALL)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed:', path)
