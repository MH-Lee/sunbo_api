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
        AA06, AA22, AB01, AD01
        )

list_dir = os.listdir('./utils/data/total')
# list_dir[6]
list_dir_sample = os.listdir('./utils/data/sample')
# list_dir_sample[6]
#
# em01_sample = pd.read_excel('./utils/data/sample/{}'.format(list_dir_sample[6]))
# str(em01_sample.loc[0, '사업자번호']).strip()

def EM01_send():
    start_time = time.time()
    data_em01 = pd.read_csv('./utils/data/total/{}'.format(list_dir[6]), header=None, engine='python', sep='\|',encoding='cp949')
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
        if i % 100 == 0:
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


if __name__ == "__main__":
    EM01_send()
