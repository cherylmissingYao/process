import urllib2

#url = "http://yotta.xjtushilei.com:8083/domain/getDomainDetailAsRDF?domainName=Data%20Structure"
url = "http://yotta.xjtushilei.com:8083/domain/getDomainTreeByDomainName?domainName=Data%20Structure"

rq = urllib2.Request(url)
rs = urllib2.urlopen(rq).read()

#f = open('./data_structure/getDomainTreeByDomainName.txt', 'w')
#f.write(rs)
#f.close()
