from src import storage


def test_info_page(test_client):
    storage._delete_calls()


    timestamp2 = "2023-07-30 12:24:17"
    storage.add_summary_call(timestamp2)
    storage.add_transcript_call(timestamp2)

    timestamp = "2023-07-29 12:24:17"
    storage.add_summary_call(timestamp)
    storage.add_summary_call(timestamp)
    storage.add_summary_call(timestamp)
    storage.add_transcript_call(timestamp)
    storage.add_transcript_call(timestamp)


    response = test_client.get('/stats')
    assert response.status_code == 200
    assert response.content_type == 'text/html; charset=utf-8'
    assert "2023-07-29: summary 3, transcript 2" in response.text
    assert "2023-07-30: summary 1, transcript 1" in response.text
    assert response.text.index("2023-07-30") < response.text.index("2023-07-29") 
