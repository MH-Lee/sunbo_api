import pandas as pd
import numpy as np
import os, sys, glob
import datetime
import time
start_path = os.getcwd()
proj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onspace.settings")
sys.path.append(proj_path)
os.chdir(proj_path)
import django

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from information.models import (
        CompanyCode, EM01, AB09,
        AA06, AA22, AB01, AD01, AZ06
        )

list_dir = os.listdir('./utils/data/total')
list_dir[2]
# list_dir_sample = os.listdir('./utils/data/sample')
# list_dir_sample[6]
#
# em01_sample = pd.read_excel('./utils/data/sample/{}'.format(list_dir_sample[6]))
# str(em01_sample.loc[0, '사업자번호']).strip()

def EM01_send():
    start_time = time.time()
    data_em01 = pd.read_csv('./utils/data/total/{}'.format(list_dir[7]), header=None, engine='python', sep='\|',encoding='cp949')
    em01_header = ['업체코드', '사업자번호', '법인번호', '기업자료상태구분코드', '기업주체구분코드',\
                    '기업규모구분코드', '기업상세구분코드', '상장시장구분코드', '관리종목여부',\
                    '외부감사여부', '기업존속여부', '재무구분코드', '결산월', '창업일', '설립일',\
                    '종업원기준일', '종업원수', '한글업체명', '영문업체명', '약식업체명', '한글대표자명',\
                    '영문대표자명', '폐쇄여부구분코드', '그룹코드', '표준산업코드', '주거래은행코드',
                    '한글은행지점명', '영문은행지점명', '한글주요제품명', '영문주요제품명', '홈페이지URL',\
                    '이메일']
    data_em01.drop(32, axis=1, inplace=True)
    data_em01.columns = em01_header
    data_em01['업체코드'] = data_em01['업체코드'].apply(lambda x: str(x).zfill(6))
    data_em01['사업자번호'] = data_em01['사업자번호'].apply(lambda x: str(x).zfill(10))
    data_em01['법인번호'] = data_em01['법인번호'].apply(lambda x: str(x).zfill(13))
    data_em01['기업자료상태구분코드'] = data_em01['기업자료상태구분코드'].apply(lambda x: str(x).zfill(2))
    data_em01['재무구분코드'] = data_em01['재무구분코드'].apply(lambda x: str(x).zfill(2))
    data_em01['기업상세구분코드'] = data_em01['기업상세구분코드'].apply(lambda x: str(x).zfill(3))
    data_em01['그룹코드'] = data_em01['그룹코드'].apply(lambda x: str(x).zfill(3))
    data_em01['표준산업코드'] = data_em01['표준산업코드'].apply(lambda x: str(x).zfill(10))
    data_em01['주거래은행코드'] = data_em01['주거래은행코드'].apply(lambda x: str(x).zfill(3))
    end_time = time.time()
    print(end_time - start_time)
    for i in range(data_em01.shape[0]):
        if i % 1000 == 0:
            print(round(i/data_em01.shape[0],3) *100)
        com_code= str(data_em01.loc[i, '업체코드']).strip()
        br_no= str(data_em01.loc[i, '사업자번호']).strip()
        com_name= str(data_em01.loc[i, '한글업체명']).strip()
        cor_no= str(data_em01.loc[i, '법인번호']).strip()
        market_code= str(data_em01.loc[i, '상장시장구분코드']).strip()
        ccode_obj = CompanyCode(com_code=com_code,
                                br_no=br_no,
                                com_name=com_name,
                                cor_no=cor_no,
                                market_code=market_code)
        ccode_obj.save()
        com_status = str(data_em01.loc[i, '기업자료상태구분코드']).strip()
        com_identify = str(data_em01.loc[i, '기업주체구분코드']).strip()
        com_size = str(data_em01.loc[i, '기업규모구분코드']).strip()
        com_detail = str(data_em01.loc[i, '기업상세구분코드']).strip()
        issues_admin= str(data_em01.loc[i, '관리종목여부']).strip()
        ext_audit = str(data_em01.loc[i, '외부감사여부']).strip()
        com_exist = str(data_em01.loc[i, '기업존속여부']).strip()
        fin_div = str(data_em01.loc[i, '재무구분코드']).strip()
        settlement_month = str(data_em01.loc[i, '결산월']).strip()
        established_date = str(data_em01.loc[i, '업체코드']).strip()
        try:
            no_employee = int(str(data_em01.loc[i, '종업원수']).strip())
        except ValueError:
            no_employee = None
        com_name_en = data_em01.loc[i, '영문업체명'].strip()
        com_abbreviation = data_em01.loc[i, '약식업체명'].strip()
        ceo_name = data_em01.loc[i, '한글대표자명'].strip()
        ceo_name_en = data_em01.loc[i, '영문대표자명'].strip()
        closure_status = str(data_em01.loc[i, '폐쇄여부구분코드'].strip())
        group_code =str(data_em01.loc[i, '그룹코드'].strip())
        sic = str(data_em01.loc[i, '표준산업코드'].strip())
        bank_code = str(data_em01.loc[i, '주거래은행코드'].strip())
        main_product_ko = data_em01.loc[i, '한글주요제품명'].strip()
        main_product_en = data_em01.loc[i, '영문주요제품명'].strip()
        hompage = data_em01.loc[i, '홈페이지URL'].strip()
        com_email = data_em01.loc[i, '이메일'].strip()
        em01_obj = EM01(com_code=ccode_obj,
                        com_status=com_status,
                        com_identify=com_identify,
                        com_size=com_size,
                        com_detail=com_detail,
                        issues_admin=issues_admin,
                        ext_audit=ext_audit,
                        com_exist=com_exist,
                        fin_div=fin_div,
                        settlement_month=settlement_month,
                        established_date=established_date,
                        no_employee=no_employee,
                        com_name_en=com_name_en,
                        com_abbreviation=com_abbreviation,
                        ceo_name=ceo_name,
                        ceo_name_en=ceo_name_en,
                        closure_status=closure_status,
                        group_code=group_code,
                        sic=sic,
                        bank_code=bank_code,
                        main_product_ko=main_product_ko,
                        main_product_en=main_product_en,
                        hompage=hompage,
                        com_email=com_email
                        )
        em01_obj.save()
    print('EM01 업로드')

