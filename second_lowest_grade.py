ml = []
scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    ml.append([name, score])
    scores.append(score) 
scores_sorted = sorted(set(scores))
second_lowest = scores_sorted[1] if len(scores_sorted)> 1 else scores_sorted[0]
answers = []
for i in ml:
    if second_lowest == i[1]:
        answers.append(i[0])
answer = sorted(answers)
print("\n".join(answer))