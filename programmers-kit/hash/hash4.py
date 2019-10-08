def solution(genres, plays):
    play_dictionary = dict()
    genres = [(genre, i) for i, genre in enumerate(genres)]
    genres = [(play, *genre) for genre, play in zip(genres, plays)]
    genres.sort(key=lambda x: x[0], reverse=True)
    answer = list()

    for genre in genres:
        if genre[1] not in play_dictionary:
            play_dictionary[genre[1]] = genre[0]
        else:
            play_dictionary[genre[1]] += genre[0]

    play_dictionary = sorted(play_dictionary, key=lambda x: play_dictionary[x], reverse=True)

    for key in play_dictionary:
        count = 0
        for genre in genres:
            if key == genre[1] and count < 2:
                answer.append(genre[2])
                count += 1

    return answer

    print(genres)
    print(play_dictionary)