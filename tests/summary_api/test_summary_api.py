import pytest
from os.path import join
from helpers import read_file


@pytest.mark.parametrize("video_id", [
    ("x7KedT6uvus"), ("FrMRyXtiJkc"), ("STpbPXW9-pA")
])
@pytest.mark.vcr()
def test_make_summary(test_client, video_id, test_dir_path):
    query_string = {'video_url': f'https://www.youtube.com/watch?v={video_id}'}
    response = test_client.post('/summary', query_string=query_string)
    assert response.status_code == 200
    expected = read_file(join(test_dir_path, f"expected/{video_id}_summary.html"))
    assert expected == response.text