import csv
import random
import uuid
from faker import Faker

fake = Faker()

# 고정 개수
NUM_ARTISTS = 20000
NUM_FOLLOWS = 30000
NUM_ALBUMS = 20000
NUM_TRACKS = 30000


def get_image_url(i):
    return f"https://picsum.photos/seed/image{i}/400/300"


# Artist
with open('artist.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'uuid', 'name', 'email', 'link1', 'link2', 'description', 'provider', 'artist_image', 'role',
                     'is_deleted'])
    for i in range(1, NUM_ARTISTS + 1):
        name = fake.user_name()
        provider = random.choice(['google', 'kakao', 'naver']);
        writer.writerow([
            i + 1000,
            str(uuid.uuid4()),
            name,
            name + str(i) + "@" + provider + ".com",
            fake.url(),
            fake.url(),
            fake.text(max_nb_chars=100).replace('\n','  '),
            provider,
            get_image_url(i),
            'ROLE_USER',
            0
        ])

# Follow (follower_id, following_id는 artist의 id)
with open('follow.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'follower_id', 'following_id'])
    for i in range(1, NUM_FOLLOWS + 1):
        follower = random.randint(1 + 1000, NUM_ARTISTS + 1000)
        following = random.randint(1 + 1000, NUM_ARTISTS + 1000)
        while following == follower:
            following = random.randint(1 + 1000, NUM_ARTISTS + 1000)
        writer.writerow([i + 1000, follower, following])

# Album
with open('album.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'uuid', 'title', 'description', 'art_image', 'release_date', 'artist_id', 'is_deleted'])
    for i in range(1, NUM_ALBUMS + 1):
        writer.writerow([
            i + 1000,
            str(uuid.uuid4()),
            fake.sentence(nb_words=3).rstrip('.'),
            fake.text(max_nb_chars=100).replace('\n','  '),
            get_image_url(i + NUM_ARTISTS),
            fake.date_between(start_date='-5y', end_date='today').isoformat(),
            random.randint(1 + 1000, NUM_ARTISTS + 1000),
            0
        ])

# Track
with open('track.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'uuid', 'title', 'lyric', 'track_url', 'duration', 'album_id', 'is_deleted'])
    for i in range(1, NUM_TRACKS + 1):
        writer.writerow([
            i + 1000,
            str(uuid.uuid4()),
            fake.catch_phrase().replace('\n','  '),
            fake.text(max_nb_chars=30).replace('\n','  '),
            fake.url(),
            random.randint(100, 360),  # 초 단위
            random.randint(1 + 1000, NUM_ALBUMS + 1000),
            0
        ])
