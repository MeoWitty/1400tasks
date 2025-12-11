max_zhiteley = 0
kvartira_s_max = 0
while True:
    kvartira = int(input())
    if kvartira == 0:
        break
    zhiteley = int(input())
    if zhiteley > max_zhiteley:
        max_zhiteley = zhiteley
        kvartira_s_max = kvartira
    elif zhiteley == max_zhiteley and kvartira > kvartira_s_max:
        kvartira_s_max = kvartira
print(kvartira_s_max)