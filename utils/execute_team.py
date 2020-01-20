import pandas as pd
import numpy as np
import os, sys, glob
import datetime

start_path = os.getcwd()
proj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onspace.settings")
sys.path.append(proj_path)
os.chdir(proj_path)
import django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import time
import pandas as pd
from information.models import (
        EM01, 
        AA06,
        AA22,
        CompanyCode, 
        EM02, 
        AB01, 
        AD01
)

print('aa22 setting')
start_time = time.time()
valid_df = pd.read_csv('./utils/data/fif_billion_df.csv', encoding='cp949')
com_code_list = valid_df['com_code'].tolist()
aa22_valid = AA22.objects.filter(date_birth__lte=19600101).filter(position__icontains='대표이사').filter(com_code__in = com_code_list)
list_aa22 = aa22_valid.values('com_code','date', 'name', 'date_birth', 'position')
aa22_df = pd.DataFrame(list_aa22)
aa22_colnames = ['회사코드', '취임날짜', '이름', '생일', '직책']
aa22_df.columns = aa22_colnames
aa22_df.sort_values(['회사코드', '취임날짜', '생일'], ascending=[True, False, False], inplace=True)
aa22_df = aa22_df[aa22_df['생일']!='']
aa22_df = aa22_df[aa22_df['생일']!='19000000']
aa22_df.drop_duplicates(subset=['회사코드'], keep='first', inplace=True) 
aa22_df.to_csv('./utils/execute_search/valid_aa22.csv', encoding='cp949', index=False)
aa22_list = aa22_df['회사코드'].tolist()
end_time = time.time()
print(end_time - start_time)

print('em01 setting')
start_time = time.time()
em01_valid_obj = EM01.objects.filter(com_code__in = aa22_list)
list_em01 = list(em01_valid_obj.values('com_code', 'com_abbreviation', 'com_name_en', 'com_size', 'ceo_name', 'main_product_ko', 'established_date'))
em01_df = pd.DataFrame(list_em01)
em01_colnames = ['회사코드', '회사명', '회사명(영문)', '회사규모', 'ceo 이름','주요생산 제품', '설립일']
em01_df.columns = em01_colnames
em01_df = em01_df[em01_df['회사규모'] != '1']
em01_df.to_csv('./utils/execute_search/em01_df.csv', encoding='cp949', index=False)
em01_list = em01_df['회사코드'].to_list()
end_time = time.time()
print(end_time - start_time)

print('em02 setting')
start_time = time.time()
em02_valid_obj = EM02.objects.filter(com_code__in = em01_list).filter(bp_name_ko='본사')
list_em02 = list(em02_valid_obj.values('com_code', 'address_ko', 'business_type', 'business_condition'))
em02_df = pd.DataFrame(list_em02)
em02_colnames = ['회사코드', '회사주소', '업종명', '업태명']
em02_df.columns = em02_colnames
em02_df.to_csv('./utils/execute_search/em02_df.csv', encoding='cp949', index=False)
end_time = time.time()
print(end_time - start_time)

print('data merging')
start_time = time.time()
em01aa22_df = pd.merge(em01_df, aa22_df, how='inner', on='회사코드') 
em01aa22em02_df = pd.merge(em01aa22_df, em02_df, how='left', on='회사코드') 
em01aa22em02_df.to_csv('./utils/execute_search/em01aa22em02_df.csv', encoding='cp949', index=False)
end_time = time.time()
print(end_time - start_time)

'''
매출 :121000
매출총이익: 123000
영업이익: 125000
총자산 : 115000
총부채 : 118000
'''

rep_dict = {'매출' :['12','1000'],
            '매출총이익': ['12','3000'],
            '영업이익': ['12','5000'],
            '총자산' : ['11','5000'],
            '총부채' : ['11','8000']}


