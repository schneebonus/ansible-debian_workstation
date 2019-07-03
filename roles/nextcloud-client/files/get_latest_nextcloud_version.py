'''
Script tries to get the latest nextcloud client version.
'''
import requests
from bs4 import BeautifulSoup
import re
from distutils.version import StrictVersion

release_server = "https://download.nextcloud.com/desktop/releases/Linux/"

versions_request = requests.get(release_server)
versions = []

if versions_request.status_code == 200:
    versions_html = versions_request.text
    versions_soup = BeautifulSoup(versions_html, features="lxml")

    for link in versions_soup.findAll('a'):
        if link['href'].startswith("Nextcloud-"):
            m = re.search('Nextcloud-(.*)-x86_64.AppImage', link['href'])
            version = m.group(1)
            versions.append(version)

if len(version) > 0:
    versions.sort(key=StrictVersion)
    print(versions[-1])

else:
    # did not get the version number. Print "Error" instead.
    print("Error")
