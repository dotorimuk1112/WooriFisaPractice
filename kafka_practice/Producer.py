import pandas as pd
import json
import random
from kafka import KafkaProducer
from kafka.errors import KafkaError
import myconfig

####################################################
######## 추천 영화 리스트 생성(kafka 메시지) ########
####################################################

# 1. 5000개의 영화 데이터를 로드
rawdf = pd.read_csv('C:/Users/CHK/Desktop/kafka/kafka/kafka1/dfs/tmdb_5000_movies.csv')

# 2. 시청 기록이라고 가정하고 5000개 중 100개의 영화 무작위로 추출하여 customer_name.csv로 저장
customer_watchlist = rawdf.sample(n=100)
customer_watchlist.to_csv(f'C:/Users/CHK/Desktop/kafka/kafka/kafka1/dfs/{myconfig.customer_name}.csv', index=False)

# 3. dictionary 형태로 돼있는 장르를 리스트화
customer_watchlist['genres'] = customer_watchlist['genres'].apply(lambda x: json.loads(x.replace("'", "\"")))
all_genres = [genre['name'] for genres in customer_watchlist['genres'] for genre in genres]

# 4. 시청 기록의 최빈 장르를 해당 고객의 최애 장르로 추출
most_watched_genre = max(all_genres, key=all_genres.count)

# 해당 장르에 맞는 영화 목록을 추출
customer_a_favorites = customer_watchlist[customer_watchlist['genres'].apply(
    lambda x: most_watched_genre in [genre['name'] for genre in x])].sort_values(
        by='popularity', ascending=False).head(10)
favorites_filename = f'{myconfig.customer_name}_favorites.csv'
customer_a_favorites.to_csv(f'C:/Users/CHK/Desktop/kafka/kafka/kafka1/fav_dfs/{favorites_filename}', index=False)

##################################################################################################################################

#####################################################
######## 메시지 생성 및 Producer로 메시지 전달 ########
#####################################################

# Kafka producer 설정
producer = KafkaProducer(
    bootstrap_servers=[myconfig.port],
    key_serializer=lambda v: str(v).encode('utf-8'),  # key에 대한 serializer 추가
    value_serializer=lambda v: str(v).encode('utf-8')
)

# 3. Topic은 A, key는 장르, value는 영화 제목 형태의 메시지를 브로커에 저장
try:
    # Send most-watched genre as the key and favorites filename as the value
    producer.send(myconfig.customer_name, key=most_watched_genre, value=favorites_filename)
    print(f"{myconfig.customer_name}님이 가장 좋아하시는 영화를 추출했습니다.")
    print(f"Produced message for customer A: Most-watched genre - {most_watched_genre}, Favorites - {favorites_filename}")
except KafkaError as e:
    print(f"Error while producing message for customer A: {e}")
finally:
    producer.close()