#!/usr/bin/env python
# -*- codding: utf-8 -*- 
import json, logging

import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import DataModel

logger = logging.getLogger('getFundData')
logger.setLevel(logging.DEBUG)

class FundCrawler:
    def __init__(self, dbStr):
        self.fundList = []
        self.fundCompanyList = []
        self.fundListUrl = 'http://fund.eastmoney.com/js/fundcode_search.js'
        self.fundCompanyUrl = 'http://fund.eastmoney.com/js/jjjz_gs.js?dt=1463791574015'
        self.engine = create_engine(dbStr)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def getFundList(self):
        """从天天基金网上抓取基金列表"""        
        fundListStr = requests.get(self.fundListUrl).content.decode('utf-8').strip('\ufeffvar r = ').strip(';')
        self.fundList = json.loads(fundListStr)

    def fundList2Db(self):
        if not self.fundList:
            return 
        for k, fund in enumerate(self.fundList):
            item = DataModel.FundBasic(
                code = fund[0],
                name = fund[2],
                type_name = fund[3],
                pinyin_name = fund[4],
                pinyin_brief = fund[1]
            )
            self.session.add(item)
            logger.debug("%d records is saved." % (k +1))
        try:
            self.session.commit()
        except:
            self.session.rollback()

    def getFundCompanyList(self):
        temp = requests.get(self.fundCompanyUrl).content.decode('utf-8').\
            strip('\ufeffvar gs={op:').strip('};')
        self.fundCompanyList = json.loads(temp)
    

    def companyList2Db(self):
        if not self.fundCompanyList:
            return
        for k, company in enumerate(self.fundCompanyList):
            item = DataModel.FundCompany(
                code = company[0],
                name = company[1]
            )
            self.session.add(item)
            logger.debug("%d company records is saved." % (k + 1))
        try:
            self.session.commit()
        except Exception as e:
            logger.error(e.msg)
            self.session.rollback()

    
    def run(self):
        self.getFundList()
        self.fundList2Db()
        self.getFundCompanyList()
        self.companyList2Db()
    
    def create_table(self):
        DataModel.Base.metadata.create_all(self.engine)

url = 'https://www.kjj.com/netvalue-history-info-list.php?code=001186&startDate=2019-03-02&endDate=2020-03-02'


if __name__ == "__main__":
    fundCrawler = FundCrawler("sqlite:///fund.db")
    fundCrawler.create_table()
    fundCrawler.run()
    
    