print('data generate')
start_time = time.time()
final_code = em01aa22em02_df['회사코드'].tolist()
make_df_first = True
for rep_key in list(rep_dict.keys()):
	print(rep_key)
	if make_df_first:
		total_df = em01aa22em02_df
		make_df_first = False
	total_fin_db = AB01.objects.filter(date__gte = 20150101).filter(date__lte=20181231).filter(settlement='K').filter(rep_code=rep_dict[rep_key][0]).filter(item_code=rep_dict[rep_key][1]).filter(com_code__in = final_code)
	total_fin_df = pd.DataFrame(list(total_fin_db.values('date', 'com_code', 'price')))
	total_fin_df2 = total_fin_df[total_fin_df['date'].str.contains('1231')]
	total_finance = total_fin_df2.pivot(index='com_code', columns='date', values='price').reset_index()
	total_finance.columns = ['회사코드', '2015년 {}'.format(rep_key), '2016년 {}'.format(rep_key), '2017년 {}'.format(rep_key), '2018년 {}'.format(rep_key)]
	total_df = pd.merge(total_df, total_finance, how='left', on='회사코드') 

total_df.to_csv('./final_ceo_df.csv', index=False, encoding='cp949')
end_time = time.time()
print(end_time - start_time)

print('data generate2')
start_time = time.time()
for rep_key in list(rep_dict.keys()):
	print(rep_key)
	total_fin_db_con = AD01.objects.filter(date__gte = 20150101).filter(date__lte=20181231).filter(settlement='K').filter(rep_code=rep_dict[rep_key][0]).filter(item_code=rep_dict[rep_key][1]).filter(com_code__in = final_code)
	total_fin_df_con = pd.DataFrame(list(total_fin_db_con.values('date', 'com_code', 'price')))
	total_fin_df_con2 = total_fin_df_con[total_fin_df_con['date'].str.contains('1231')]
	total_finance_con = total_fin_df_con2.pivot(index='com_code', columns='date', values='price').reset_index()
	total_finance_con.columns = ['회사코드', '2015년 {}(연결)'.format(rep_key), '2016년 {}(연결)'.format(rep_key), '2017년 {}(연결)'.format(rep_key), '2018년 {}(연결)'.format(rep_key)]
	total_df = pd.merge(total_df, total_finance_con, how='left', on='회사코드')

total_df.to_csv('./final_ceo_df2.csv', index=False, encoding='cp949')
end_time = time.time()
print(end_time - start_time)

stockholder_list = AA06.objects.filter(com_code__in = final_code)
list_aa06 = list(stockholder_list.values('date', 'com_code', 'stock_type', 'settlement', 'shareholder_name','relation_owner','rate_of_share'))
aa06_df = pd.DataFrame(list_aa06)
aa06_df.columns = ['date', '회사코드', '주식구분', '결산구분', '주주이름', '주주와의 관계', '지분비율']
stock_type = {'1':'보통주', '2':'우선주', '3':'합계', '4':'기타주식'}
settlement_type = {'1':'결산', '2':'반기', '3':'기타', '4':'1/4분기', '5':'3/4분기'}
aa06_df['주식구분'] = aa06_df['주식구분'].map(stock_type)
aa06_df['결산구분'] = aa06_df['결산구분'].map(settlement_type)
aa06_df.sort_values(['회사코드', 'date'], ascending=[True, False], inplace=True)
aa06_df.drop_duplicates(subset=['회사코드', '주주이름'], inplace=True, keep='first')
aa06_df.to_csv('./utils/execute_search/aa06_df.csv', encoding='cp949', index=False)

print('data generate3')
start_time = time.time()
total_df['주요주주'] = None
for com_code in final_code:
	try:
		recent_date = aa06_df[aa06_df['회사코드'] == com_code].head(1).date.values[0]
		tmp_df = aa06_df.loc[(aa06_df['회사코드'] == com_code) & (aa06_df['date'] == recent_date)]
		sh_list = [tuple(x) for x in tmp_df[['date', '주주이름', '주식구분', '결산구분', '주주와의 관계', '지분비율']].values]
		total_df.loc[total_df['회사코드']==com_code, '주주구성'] = str(sh_list)
	except:
		print(com_code)
		continue

end_time = time.time()
print(end_time - start_time)

total_df.to_csv('./final_ceo_df3.csv', index=False, encoding='cp949')