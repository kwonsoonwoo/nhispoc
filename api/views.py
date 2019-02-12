import json
import subprocess

import requests
from django.shortcuts import render, redirect
from .models import Data


def data_list(request):
    # 배포용
    # Data model에 있는 데이터 조회
    datas = Data.objects.all()
    cmd = "ifconfig ens3 | grep Mask | cut -d: -f 2 | awk '{print$1}'"
    # meta_data.json 파일 get 요청
    meta_data_json = requests.get("http://169.254.169.254/openstack/latest/meta_data.json")
    # json형식 파일을 Python Dictionary 형태로 변경
    meta_data = json.loads(meta_data_json.text)
    # public-ipv4 파일 get 요청
    public_ipv4_data = requests.get("http://169.254.169.254/latest/meta-data/public-ipv4")
    # public-ipv4 텍스트 변수 지정
    public_ipv4 = public_ipv4_data.text
    # local-ipv4 파일 get 요청
    local_ipv4 = subprocess.check_output([cmd], shell=True, universal_newlines=True)
    # local-ipv4 텍스트 변수 지정
    # local_ipv4 = local_ipv4_data.text
    # index.html Template에 context 변수로 전달
    context = {
        'datas': datas,
        'meta_data': meta_data,
        'public_ipv4': public_ipv4,
        'local_ipv4': local_ipv4
    }
    return render(request, 'index.html', context)

    # # 로컬용
    # datas = Data.objects.all()
    # meta_data = {
    #     "availability_zone": "nova"
    # }
    # public_ipv4 = '101.55.126.218'
    # local_ipv4 = '10.30.0.11'
    # context = {
    #     'datas': datas,
    #     'meta_data': meta_data,
    #     'public_ipv4': public_ipv4,
    #     'local_ipv4': local_ipv4
    # }
    # return render(request, 'index.html', context)


def data_create(request):
    if request.method == 'POST':
        data = Data.objects.create(
            content=request.POST['content'],
        )
        data.save()
        return redirect('data-list')
    return render(request, 'index.html')
