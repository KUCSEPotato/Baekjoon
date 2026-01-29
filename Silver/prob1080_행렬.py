# ---------------------------------------------------------------------------------------------------- #
# https://www.acmicpc.net/problem/1080
# 문제
# 0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.

# 행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)

# 입력
# 첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.

# 출력
# 첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.
# ---------------------------------------------------------------------------------------------------- #
class RangeError(Exception):
    pass

def operation(A: list[list], row: int, col: int) -> None:
    for row_pos in range(row, row+3):
        for col_pos in range(col, col+3):
            A[row_pos][col_pos] = 1 - A[row_pos][col_pos] # filp

def is_possible(A: list[list], B: list[list], N: int, M: int) -> int:

    if N < 3 or M < 3: return 0 if A == B else -1

    cnt = 0

    for row in range(N-2):
        for col in range(M-2):
            if A[row][col] != B[row][col]: 
                operation(A=A, row=row, col=col)
                cnt +=1
        
        if A == B: return cnt
    
    if A != B: return -1

def main():
    N, M = map(int, input().split())

    matrix_A = []
    matrix_B = []

    # Matrix A
    for _ in range(N):
        row = list(map(int, input().strip()))
        
        if len(row) != M:
            raise RangeError(f"Row's Length is out of Range!: Row Length -> {len(row)}")

        matrix_A.append(row)

    # Matrix B
    for _ in range(N):
        row = list(map(int, input().strip()))

        if len(row) != M:
            raise RangeError(f"Row's Length is out of Range!: Row Length -> {len(row)}")
        
        matrix_B.append(row)


    print(is_possible(A=matrix_A, B=matrix_B, N=N, M=M))
    

if __name__ == "__main__":
    main()