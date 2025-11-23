n=int(input())
y=n//12
m=n%12
if m==0:print(f"{y} лет ровно")
elif y%10==1 and y%100!=11:print(f"{y} год {m} месяцев")
elif 2<=y%10<=4 and(y%100<10 or y%100>=20):print(f"{y} года {m} месяцев")
else:print(f"{y} лет {m} месяцев")