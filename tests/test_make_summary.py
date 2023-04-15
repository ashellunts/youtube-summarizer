from src import summary


def _test_make_summary():
    s = summary.make("Hello my name is Alex and I am software engineer. I make apps and sites.")
    assert "software engineer" in s and len(s) > 100
