from django.test import TestCase
from information.models import CompanyCode
import pandas as pd

# em01 = data[['업체코드', '기업자료상태구분코드', '기업주체구분코드', '기업규모구분코드',\
#              '기업상세구분코드', '관리종목여부', '외부감사여부', '기업존속여부', '재무구분코드',\
#              '결산월', '설립일', '종업원수', '영문업체명', '약식업체명', '한글대표자명', '영문대표자명',\
#              '폐쇄여부구분코드', '그룹코드', '표준산업코드', '주거래은행코드', '한글주요제품명',\
#              '영문주요제품명', '홈페이지URL', '이메일']]
# em01.iloc[3].to_dict()
class CompanyCodeTestCase(TestCase):
    # maek user data
    def setUp(self):
        company_code, code_created = CompanyCode.objects.get_or_create(com_code='001471',
                                                                       br_no='3068130866',
                                                                       com_name='(주)케이티앤지',
                                                                       cor_no='1601110067804',
                                                                       market_code='1'
                                                                       )

        self.company_code = company_code
        # Verify that user data has been created
        self.assertTrue(code_created, msg='failed to save user data')
        self.assertEqual(CompanyCode.objects.all().count(), 1, msg='user data not created properly')

    def test_code_is_created(self):
        self.ccode_test = CompanyCode.objects.all().first()
        com_code=self.ccode_test.com_code
        br_no=self.ccode_test.br_no
        com_name=self.ccode_test.com_name
        cor_no=self.ccode_test.cor_no
        market_code=self.ccode_test.market_code
        self.assertEqual(com_code, '001471')
        self.assertEqual(br_no, '3068130866')
        self.assertEqual(com_name, '(주)케이티앤지')
        self.assertEqual(cor_no, '1601110067804')
        self.assertEqual(market_code, '1')


    def test_em01_is_created(self):
        objects.get_or_create(com_code=self.company_code,
                              com_status = '0',
                              com_identify= '1',
                              com_size='1',
                              com_detail='511',
                              issues_admin=,
                              ext_audit=,
                              com_exist=,
                              fin_div=,
                              settlement_month=,
                              established_date=,
                              no_employee=,
                              com_name_en=,
                              com_abbreviation=,
                              ceo_name=,
                              ceo_name_en=,
                              closure_status=,
                              group_code=,
                              sic=,
                              bank_code=,
                              main_product_ko=,
                              main_product_en=,
                              hompage=,
                              com_email=,
                              )
