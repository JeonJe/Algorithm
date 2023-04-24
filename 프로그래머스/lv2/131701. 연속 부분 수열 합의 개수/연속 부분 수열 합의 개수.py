def solution(elements):
    N = len(elements)
    elements *= 2
    return len(set(sum(elements[j:j+n]) for j in range(N) for n in range(1, N+1)))