def AB09_send():
    data_ab09 = pd.read_csv('./utils/data/total/{}'.format(list_dir[3]), header=None, engine='python',\
                            sep='\|',encoding='cp949')
    ab09_header = ['보고서코드', '항목코드', '항목명(한글)', '항목명(영문)', '재무전체사용여부',\
                    '재무전체사용순서', '재무분석사용여부', '재무분석사용순서', '재무약식사용여부',\
                    '재무약식사용순서', '연결전체사용여부', '연결전체사용순서', '연결분석사용여부',\
                    '연결분석사용순서', '연결약식사용여부', '연결약식사용순서', '주요재무사용순서']
    data_ab09.drop(17, axis=1, inplace=True)
    data_ab09.columns = ab09_header
    data_ab09['항목코드'] = data_ab09['항목코드'].apply(lambda x: str(x).zfill(4))
    data_ab09['보고서키'] = data_ab09['보고서코드'] + '_' + data_ab09['항목코드']
    for i in range(data_ab09.shape[0]):
        if i % 1000 == 0:
            print(round(i/data_ab09.shape[0],3) *100)
        ab09_obj = AB09(rep_key=data_ab09.loc[i, '보고서키'].strip(),
                        rep_code=data_ab09.loc[i, '보고서코드'].strip(),
                        item_code=data_ab09.loc[i, '항목코드'].strip(),
                        item_name=data_ab09.loc[i, '항목명(한글)'].strip(),
                        item_name_en=data_ab09.loc[i, '항목명(영문)'].strip(),
                        use_finance=data_ab09.loc[i, '재무전체사용여부'].strip(),
                        order_finance=int(data_ab09.loc[i, '재무전체사용순서']),
                        use_fin_analysis=data_ab09.loc[i, '재무분석사용여부'].strip(),
                        order_fin_analysis=int(data_ab09.loc[i, '재무분석사용순서']),
                        use_fin_abb=data_ab09.loc[i, '재무약식사용여부'].strip(),
                        order_fin_abb=int(data_ab09.loc[i, '재무약식사용순서']),
                        use_consolidated=data_ab09.loc[i, '연결전체사용여부'].strip(),
                        order_consolidated=int(data_ab09.loc[i, '연결전체사용순서']),
                        use_consolidated_analysis=data_ab09.loc[i, '연결분석사용여부'].strip(),
                        order_consolidated_analysis=int(data_ab09.loc[i, '연결분석사용순서']),
                        use_consolidated_abb=data_ab09.loc[i, '연결약식사용여부'].strip(),
                        order_consolidated_abb=int(data_ab09.loc[i, '연결약식사용순서']),
                        order_main_fin=int(data_ab09.loc[i, '주요재무사용순서'])
                        )
        ab09_obj.save()
    print('AB09 업로드')

