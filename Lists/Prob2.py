# Problem Statement-> Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up. 


if __name__ == 'Prob.py':
    n = int(input("Enter the number of scores: "))
    arr = map(int, input().split())
    runner_up = list(set(arr))
    runner_up.sort()
    print(runner_up[-2])


