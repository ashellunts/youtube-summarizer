import pytest
from os.path import join
from helpers import read_file, write_file


@pytest.mark.parametrize("video_id", [
    ("x7KedT6uvus"), ("FrMRyXtiJkc"), ("STpbPXW9-pA")
])
@pytest.mark.vcr()
def test_summary_api(test_client, video_id, test_dir_path):
    query_string = {'video_url': f'https://www.youtube.com/watch?v={video_id}'}
    response = test_client.post('/summary', query_string=query_string)
    assert response.status_code == 200
    expected_filename = join(test_dir_path, f"expected/{video_id}_summary.html")
    expected = read_file(expected_filename)
    if expected != response.text:
        actual_path = join(test_dir_path, f"_actual_{video_id}.html")
        write_file(actual_path, response.text)
        assert False, f"The actual response({actual_path}) does not match the expected ({expected_filename})"
