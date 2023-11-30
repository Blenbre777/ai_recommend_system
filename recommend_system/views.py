from django.shortcuts import render
from recommend_system.AImodels.Models import pinterest

def recommend_form(request):
    filenames = [i+1 for i in range(49)] # 1 ~ 49

    # context: template html로 보내는 데이터 설정
    # template으로 데이터 전달은 dictionary 형태로해야함.
    return render(request, 'recommend_form.html', context={"filenames": filenames})

def recommend_proc(request):
    recommend_data = request.POST['recommend_data']

    recommend_result = pinterest(recommend_data) # 딥러닝 모델 사용

    # template으로 데이터 전달은 dictionary 형태로해야함.
    # return render(request, 'recommend_proc.html', context={"msg": "추천 처리됨"})
    return render(request, 'recommend_proc.html', context={"recommend_result": recommend_result})