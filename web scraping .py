import requests
import pyfiglet
import os
from bs4 import BeautifulSoup
from bs4 import *
from urllib.request import urlopen as uReq

banner = pyfiglet.figlet_format("web scarping ")
print(banner)

print("=="*60)
print(" 1.image scarping")
print(" 2.Extracking links")
print(" 3.Parsing HTML")
print("=="*60)

user_ch = str(input(" select number : "))
url_input = str(input(" please give the site uel  : "))
url = requests.get(url_input)
print(url)

if user_ch  in ( "1", "2", "3", "4", "5"):
    if user_ch == "1":
        def folder_create(images):
             try:
                     folder_name = input("Enter Folder Name:- ")
                     os.mkdir(folder_name)
             except:
                      print("Folder Exist with that name!")
                      folder_create()
             download_images(images, folder_name)



        def download_image(image,folder_name):
            count = 0
            print(f"totally {len(image)} found !!!")
            if len(image) != 0:
                for i,img in enumerate(image):
                    try:
                        image_link = image["data-srcset","data-src","data-fallback-src","src"]
                    except:
                        try:
                           image_link = img["data-srcset"]
                        except:
                            try:
                               image_link = img["data-src"]
                            except:
                                try:
                                  image_link = img["data-fallback-src"]
                                except:
                                     try:
                                       image_link = img["src"]
                                     except:
                                         pass
                try:
                  r = requests.get(image_link).content
                  try:
                    r = str(r, 'utf-8')
                  except UnicodeDecodeError:
                    with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
                        f.write(r)
                        count += 1
                except:
                    pass

                if count == len(images):
                   print("All Images Downloaded!")
                else:
                  print(f"Total {count} Images Downloaded Out of {len(images)}")
 
        def main(url):
           r = requests.get(url)
           soup = BeautifulSoup(r.text, 'html.parser')
           images = soup.findAll('img')
           folder_create(images)

        main(url_input)

    elif user_ch == "2":   
        url = url_input()
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        urls = []
        for link in soup.find_all('a'):
            print(link.get('href'))

    elif user_ch == "3":
        r = requests.get(url_input)
        print(r)
        soup = BeautifulSoup(r.content, 'html.parser')
        print(soup.prettify())
    else:
        print("please select number or your choising number is wrong ......!!!!")

