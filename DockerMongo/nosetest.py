import nose 
import acp_times 

start_time = "2018-17-19T00:00:00+00:00"

def test_valid_open():
    assert acp.open_time(150, 200 , start_time) = "2018-17-19T04:25:00+00:00"


def test_invalid_open(): 
    assert acp.open_time(-100, 200 , start_time) = "2018-17-19T02:56:00+00:00"

def test_valid_close():
    assert acp.open_time(100, 200 , start_time) = "2018-17-19T06:40:00+00:00"


def test_invalid_open(): 
    assert acp.open_time(-100, 200 , start_time) = "2018-17-19T06:40:00+00:00"


def test_zero():
	assert acp.open_time(-100, 200 , start_time) = "2018-17-19T00:00:00+00:00"


