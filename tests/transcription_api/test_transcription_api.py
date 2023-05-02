import pytest
from os.path import join
from helpers import read_file, write_file
from src import storage
from datetime import datetime


@pytest.mark.vcr()
def test_transcription_api(test_client, test_dir_path):
    storage._delete_calls()

    response = test_client.get('/info')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.json == {}

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

    response = test_client.get('/info')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert len(response.json) == 1
    value = response.json["1"]
    assert ",get_transcript" in value
    timestamp_recorded = value.replace(",get_transcript", "")
    timestamp_recorded = datetime.strptime(timestamp_recorded, "%Y-%m-%d %H:%M:%S")
    timestamp_now = datetime.now()
    diff_in_seconds = (timestamp_now - timestamp_recorded).total_seconds()
    assert diff_in_seconds < 3
    storage._delete_calls()
