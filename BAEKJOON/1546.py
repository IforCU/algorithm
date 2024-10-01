N = int(input())
scores = list(map(int, input().split()))
newScores = []
maxScore = max(scores)
for i in scores:
    newScores.append(i/maxScore*100)
print(sum(newScores) / len(newScores))