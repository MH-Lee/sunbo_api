from django.db import models
from information.choice.choice_dic import (
    CLOSURE_STATUS, COMPANY_SIZE, COMPANY_EXISTENCE,
    CR_CODE, EXTERNAL_AUDIT, FINANCE_DIV, IDENTIFIY,
    ISSUES_ADMIN, MARKET_CODE, SETTLEMENT_TYPE,
    SETTLEMENT_TYPE2, STATUS, STOCK_TYPE, USE_BINARY,
    BS_REPORT, CLOSURE_CODE, BP_CODE,
    )

# Create your models here.
class CompanyCode(models.Model):
    com_code = models.CharField(max_length=6, primary_key=True, verbose_name="업체코드")
    br_no = models.CharField(max_length=10, blank=True, null=True, verbose_name="사업자번호")
    com_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='한글업체명')
    cor_no = models.CharField(max_length=13, blank=True, null=True,\
                              verbose_name="법인번호")
    market_code = models.CharField(max_length=1, choices=MARKET_CODE,\
                                   blank=True, null=True, verbose_name='상장시장구분코드')

    def __str__(self):
        return '{}-{}'.format(self.com_code, self.com_name)

    class Meta:
        db_table = 'Compnay Code'
        verbose_name = '업체코드'
        verbose_name_plural = '업체코드'


class EM01(models.Model):
    com_code =  models.ForeignKey('CompanyCode', on_delete=models.CASCADE,
                                    related_name='em01_code', verbose_name='업체코드')
    com_status = models.CharField(max_length=2, choices=STATUS,\
                                  blank=True, null=True,
                                  verbose_name="기업자료상태구분코드")
    com_identify = models.CharField(max_length=1, blank=True, null=True,\
                                    verbose_name='기업주체구분코드')
    com_size = models.CharField(max_length=1, blank=True, null=True,\
                                verbose_name='기업규모구분코드')
    com_detail = models.CharField(max_length=3, blank=True, null=True)
    issues_admin = models.CharField(max_length=1, choices=ISSUES_ADMIN,\
                                   blank=True, null=True, verbose_name='관리종목여부')
    ext_audit = models.CharField(max_length=1, choices=EXTERNAL_AUDIT,\
                                 blank=True, null=True, verbose_name='외부감사여부')
    com_exist = models.CharField(max_length=1, choices=COMPANY_EXISTENCE,\
                                 blank=True, null=True, verbose_name='기업존속여부')
    fin_div = models.CharField(max_length=2, choices=FINANCE_DIV, blank=True,\
                               null=True, verbose_name= '재무구분코드')
    settlement_month = models.CharField(max_length=2, blank=True, null=True,\
                                        verbose_name='결산월')
    established_date = models.CharField(max_length=8, blank=True, null=True,\
                                        verbose_name='설립일')
    no_employee = models.IntegerField(blank=True, null=True, verbose_name='종업원수')
    com_name_en = models.CharField(max_length=100, blank=True, null=True, verbose_name='영문업체명')
    com_abbreviation = models.CharField(max_length=100, blank=True, null=True, verbose_name='약식업체명')
    ceo_name = models.CharField(max_length=70, blank=True, null=True, verbose_name='한글대표자명')
    ceo_name_en = models.CharField(max_length=150, blank=True, null=True, verbose_name='영문대표자명')
    closure_status = models.CharField(max_length=1, choices=CLOSURE_STATUS,\
                                      blank=True, null=True, verbose_name='폐쇄여부구분코드')
    group_code = models.CharField(max_length=3, blank=True, null=True, verbose_name='그룹코드')
    sic = models.CharField(max_length=10, blank=True, null=True, verbose_name='표준산업코드')
    bank_code = models.CharField(max_length=3, blank=True, null=True, verbose_name='주거래은행코드')
    main_product_ko = models.CharField(max_length=150, blank=True, null=True, verbose_name='한글주요제품명')
    main_product_en = models.CharField(max_length=150, blank=True, null=True, verbose_name='영문주요제품명')
    hompage = models.CharField(max_length=100, blank=True, null=True, verbose_name='홈페이지')
    com_email = models.CharField(max_length=100, blank=True, null=True, verbose_name='이메일')

    def __str__(self):
        return '{}-{} CEO: {}'.format(self.com_code, self.com_abbreviation, self.ceo_name)

    class Meta:
        db_table = 'em01'
        verbose_name = '업체개요'
        verbose_name_plural = '업체개요'


