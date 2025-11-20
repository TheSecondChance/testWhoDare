import time
import pytest
from time_checker import TimeChecker

def test_time_checker_basic():
	tc = TimeChecker()
	tc.start()
	time.sleep(0.1)
	elapsed = tc.elapsed()
	assert elapsed >= 0.1
	tc.reset()
	time.sleep(0.05)
	elapsed2 = tc.elapsed()
	assert elapsed2 >= 0.05

def test_time_checker_not_started():
	tc = TimeChecker()
	with pytest.raises(ValueError):
		tc.elapsed()
def test_time_checker_multiple_starts():
	tc = TimeChecker()
	tc.start()
	time.sleep(0.1)
	elapsed1 = tc.elapsed()
	time.sleep(0.1)
	elapsed2 = tc.elapsed()
	assert elapsed2 >= elapsed1