if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    maxnum = float('-inf')
    runner = float('-inf')
    for score in arr:
        if score > maxnum:
            runner = maxnum
            maxnum = score
        elif score > runner and score != maxnum:
            runner = score
    print(runner)
    


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna