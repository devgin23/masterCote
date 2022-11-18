# 2525

hour, minute = map(int, input().split())
elapsed = int(input())

minute += elapsed

while minute >= 60:
    minute -= 60
    hour += 1
    
if hour >= 24: hour -= 24

print(hour, minute)