import calcstats


def test_num_friends_length():
    """ testing length of data, expecting 204 """
    assert len(num_friends) == 204, "expects the data to have 203 entires"


def test_count_nums():
    """ testing integer counter """
    assert calcstats.count_nums([1, 1, 2]) == {1: 2, 2: 1}, "returns a list of ints"


def test_pad_w_zeros():
    """ testing padding counter with zeros """
    padded_num_friends = tuple(calcstats.pad_w_zeros(calcstats.count_nums(num_friends)))
    assert (
        len(padded_num_friends) == 100 + 1
    ), "length is max of the numbers plus the zero"
    assert padded_num_friends[0] == 0, "has 0 zeros"
    assert padded_num_friends[1] == 22, "has 22 ones"
    assert padded_num_friends[49] == 1, "has 1 forty-nine"


def test_mean():
    """mean yields a resonable mean"""
    assert 7.33 < calcstats.mean(num_friends) < 7.34


def test_median():
    """median func yields the median"""
    assert calcstats.median([1, 10, 2, 9, 5]) == 5
    assert calcstats.median([1, 9, 2, 10]) == (2 + 9) / 2
    assert calcstats.median(num_friends) == 6


def test_quantile():
    """quantil func yields quantiles"""
    assert calcstats.quantile(num_friends, 0.10) == 1
    assert calcstats.quantile(num_friends, 0.25) == 3
    assert calcstats.quantile(num_friends, 0.75) == 9
    assert calcstats.quantile(num_friends, 0.90) == 13


def test_mode():
    """mode func returns most common values"""
    assert set(calcstats.mode(num_friends)) == {1, 6}


def test_data_range():
    """data range func returns the range"""
    assert calcstats.data_range(num_friends) == 99


num_friends = [
    100.0,
    49,
    41,
    40,
    25,
    21,
    21,
    19,
    19,
    18,
    18,
    16,
    15,
    15,
    15,
    15,
    14,
    14,
    13,
    13,
    13,
    13,
    12,
    12,
    11,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    8,
    8,
    8,
    8,
    8,
    8,
    8,
    8,
    8,
    8,
    8,
    8,
    8,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
]

