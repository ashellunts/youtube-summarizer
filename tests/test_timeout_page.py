import time

def test_timeout_page(test_client):
    duration = 3
    start_time = time.time()
    response = test_client.get(f'/timeout?duration={duration}')
    elapsed_time = time.time() - start_time
    assert response.status_code == 200
    assert response.content_type == 'text/html; charset=utf-8'
    assert f"waited {duration} seconds" == response.text
    assert elapsed_time >= duration