class EM02(models.Model):
    com_code =  models.ForeignKey('CompanyCode', on_delete=models.CASCADE,\
                                   related_name='em02_code', verbose_name='업체코드')
    serial_no = models.CharField(max_length=4, blank=True, null=True, verbose_name='일련번호')
    bp_code = models.CharField(max_length=2, choices=BP_CODE, blank=True, null=True, verbose_name='사업장구분코드')
    bp_name_ko = models.CharField(max_length=200, blank=True, null=True, verbose_name='한글사업장명칭')
    bp_name_en = models.CharField(max_length=200, blank=True, null=True, verbose_name='영문사업장명칭')
    phone_no = models.CharField(max_length=20, blank=True, null=True, verbose_name='전화번호')
    fax = models.CharField(max_length=20, blank=True, null=True, verbose_name='팩스번호')
    postal_code = models.CharField(max_length=6, blank=True, null=True, verbose_name='우편번호')
    address_ko = models.CharField(max_length=130, blank=True, null=True, verbose_name='한글사업장주소')
    address_en = models.CharField(max_length=150, blank=True, null=True, verbose_name='영문사업장주소')
    open_date =  models.CharField(max_length=8, blank=True, null=True, verbose_name='개업일자')
    business_type = models.CharField(max_length=70, blank=True, null=True, verbose_name='업종명')
    business_condition = models.CharField(max_length=70, blank=True, null=True, verbose_name='업태명')
    closure_code = models.CharField(max_length=1, choices=CLOSURE_CODE, blank=True, null=True, verbose_name='폐업구분코드')
    closure_date = models.CharField(max_length=8, blank=True, null=True, verbose_name='폐업일자')

    def __str__(self):
        return 'company_code: {} business_type: {}'.format(self.com_code, self.business_type)


class AA06(models.Model):
    com_code =  models.ForeignKey('CompanyCode', on_delete=models.CASCADE,
                                   related_name='aa06_code', verbose_name='업체코드')
    date = models.CharField(max_length=8, blank=True, null=True, verbose_name='기준일자')
    serial_no = models.CharField(max_length=4, blank=True, null=True, verbose_name='일련번호')
    stock_type = models.CharField(max_length=1, choices=STOCK_TYPE, blank=True, null=True, verbose_name='주식구분')
    settlement = models.CharField(max_length=1, choices=SETTLEMENT_TYPE, blank=True, null=True, verbose_name='결산구분')
    shareholder_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='주주명')
    no_share = models.IntegerField(blank=True, null=True, verbose_name='소유주식수')
    rate_of_share = models.FloatField(blank=True, null=True, verbose_name='지분율')
    relation_owner = models.CharField(max_length=30, blank=True, null=True, verbose_name='대주주와관계')
    relation_com = models.CharField(max_length=30, blank=True, null=True, verbose_name='회사와관계')

    def __str__(self):
        return 'date: {} company_code: {} name: : {} relationship: {}'.format(self.date, self.com_code, self.shareholder_name, self.relation_owner)

    class Meta:
        db_table = 'aa06'
        verbose_name = '주요주주'
        verbose_name_plural = '주요주주'


class AA22(models.Model):
    com_code = models.ForeignKey('CompanyCode', on_delete=models.CASCADE,
                                  related_name='aa22_code', verbose_name='업체코드')
    date = models.CharField(max_length=8, blank=True, null=True, verbose_name='기준일자')
    serial_no = models.CharField(max_length=4, blank=True, null=True, verbose_name='일련번호')
    settlement = models.CharField(max_length=1, choices=SETTLEMENT_TYPE, blank=True, null=True, verbose_name='결산구분')
    position = models.CharField(max_length=20, blank=True, null=True, verbose_name='직위')
    name = models.CharField(max_length=20, blank=True, null=True, verbose_name='성명')
    date_birth = models.CharField(max_length=20, blank=True, null=True, verbose_name='생년월일')
    recent_career = models.CharField(max_length=60, blank=True, null=True, verbose_name='최근경력')

    def __str__(self):
        return 'date: {} company_code: {} name: : {} position: {}'.format(self.date, self.com_code, self.name, self.position)

    class Meta:
        db_table = 'aa22'
        verbose_name = '경영진구성'
        verbose_name_plural = '경영진구성'