def AZ06_send():
    data_az06 = pd.read_csv('./utils/data/total/{}'.format(list_dir[6]), header=None, engine='python',\
                            sep='\|',encoding='cp949')
    az06_header = ['업체코드', '내용코드', '기준일자']
    data_az06.drop(3, axis=1, inplace=True)
    data_az06.columns = az06_header
    data_az06['업체코드'] = data_az06['업체코드'].apply(lambda x: str(x).zfill(6))
    data_az06['내용코드'] = data_az06['내용코드'].apply(lambda x: str(x).zfill(2))
    for i in range(data_az06.shape[0]):
        if i % 1000 == 0:
            print(round(i/data_az06.shape[0],3) *100)
        az06_obj = AZ06(com_code=CompanyCode.objects.get(com_code=data_az06.loc[i, '업체코드'].strip()),
                        cr_code=str(data_az06.loc[i, '내용코드']).strip(),
                        date=data_az06.loc[i, '기준일자']
                        )
        az06_obj.save()
    print('AZ06 업로드')

def AA22_send():
    data_aa22 = pd.read_csv('./utils/data/total/{}'.format(list_dir[1]), header=None, engine='python', sep='\|')
    aa22_header = ['업체코드', '기준일자', '일련번호', '결산구분', '직위', '성명', '생년월일', '최근경력']
    data_aa22.drop(8, axis=1, inplace=True)
    data_aa22.columns = aa22_header
    data_aa22['일련번호'] = data_aa22['일련번호'].apply(lambda x: str(x).zfill(4))
    for i in range(data_aa22.shape[0]):
        if i % 1000 == 0:
            print(round(i/data_aa22.shape[0],3) *100)
        aa22_obj = AA22(com_code=CompanyCode.objects.get(com_code=data_aa22.loc[i, '업체코드'].strip()),
                        date=data_aa22.loc[i, '기준일자'],
                        serial_no=data_aa22.loc[i, '일련번호'],
                        settlement=data_aa22.loc[i, '결산구분'],
                        position=data_aa22.loc[i, '직위'].strip(),
                        name=data_aa22.loc[i, '성명'].strip(),
                        date_birth=data_aa22.loc[i, '생년월일'].strip(),
                        recent_career=data_aa22.loc[i, '최근경력'].strip()
                        )
        aa22_obj.save()
    print('aa22 업로드')

def AA06_send():
    start_time = time.time()
    data_aa06 = pd.read_csv('./utils/data/total/{}'.format(list_dir[0]), header=None, engine='python',\
                        sep='\|',encoding='cp949')
    aa06_header = ['업체코드', '기준일자', '일련번호','주식구분', '결산구분', '주주명', \
                   '소유주식수', '지분율', '대주주와의 관계', '회사와의 관계']
    data_aa06.drop(10, axis=1, inplace=True)
    data_aa06.columns = aa06_header
    data_aa06['일련번호'] = data_aa06['일련번호'].apply(lambda x: str(x).zfill(4))
    end_time = time.time()
    print(end_time - start_time)
    for i in range(data_aa06.shape[0]):
        if i % 1000 == 0:
            print(round(i/data_aa06.shape[0],3) *100)
        aa06_obj = AA06(com_code=CompanyCode.objects.get(com_code=data_aa06.loc[i, '업체코드'].strip()),
                        date=data_aa06.loc[i, '기준일자'],
                        serial_no=data_aa06.loc[i, '일련번호'],
                        stock_type=data_aa06.loc[i, '주식구분'],
                        settlement=data_aa06.loc[i, '결산구분'],
                        shareholder_name=data_aa06.loc[i, '주주명'].strip(),
                        no_share=data_aa06.loc[i, '소유주식수'],
                        rate_of_share=data_aa06.loc[i, '지분율'],
                        relation_owner=data_aa06.loc[i, '대주주와의 관계'].strip(),
                        relation_com=data_aa06.loc[i, '회사와의 관계'].strip()
                        )
        aa06_obj.save()
    print('aa06 업로드')

