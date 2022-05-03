from math import ceil, floor

from elasticsearch import Elasticsearch
import imgkit
from collections import Counter
import myemail as mail

threshold=5
true,false=True,False
client = Elasticsearch(['oa-elastic.yo-digital.com'],
                       http_auth=('alert', 'AlertPassw0rd'),
                       port=9200,
                       timeout=20,
                       max_retries=5,
                       retry_on_timeout=True,
                       )

def StatusCount(body):
    result={}
    for bucket in body["aggregations"]["group_by_httpStatus"]["buckets"]:
       result.update({bucket["key"]:bucket["doc_count"]})
    return result

def FaliureRate():
    natco=['hu']
    check=0
    with open('httpUrl') as fh1:
        faliure = """<html>
        <head>
        <style>
        table {
          border: 2px solid pink;
          border-collapse: collapse;
          max-width: 700px;
          width: 100%;
           height: 600px;
            font-size:16px;
             background: #f1f1f1;
        }
        tr td {
        border: 2px solid pink;
          vertical-align: center;
           text-align: center;
            height: 15px;
            background: #f0f0f0;
             padding: 10px;
             font-size: 20px;    
        }
        </style>
        </head>
        <body>
        <table>
        <th style="background: #fff; height: 100px;" colspan="5">
        <img src="https://git.yo-digital.com/uploads/-/system/appearance/header_logo/1/Telekom_Logo_2013.svg.png" width="100" height="50">
        </th>
        <tr>
        <th>Index=rdk-requestlog-prod-*</th>,<th>KibanaName=dashboard.yo</th>,<th>Query:httpUrl:$httpUrl_name AND (httpStatus:[400 TO 599])</th>
        </tr>

        <tr>


        <th style="width:20%;vertical-align: top; text-align: center; height: 25px;background: #ccc; padding: 10px;">Natco</th>
        <th style="width:20%;vertical-align: top; text-align: center; height: 25px;background: #ccc; padding: 10px;">httpUrl</th>
        <th style="width:60%;vertical-align: top; text-align: center; height: 25px;background: #ccc; padding: 10px;">httpStatus</th>
        <th style="width:20%;vertical-align: top; text-align: center; height: 25px;background: #ccc; padding: 10px;">Total-Failure-Rate</th>
        <th style="width:20%;vertical-align: top; text-align: center; height: 25px;background: #ccc; padding: 10px;">http-Count</th>
        </tr>"""
        for nat in natco:
            for line in fh1.readlines():

                line=str(line.strip())
                text='natcoCode: \"{}\" AND httpUrl: \"{}\"'.format(nat,line)
                # body=client.search(index='rdk-requestlog-prod-*', body={"query":{"bool":{"filter":{"bool":{"must":[{"range":{"@timestamp":{"gt":"now-10d/d","lte":"now/d"}}},{"query_string":{"query":text}}]}}}},"aggs":{"percentage_match_aggs":{"filters":{"other_bucket":true,"filters":{"match_bucket":{"bool":{"must":[{"range":{"httpStatus":{"to":599,"from":400}}}]}}}}}}})
                body=client.search(index='rdk-requestlog-prod-*', body={"query":{"bool":{"filter":{"bool":{"must":[{"range":{"@timestamp":{"gt":"now-10d/d","lte":"now/d"}}},{"query_string":{"query":text}}]}}}},"aggs":{"group_by_httpStatus":{"terms":{"field":"httpStatus"}}}})
                # print("this is body",body,"body ends here")
                print(StatusCount(body))
                # match=body['aggregations']['percentage_match_aggs']['buckets']['match_bucket']['doc_count']
                # other=body['aggregations']['percentage_match_aggs']['buckets']['_other_']['doc_count']
                # total=match+other
                #
                # if total == 0:
                #     agg_value=0
                #
                # else:
                #     agg_value=((match*100)/total)
                #     agg_value=round(agg_value,2)
                #
                #     if agg_value >= threshold:
                #         check=1
                #         status=StatusCount(body)
                #         statusTotalCount=len(status)
                #         i=1
                #         for code in status.keys():
                #             natco_td="<td rowspan=\"{}\">{}</td>".format(statusTotalCount,nat) if i==1 else ""
                #             line_td="<td rowspan=\"{}\">{}</td>".format(statusTotalCount,line) if i==1 else ""
                #             code_td="<td>{}</td>".format(code)
                #             agg_value_td="<td rowspan=\"{}\">{}%</td>".format(statusTotalCount,agg_value) if i==1 else ""
                #             statusCodeCount_td="<td>{}</td>".format(status[code])
                #             match_td="<td rowspan=\"{}\">{}</td>".format(statusTotalCount,match) if i==1 else ""
                #             # body_html=("<tr><td style='vertical-align: top; text-align: center; height: 15px;background: #f0f0f0; padding: 10px;font-size: 20px'>{}</td><td style='vertical-align: top; text-align: center; height: 15px;background: #f0f0f0; padding: 10px;font-size: 20px'>{}</td><td style='vertical-align: top; text-align: center; height: 15px;background: #f0f0f0; padding: 10px;font-size: 20px'>{}</td><td style='vertical-align: top; text-align: center; height: 15px;background: #f0f0f0; padding: 10px;font-size: 20px'>{}</td><td style='vertical-align: top; text-align: center; height: 15px;background: #f0f0f0; padding: 10px;font-size: 20px'>{}</td></tr>".format(natco,line,code,agg_value if i==ceil(statusCount/2) else "",status[code]))
                #             # body_html=("<tr>{}{}{}{}{}</tr>".format(natco_td,line_td,code_td,agg_value_td,statusCodeCount_td))
                #             body_html=("<tr>{}{}{}{}{}</tr>".format(natco_td,line_td,code_td,agg_value_td,match_td))
                #             faliure = faliure + body_html + "\n"
                #             i+=1

FaliureRate()
