def solution(plans):
    answer = []
    stack = []

    tasks = []
    for name, start, playtime in plans:
        h, m = map(int, start.split(":"))
        start_min = h * 60 + m
        tasks.append((start_min, name, int(playtime)))
    
    tasks.sort()
    
    for i in range(len(tasks) - 1):
        start, name, playtime = tasks[i]
        next_start = tasks[i + 1][0]

        available = next_start - start

        # 다음 과제 시작 전에 끝낼 수 있는 경우
        if playtime <= available:
            answer.append(name)
            remain = available - playtime

            # 남은 시간 동안 중단된 과제 재개
            while stack and remain > 0:
                prev_name, prev_time = stack.pop()

                if prev_time <= remain:
                    answer.append(prev_name)
                    remain -= prev_time
                else:
                    stack.append((prev_name, prev_time - remain))
                    break

        # 다음 과제 시작 때문에 중단되는 경우
        else:
            stack.append((name, playtime - available))

    # 마지막으로 시작하는 과제 완료
    answer.append(tasks[-1][1])

    # 중단된 과제를 최근 것부터 완료
    while stack:
        name, remain = stack.pop()
        answer.append(name)
    
    
    return answer