import numpy as np
import sys, time, librosa

def stZCR(frame):
    count = len(frame)
    countZ = np.sum(np.abs(np.diff(np.sign(frame)))) / 2
    return (np.float64(countZ) / np.float64(count-1.0))

def stEnergy(frame):
    return np.sum(frame ** 2) / np.float64(len(frame))

def feature_extraction(filename):
    start_point = time.time()
    print("== 파일 " + filename + " 처리 시작.")

    # 데이터 모노로 로드
    data, rate = librosa.core.load(filename, mono=True)

    # 44100Hz로 리샘플링
    librosa.core.resample(data, rate, 44100)
    rate = 44100

    # 전체 길이 가져오기
    duration = librosa.core.get_duration(y=data, sr=rate)
    print("전체 길이: " + str(round(duration, 2)) + " 초")

    # 템포 추출
    onset_env = librosa.onset.onset_strength(y=data, sr=rate)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=rate)
    print("템포: " + str(round(tempo[0], 2)) + " bpm")

    # MFCC 추출
    mfcc = librosa.feature.mfcc(y=data, sr=rate)
    avg_mfcc = np.mean(mfcc)
    max_mfcc = np.amax(mfcc)
    min_mfcc = np.amin(mfcc)
    var_mfcc = np.var(mfcc)
    std_mfcc = np.std(mfcc)
    print("MFCC 평균: " + str(avg_mfcc) + " 최대 MFCC: " + str(max_mfcc) + " 최소 MFCC:" + str(min_mfcc))
    print("MFCC 분산: " + str(var_mfcc) + " MFCC 표준편차: " + str(std_mfcc))

    # 데이터를 프레임으로 분할
    data_frames = librosa.util.frame(data, frame_length=4096, hop_length=1024)

    # Zero Crossing Rate 구하기
    ZCRs = []
    [ZCRs.append(stZCR(frame)) for frame in data_frames]
    avg_ZCR = np.mean(ZCRs)
    var_ZCR = np.var(ZCRs)
    std_ZCR = np.std(ZCRs)
    print("평균 Zero Crossing Rate: " + str(avg_ZCR) + " ZCR 분산:" + str(var_ZCR) + " ZCR 표준편차: " + str(std_ZCR))

    # Energy 구하기
    energies = []
    [energies.append(stEnergy(frame)) for frame in data_frames]
    avg_energy = np.mean(energies)
    max_energy = np.amax(energies)
    min_energy = np.amin(energies)
    std_energy = np.std(energies)
    print("평균 에너지: " + str(avg_energy) + " 최대 에너지: " + str(max_energy) + " 최소 에너지: " + str(min_energy) + " 에너지 표준편차: " + str(std_energy))

    # 최대 에너지 포인트의 인덱스 및 데이터 가져오기 (해당 프레임에서 특징을 추출하기 위해)
    max_energy_idx = np.argmax(energies)
    max_energy_frame = librosa.core.frames_to_time(data_frames[max_energy_idx], rate, hop_length=1024)

    # 최소 에너지 포인트의 인덱스 및 데이터 가져오기 (해당 프레임에서 특징을 추출하기 위해)
    min_energy_idx = np.argmin(energies)
    min_energy_frame = librosa.core.frames_to_time(data_frames[min_energy_idx], rate, hop_length=1024)

    # 하모닉 데이터
    chroma = librosa.feature.chroma_stft(data, rate)
    max_chroma = librosa.feature.chroma_stft(max_energy_frame, rate)
    min_chroma = librosa.feature.chroma_stft(min_energy_frame, rate)

    # 하모닉 데이터 평균 및 차이
    avg_harmonic = np.mean(chroma)
    std_harmonic = np.std(chroma)

    avg_harmonic_in_max = np.mean(max_chroma)
    avg_harmonic_in_min = np.mean(min_chroma)

    diff_avg_harmonic_max = np.fabs(avg_harmonic - avg_harmonic_in_max)
    diff_avg_harmonic_min = np.fabs(avg_harmonic - avg_harmonic_in_min)
    diff_avg_harmonic_maxmin = np.fabs(avg_harmonic_in_max - avg_harmonic_in_min)

    print("평균 하모닉: " + str(avg_harmonic) + " 하모닉의 표준편차: " + str(std_harmonic))
    print("최대에서 평균 하모닉: " + str(avg_harmonic_in_max) + " 최소에서 평균 하모닉: " + str(avg_harmonic_in_min))
    print("평균과 최대의 하모닉 차이: " + str(diff_avg_harmonic_max))
    print("평균과 최소의 하모닉 차이: " + str(diff_avg_harmonic_min))
    print("최소-최대의 하모닉 차이: " + str(diff_avg_harmonic_maxmin))

    print("== 파일 " + filename + " 처리에 걸린시간: " + str(round(time.time() - start_point, 2)))

    results = [filename, duration, tempo,
               avg_mfcc, max_mfcc, min_mfcc, var_mfcc, std_mfcc,
               avg_ZCR, var_ZCR, std_ZCR,
               avg_energy, max_energy, min_energy, std_energy,
               avg_harmonic, avg_harmonic_in_max, avg_harmonic_in_min,
               diff_avg_harmonic_max, diff_avg_harmonic_min, diff_avg_harmonic_maxmin]

    return results

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("파일 명을 입력해주세요!")
        sys.exit(2)

    input_files = sys.argv[1:]

    start_point = time.time()

    results = []
    [results.append(feature_extraction(file)) for file in input_files]
    print("= 전체 걸린시간(sec): " + str(round(time.time() - start_point, 2)))

    emotions = []
    for result in results:
        print(result[0] + " 의 감정: ")
        emotion = []

