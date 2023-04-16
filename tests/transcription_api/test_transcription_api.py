import pytest
from os.path import join
from helpers import read_file, write_file


@pytest.mark.vcr()
def test_transcription_api(test_client, test_dir_path):
    video_id = "JzPfMbG1vrE"
    query_string = {'video_url': f'https://www.youtube.com/watch?v={video_id}'}
    response = test_client.post('/transcription', query_string=query_string)
    assert response.status_code == 200
    expected = read_file(join(test_dir_path, f"expected.html"))
    if expected != response.text:
        write_file(join(test_dir_path, f"_actual.html"), response.text)
        assert False, "The actual response does not match the expected response. See actual.html for details."
