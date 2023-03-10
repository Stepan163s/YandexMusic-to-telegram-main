import os

from yandex_music import Client


client = Client('token').init()


queues = client.queues_list()
last_queue = client.queue(queues[0].id)
last_track_id = last_queue.get_current_track()
last_track = last_track_id.fetch_track()
artists = ', '.join(last_track.artists_name())
title = last_track.title
print(f'{artists} - {title}')

