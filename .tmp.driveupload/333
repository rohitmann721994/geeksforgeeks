import datetime
import os
import pandas as pd
from bs4 import BeautifulSoup
import requests
import coloredlogs, logging
import configparser
import json



class Amazon():
    def __init__(self):
        self.logging = logging.getLogger(__name__)
        fieldstyle = {'asctime': {'color': 'green'},
                      'levelname': {'bold': True, 'color': 'black'},
                      'filename':{'color':'cyan'},
                      'funcName':{'color':'blue'}}
        levelstyles = {'critical': {'bold': True, 'color': 'red'},
                       'debug': {'color': 'green'},
                       'error': {'color': 'red'},
                       'info': {'color':'magenta'},
                       'warning': {'color': 'yellow'}}
        coloredlogs.install(
                            logger=self.logging,
                            fmt='%(asctime)s [%(levelname)s] - [%(filename)s > %(funcName)s() > %(lineno)s] - %(message)s',
                            datefmt='%H:%M:%S',
                            field_styles=fieldstyle,
                            level_styles=levelstyles)
        self.config=self.readConfig()
        self.searchString=self.config['AMAZON']['SEARCH_STRING']
        print(self.searchString)
        self.pageIndex=1
        self.rawUrl="https://www.amazon.in/s?k={}&page={}"
        self.itemsTuple=()
        self.url=self.urlCreator()
        self.DateToday=datetime.date.today()
        print("date.today :",datetime.date.today())
        self.soup=BeautifulSoup
        self.data={'title':[]}
        self.fileToday= "{}_{}.csv".format(self.searchString,datetime.date.today())
        self.fileYesterday= "{}_{}.csv".format(self.searchString,datetime.date.today()-datetime.timedelta(days=1))

    def readConfig(self):
        config = configparser.ConfigParser()
        config.read('amazon.ini')
        return config

    def fileProcessorforPanda(self)->bool:

        try:
            if not os.path.exists(self.fileToday):
                open(self.fileToday,'x')
                pd.DataFrame({'title':['NA']},columns=list(amazon.data.keys())).to_csv(self.fileToday,header=True)
            fileToday= pd.read_csv(self.fileToday)
            if os.path.exists(self.fileYesterday):
                # open(self.fileYesterday,'x')
                # pd.DataFrame({'title':['NA']},columns=list(amazon.data.keys())).to_csv(self.fileYesterday,header=True)
                try:
                    fileYesterday =pd.read_csv(self.fileYesterday)

                    self.logging.info("Items new added :",fileToday['title']-fileYesterday['title'])
                    self.logging.info("Items removed :",fileYesterday['title']-fileToday['title'])

                except Exception as e:
                    self.logging.warning("last file not found :",e)
            df=pd.DataFrame(data=self.data,columns=list(amazon.data.keys()))
            df.to_csv (fileToday, index = False,header=True)

            return True
        except Exception as e:
            self.logging.exception(e)
            return False

    def fileProcessorWithoutPanda(self):
        try:
            with open(self.fileToday,'w') as fileToday:
                fileToday.write(json.dumps(self.data))
                if os.path.exists(self.fileYesterday):

                    fileYesterday=json.loads(open(self.fileYesterday,'r').read())

                    added=[i for i in self.data['title'] if i not in fileYesterday['title']]
                    removed=[i for i in fileYesterday['title'] if i not in self.data['title'] ]
                    print("Items new added :",added) if added else None
                    print("Items removed :",removed) if removed else None
                    print("No change") if self.data['title']==fileYesterday['title'] else None

                fileToday.close()
        except Exception as e:
            self.logging.exception(e)



    def urlCreator(self)->str:
        return self.rawUrl.format(self.searchString,self.pageIndex)

    def ifNextPageExist(self,soup:BeautifulSoup)->bool:
        try:
            for link in soup.findAll('a'):
                if link.has_attr('href'):
                    if( "/s?k={}&page={}".format(self.searchString,self.pageIndex+1) in link['href'] ):
                        print("next page link Found :",link['href'])
                        return True

            return False
        except AttributeError:
            return False

    def amazonSearch(self):

        itemsList=[]

        print("url to visit :",self.url)

        HEADERS = {
            'authority': 'www.amazon.in',
            'rtt': '500',
            'downlink': '1.55',
            'ect': '3g',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'service-worker-navigation-preload': 'true',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://www.amazon.in/s?k=samsung&ref=nb_sb_noss',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            # 'cookie': 'ubid-acbin=257-2678800-5308537; lc-acbin=en_IN; i18n-prefs=INR; session-id=257-6697844-0818701; csd-key=eyJ3YXNtVGVzdGVkIjp0cnVlLCJ3YXNtQ29tcGF0aWJsZSI6dHJ1ZSwid2ViQ3J5cHRvVGVzdGVkIjpmYWxzZSwidiI6MSwia2lkIjoiMzU0M2NhIiwia2V5IjoiRXg0VkJVUHltRm9WcGhzRFNNam5RY1poS21PTnRHbW5BTmtrWHRsM2pIaVdJdkducWp3ZHQ3U0YrQXNHMm14OWNYQkIrTnRLV1M2VlArZUVBN3B6dVhXUkxSMXVhRTRWOGlXWVhSNjZLcC9BMFF4Wk0rY2czMmJJbGxneDMrK0MxMUhJaHExa3JoSVpQdmNyT1I3VUNrNGlxbzlnLzdXMWVYL3BKMGczMVFVRXhaZHRxaTZ3VnRVc2Zsa01GYzR0b0NTR0hCMzVVZUx1YVRzMzBSbXg4SXc1MWpIN3FkQkc2VzdBZU5aNnJpaVZFTzRvakFlZ2FQRm94ZnZodHV1NE15UWVoVVV5NXM2SmFGWkEwMEFENzRNcmJHQUFCaXd6ZlYyVmFxMy90aWtFY0FBTmlBczNkUDg2Njg2Z1ZaYlY4WS9SbWcxTzNqZFNtRmNDNmpFZEp3PT0ifQ==; visitCount=22; s_fid=11F62489F3928206-0D279C882B0E7105; s_cc=true; session-token="drK4x6EfFmhFRY/H90W787Q7ArGOseTQbpNRZ2WxAAf1Pr7GcqeRHhk1ZF+Ew3uQ6X/4MrvOpj0WPASf6WUNliFQrMCxGbQzIJmoOvk4Eyd1vBIxDQmWt08EtT3PzS2844QBJlYRoa8SDuwq3JOZDTd0tic6sV6kaQIOq//vys29jqV/DHNlYNh3MPoknu8pXLn/8DAqwDyRqgMRmQVTlRDau7qgSCqGHDPmdbFA1Fs="; x-acbin="h1meqLU5DtGfZqJNG85suWLQ?fGdh8JrWu3jqm6Om2waTC1UcsEyMvm5nGS@b4uj"; at-acbin=Atza|IwEBIFhJRnFUhZPLtONj2AHnI-iW8MOckL4CXhFjcDbVpPfH4wqr9lZ_1-h-BONdFf2RiAOgjjhsd8sM8tdZ0S-z6ktwZNXcBq0FKMrwpDs093gub7hzORYWTHSeshfYfjeviEpHxeXx29pkVH8XV2K835Z7H0HSzk0mkZB234VeaLAULsTpokeBKNglotMUPgw-pe2gVc8oS4592jxkeBHDJI5ann1VNjx5lFkO_3dJCG6efA; sess-at-acbin="8fMZ4Q+jsw6GW9zEgYoZ3U7KoACJUh4tACIbvaquxvA="; sst-acbin=Sst1|PQGfbdEVM2tiGFUzWALD2GllDP04awP_yjyJ0-j_Cu1k_UrzG_ddqKy7_NuhNi88ovQ2LETZO-k-IEDpX-8ZKhM6V1C7NVb1XRzZMstkszni7QHYujse9Mp6QrHm9I5ceshmzkOcGyTaacHYIRTPU_G1brobTW8EbHKwfRY7IMZ-2ttbBhiWceSP5UfSNWxI9mJhX2TOkJ3e4NaDmM-K7xCcCwqbWnjzj4hl13aixn9MHUs3d_5iuPfI_uqRjP13dKkJy4HP6KYbrofEF72OEatSfd8x9dEPubX1LFyH8F-f1e0ImrCvGFnTWWdxL-65KeHIaTiC7McZEqFSyv9AIFMpoClwW8ZQEm_88THVRM2fPCA; _rails-root_session=RWJQQ3gyVUFjUDFpN2d5UXpXT2dzb2xUb1FUVy9sVkdVWjh4VkdJOUFLejdJVkxoY0Qvb2o1TUQ4SytuR0h3N1RadWdPclc3dlFyc3d5Z2NLVUZEYkg0aXZJd0N0TjQwTlhYUnc1TWFIMmF3L3YzaEJoNnhrSDMrZE1CNC8wSytIMDZxNlYyS0Q4VTR0b3gxR2hkNEg1R0tVUmxINjBUVDV5bHRrdkdZS1kwd1RSTk0zTGFoRHVEZDVDSERIOXk1LS1kUmNFd3ZHRjBtenR4L05ROXkxRm9nPT0%3D--fb492a63a0b35345b68cbd5ea7dbd0fe11642800; s_sq=amazdiinprod%3D%2526pid%253Dhttps%25253A%25252F%25252Faffiliate-program.amazon.in%25252Fsignup%25253Fopenid.assoc_handle%25253Damzn_associates_in%252526openid.claimed_id%25253Dhttps%2525253A%2525252F%2525252Fwww.amazon.in%2525252Fap%2525252Fid%2525252Famzn1.account.AFNJQHFMVNGZRWIK4GKFLZYQVIOQ%252526openid.identity%25253Dhttps%2525253A%2525252F%2525252Fwww.amazon.in%2525252Fap%2525252Fid%2525252Famzn1.account.AF%2526oid%253Dhttps%25253A%25252F%25252Faffiliate-program.amazon.in%25252Fhome%2526ot%253DA%26amazditemplate%3D%2526pid%253Dhttps%25253A%25252F%25252Faffiliate-program.amazon.in%25252Fsignup%25253Fopenid.assoc_handle%25253Damzn_associates_in%252526openid.claimed_id%25253Dhttps%2525253A%2525252F%2525252Fwww.amazon.in%2525252Fap%2525252Fid%2525252Famzn1.account.AFNJQHFMVNGZRWIK4GKFLZYQVIOQ%252526openid.identity%25253Dhttps%2525253A%2525252F%2525252Fwww.amazon.in%2525252Fap%2525252Fid%2525252Famzn1.account.AF%2526oid%253Dhttps%25253A%25252F%25252Faffiliate-program.amazon.in%25252Fhome%2526ot%253DA; session-id-time=2082787201l; csm-hit=tb:3G5F038G71ARQD9TAQ17+s-ZE61SAXWKBEJ25MX1VRB|1641454221177&t:1641454221177&adb:adblk_yes'
        }
        webpage = requests.get(self.url, headers=HEADERS)
        self.soup = BeautifulSoup(webpage.content, "lxml")
        try:
            searchResult = self.soup.findAll("div",attrs={"data-component-type": 's-search-result'})

            for item in searchResult:
                # iterating through items for title
                title=item.find("h2").find("span")
                title_value = title.string.strip().replace(',', '').lower()

                if title_value not in self.data['title']:
                    self.data['title'].append(title_value)
                    self.logging.info('title added:'+title_value)

        except AttributeError:
            self.logging.exception("url:"+self.url,AttributeError)

    def run(self):
        while True:
            self.amazonSearch()
            if not(self.ifNextPageExist(self.soup)):
                break
            self.pageIndex+=1
            self.url=self.urlCreator()
        # self.fileProcessorforPanda()
        self.fileProcessorWithoutPanda()

if __name__=="__main__":

    amazon=Amazon()
    amazon.run()
    #
    # a={'title':'my name','title2':"asdf 2"}
    #
    # print(a['title'])

