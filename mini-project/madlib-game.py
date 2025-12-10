
place = input("Một nơi chốn: ")
who = input("Một người/nhân vật: ")
adjective = input("Một tính từ : ")
clothing_item = input("Một món quần áo: ")
noun = input("Một danh từ : ")
feeling = input("Một cảm xúc : ")
verb = input("Một động từ nguyên mẫu: ")

story = f"""
today, when i went to {place} i saw {who}.
{who} was/were wearing a really {adjective} {clothing_item} and carrying a {noun}.
i was so {feeling} that i decided to {verb} right in front of them!
"""

print(story)
