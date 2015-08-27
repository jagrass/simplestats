from stats import mean 
# do not need to call stats.py

from nose.tools import assert_equal, assert_almost_equal

def test_mean():
        assert_equal(mean([2,4]), 3) 
        # check to see if statment is true
        # nothing will happen if true
# test_mean()

###

def test_float_mean():
        assert_equal(mean([1,2]), 1.5)
        # same idea as above - different answer
        # result in an error
# test_float_mean()

###

def test_neg_mean():
	assert_almost_equal(mean([-2,2,4]), 1.333, places=3)
# test_neg_mean()

