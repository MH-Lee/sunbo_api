import os
import pandas as pd

dic_list = os.listdir('./data')

# aa06.txt
aa06_header = ['업체코드', '기준일자', '일련번호','주식구분', '결산구분', '주주명', \
                '소유주식수', '지분율', '대주주와의 관계', '회사와의 관계']
data = pd.read_csv('./data/{}'.format(dic_list[0]), header=None, engine='python',\
                    sep='\|',encoding='cp949', nrows=1000)
data.drop(10, axis=1, inplace=True)
data['일련번호'] = data['일련번호'].apply(lambda x: str(x).zfill(4))
data.columns = aa06_header
data.to_excel('./refine_data/aa06.xlsx', index=False, encoding='cp949')

# aa17.txt
dic_list[1]
data17 = pd.read_csv('./data/{}'.format(dic_list[1]), header=None, engine='python',\
                    sep='\|',encoding='cp949', nrows=1000)

data17.to_excel('./refine_data/aa17.xlsx', index=False, encoding='cp949')

# 'aa22.txt'
dic_list[2]
data22 = pd.read_csv('./data/{}'.format(dic_list[2]), header=None, engine='python',\
                    sep='\|',encoding='cp949', nrows=1000)

aa22_header = ['업체코드', '기준일자', '일련번호', '결산구분', '직위', '성명', '생년월일', '최근경력']
data22.drop(8, axis=1, inplace=True)
data22.columns = aa22_header
data22['일련번호'] = data22['일련번호'].apply(lambda x: str(x).zfill(4))
data22.to_excel('./refine_data/aa22.xlsx', index=False, encoding='cp949')

# 'ab00.txt'
dic_list[3]
data_ab00 = pd.read_csv('./data/{}'.format(dic_list[3]), header=None, engine='python',\
                    sep='\|',encoding='cp949', nrows=1000)
ab00_header = ['업체코드', '결산구분', '기준일자', '원본구분']
data_ab00.head()
data_ab00.drop(4, axis=1, inplace=True)
data_ab00.columns = ab00_header
data_ab00.to_excel('./refine_data/ab00.xlsx', index=False, encoding='cp949')


# 'ab01.txt'
dic_list[4]
data_ab01 = pd.read_csv('./data/{}'.format(dic_list[4]), header=None, engine='python',\
                    sep='\|',encoding='cp949', nrows=1000)
data_ab01.head()
ab01_header = ['업체코드', '결산구분', '기준일자', '보고서코드', '항목코드', '금액', '구성비', '증감율']
data_ab01.drop(8, axis=1, inplace=True)
data_ab01.columns = ab01_header
data_ab01.to_excel('./refine_data/ab01.xlsx', index=False, encoding='cp949')

# 'ab09.txt'
dic_list[5]
data_ab09 = pd.read_csv('./data/{}'.format(dic_list[5]), header=None, engine='python',\
                    sep='\|',encoding='cp949', nrows=1000)
data_ab09.head()
ab09_header = ['보고서코드', '항목코드', '항목명(한글)', '항목명(영문)', '재무전체사용여부',\
                '재무전체사용순서', '재무분석사용여부', '재무분석사용순서', '재무약식사용여부',\
                '재무약식사용순서', '연결전체사용여부', '연결전체사용순서', '연결분석사용여부',\
                '연결분석사용순서', '연결약식사용여부', '연결약식사용순서', '주요재무사용순서']
data_ab09.drop(17, axis=1, inplace=True)
data_ab09['항목코드'] = data_ab09['항목코드'].apply(lambda x: str(x).zfill(4))
data_ab09.columns = ab09_header
data_ab09.to_excel('./refine_data/ab09.xlsx', index=False, encoding='cp949')

# 'abi0.txt'
dic_list[6]
data_abi0 = pd.read_csv('./data/{}'.format(dic_list[6]), header=None, engine='python',\
                    sep='\|',encoding='cp949', nrows=1000)
