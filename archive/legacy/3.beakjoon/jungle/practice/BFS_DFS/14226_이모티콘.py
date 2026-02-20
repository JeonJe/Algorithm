from collections import deque
S = int(input())

visited=dict()
#(화면에서 이모티콘 개수, 클립보드 이모티콘 개수) = 시간
visited[(1,0)] = 0

que = deque()
#화면 이모티콘개수, 클립보드 이모티콘 개수
que.append((1,0))

while que:
    display, clipboard = que.popleft()

    if display == S:
        print(visited[(display,clipboard)])
        exit()
    
    # 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다. (덮어쓰기)
    if (display,display) not in visited.keys():
        visited[(display,display)] = visited[(display,clipboard)] + 1
        que.append((display, display))
    # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
    if (display+clipboard,clipboard) not in visited.keys():
        visited[(display + clipboard, clipboard)] = visited[(display,clipboard)] + 1
        que.append((display+clipboard, clipboard))
    # 3. 화면에 있는 이모티콘 중 하나를 삭제한다.
    if (display-1,clipboard) not in visited.keys():
        visited[(display-1,clipboard)] = visited[(display,clipboard)] + 1
        que.append((display-1,clipboard))
