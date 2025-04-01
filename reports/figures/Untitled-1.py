
def seconds_to_see_performance(N, heights):
    bhoomi_height = heights[-1]
    seconds = 0
    
    for i in range(N - 2, -1, -1):
        if heights[i] > bhoomi_height:
            seconds += 1
        else:
            break
    
    return seconds

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    N = int(input())
    heights = list(map(int, input().split()))
    
    result = seconds_to_see_performance(N, heights)
    print(result)
