from bs4 import BeautifulSoup
import re
import urllib.request
import csv
import os
import pickle
import requests


""" retrieve product ids from department page """
def get_ids(s):
    prods = []
    for link in soup.find_all('a'):
        prod = '/us/en/catalog/products/'

        l = link.get('href')
        if l is None:
            pass
        elif prod in l:
            # print (l)
            prod_num = re.findall(r'\d+', l)[0]
            if prod_num not in prods:
                prods.append(prod_num)

    return prods

""" retrieve product information from product page """
def get_prod_info(s):
    info = []

    try:
        product_name = s.h1.span.contents[0].strip()
        info.append(product_name)
    except Exception as e:
        print("information extraction error: " + str(e))
        info.append("na")

    try:
        article_number = s.find("div", {"id": "itemNumber"}).contents[0]
        info.append(article_number)
    except Exception as e:
        print("information extraction error: " + str(e))
        info.append("na")

    try:
        product_description = s.find("div", {"id": "salesArg"}).contents[0].strip()
        info.append(product_description)
    except Exception as e:
        print("information extraction error: " + str(e))
        info.append("na")

    try:
        designer = s.find("div", {"id": "designer_right"}).contents[0].strip()
        info.append(designer)
    except Exception as e:
        print("information extraction error: " + str(e))
        info.append("na")

    try:
        num_of_ratings = s.find_all("a", {"class": "ratingsCount"})[1].contents[0].lstrip('(').rstrip(')')
        info.append(num_of_ratings)
    except Exception as e:
        print("information extraction error: " + str(e))
        info.append("na")

    try:
        overall_rating = s.find_all("a", {"class": "ratingsCount"})[0].contents[0]
        info.append(overall_rating)
    except Exception as e:
        print("information extraction error: " + str(e))
        info.append("na")

    # product_dept = soup.find("a", {"id": "lnkMainMenu8Header"}).span.contents[0]
    try:
        product_dept = s.find("a", {"id": "lnkMainMenu8Header"}).span.contents[0]
        info.append(product_dept)
    except Exception as e:
        print("information extraction error: " + str(e))
        info.append("na")

    # product_subfunction = soup.find("meta", {"name": "category_name"})['content']
    try:
        product_subfunction = s.find("meta", {"name": "category_name"})['content']
        info.append(product_subfunction)
    except Exception as e:
        print("information extraction error: " + str(e))
        info.append("na")

    js = s.find_all("script", {"type": "text/javascript", "language":"JavaScript"})[9].string
    js_2 = [s for s in js.splitlines() if "var jProductData" in s][0].strip().lstrip("var jProductData = ")
    start_product_data = "pkgInfo\":"
    temp = (js_2[js_2.index(start_product_data) + len(start_product_data):])
    temp_list = eval(temp[:temp.index("}]")] + "}]")
    # print (temp_list)

    # num_of_packages = temp_list[0]['quantity']
    try:
        num_of_packages = temp_list[0]['quantity']
        info.append(num_of_packages)
    except Exception as e:
        print("information extraction error: " + str(e))
        info.append("na")

    # package_width = temp_list[0]['widthMet']
    try:
        package_width = temp_list[0]['widthMet']
        info.append(package_width)
    except Exception as e:
        print("information extraction error: " + str(e))
        info.append("na")

    # package_height = temp_list[0]['heightMet']
    try:
        package_height = temp_list[0]['heightMet']
        info.append(package_height)
    except Exception as e:
        print("information extraction error: " + str(e))
        info.append("na")

    # package_length = temp_list[0]['lengthMet']
    try:
        package_length = temp_list[0]['lengthMet']
        info.append(package_length)
    except Exception as e:
        print("information extraction error: " + str(e))
        info.append("na")

    # package_weight = temp_list[0]['weightMet']
    try:
        package_weight = temp_list[0]['weightMet']
        info.append(package_weight)
    except Exception as e:
        print("information extraction error: " + str(e))
        info.append("na")

    # pdf link (download to a folder)
    url_base = "https://www.ikea.com"
    url_product_manual = s.find("div", {"id": "attachmentList"}).find_all('a')[1]['href']
    product_manual = url_base + url_product_manual
    # product_manual_pdf = 'manuals/' + url_product_manual + '.pdf'
    response = requests.get(product_manual)
    with open('manuals/test.pdf', 'wb') as f:
        f.write(response.content)
    print ("product manual saved to " + 'test.pdf')

    return info

if __name__ == '__main__':
    """ First, download all department pages as html """
    # with open('depts.csv', newline='', encoding='utf-8') as f:
    #     reader = csv.reader(f)
    #     dept_list = list(reader)
    # print(len(dept_list))

    # counter = 1
    # for dept_url in dept_list:
    #     ikea_url = "https://www.ikea.com" + dept_url[0]
    #     # print (ikea_url.encode('utf-8').decode('cp1252'))
    #     # print (type(ikea_url))
    #     urllib.request.urlretrieve(ikea_url.encode('utf-8').decode('cp1252'), "depts/d" + str(counter) + ".html")
    #     counter = counter + 1

    """ Next, retrieve all product ID's and pickle to file """
    # print(soup.prettify())
    # res = []
    # for filename in os.listdir('depts/'):
    #     with open("depts/" + filename) as fp:
    #         soup = BeautifulSoup(fp, features="lxml")
    #         soup_res = get_ids(soup)
    #         if soup_res is None:
    #             print (filename)
    #         else:
    #             res.extend(soup_res)
    #
    # with open('./product_ids.pkl', 'wb') as fpd:
    #     pickle.dump(res, fpd)

    """ Next, download all product pages as html """
    all_ids = []
    with open('./product_ids.pkl', 'rb') as fpl:
        all_ids = pickle.load(fpl)

    # # TODO: got 11085 products, is this right?
    # print (len(all_ids))
    # print (type(all_ids))
    # print (type(all_ids[0]))

    # test_prod = 'https://www.ikea.com/us/en/catalog/products/70246089'
    # test_prod_ood = 'https://www.ikea.com/us/en/catalog/products/00301499'
    # urllib.request.urlretrieve(test_prod.encode('utf-8').decode('cp1252'), "test_prod.html")
    # urllib.request.urlretrieve(test_prod_ood.encode('utf-8').decode('cp1252'), "test_prod_ood.html")

    all_prods = [["Product Name", "Article Number", "Product Description", "Designer", "Number of Ratings", "Overall Rating", "Product Department", "Product Subfunction", "Number of Packages", "Package Width", "Package Height", "Package Length", "Package Weight", "Product Manual"]]
    with open('test_prod.html') as fp:
        soup = BeautifulSoup(fp, features='lxml')
        soup_res = get_prod_info(soup)
        print (soup_res)

    # counter = 1
    # for prod_id in all_ids:
    #     prod_url = "https://www.ikea.com/us/en/catalog/products/" + prod_id
    #     print (prod_url.encode('utf-8').decode('cp1252'))
    #     # urllib.request.urlretrieve(ikea_url.encode('utf-8').decode('cp1252'), "depts/d" + str(counter) + ".html")
    #     counter = counter + 1
