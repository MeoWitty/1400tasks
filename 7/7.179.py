max_zhiteley = 0
kvartira_max = 0
while True:
    kvartira = int(input())
    if kvartira == 0:
        break
    zhiteley = int(input())
    if zhiteley > max_zhiteley:
        max_zhiteley = zhiteley
        kvartira_max = kvartira
print(kvartira_max)