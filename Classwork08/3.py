a = list(map(str, input().split()))
count = 0
for word in a:
    if len(word) >= 3:
        if ((word[0] == 'a') and (word[1] == 'b')) or  ((word[-1] == 'a') and (word [-2] =='b')) or (word[0] == 'a') and (word[1] == 'b') and  (word[-1] == 'a') and (word [-2] =='b') :
            count += 1
print(count)