class AB01(models.Model):
    com_code = models.ForeignKey('CompanyCode', on_delete=models.CASCADE,
                                  related_name='ab01_code', verbose_name='업체코드')
    settlement = models.CharField(max_length=1, choices=SETTLEMENT_TYPE2, blank=True, null=True, verbose_name='결산구분')
    date = models.CharField(max_length=8, blank=True, null=True, verbose_name='기준일자')
    rep_code = models.CharField(max_length=2, choices=BS_REPORT, verbose_name="보고서코드")
    item_code = models.CharField(max_length=4, verbose_name="항목코드")
    price = models.BigIntegerField(blank=True, null=True, verbose_name="금액")
    ratio = models.FloatField(blank=True, null=True, verbose_name='구성비')
    change_rate = models.FloatField(blank=True, null=True, verbose_name='증감율')

    def __str__(self):
        return 'company code: {} report: {} '.format(self.com_code, self.rep_code)

    class Meta:
        db_table = 'ab01'
        verbose_name = '재무제표'
        verbose_name_plural = '재무제표'


class AB09(models.Model):
    rep_key = models.CharField(max_length=6, primary_key=True, verbose_name="업체코드")
    rep_code = models.CharField(max_length=2, choices=BS_REPORT, verbose_name="보고서코드")
    item_code = models.CharField(max_length=4, verbose_name="항목코드")
    item_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="한글항목명")
    item_name_en = models.CharField(max_length=80, blank=True, null=True, verbose_name="영어항목명")
    use_finance = models.CharField(max_length=1, blank=True, null=True,
                                    choices=USE_BINARY, verbose_name="재무전체사용여부")
    order_finance = models.IntegerField(blank=True, null=True, verbose_name="재무전체사용순서")
    use_fin_analysis = models.CharField(max_length=1, blank=True, null=True,
                                        choices=USE_BINARY, verbose_name="재무분석사용여부")
    order_fin_analysis = models.IntegerField(blank=True, null=True, verbose_name="재무분석사용순서")
    use_fin_abb = models.CharField(max_length=1, blank=True, null=True,
                                   choices=USE_BINARY, verbose_name="재무약식사용여부")
    order_fin_abb = models.IntegerField(blank=True, null=True, verbose_name="재무약식사용순서")
    use_consolidated = models.CharField(max_length=1, blank=True, null=True,
                                        choices=USE_BINARY, verbose_name="연결전체사용여부")
    order_consolidated = models.IntegerField(blank=True, null=True, verbose_name="연결전체사용순서")
    use_consolidated_analysis = models.CharField(max_length=1, blank=True, null=True,
                                                 choices=USE_BINARY, verbose_name="연결분석사용여부")
    order_consolidated_analysis = models.IntegerField(blank=True, null=True, verbose_name="연결분석사용순서")
    use_consolidated_abb = models.CharField(max_length=1, blank=True, null=True,
                                            choices=USE_BINARY, verbose_name="연결약식사용여부")
    order_consolidated_abb = models.IntegerField(blank=True, null=True, verbose_name="연결약식사용순서")
    order_main_fin = models.IntegerField(blank=True, null=True, verbose_name="주요재무사용순서")

    def __str__(self):
        return 'report: {} report name: {} '.format(self.rep_key, self.item_name)

    class Meta:
        db_table = 'ab09'
        verbose_name = '계정코드'
        verbose_name_plural = '계정코드'


class AD01(models.Model):
    com_code = models.ForeignKey('CompanyCode', on_delete=models.CASCADE, verbose_name='업체코드')
    settlement = models.CharField(max_length=1, choices=SETTLEMENT_TYPE2, blank=True, null=True, verbose_name='결산구분')
    date = models.CharField(max_length=8, blank=True, null=True, verbose_name='기준일자')
    rep_code = models.CharField(max_length=2, choices=BS_REPORT, verbose_name="보고서코드")
    item_code = models.CharField(max_length=4, verbose_name="항목코드")
    price = models.BigIntegerField(blank=True, null=True, verbose_name="금액")
    ratio = models.FloatField(blank=True, null=True, verbose_name='구성비')
    change_rate = models.FloatField(blank=True, null=True, verbose_name='증감율')

    def __str__(self):
        return 'company code: {} report: {} '.format(self.com_code, self.rep_code)

    class Meta:
        db_table = 'ad01'
        verbose_name = '연결재무제표'
        verbose_name_plural = '연결재무제표'


class AZ06(models.Model):
    com_code = models.ForeignKey('CompanyCode', on_delete=models.CASCADE, verbose_name='업체코드')
    cr_code = models.CharField(max_length=2, choices=CR_CODE, blank=True, null=True, verbose_name='결산구분')
    date = models.CharField(max_length=8, blank=True, null=True, verbose_name='기준일자')

    def __str__(self):
        return 'date: {} company_code: {} cr_code: : {} '.format(self.date, self.com_code, self.cr_code)

    class Meta:
        db_table = 'az06'
        verbose_name = '법정관리'
        verbose_name_plural = '법정관리'
