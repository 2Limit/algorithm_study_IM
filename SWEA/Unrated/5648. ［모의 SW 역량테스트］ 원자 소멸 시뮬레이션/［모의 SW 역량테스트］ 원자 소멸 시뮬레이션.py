T = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for tc in range(1, T + 1):
    N = int(input())
    atoms = []
    for _ in range(N):
        x, y, d, k = map(int, input().split())
        atoms.append([x * 2, y * 2, d, k])

    answer = 0
    while atoms:
        pos_map = {}

        for x, y, d, k in atoms:
            nx = x + dx[d]
            ny = y + dy[d]

            if -2000 <= nx <= 2000 and -2000 <= ny <= 2000:
                if (nx, ny) not in pos_map:
                    pos_map[(nx, ny)] = []
                pos_map[(nx, ny)].append((nx, ny, d, k))

        atoms = []
        for pos in pos_map:
            if len(pos_map[pos]) >= 2:
                for atom in pos_map[pos]:
                    answer += atom[3]
            else:
                atoms.append(pos_map[pos][0])

    print(f"#{tc} {answer}")