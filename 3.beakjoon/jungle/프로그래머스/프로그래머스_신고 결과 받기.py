from collections import defaultdict 
def solution(id_list, report, k):
    repoted_info = defaultdict(list)
    repoter_info = defaultdict(list)
    
    #신고당한사람 - 신고한사람 리스트
    for i in range(len(report)):
        reporter, reported = report[i].split()
        
        if reported not in repoter_info[reporter]:
            repoter_info[reporter].append(reported)

        if reporter not in repoted_info[reported]:
            repoted_info[reported].append(reporter)
    
    #key는 신고당한사람, value는 신고한사람
    #몇번 신고당했는지 카운트
    nums = defaultdict(int)
    for key, value in repoted_info.items():
        nums[key] += len(value)
    
    #key는 신고한사람, value는 신고당한 사람들
    #신고당한 사람이 정지상태이면 신고한사람 받은메일 1개 추가
    reporting = defaultdict(int)
    for key,value in repoter_info.items():
        for v in value:
            if nums[v] >= k:
                reporting[key] += 1 

    ans = []
    for i in id_list:
        ans.append(reporting[i])

    return ans

# id_lsit = ["muzi", "frodo", "apeach", "neo"]
id_lsit = ["con", "ryan"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2
print(solution(id_lsit,report,k))