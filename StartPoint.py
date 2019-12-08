
from scrapy.cmdline import execute
# execute(['scrapy','crawl','Lianjia'])
execute(['scrapy','crawl','Lianjia', '-o', 'Lianjia_result.csv', '-t', 'csv'])

