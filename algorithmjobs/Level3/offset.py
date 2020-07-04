# ---------------------------------------------------------------

# 문제 : 5x5 2차원 배열이 주어질 때 
# 어떤 원소가 상하좌우에 있는 원소보다 작을 때 
# 해당 위치에 * 을 표시하는 프로그램을 작성하시오. 
# 경계선에 있는 수는 상하좌우 중 존재하는 원소만을 비교한다.

# 입력 : 5x5 행렬의 정보가 25 개의 수로 주어진다. 각 수는 0 에서 9 사이 수이다.

# 출력 : *를 포함한 행렬을 출력예의 형식으로 출력한다.

# 예제 입력 :
# 3 4 1 4 9
# 2 9 4 5 8
# 9 0 8 2 1
# 7 0 2 8 4
# 2 7 2 1 4

# 예제 출력 :
# 3 4 * 4 9 
# * 9 4 5 8 
# 9 0 8 2 * 
# 7 0 2 8 4 
# * 7 2 * 4 

# ---------------------------------------------------------------

nowX = 0  # X좌표 저장
nowY = 0  # Y좌표 저장

# 5x5 행렬 셋팅
matrix = [[0]*5 for i in range(5)]
matrix = [[int(x) for x in input().split()]for y in range(5)]


for nowY in range(5):
  for nowX in range(5):
  
    now = matrix[nowY][nowX]
    
    if (nowX < 4) :
      right = matrix[nowY][nowX+1]
    else :
      right = 10
      
    if (nowX > 0) :
      left = matrix[nowY][nowX-1]
    else :
      left = 10
      
    if (nowY < 4) :
      bottom = matrix[nowY+1][nowX]
    else :
      bottom = 10
      
    if (nowY > 0) :
      top = matrix[nowY-1][nowX]
    else :
      top = 10
    
    if (now < right and now < top and now < left and now < bottom) :
      print('* ', end='')
    else :
      print(matrix[nowY][nowX], end=' ')
      
    if (nowX == 4):
      print()
