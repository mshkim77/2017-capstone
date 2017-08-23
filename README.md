# Context sentiment analysis based on speech, tones and word emotions
화법이 내재하고 있는 언어적 요소인 단어와 비언어적 요소인 말의 속도, 톤 등을 분석하여 화자의 감정을 분석하는 시스템

## Introduction
부경대학교의 학부생이 진행하는 4학년 과목의 과제 기획 (캡스톤 디자인) 프로젝트 입니다.

### 프로젝트 개요
의사소통 연구자들에 의하면 인간 간 의사소통에서 메시지의 60-95%는 발화된 내용이나 글과 같은 언어적 요소보다 얼굴 표정, 눈빛, 강세, 억양, 목소리의 톤, 동작, 자세, 옷차림 등 비 언어적 요소로 전달된다고 한다.따라서 이러한 비 언어적 요소 중, 말의 강세, 억양, 목소리 톤 등과 언어적 요소인 전체 문장을 ‘플루칙의 감정의 쳇바퀴’를 기반으로 하여, 수치화 한 후, 컴퓨터를 이용하여 분석 및 데이터화 한다. 그리고 그 결과로, 전체 발화 속의 문맥에 대한 화자의 감정을 도출하고자 한다.

### 인원 구성 (가나다 순)
- 김민승 (부경대학교 컴퓨터공학과)
- 박수덕 (부경대학교 컴퓨터공학과)
- 박소현 (부경대학교 인쇄정보공학과)
- 정준혁 (부경대학교 컴퓨터공학과)

### 사용할 언어 및 기술
- (Backend) <Web & Engine> Python 3 with Django, NumPy, SciPy, Tensorflow
- (Backend) <Audio Processing> Librosa, Pydub, ffmpeg
- (Backend) <Database> MongoDB
- (Frontend) HTML5, CSS, JavaScript
- (Frontend) WebRTC
