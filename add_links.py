import re

PRODUCT_URL = "https://discord.com/channels/1226995485966073919/1234482277870997536/1503453660162560202"
REPLACEMENT = f'<strong><a href="{PRODUCT_URL}" style="color:var(--gold);text-decoration:none;" target="_blank" rel="nofollow">ProvaDent</a></strong>'

def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into segments: tags/attributes vs text nodes
    # Replace ProvaDent only outside of HTML tags
    result = []
    i = 0
    while i < len(content):
        if content[i] == '<':
            # Find closing >
            end = content.find('>', i)
            if end == -1:
                result.append(content[i:])
                break
            result.append(content[i:end+1])  # keep tag as-is
            i = end + 1
        else:
            # Text node — find next <
            end = content.find('<', i)
            if end == -1:
                chunk = content[i:]
                result.append(chunk.replace('ProvaDent', REPLACEMENT))
                break
            chunk = content[i:end]
            result.append(chunk.replace('ProvaDent', REPLACEMENT))
            i = end

    return ''.join(result)

for fname in ['index.html', 'provadent-child/page-provadent-review.php']:
    path = f"C:/Users/eulle/Downloads/review-provadent/{fname}"
    new_content = process_file(path)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Done: {fname}")
