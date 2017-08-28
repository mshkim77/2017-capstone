from audioManager.models import AudioFile, AudioFeature, SampleAudioFeatures
from django.forms.models import model_to_dict

import tensorflow as tf
import numpy as np

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)


def predict_values(x_data, y_data, x_predict):
    # 트레이닝용 데이터 추출
    X_training = x_data
    Y_training = y_data

    # 텐서플로우 데이터 생성
    x_tensor = tf.placeholder(tf.float32)
    y_tensor = tf.placeholder(tf.float32)

    # 거리 계산 함수 설정 (멘하탄)
    distance = tf.reduce_sum(tf.abs(tf.add(x_tensor, tf.negative(y_tensor))), axis=1)

    # 거리 계산 결과 가장 작은 값(argmin) = 거리가 가장 가까운 값을 반환하도록 설정
    pred = tf.argmin(distance)

    # 텐서플로 변수들 초기화
    init = tf.global_variables_initializer()

    # 텐서플로 시작
    with tf.Session() as sess:
        sess.run(init)

        # 가장 가까운 인덱스 가져오고
        nn_index = sess.run(pred, feed_dict={x_tensor: x_data, y_tensor: x_predict})

        # 그 인덱스의 Y값 반환
        return y_data[nn_index]

# @celery_app.tasks
def knn_tone_emotion_analysis(audio_id):
    audio_obj = AudioFile.objects.get(pk=audio_id)
    audio_features = AudioFeature.objects.get(pk=audio_obj)

    # 전체 가져오기
    all_features = SampleAudioFeatures.objects.all()

    # 각각의 키 생성 (필터용)
    feature_keys = ['duration', 'tempo',
                    'avg_mfcc', 'max_mfcc', 'min_mfcc', 'var_mfcc', 'std_mfcc',
                    'avg_ZCR', 'var_ZCR', 'std_ZCR',
                    'avg_energy', 'max_energy', 'min_energy', 'std_energy',
                    'avg_harmonic', 'avg_harmonic_in_max', 'avg_harmonic_in_min',
                    'diff_avg_harmonic_max', 'diff_avg_harmonic_min', 'diff_avg_harmonic_maxmin']
    emotion_keys = ["rage", "vigilance", "ecstasy", "admiration", "amazement", "terror", "grief", "loathing"]

    # 데이터 추출 (Dict)
    features_arr = []
    emotions_arr = []

    # 딕셔너리 데이터를 어레이로
    for i in range(0, len(all_features)):
        tmp_arr = []
        tmp_model = model_to_dict(all_features[i])
        for j in range(0, len(feature_keys)):
            tmp_arr.append(tmp_model[feature_keys[j]])
        features_arr.append(tmp_arr)

    for i in range(0, len(all_features)):
        tmp_arr = []
        tmp_model = model_to_dict(all_features[i])
        for j in range(0, len(emotion_keys)):
            tmp_arr.append(tmp_model[emotion_keys[j]])
        emotions_arr.append(tmp_arr)

    if len(features_arr) is 0 or len(emotions_arr) is 0:
        return False

    # 그리고 넘파이 배열로 변환
    x_data = np.array(features_arr)
    y_data = np.array(emotions_arr)

    # 감정을 소프트 맥스로 한번 넣어서 정규화
    softmax_y = []
    [softmax_y.append(softmax(elem)) for elem in y_data]

    # 그리고 Y(감정)를 추론할 데이터 추출
    target_for_predict = []
    tmp_target = model_to_dict(audio_features)

    for i in range(0, len(feature_keys)):
        target_for_predict.append(tmp_target[feature_keys[i]])

    # 넘파이 배열로 변환
    x_predict_data = np.array(target_for_predict)

    print("X_Predict_data")
    print(x_predict_data)

    # 결과가 저장 될 배열 생성
    predict_results = []

    # 그리고 각각의 감정에 대해 루프
    for i in range(0, len(y_data[0])):
        filtered_y = []
        [filtered_y.append(elem[i]) for elem in softmax_y]
        predict_results.append(predict_values(x_data, filtered_y, x_predict_data))

    # 그리고 결과 값 업데이트
    audio_features.rage = predict_results[0]
    audio_features.vigilance = predict_results[1]
    audio_features.ecstasy = predict_results[2]
    audio_features.admiration = predict_results[3]
    audio_features.amazement = predict_results[4]
    audio_features.terror = predict_results[5]
    audio_features.grief = predict_results[6]
    audio_features.loathing = predict_results[7]

    audio_features.save()

    print("추론 결과")
    print(predict_results)

    return True