data_abi0.head()
abi0_header = ['업체코드', '결산구분', '기준일자', '원본구분']
data_abi0.drop(4, axis=1, inplace=True)
data_abi0.columns = abi0_header
data_abi0['업체코드'] = data_abi0['업체코드'].apply(lambda x: str(x).zfill(6))
data_abi0.to_excel('./refine_data/abi0.xlsx', index=False, encoding='cp949')

# 'abi1.txt'
dic_list[7]
data_abi1 = pd.read_csv('./data/{}'.format(dic_list[7]), header=None, engine='python',\
                    sep='\|',encoding='cp949', nrows=1000)
data_abi1.head()
abi1_header = ['업체코드', '결산구분', '기준일자', '보고서코드', '항목코드', '금액', '구성비', '증감율']
data_abi1.drop(8, axis=1, inplace=True)
data_abi1.columns = abi1_header
data_abi1['업체코드'] = data_abi1['업체코드'].apply(lambda x: str(x).zfill(6))
data_abi1['항목코드'] = data_abi1['항목코드'].apply(lambda x: str(x).zfill(6))
data_abi1.to_excel('./refine_data/abi7.xlsx', index=False, encoding='cp949')

# 'abi9.txt'
dic_list[8]
data_abi9 = pd.read_csv('./data/{}'.format(dic_list[8]), header=None, engine='python',\
                    sep='\|',encoding='cp949', nrows=1000)
data_abi9.head()
abi9_header = ['보고서코드', '항목코드', '항목명(한글)', '항목명(영문)', '재무전체사용여부',\
                '재무전체사용순서', '재무분석사용여부', '재무분석사용순서', '재무약식사용여부',\
                '재무약식사용순서', '연결전체사용여부', '연결전체사용순서', '연결분석사용여부',\
                '연결분석사용순서', '연결약식사용여부', '연결약식사용순서', '주요재무사용순서',\
                '재무값단위']
data_abi9.drop(18, axis=1, inplace=True)
data_abi9.columns = abi9_header
data_abi9['항목코드'] = data_abi9['항목코드'].apply(lambda x: str(x).zfill(6))
data_abi9.to_excel('./refine_data/abi9.xlsx', index=False, encoding='cp949')

# 'ad00.txt'
dic_list[9]
data_ad00 = pd.read_csv('./data/{}'.format(dic_list[9]), header=None, engine='python',\
                    sep='\|',encoding='cp949', nrows=1000)
data_ad00.head()
ad00_header =  ['업체코드', '결산구분', '기준일자', '구분']
data_ad00.drop(4, axis=1, inplace=True)
data_ad00.columns = ad00_header
data_ad00['업체코드'] = data_ad00['업체코드'].apply(lambda x: str(x).zfill(6))
data_ad00.to_excel('./refine_data/ad00.xlsx', index=False, encoding='cp949')

# 'ad01.txt'
dic_list[10]
data_ad01 = pd.read_csv('./data/{}'.format(dic_list[10]), header=None, engine='python',\
                    sep='\|',encoding='cp949', nrows=1000)
data_ad01.head()
ad01_header =  ['업체코드', '결산구분', '기준일자', '보고서코드', '항목코드', '금액', '구성비', '증감율']
data_ad01.drop(8, axis=1, inplace=True)
data_ad01.columns = ad01_header
data_ad01['업체코드'] = data_ad01['업체코드'].apply(lambda x: str(x).zfill(6))
data_ad01['항목코드'] = data_ad01['항목코드'].apply(lambda x: str(x).zfill(4))
data_ad01.to_excel('./refine_data/ad01.xlsx', index=False, encoding='cp949')

# 'adi0.txt'
dic_list[11]
data_adi0 = pd.read_csv('./data/{}'.format(dic_list[11]), header=None, engine='python',\
                    sep='\|',encoding='cp949', nrows=1000)
