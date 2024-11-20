from watch import parse

def test_valid_embed_url():
    html = '<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
    assert parse(html) == "https://youtu.be/xvFZjo5PgG0"

def test_valid_embed_url_with_http():
    html = '<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>'
    assert parse(html) == "https://youtu.be/xvFZjo5PgG0"

def test_valid_embed_url_with_www():
    html = '<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
    assert parse(html) == "https://youtu.be/xvFZjo5PgG0"

def test_no_iframe():
    html = '<div>No iframe here</div>'
    assert parse(html) == None

def test_no_youtube_url():
    html = '<iframe src="https://vimeo.com/123456"></iframe>'
    assert parse(html) == None
