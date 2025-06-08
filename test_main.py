from main import is_prime, fibonacci
import pytest

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(4) is False
    assert is_prime(17) is True

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5

@pytest.mark.benchmark
def test_fibonacci_benchmark(benchmark):
    result = benchmark(fibonacci, 20)
    assert result > 0
