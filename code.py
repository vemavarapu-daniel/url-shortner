import pyshorteners
link = input("link:")
uplink=pyshorteners.Shorteners()
link=uplink.tinyurl.short(link)
print(link)
