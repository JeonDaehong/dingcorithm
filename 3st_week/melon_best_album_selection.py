# Q. 멜론에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 한다. ( 상위 2곡만 뽑으라는 것임. )
# 노래는 인덱스로 구분하며, 노래를 수록하는 기준은 다음과 같다.
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록한다. (단, 각 장르에 속한 노래의재생 수 총합은 모두 다르다.)
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록한다.
# 노래의 장르를 나타내는 문자열 배열 genres 와
# 노래별 재생 횟수를 나타내는 정수 배열 plays 가 주어질 때,
# 베스트 앨범에 들어갈 노래의 인덱스를 순서대로 반환하시오.

# 25.10.07 : 1050 ~ 1113
# 한 번 더 풀어 볼 필요성이 있음.
def get_melon_best_album(genre_array, play_array):
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}

    for i in range(len(genre_array)):
        genre = genre_array[i]
        play = play_array[i]
        if genre in genre_total_play_dict:
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])
        else:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]

    # 속한 노래가 많이 재생된 장르 정렬
    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)

    result = []
    for genre, play in sorted_genre_play_array:
        # 장르 내에서 많이 재생된 노래 순서로 정렬
        sorted_genre_index_play_array = sorted(genre_index_play_array_dict[genre], key=lambda item: item[1], reverse=True)
        # 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래 정렬
        # ( => 이 부분은, sorted 함수 자체가 안정 정렬이기 때문에, 할 필요 없음. => 만약 고유 번호가 높은 순서였으면, 해줬어야 함.)
        genre_song_count = 0
        for index, play in sorted_genre_index_play_array:
            if genre_song_count >= 2:
                break
            result.append(index)
            genre_song_count += 1

    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))