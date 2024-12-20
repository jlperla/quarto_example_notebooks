import jsonargparse
def example(M: int = 2,
    sigma: float = 0.0001):
    print(M * sigma)

if __name__ == "__main__":
    jsonargparse.CLI(example)