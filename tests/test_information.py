from django.test import TestCase
from information.models import (
    CompanyCode, EM01, AA06,
    AA22, AB01, AB09, AD01, AZ06
    )
import pandas as pd


class informationTestCase(TestCase):
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

        ab09, created = AB09.objects.get_or_create(rep_key='28_0020',
                                                    rep_code='28',
                                                    item_code='0020',
                                                    item_name='평균순유형자산',
                                                    item_name_en='Other operating expenses',
                                                    use_finance='O',
                                                    order_finance=0,
                                                    use_fin_analysis='O',
                                                    order_fin_analysis=0,
                                                    use_fin_abb='X',
                                                    order_fin_abb=0,
                                                    use_consolidated='X',
                                                    order_consolidated=0,
                                                    use_consolidated_analysis='X',
                                                    order_consolidated_analysis=0,
                                                    use_consolidated_abb='X',
                                                    order_consolidated_abb=0,
                                                    order_main_fin=0
                                                    )

        self.ab09 = ab09
        self.assertTrue(created, msg='failed to save AB09 data')
        self.assertEqual(AB09.objects.count(), 1, msg='AB09 data not created properly')

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
        em, created = EM01.objects.get_or_create(com_code=self.company_code,
                                                  com_status = '0',
                                                  com_identify= '1',
                                                  com_size='1',
                                                  com_detail='511',
                                                  issues_admin='N',
                                                  ext_audit='Y',
                                                  com_exist='Y',
                                                  fin_div='00',
                                                  settlement_month=12,
                                                  established_date='19971001',
                                                  no_employee=4305,
                                                  com_name_en='KT&G Corporation',
                                                  com_abbreviation='케이티앤지',
                                                  ceo_name='백복인',
                                                  ceo_name_en='Baek,Bok In',
                                                  closure_status='N',
                                                  group_code='B79',
                                                  sic='10C1200000',
                                                  bank_code='003',
                                                  main_product_ko='잎담배,제조담배,홍삼,홍삼제품 제조,판매',
                                                  main_product_en='Filter Cigarette',
                                                  hompage='www.ktng.com',
                                                  com_email='',
                                                  )
        self.assertTrue(created, msg='failed to save EM01 data')
        self.assertEqual(EM01.objects.count(), 1, msg='EM01 data not created properly')

    def test_aa06_is_created(self):
        aa06, created = AA06.objects.get_or_create(com_code=self.company_code,
                                                    date= 20160328,
                                                    serial_no=1,
                                                    stock_type=3,
                                                    settlement=3,
                                                    shareholder_name='양**',
                                                    no_share=4,
                                                    rate_of_share=47.0,
                                                    relation_owner='본인',
                                                    relation_com='대표이사'
                                                    )
        self.assertTrue(created, msg='failed to save AA06 data')
        self.assertEqual(AA06.objects.count(), 1, msg='AA06 data not created properly')

    def test_aa22_is_created(self):
        aa22, created = AA22.objects.get_or_create(com_code=self.company_code,
                                                    date=20150306,
                                                    serial_no=4,
                                                    settlement=3,
                                                    position='감사',
                                                    name='함**',
                                                    date_birth=19760128,
                                                    recent_career=''
                                                    )
        self.assertTrue(created, msg='failed to save AA22 data')
        self.assertEqual(AA22.objects.count(), 1, msg='AA22 data not created properly')

    def test_az06_is_created(self):
        az06, created = AZ06.objects.get_or_create(com_code=self.company_code,
                                                    cr_code='10',
                                                    date=20190917
                                                    )
        self.assertTrue(created, msg='failed to save AZ06 data')
        self.assertEqual(AZ06.objects.count(), 1, msg='AZ06 data not created properly')

    def test_ab01_is_created(self):
        ab01, created = AB01.objects.get_or_create(com_code=self.company_code,
                                                    settlement='K',
                                                    date=20141231,
                                                    rep_code='28',
                                                    item_code='0020',
                                                    price=22317,
                                                    ratio=10.3,
                                                    change_rate=142.2,
                                                    rep_key=self.ab09
                                                    )
        self.assertTrue(created, msg='failed to save ab01 data')
        self.assertEqual(AB01.objects.count(), 1, msg='ab01 data not created properly')

    def test_ad01_is_created(self):
        ad01, created = AD01.objects.get_or_create(com_code=self.company_code,
                                                    settlement='B',
                                                    date=20141231,
                                                    rep_code='28',
                                                    item_code='0020',
                                                    price=22317,
                                                    ratio=10.3,
                                                    change_rate=142.2,
                                                    rep_key=self.ab09
                                                    )
        self.assertTrue(created, msg='failed to save ad01 data')
        self.assertEqual(AD01.objects.count(), 1, msg='ad01 data not created properly')
