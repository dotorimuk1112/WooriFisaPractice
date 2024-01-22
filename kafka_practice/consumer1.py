import pandas as pd
from kafka import KafkaConsumer
import myconfig
import os.path

# Kafka consumer 설정
consumer = KafkaConsumer(
    myconfig.customer_name,
    bootstrap_servers=[myconfig.port],
    group_id='friend_consumer1',
    auto_offset_reset='earliest',
    enable_auto_commit=False,  # 수동으로 offset을 커밋하도록 설정
    key_deserializer=lambda x: x.decode('utf-8'),
    value_deserializer=lambda x: x.decode('utf-8')
)

# 1. A의 친구인 타 고객이 친구 A가 많이 본 영화를 알고 싶음.
# 2. topic A를 입력하면 친구 A가 가장 많이 본 영화 목록인 A_favorites를 바탕으로 만들어진 메시지를 친구가 받아볼 수 있게 함
for message in consumer:
    most_watched_genre = message.key
    favorites_filename = f'C:/Users/CHK/Desktop/kafka/kafka/kafka1/fav_dfs/{message.value}'

    # 3. 메시지는 print로 터미널에서 확인할 수 있도록 코딩

    # CSV 파일이 존재하는지 확인
    if os.path.isfile(favorites_filename):
        favorites_df = pd.read_csv(favorites_filename)

        # 필요한 정보만 뽑아서 출력 (관객수 상위 10개만)
        print(f'{myconfig.customer_name}님 시청 기록의 최애 장르 중 관객수 상위 10개의 영화 목록입니다.')
        print(f"친구 {myconfig.customer_name}님의 최애 장르는 {most_watched_genre}입니다.")
        print(f"아래는 추천 리스트입니다.")

        top_10_movies = favorites_df.nlargest(10, 'popularity')
        for index, row in top_10_movies.iterrows():
            # 장르 이름, 영화 제목, 관객수 출력
            print(f"Genre: {row['genres']}, Movie Title: {row['original_title']}, Audience: {row['popularity']}")
        
        print("=" * 30)  # 구분을 위해 출력 사이에 줄 추가

        # 수동으로 offset을 커밋
        consumer.commit()
    else:
        print(f"Error: File not found - {favorites_filename}")
