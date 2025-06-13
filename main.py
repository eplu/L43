from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

def generate_fibonacci(n: int) -> List[int]:
    """
    產生費波那契數列到指定數目。
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_fib)
        return fib_sequence

@app.get("/fibonacci/{count}", response_model=List[int])
def get_fibonacci_sequence(count: int):
    """
    接收一個正整數 `count`，並返回該數目的費波那契數列。
    例如：
    - 輸入 1 得到 [0]
    - 輸入 2 得到 [0, 1]
    - 輸入 5 得到 [0, 1, 1, 2, 3]
    """
    if count <= 0:
        raise HTTPException(
            status_code=400,
            detail="請輸入一個大於零的正整數。"
        )

    return generate_fibonacci(count)
