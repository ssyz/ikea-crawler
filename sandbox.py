from bs4 import BeautifulSoup
from selenium import webdriver


browser = webdriver.Firefox() #replace with .Firefox(), or with the browser of your choice
url = "https://www.ikea.com/us/en/catalog/products/80155205/"
browser.get(url) #navigate to the page
innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
print (innerHTML)





# product_file = 'test_prod.html'
# with open(product_file) as fp:
#     soup = BeautifulSoup(fp, features='lxml')
#     all_varjproductdata = []
#     js = soup.find_all("script", {"type": "text/javascript", "language":"JavaScript"})
#     for j in js:
#         for x in j.contents:
#             if "var jProductData" in str(x):
#                 j_product_data = x[x.index('{"product\":'):x.index('var jsonProduct')]
#                 print (str(j_product_data).strip())



# product_file = 'test_prod.html'
# with open(product_file) as fp:
#     soup = BeautifulSoup(fp, features='lxml')
#     # manuals vs assembly instuctions, which do you want?
#     url_product_manual = soup.find("div", {"id": "attachmentList"}).find_all('a')
#     print (url_product_manual)
#
#     # js = soup.find_all("script", {"type": "text/javascript", "language":"JavaScript"})
#     # for j in js:
#     #     for x in j.contents:
#     #         if "var jProductData" in str(x):
#     #             j_product_data = x[x.index("pkgInfo\":")+len("pkgInfo\":"):x.index("}]}]")] + "}]"
#     #             j_product_data_list = eval(j_product_data)
#     #             print (j_product_data_list)
#     #             print (type(j_product_data_list))


