import re

f = open("sitemap-cs.xml", "r")
res = f.readlines()
ls = []
for d in res:
    data = re.findall(r"<loc>.*</loc>", d)
    ls.extend(
        [
            print(
                i.replace("<loc>", "").replace("</loc>", ""),
                file=open("links.txt", "a+"),
            )
            for i in data
            if "repair-center" in i
        ]
    )
print(len(ls))
