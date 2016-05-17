#!/usr/bin/python
import json
import urllib2
packages = []


def sizeof_fmt(num, suffix='B'):
    # stolen from stackoverflow, provided by Fred Cirera.
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def wget(url):
    filename = url.split('/')[-1]
    stream = urllib2.urlopen(url)
    info = stream.info()
    fileSize = info.getheaders("Content-Length")
    friendlySize = sizeof_fmt(int(fileSize[0]))
    with open(filename, 'wb') as output:
        print("Downloading {0} ({1})".format(filename, friendlySize))
        output.write(stream.read())
    return

with open("list.json", 'r') as f:
    parsed_list = json.loads(f.read())

for i in parsed_list:
    packages.append(i)

for package in packages:
    wget(parsed_list[package]["url"])