# js = '{"product":{"items":[{"custMaterials":"Base/ Outer tube/ Mounting plate: Steel, Epoxy/polyester powder coating<br/>Cover/ Adjustment lever: Stainless steel<br/>Foot ring/ Stop fitting: Polypropylene<br/>Ring: Polyamide<br/>Foot rest: Aluminum, Stainless steel, Epoxy/polyester powder coating<br/>Seat/ Lid: Reinforced polypropylene<br/>","descriptiveAttributes":{},"imperial":"Tested for: 243 lb<br/>Width: 15 \\"<br/>Depth: 14 1/8 \\"<br/>Height: 33 1/8 \\"<br/>Diameter: 16 1/2 \\"<br/>Seat height: 29 7/8 \\"<br/>Min. seat height: 22 \\"<br/>Max. seat height: 29 7/8 \\"<br/><br/>","catEntryId":"3355120","dualCurrencies":false,"pkgInfoArr":[{"articleNumber":"70246089","pkgInfo":[{"heightImp":"8 &#34;","weightImp":"28 lb 2 oz","weightMet":"12.76 kg","widthImp":"17 ¾ &#34;","widthMet":"45 cm","quantity":"1","consumerPackNo":1,"lengthImp":"17 ¾ &#34;","lengthMet":"45 cm","heightMet":"20 cm"}]}],"type":"Bar stool","reqAssembly":true,"soldSeparately":"","name":"JANINGE","bti":false,"attachments":[{"atcharray":[{"attachmentPath":"/us/en/assembly_instructions/janinge-bar-stool__AA-1263780-5_pub.pdf","articleNumber":"70246089","attachmentName":"JANINGE Bar stool"}],"name":"Assembly instructions","type":"ASSEMBLY_INSTRUCTIONS"},{"atcharray":[{"attachmentPath":"/us/en/manuals/janinge-bar-stool__AA-2120737-1_pub.pdf","articleNumber":"70246089","attachmentName":"JANINGE Bar stool"}],"name":"Manuals","type":"MANUALS"}],"partNumber":"70246089","avg_rating":"3.7","validDesign":["white"],"goodToKnowPIP":"Suitable for bar heights between 35⅜&#34; and 43¼&#34;.<br/>This stool has been tested for public use and meets the requirements for safety, durability and stability set forth in the following standards: EN 16139 and ANSI/BIFMA x5.1.<br/>","techInfoArr":[],"careInst":"Wipe clean regulary with a detergent for plastic.<br/>","extendedContext":[{"articleNumber":"70246089","extendedContext":[{"avg_rating":"3.7","rating_count":"39","gprAvgRating":"3.7","ratingRange":"5","gprRatingCount":"39"}]}],"designer":"John/Jonas/Petrus/Paul/Caroline","nopackages":"1","goodToKnow":"Suitable for bar heights between 35⅜&#34; and 43¼&#34;.<br/>This stool has been tested for public use and meets the requirements for safety, durability and stability set forth in the following standards: EN 16139 and ANSI/BIFMA x5.1.<br/>","url":"/us/en/catalog/products/70246089/","packagePopupUrl":"/us/en/catalog/packagepopup/70246089/","availabilityUrl":"/us/en/catalog/availability/70246089/","environment":"","rating_count":"39","color":"white","custBenefit":"<cbs><cb><t>You sit comfortably thanks to the scooped seat.<\\/t><\\/cb><cb><t>Easy to adjust in heights using one hand.<\\/t><\\/cb><cb><t>With footrest for relaxed sitting posture.<\\/t><\\/cb><cb><t>A special surface treatment makes the seat extra scratch resistant.<\\/t><\\/cb><\\/cbs>","metric":"Tested for: 110 kg<br/>Width: 38 cm<br/>Depth: 36 cm<br/>Height: 84 cm<br/>Diameter: 42 cm<br/>Seat height: 76 cm<br/>Min. seat height: 56 cm<br/>Max. seat height: 76 cm<br/><br/>","buyable":true,"prices":{"comparisonPriceExists":false,"hasTemporaryFamilyOffer":false,"hasFamilyPrice":false,"usesUnitPriceMeasure":false,"isUnitPricePrimary":false,"normal":{"priceNormal":{"priceExclVat":"$109.00","value":"$109.00","rawPrice":109},"priceNormalDual":{},"priceNormalPerUnit":{"unit":""}},"hasEcoFee":false,"enablenlpinterval":0,"hasPrfCharge":false},"images":{"zoom":["/PIAimages/0368701_PE549626_S5.JPG","/PIAimages/0445167_PE595581_S5.JPG","/PIAimages/0445123_PE595537_S5.JPG","/PIAimages/0451760_PE600742_S5.JPG","/PIAimages/0445123_PE595537_S5.JPG","/PIAimages/0444209_PE594767_S5.JPG","/PIAimages/0441743_PE593528_S5.JPG","/PIAimages/0444239_PE594814_S5.JPG","/PIAimages/0437143_PE590689_S5.JPG"],"normal":["/PIAimages/0368701_PE549626_S3.JPG","/PIAimages/0445167_PE595581_S3.JPG","/PIAimages/0445123_PE595537_S3.JPG","/PIAimages/0451760_PE600742_S3.JPG","/PIAimages/0445123_PE595537_S3.JPG","/PIAimages/0444209_PE594767_S3.JPG","/PIAimages/0441743_PE593528_S3.JPG","/PIAimages/0444239_PE594814_S3.JPG","/PIAimages/0437143_PE590689_S3.JPG"],"thumb":["/PIAimages/0368701_PE549626_S2.JPG"],"small":["/PIAimages/0368701_PE549626_S1.JPG"],"large":["/us/en/images/products/janinge-bar-stool-white__0368701_PE549626_S4.JPG","/us/en/images/products/janinge-bar-stool-white__0445167_PE595581_S4.JPG","/us/en/images/products/janinge-bar-stool-white__0445123_PE595537_S4.JPG","/us/en/images/products/janinge-bar-stool-white__0451760_PE600742_S4.JPG","/us/en/images/products/janinge-bar-stool-white__0445123_PE595537_S4.JPG","/us/en/images/products/janinge-bar-stool-white__0444209_PE594767_S4.JPG","/us/en/images/products/janinge-bar-stool-white__0441743_PE593528_S4.JPG","/us/en/images/products/janinge-bar-stool-white__0444239_PE594814_S4.JPG","/us/en/images/products/janinge-bar-stool-white__0437143_PE590689_S4.JPG"]},"californiaTitle20Product":false,"summaryBenefit":"Challenged to solve the equation of combining design, function and quality in one chair, our designers came up with JANINGE chair. Durable enough for restaurant use \\u2013 with a design you want to take home.","designerThoughts":{"text":"&#34;JANINGE started out as a challenge \\u2013 to create a chair that could handle the everyday wear and tear of a restaurant, yet be well-designed enough to take home. We needed to design for strength, durability and stability, as well as high quality and comfort. Thanks to close cooperation and team spirit, we managed to solve the equation of combining design, function and quality in the same chair \\u2013 and at a low price.&#34;","heading":"Designers John, Jonas, Petrus, Paul and Caroline"}}],"catEntryId":"3437484","attributes":[],"partNumber":"P70246089 [GENERICPRODUCT]"}};'
#
# start_product_data = "pkgInfo\":"
# temp = (js[js.index(start_product_data) + len(start_product_data):])
# temp_list = eval(temp[:temp.index("}]")] + "}]")
# # print (temp_list)
# print (temp_list[0]['quantity'])
# print (temp_list[0]['widthMet'])
# print (temp_list[0]['heightMet'])
# print (temp_list[0]['lengthMet'])
# print (temp_list[0]['weightMet'])

# js = s.find_all("script", {"type": "text/javascript", "language":"JavaScript"})[9].string
# js_2 = [s for s in js.splitlines() if "var jProductData" in s][0].strip().lstrip("var jProductData = ")
# start_product_data = "pkgInfo\":"
# temp = (js_2[js_2.index(start_product_data) + len(start_product_data):])
# temp_list = eval(temp[:temp.index("}]")] + "}]")
# print (temp_list)
