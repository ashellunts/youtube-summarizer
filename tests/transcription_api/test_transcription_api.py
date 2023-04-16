import pytest
from os.path import join
from helpers import read_file, write_file


@pytest.mark.vcr()
def test_transcription_api(test_client, test_dir_path):
    video_id = "JzPfMbG1vrE"
    query_string = {'video_url': f'https://www.youtube.com/watch?v={video_id}'}
    response = test_client.post('/transcription', query_string=query_string)
    assert response.status_code == 200
    expected_filename = join(test_dir_path, f"expected.html")
    expected = read_file(expected_filename)
    if expected != response.text:
        actual_filename = join(test_dir_path, f"_actual.html")
        write_file(actual_filename, response.text)
        assert False, f"The actual response {actual_filename} does not match the expected {expected_filename}. See actual.html for details."
