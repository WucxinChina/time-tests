from times import compute_overlap_time, time_range

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected

def test_no_overlap():
    range1 = time_range("2024-01-01 10:00:00", "2024-01-01 11:00:00")
    range2 = time_range("2024-01-01 12:00:00", "2024-01-01 13:00:00")
    expected = []  # No overlap expected
    assert compute_overlap_time(range1, range2) == expected

def test_multiple_intervals_overlap():
    range1 = time_range("2024-01-01 10:00:00", "2024-01-01 11:00:00", 2, 300)  # Two intervals with a 5-minute gap
    range2 = time_range("2024-01-01 10:30:00", "2024-01-01 11:30:00", 2, 300)  # Two intervals with a 5-minute gap
    expected = [
        ("2024-01-01 10:30:00", "2024-01-01 10:52:30"),
        ("2024-01-01 10:57:30", "2024-01-01 11:00:00")
    ]  # Expected overlap intervals
    assert compute_overlap_time(range1, range2) == expected

def test_touching_ranges_no_overlap():
    range1 = time_range("2024-01-01 10:00:00", "2024-01-01 11:00:00")
    range2 = time_range("2024-01-01 11:00:00", "2024-01-01 12:00:00")
    expected = []  # No overlap as they only touch at the end
    assert compute_overlap_time(range1, range2) == expected