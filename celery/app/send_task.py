from app import fibonacci

if __name__ == "__main__":
    n = 35
    result = fibonacci.delay(n)
    print(f"Task result: {result.get(timeout=1800)}")
