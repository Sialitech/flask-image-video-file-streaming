# flask-image-video-file-streaming

1. run `pip install -r requirements-opencv.txt`
2. Change port in `app.py`.
3. Place images/video in a folder.
4. create environment variables:
   1. `VOLUME_PATH` path to files folder.
   2. `SRC` value should be `"images"` or `"video"`.
5. run `python app.py`

## CREDIT TO

 Article [video streaming with Flask](http://blog.miguelgrinberg.com/post/video-streaming-with-flask) and its follow-up [Flask Video Streaming Revisited](http://blog.miguelgrinberg.com/post/flask-video-streaming-revisited).
