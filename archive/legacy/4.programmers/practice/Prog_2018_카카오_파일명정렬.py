from collections import defaultdict 

def find_num_indexs(filename):
    start_idx, end_idx = 0, 0
    find_num = False
    num_cnt = 0
    for j in range(len(filename)):
        if filename[j].isdigit() and not find_num:
            find_num = True
            start_idx,end_idx = j,j
            num_cnt = 1
        elif filename[j].isdigit() and find_num:
            num_cnt+=1
            end_idx = j
            if num_cnt >= 5:
                break
        elif not filename[j].isdigit() and find_num:
            end_idx = j-1
            break 
            
    return [start_idx, end_idx]
    
def solution(files):
    answer = []
    dict = defaultdict(list)
    
    for i in range(len(files)):
        file_name = files[i]
        n_start_idx, n_end_idx = find_num_indexs(file_name)
        HEAD = file_name[:n_start_idx].lower()
        NUMBER = file_name[n_start_idx:n_end_idx+1]
        dict[file_name] = [HEAD,NUMBER,i]
    
    sorted_dict = list(sorted(dict.items(), key= lambda x : (x[1][0],int(x[1][1]))))

    for key, _ in sorted_dict:
        answer.append(key)

    return answer


input = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(input))