import bs4, numpy, pandas, requests

baseurl = "https://www.amazon.ca/s?i=electronics&bbn=677230011&rh=n%3A667823011%2Cn%3A%21677211011%2Cn%3A677230011%2Cp_89%3ACanon&pf_rd_i=677230011&pf_rd_m=A3DWYIK6Y9EEQB&pf_rd_p=f16562e7-0166-4ff7-9483-53f1054cbad7&pf_rd_p=f16562e7-0166-4ff7-9483-53f1054cbad7&pf_rd_r=43Q5KGE2XMHT9S05FBTZ&pf_rd_r=43Q5KGE2XMHT9S05FBTZ&pf_rd_s=merchandised-search-leftnav&pf_rd_t=101&ref=ca_ce_lnav_cam_s1l2_canon"

page = requests.get(baseurl)
startpage = 1

pagesoup = bs4.BeautifulSoup(page.content, features="html.parser")
nextbutton = pagesoup.find_all('ul', class_="pagination")
print(pagesoup)
