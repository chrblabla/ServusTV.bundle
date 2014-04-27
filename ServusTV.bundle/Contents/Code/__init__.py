STREAM_URL = 'http://servustvhd-i.akamaihd.net/hls/live/205540/servustvhdde/playlist.m3u8'

@handler('/video/servustv', 'ServusTV')
def MainMenu():
  oc = ObjectContainer(no_cache=True)
  oc.add(LiveStream())
  return oc

@route('/video/servustv/play')
def LiveStream(include_container=False):
  vco = VideoClipObject(
    key = Callback(LiveStream, include_container=True),
    rating_key = STREAM_URL,
    title = 'Watch ServusTV',
    thumb = R('icon-default.png'),
    items = [
      MediaObject(
        parts = [
          PartObject(
            key = HTTPLiveStreamURL(STREAM_URL)
          )
        ]
      )
    ]
  )

  if include_container:
    return ObjectContainer(objects=[vco])
  else:
    return vco
