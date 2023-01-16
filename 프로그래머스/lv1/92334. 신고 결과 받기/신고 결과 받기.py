from collections import defaultdict 
def solution(id_list, report, k):
    answer = defaultdict(int)
    ans = []
    nums = defaultdict(int)
    repo_info = defaultdict(list)
    repo = defaultdict(list)
    
    #신고당한사람 - 신고한사람 리스트
    for i in range(len(report)):
        reporter, reported = report[i].split()
        
        if reported not in repo[reporter]:
            repo[reporter].append(reported)

        if reporter not in repo_info[reported]:
            repo_info[reported].append(reporter)
    
    #key는 신고당한사람, value는 신고한사람
    for key, value in repo_info.items():
        nums[key] += len(value)
    
    for key,value in repo.items():
        for v in value:
            if nums[v] >= k:
                answer[key] += 1 

    for i in id_list:
        ans.append(answer[i])
    return ans