data_adi0.head()
adi0_header =  ['업체코드', '결산구분', '기준일자', '구분']
data_adi0.drop(4, axis=1, inplace=True)
data_adi0.columns = adi0_header
data_adi0['업체코드'] = data_adi0['업체코드'].apply(lambda x: str(x).zfill(6))
data_adi0.to_excel('./refine_data/adi0.xlsx', index=False, encoding='cp949')

# 'adi1.txt'
dic_list[12]
data_adi1 = pd.read_csv('./data/{}'.format(dic_list[12]), header=None, engine='python',\
                    sep='\|',encoding='cp949', nrows=1000)
data_adi1.head()
adi1_header = ['업체코드', '결산구분', '기준일자', '보고서코드', '항목코드', '금액', '구성비', '증감율']
data_adi1.drop(8, axis=1, inplace=True)
data_adi1.columns = adi1_header
data_adi1['업체코드'] = data_adi1['업체코드'].apply(lambda x: str(x).zfill(6))
data_adi1['항목코드'] = data_adi1['항목코드'].apply(lambda x: str(x).zfill(4))
data_adi1.to_excel('./refine_data/adi1.xlsx', index=False, encoding='cp949')

# 'az06.txt'
dic_list[13]
data_az06 = pd.read_csv('./data/{}'.format(dic_list[13]), header=None, engine='python',\
                    sep='\|',encoding='cp949', nrows=10000)
data_az06.head()
az06_header = ['업체코드', '내용코드', '기준일자']
data_az06.drop(3, axis=1, inplace=True)
data_az06.columns = az06_header
data_az06['업체코드'] = data_az06['업체코드'].apply(lambda x: str(x).zfill(6))
data_az06['내용코드'] = data_az06['내용코드'].apply(lambda x: str(x).zfill(2))
data_az06.to_excel('./refine_data/az06.xlsx', index=False, encoding='cp949')

# 'em01.txt'
dic_list[14]
data_em01 = pd.read_csv('./data/{}'.format(dic_list[14]), header=None, engine='python',\
                    sep='\|',encoding='cp949', nrows=1000)
data_em01.head()
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
data_em01['기업상세구분코드'] = data_em01['기업상세구분코드'].apply(lambda x: str(x).zfill(3))
data_em01['그룹코드'] = data_em01['그룹코드'].apply(lambda x: str(x).zfill(3))
data_em01['표준산업코드'] = data_em01['표준산업코드'].apply(lambda x: str(x).zfill(10))
data_em01['주거래은행코드'] = data_em01['주거래은행코드'].apply(lambda x: str(x).zfill(3))
data_em01.to_excel('./refine_data/em01.xlsx', index=False, encoding='cp949')

# 'em02.txt'
dic_list[15]
data_em02 = pd.read_csv('./data/{}'.format(dic_list[15]), header=None, engine='python',\
                    sep='\|',encoding='cp949', nrows=1000)
data_em02.head()
em02_header = ['업체코드', '일련번호', '사업자번호', '사업장구분코드', '한글사업장명칭',\
                '영문사업장명칭', '전화번호', '팩스번호', '우편번호', '한글사업장주소',\
                '영문사업장주소', '개업일자', '업종명', '업태명', '폐업구분코드', '폐업일자']
data_em02.drop(16, axis=1, inplace=True)
data_em02.columns = em02_header
data_em02['업체코드'] = data_em02['업체코드'].apply(lambda x: str(x).zfill(6))
data_em02['일련번호'] = data_em02['일련번호'].apply(lambda x: str(x).zfill(4))
data_em02['사업자번호'] = data_em02['사업자번호'].apply(lambda x: str(x).zfill(10))
data_em02['사업장구분코드'] = data_em02['사업장구분코드'].apply(lambda x: str(x).zfill(2))
data_em02['우편번호'] = data_em02['우편번호'].apply(lambda x: str(x).zfill(5))
data_em02.to_excel('./refine_data/em02.xlsx', index=False, encoding='cp949')