def AD01_send(idx=0):
    start_time = time.time()
    data_ad01 = pd.read_csv('./utils/data/total/{}'.format(list_dir[5]), header=None, engine='python', sep='\|')
    ad01_header =  ['업체코드', '결산구분', '기준일자', '보고서코드', '항목코드', '금액', '구성비', '증감율']
    if idx != 0:
        data_ad01 = data_ad01.iloc[idx:]
        print(data_ad01.iloc[0])
    data_ad01.drop(8, axis=1, inplace=True)
    data_ad01.columns = ad01_header
    data_ad01['업체코드'] = data_ad01['업체코드'].apply(lambda x: str(x).zfill(6))
    data_ad01['항목코드'] = data_ad01['항목코드'].apply(lambda x: str(x).zfill(4))
    end_time = time.time()
    print(end_time - start_time)
    for i in list(data_ad01.index):
        if i % 1000 == 0:
            print(round(i/data_ad01.shape[0],3) *100)
        try:
            ad01_obj = AD01(com_code=CompanyCode.objects.get(com_code=data_ad01.loc[i, '업체코드'].strip()),
                            settlement=data_ad01.loc[i, '결산구분'].strip(),
                            date=data_ad01.loc[i, '기준일자'],
                            rep_code=data_ad01.loc[i, '보고서코드'],
                            item_code=data_ad01.loc[i, '항목코드'],
                            price=data_ad01.loc[i, '금액'],
                            ratio=data_ad01.loc[i, '구성비'],
                            change_rate=data_ad01.loc[i, '증감율']
                            )
        except Exception as e:
            print("error: ", e)
            print(data_ad01.loc[i, '보고서키'].strip())
        ad01_obj.save()
    print('ad01 업로드')

def AB01_send(idx=0):
    start_time = time.time()
    chunk_size = 2*10**5
    ab01_data_list = list()
    for i, chunk in enumerate(pd.read_csv('./utils/data/total/{}'.format(list_dir[2]), header=None, engine='python', chunksize=chunk_size, sep='\|')):
        print(i)
        data_ab01 = chunk
        ab01_header =  ['업체코드', '결산구분', '기준일자', '보고서코드', '항목코드', '금액', '구성비', '증감율']
        if idx != 0:
            data_ab01 = data_ab01.iloc[idx:]
            print(data_ab01.iloc[0])
        data_ab01.drop(8, axis=1, inplace=True)
        data_ab01.columns = ab01_header
        data_ab01['업체코드'] = data_ab01['업체코드'].apply(lambda x: str(x).zfill(6))
        data_ab01['항목코드'] = data_ab01['항목코드'].apply(lambda x: str(x).zfill(4))
        end_time = time.time()
        print(end_time - start_time)
        for i in list(data_ab01.index):
            if i % 1000 == 0:
                print(round(i/len(list(data_ab01.index)),3) *100)
            ab01_obj = AB01(com_code=CompanyCode.objects.get(com_code=data_ab01.loc[i, '업체코드'].strip()),
                            settlement=data_ab01.loc[i, '결산구분'].strip(),
                            date=data_ab01.loc[i, '기준일자'],
                            rep_code=data_ab01.loc[i, '보고서코드'],
                            item_code=data_ab01.loc[i, '항목코드'],
                            price=data_ab01.loc[i, '금액'],
                            ratio=data_ab01.loc[i, '구성비'],
                            change_rate=data_ab01.loc[i, '증감율'])
            ab01_data_list.append(ab01_obj)
    AB01.objects.bulk_create(ab01_data_list)
    print('AB01 업로드')


if __name__ == "__main__":
    # EM01_send()
    # AB09_send()
    # AZ06_send()
    # AA22_send()
    # AD01_send()
    # AA06_send()
    AB01_send()
