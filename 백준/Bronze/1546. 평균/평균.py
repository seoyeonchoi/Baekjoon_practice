#1546
subject = int(input())
subject_scores = list(map(int, input().split()))
subject_scores.sort(reverse=True)

M = subject_scores[0]
sum_score = 0
for score in subject_scores:
    score = score/M*100
    sum_score += score

mean_score = sum_score / subject
print(mean_score)