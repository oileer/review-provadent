OLD = "https://discord.com/channels/1226995485966073919/1234482277870997536/1503453660162560202"
NEW = "https://dentalsugarhack.com/?hopId=a1cb4e8f-eac3-48da-a782-57d5e8bb4374&hop=antaresss"

files = [
    "C:/Users/eulle/Downloads/review-provadent/index.html",
    "C:/Users/eulle/Downloads/review-provadent/provadent-child/page-provadent-review.php"
]

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace(OLD, NEW)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated:", path)
