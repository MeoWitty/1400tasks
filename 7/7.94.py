n = int(input())
count_max = 0
pred_pred = 0
pred = 0
for i in range(n):
    tek = int(input())
    if i >= 2:
        if pred > pred_pred and pred > tek:
            count_max += 1
    pred_pred = pred
    pred = tek
print(count_max)