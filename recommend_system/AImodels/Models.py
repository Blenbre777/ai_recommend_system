import os

# import cv2
import numpy as np
from tensorflow.keras.models import load_model

def pinterest(data):
    data = np.array(data.split(','), dtype=int)
    print('-> data: ', data)

    data = np.array([data])
    print('-> data: ', data)

    path = os.path.dirname(os.path.abspath(__file__))
    print('-> path:', path) 

    model = load_model(os.path.join(path, 'Pinterest.h5')) # 모델 읽기 ★
    
    p = model.predict(data) # 모델 사용
    print('-> p:', p) # [[0.54815423 0.01504818 0.01776066 0.16331927 0.25571758 0.06331927 0.15571758]]
    
    # 0: 문화체험, 1: 자연감상 , 2: 활동과 스포츠, 3: 역사 탐방, 4: 쇼핑, 5: 맛집 탐방, 6: 휴양과 휴식  
    index = np.argmax(p) 
    print('-> index: ', index) # 0 ~ 4
    per = round(np.max(p) * 100, 1)
    print('-> per: ', per) 

    if index == 0:
        label = '문화체험'
    elif index == 1:
        label = '자연감상'
    elif index == 2:
        label = '활동과 스포츠'
    elif index == 3:
        label = '역사 탐방'
    elif index == 4:
        label = '쇼핑'
    elif index == 5:
        label = '맛집 탐방'
    elif index == 6:
        label = '휴양과 휴식'

    result = {}   # Dictionary
    if per >= 20: # 확률이 20% 이상인지 체크
        result = {"index": index, "label": label, "per": per}
    else:
        result = {"index": index, "label": f'가장 인접한 추천: {label}', "per": per}
   
    return result 