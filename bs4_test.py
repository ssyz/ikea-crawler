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
    for link in s.find_all('a'):
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
    print("-------- PRODUCT EXTRACTION LOGS --------")

    info = []

    try:
        product_name = s.h1.span.contents[0].strip()
        info.append(product_name)
    except Exception as e:
        print("Product Name extraction error: " + str(e))
        info.append("na")

    try:
        article_number = s.find("div", {"id": "itemNumber"}).contents[0]
        info.append(article_number)
    except Exception as e:
        print("Article Number extraction error: " + str(e))
        info.append("na")

    try:
        product_description = s.find("div", {"id": "salesArg"}).contents[0].strip()
        info.append(product_description)
    except Exception as e:
        print("Product Description extraction error: " + str(e))
        info.append("na")

    try:
        designer = s.find("div", {"id": "designer_right"}).contents[0].strip()
        info.append(designer)
    except Exception as e:
        print("Designer extraction error: " + str(e))
        info.append("na")

    try:
        num_of_ratings = s.find_all("a", {"class": "ratingsCount"})[1].contents[0].lstrip('(').rstrip(')')
        info.append(num_of_ratings)
    except Exception as e:
        print("Number of Ratings extraction error: " + str(e))
        info.append("na")

    try:
        overall_rating = s.find_all("a", {"class": "ratingsCount"})[0].contents[0]
        info.append(overall_rating)
    except Exception as e:
        print("Overall Rating extraction error: " + str(e))
        info.append("na")

    # product_dept = soup.find("a", {"id": "lnkMainMenu8Header"}).span.contents[0]
    try:
        product_dept = s.find("a", {"id": "lnkMainMenu8Header"}).span.contents[0]
        info.append(product_dept)
    except Exception as e:
        print("Product Department extraction error: " + str(e))
        info.append("na")

    # product_subfunction = soup.find("meta", {"name": "category_name"})['content']
    try:
        product_subfunction = s.find("meta", {"name": "category_name"})['content']
        info.append(product_subfunction)
    except Exception as e:
        print("Product Subfunction extraction error: " + str(e))
        info.append("na")

    all_varjproductdata = ""
    temp_list = [{'weightMet': 'na', 'widthMet': 'na', 'quantity': 'na', 'lengthMet': 'na', 'heightMet': 'na'}]
    try:
        js = s.find_all("script", {"type": "text/javascript", "language":"JavaScript"})
        for j in js:
            for x in j.contents:
                if "var jProductData" in str(x):
                    all_varjproductdata = str(x[x.index('{"product\":'):x.index('var jsonProduct')]).strip()
                    j_product_data = x[x.index("pkgInfo\":")+len("pkgInfo\":"):x.index("}]}]")] + "}]"
                    temp_list = eval(j_product_data)
    except Exception as e:
        print("Product Data extraction error: " + str(e))

    # write the line containing “var jProductData” into a single file (jproductdata.csv), one per line
    # first column is article number, second column is jproductdata
    #### WRITE TO CSV
    # all_varjproductdata_list = [info[1], all_varjproductdata]
    # with open("jproductdata.csv", "a") as fp:
    #     wr = csv.writer(fp)
    #     wr.writerow(all_varjproductdata_list)

    # num_of_packages = temp_list[0]['quantity']
    try:
        num_of_packages = temp_list[0]['quantity']
        info.append(num_of_packages)
    except Exception as e:
        print("Quantity extraction error: " + str(e))
        info.append("na")

    # package_width = temp_list[0]['widthMet']
    try:
        package_width = temp_list[0]['widthMet']
        info.append(package_width)
    except Exception as e:
        print("Package Width extraction error: " + str(e))
        info.append("na")

    # package_height = temp_list[0]['heightMet']
    try:
        package_height = temp_list[0]['heightMet']
        info.append(package_height)
    except Exception as e:
        print("Package Height extraction error: " + str(e))
        info.append("na")

    # package_length = temp_list[0]['lengthMet']
    try:
        package_length = temp_list[0]['lengthMet']
        info.append(package_length)
    except Exception as e:
        print("Package Length extraction error: " + str(e))
        info.append("na")

    # package_weight = temp_list[0]['weightMet']
    try:
        package_weight = temp_list[0]['weightMet']
        info.append(package_weight)
    except Exception as e:
        print("Package Weight extraction error: " + str(e))
        info.append("na")


    # pdf link (download to a folder)
    try:
        url_base = "https://www.ikea.com"
        url_product_manual = s.find("div", {"id": "attachmentList"}).find_all('a')[0]['href']

        url_pdf = url_product_manual[14:-4].replace("/", "")
        product_manual = url_base + url_product_manual
        response = requests.get(product_manual)
        pdf_name = url_pdf + '.pdf'
        info.append(pdf_name)
        #### DOWNLOAD
        # with open('assembly/' + pdf_name, 'wb') as f:
        #     f.write(response.content)
        # print ("product assembly instructions saved to " + pdf_name)
    except Exception as e:
        print("Product assembly instructions extraction error: " + str(e))

    print (info)
    print("---------------- END ----------------")
    print ()

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
    # all_ids = []
    # with open('./product_ids.pkl', 'rb') as fpl:
    #     all_ids = pickle.load(fpl)
    #     # print (all_ids)
    #
    # # # TODO: got 11085 ids --> 8050 products (3035 not found), is this right?
    # # print (len(all_ids))
    # # print (type(all_ids))
    # # print (type(all_ids[0]))
    #
    # # test_prod = 'https://www.ikea.com/us/en/catalog/products/70246089'
    # # test_prod_2 = 'https://www.ikea.com/us/en/catalog/products/30081467'
    # # test_prod_2 = 'https://www.ikea.com/us/en/catalog/products/20275814'
    # # test_prod_ood = 'https://www.ikea.com/us/en/catalog/products/00301499'
    #
    # counter = 1
    # for prod_id in all_ids:
    #     prod_url = "https://www.ikea.com/us/en/catalog/products/" + prod_id
    #     try:
    #         urllib.request.urlretrieve(prod_url.encode('utf-8').decode('cp1252'), "prods/p" + str(counter) + ".html")
    #         counter = counter + 1
    #     except Exception as e:
    #         print("product " + prod_url + " not found: " + str(e))
    #         print("SKIPPED")

    """ Finally, download product information to csv """
    all_prods = [["Product Name", "Article Number", "Product Description", "Designer", "Number of Ratings", "Overall Rating", "Product Department", "Product Subfunction", "Number of Packages", "Package Width", "Package Height", "Package Length", "Package Weight", "Assembly Instructions"]]
    for i in range(1, 8051):
        product_file = 'prods/p' + str(i) + '.html'
        print ()
        print (product_file)
        with open(product_file) as fp:
            soup = BeautifulSoup(fp, features='lxml')
            soup_res = get_prod_info(soup)
            all_prods.append(soup_res)

    # write results to CSV
    file_w = open('results.csv', 'w', newline='')
    file_writer = csv.writer(file_w)
    for entry in all_prods:
        file_writer.writerow(entry)
    file_w.close()
