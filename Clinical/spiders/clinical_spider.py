import scrapy
import re
import time
from Clinical.items import ClinicalItem
from Clinical.items import RecordItem
from Clinical.items import ShowItem
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


class ClinicalSpider(CrawlSpider):
    name = "clinical"
    # allowed_domains = ["clinicaltrials.gov"]
    # start_urls = [
    #     #"http://www.clinicaltrials.gov/ct2/results?recr=Recruiting&term=cancer&state1=NA%3AUS%3AAL"
    #     "http://www.clinicaltrials.gov/ct2/results?recr=Recruiting&term=cancer&state1=NA%3AUS%3AAK"
    # ]
    start_urls = []
    rules = (
    # #     # Extract links matching 'category.php' (but not matching 'subsection.php')
    # #     # and follow links from them (since no callback means follow=True by default).
    # #     # Rule(LinkExtractor(allow=(r'ct2/show/', ), deny=('subsection\.php', ), callback='parse_item')),
    # #     # Extract links matching 'item.php' and parse them with the spider's method parse_item
    # #     # Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
    # #     Rule(LinkExtractor(allow=(r'ct2/show/',)), callback='parse_item',follow='True'), 

        # Rule(LinkExtractor(allow=(r'ct2/show/',), restrict_xpaths='//div[@class="indent1 header3"]/table[@class="data_table margin-top"]/tr[@style="vertical-align:top"]'), follow='True'),                    
        # Rule(SgmlLinkExtractor(allow=(r'ct2/result',), restrict_xpaths='//div[@id="list_page_controls_bottom"]/a[@title="Show next page of results"]'), follow=True), 
        Rule(SgmlLinkExtractor(allow=(r'ct2/show/NCT',)),callback='parse_item', process_links='create_link',),

        Rule(SgmlLinkExtractor(allow=(r'ct2/result',), restrict_xpaths='//div[@id="list_page_controls_bottom"]/a[@title="Show next page of results"]'), follow=True,),   
        
        # Rule(SgmlLinkExtractor(allow=(r'ct2/show/record/',)), callback='parse_item'),
    )   

    def __init__(self):
        super(ClinicalSpider,self).__init__()
        self.start_urls = self.create_start_url()
        pass


    # def parse(self, response):
        # for sel in response.xpath('//div[@class="indent1 header3"]/table[@class="data_table margin-top"]/tr[@style="vertical-align:top"]/td[3]'):
        #     item = ClinicalItem()
        #     item['title'] = sel.xpath('a/text()').extract()
        #     item['link'] = sel.xpath('a/@href').extract()
        #     item['condition'] = sel.xpath('table/tr[1]/td/text()').extract()
        #     interventions = sel.xpath('table/tr[2]/td/text()').extract()
        #     #item['interventions'] = re.sub('a'," ",interventions)
        #     #item['interventions'] = re.sub(r'\u00a0'," ",interventions[1])
        #     item['interventions'] = interventions
        #     yield item


    def parse_item(self,response):
        #print "------" + response.url + "\n"
        #print response.xpath("//div/h1/text()").extract()
        item = RecordItem()
        base_url = "http://www.clinicaltrials.gov"
        # item['name'] = response.xpath("//div/h1/text()").extract()
        item['record_id'] = response.xpath("//div[@id='main-content']/div/div[@class='identifier']/text()").extract()[0]
        item['url'] = response.url
        # Tracking Information
        table_path = "//div[@class='indent1']/table[@class='data_table']/"
        item['FRD'] = self.extract_text(response.xpath(table_path+"tr[2]/td/text()").extract())
        item['LUD'] = self.extract_text(response.xpath(table_path+"tr[3]/td/text()").extract())
        item['SD'] = self.extract_text(response.xpath(table_path+"tr[4]/td//text()").extract())
        item['EPCD1'] = self.extract_text(response.xpath(table_path+"tr[5]/td//text()").extract())
        item['CPOM'] = self.extract_text(response.xpath(table_path+"tr[6]/td//text()").extract())
        item['OPOM'] = self.extract_text(response.xpath(table_path+"tr[7]/td//text()").extract())
        item['CH'] = base_url + self.extract_text(response.xpath(table_path+"tr[8]/td/a/@href").extract())
        item['CSOM'] = self.extract_text(response.xpath(table_path+"tr[9]/td//text()").extract())
        item['OSOM'] = self.extract_text(response.xpath(table_path+"tr[10]/td//text()").extract())
        item['COOM'] = self.extract_text(response.xpath(table_path+"tr[11]/td//text()").extract())
        item['OOOM'] = self.extract_text(response.xpath(table_path+"tr[12]/td//text()").extract())
        # # Descriptive Information
        item['BT'] = self.extract_text(response.xpath(table_path+"tr[15]/td//text()").extract())
        item['OT'] = self.extract_text(response.xpath(table_path+"tr[16]/td//text()").extract())
        item['BS'] = self.extract_text(response.xpath(table_path+"tr[17]/td//text()").extract())
        item['DD'] = self.extract_text(response.xpath(table_path+"tr[18]/td//text()").extract())
        item['ST'] = self.extract_text(response.xpath(table_path+"tr[19]/td//text()").extract())
        item['SP'] = self.extract_text(response.xpath(table_path+"tr[20]/td//text()").extract())
        item['SDs'] = self.extract_text(response.xpath(table_path+"tr[21]/td//text()").extract())
        item['Co'] = self.extract_text(response.xpath(table_path+"tr[22]/td//text()").extract())
        item['Intv'] = self.extract_text(response.xpath(table_path+"tr[23]/td//text()").extract())
        item['SA'] = self.extract_text(response.xpath(table_path+"tr[24]/td//text()").extract())
        item['Pub'] = self.extract_text(response.xpath(table_path+"tr[25]/td//text()").extract())
        # # Recruitment Information
        item['RS'] = self.extract_text(response.xpath(table_path+"tr[29]/td//text()").extract())
        item['EE'] = self.extract_text(response.xpath(table_path+"tr[30]/td//text()").extract())
        item['CD'] = self.extract_text(response.xpath(table_path+"tr[31]/td//text()").extract())
        item['EPCD2'] = self.extract_text(response.xpath(table_path+"tr[32]/td//text()").extract())
        item['EC'] = self.extract_text(response.xpath(table_path+"tr[33]/td//text()").extract())
        item['Gend'] = self.extract_text(response.xpath(table_path+"tr[34]/td//text()").extract())
        item['Age'] = self.extract_text(response.xpath(table_path+"tr[35]/td//text()").extract())
        item['AHV'] = self.extract_text(response.xpath(table_path+"tr[36]/td//text()").extract())
        item['Cont'] = self.extract_text(response.xpath(table_path+"tr[37]/td//text()").extract())
        item['LC'] = self.extract_text(response.xpath(table_path+"tr[38]/td//text()").extract())
        # # Administrative Information        
        item['NCTN'] = self.extract_text(response.xpath(table_path+"tr[41]/td//text()").extract())
        item['OSID'] = self.extract_text(response.xpath(table_path+"tr[42]/td//text()").extract())
        item['HDMC'] = self.extract_text(response.xpath(table_path+"tr[43]/td//text()").extract())
        item['RP'] = self.extract_text(response.xpath(table_path+"tr[44]/td//text()").extract())
        item['SS'] = self.extract_text(response.xpath(table_path+"tr[45]/td//text()").extract())
        item['Coll'] = self.extract_text(response.xpath(table_path+"tr[46]/td//text()").extract())
        item['Inves'] = self.extract_text(response.xpath(table_path+"tr[47]//td/text()").extract())
        item['IPB'] = self.extract_text(response.xpath(table_path+"tr[48]//td/text()").extract())
        item['VD'] = self.extract_text(response.xpath(table_path+"tr[49]//td/text()").extract())



        # time.sleep(0.1)
        return item

    def extract_text(self,data):
        result = ""
        if len(data) > 0:
            result = data[0].replace(u'\xa0',' ')
        return result


    def parse_show(self,response):
        item = ShowItem()
        item['title'] = response.xpath("//div[@class='results-summary']/strong/text()").extract()
        item['url'] = response.url
        time.sleep(1)
        return item  

    def create_link(self,links): 
        new_links = []
        for link in links:
            link.url = link.url.replace(r'show',r'show/record')
            new_links.append(link)
            # print link.url
            # time.sleep(1)
        return new_links


        # newlinks = []
        # for link in links
        #     print link
        #     newlinks.append(link)
        # return newlinks   

    def create_start_url(self):
        urls = []
        base_url = "http://www.clinicaltrials.gov/ct2/results?"
        options = self.parse_conf("query.conf")
        # print options
        if "term" in options:
            base_url += "term=" + options["term"]
        else:
            base_url += "term="

        if "recr" not in options or options["recr"].lower()=="all":
            options["recr"] = ""
        if "state1" not in options or options["state1"].lower()=="all":
            options["state1"] = ""
        base_url += "&recr=" + options["recr"] + "&state1=" + options["state1"]
        urls.append(base_url)
        return urls

    def parse_conf(self,filename):
        options = {}
        f = open(filename)
        for line in f:
            line = line.strip()
            if '#' in line:
                (line,comment) = line.split('#',1)
            if not line:
                continue
            if '=' in line:
                option,value = line.split('=',1)
                option = option.strip()
                value = value.strip()
                options[option] = value
        f.close()
        return options