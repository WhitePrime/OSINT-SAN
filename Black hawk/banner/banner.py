#bafomet soft
import base64, codecs
magic = 'aW1wb3J0IHJhbmRvbQppbXBvcnQgdGltZQppbXBvcnQgZGF0ZXRpbWUKI2RldiBieSBiYWZvbWV0CiMgU2V0IGNvbG9yCgpXSFNMID0gJ1wwMzNbMTszMm0nCkVOREwgPSAnXDAzM1swbScKUkVETCA9ICdcMDMzWzA7MzFtJwpHTlNMID0gJ1wwMzNbMTszNG0nCgpiYW5uZXIxID0gJycnIAp7MX0gIF9fX19fX18gICBfXyAgICAgICAgICAgICAgICAgICAgICBfXyAgICAgICAgICAgICAgX18gICAgX18gICAgICAgICAgICAgICAgICAgICAgICAgIF9fICAgICAgICAKezF9IHwgICAgICAgXCB8ICBcICAgICAgICAgICAgICAgICAgICB8ICBcICAgICAgICAgICAgfCAgXCAgfCAgXCAgICAgICAgICAgICAgICAgICAgICAgIHwgIFwgICAgICAgezF9ezB9W3syfSBEZXZlbG9wZXIgYnkgezF9QmFmb21ldHsxfXswfV0KezF9IHwgJCQkJCQkJFx8ICQkICBfX19fX18gICAgX19fX19fXyB8ICQkICAgX18gICAgICAgfCAkJCAgfCAkJCAgX19fX19fICAgX18gICBfXyAgIF9fIHwgJCQgICBfXyAgezF9ezB9W3syfSDQoNCw0LfRgNCw0LHQvtGC0LDQvdC+INC00LvRjyDQutC40LHQtdGALdCw0YDQvNC40LkgU05HIHsxfXswfV0KezF9IHwgJCRfXy8gJCR8ICQkIHwgICAgICBcICAvICAgICAgIFx8ICQkICAvICBcICAgICAgfCAkJF9ffCAkJCB8ICAgICAgXCB8ICBcIHwgIFwgfCAgXHwgJCQgIC8gIFwgezF9ezB9W3syfSDQmNGB0L/QvtC70YzQt9GD0LnRgtC1INGBINGD0LTQvtCy0L7Qu9GM0YHRgtCy0LjQtdC8LnsxfXswfV0KezF9IHwgJCQgICAgJCR8ICQkICBcJCQkJCQkXHwgICQkJCQkJCR8ICQkXy8gICQkICAgICAgfCAkJCAgICAkJCAgXCQkJCQkJFx8ICQkIHwgJCQgfCAkJHwgJCRfLyAgJCQgezF9ezB9W3syfSDQktC+INGB0LvQsNCy0YMg0Lgg0YfQtdGB0YLRjCwg0LfQsCDRgdC40YHRjNC60Lgg0Lgg0LzQuNC90LXRgnsxfXswfV0KezF9IHwgJCQkJCQkJFx8ICQkIC8gICAgICAkJHwgJCQgICAgICB8ICQkICAgJCQgICAgICAgfCAkJCQkJCQkJCAvICAgICAgJCR8ICQkIHwgJCQgfCAkJHwgJCQgICAkJCAgezF9ezB9W3syfSBUZWNobmljYWwgc3VwcG9ydCB7MH10ZyB7MX1Ac2F0YW5hNjY2bXggezF9ezB9XQp7MX0gfCAkJF9fLyAkJHwgJCR8ICAkJCQkJCQkfCAkJF9fX19fIHwgJCQkJCQkXCAgICAgICB8ICQkICB8ICQkfCAgJCQkJCQkJHwgJCRfLyAkJF8vICQkfCAkJCQkJCRcICB7MX17MH1bezJ9IE9mZmljaWFsIGNoYW5uZWwgezB9dGcgezF9QG9zaW50X3Nhbl9mcmFtZXdvcmsgezF9ezB9XQp7MX0gfCAkJCAgICAkJHwgJCQgXCQkICAgICQkIFwkJCAgICAgXHwgJCQgIFwkJFwgICAgICB8ICQkICB8ICQkIFwkJCAgICAkJCBcJCQgICAkJCAgICQkfCAkJCAgXCQkXCB7MX17MH1bezJ9INCd0LXQutC+0YLQvtGA0YvQvCDQvNC+0LTRg9C70Y/QvCwg0YLRgNC10LHRg9GO0YLRgdGPIHJvb3Qg0L/RgNCw0LLQsC4gezF9ezB9XQp7MX0gIFwkJCQkJCQkICBcJCQgIFwkJCQkJCQkICBcJCQkJCQkJCBcJCQgICBcJCQgICAgICAgXCQkICAgXCQkICBcJCQkJCQkJCAgXCQkJCQkXCQkJCQgIFwkJCAgIFwkJCB7MX17MH1bezJ9IEdpdEh1YiB7MX1odHRwczovL2dpdGh1Yi5jb20vQmFmb21ldDY2NiB7MX17MH1dCgp7Mn1GcmFtZXdvcmsgOnsyfXswfSBPU0lOVCBTQU4uezB9ICAgIC'
love = 'NtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPO7ZU1ormS9VSVtrmO9KFO7Za0t0XQDfAPk0Y7EtgPj0YKEtvQDfvQDhgP+0Y3EtqP+0YiDhPQEtFOlo290VAP/0LQDfAPl0YQDiAP4YvO7Za0tVPNXrmW9E2kiLzSfVUIjMTS0MKfjsFOPoTSwnlOVLKqeVULgZv4jVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPO7ZU1ormS9VR4trmO9KFO7Za0t0XQDfAPk0Y7EtgPj0YKEtvQDfvQDhgP+0Y3EtqP+0YiDhPjt0LYDigP70LmDhgP+VAPk0YKDglOlo290VAP/0LQDfAPlYafjsDc7ZK1PLJMioJI0VUAiMaDtrmS9VPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPO7ZU1ormS9VTEyqvO7ZU1qVUflsFQDy9P90YQEu9P40LVt0YVt0LQDfAP30LQDfAPk0Y7EtgP60YHhVAPt0YQDfqP+0LYDfAP10LVt0LsDfATO0LYDhATU0Y3Div4hrmO9PvNtWlpaYzMipz1uqPuUGyAZYPOFEHEZYPOKFSAZXDbXLzShozIlZvN9VPpaW3fksDbtVS9sK19sKlNtVPNtVPNtVPNtVPOsKlNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtK19sK19sVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNXVP8tVPNtVPOpVPNtVPNtVPNtVPO8VPOpVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtYlNtVPNtVSjtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVNc8VPNxWPDxWPEpVS9sVPNtVS9sVUjtWPEsK19sVPNtVS9sK19sKlNtVPOsK19sK18tVPNtVPNtVUjtVPDxWPDxWSjtVS9sK19sKlNtVS9sK19sK18tVPNXsPNxWPNtVSjxWUjtVSjtVUjtVSk8VPDxVPNtVSjtVP8tVPNtVPOpVPNiVPNtVPNtKPNtVPNtVPO8VPDxK19sKPDxVUjtVPNtVPOpVUjtVPNtVPNtKPNtPajtWPDtVPNtVPO8VPDxVPO8VPDxsPNxWPDxWPDxKUjtVPDxWPDxWSk8VPNxWPDxWPEpVPNtVPNtVSjxWPNtVPOpVPNtKPDxWPDxWSk8VPDxWPDxWPEpVNc8VPDxVPNtK18tsPNxWPNtsPNxWUjtWPDtVUjtWPE8VPDxVPNtVPDxsPNxWPNtVSjxWPNtVPNtVPOsKPDxWPDxWSjtYlNtVPNtVPDxsPNxWPNtsPNxWPNXsPNxWS9sYlNtKUjtWPEsKl8tWPE8VPDxK18iVPDxsPNxWPDxWPDxWUjtWPDtVPNtVPNtVPNtVPO8VPOpK198VPDxsPNtWPDxWPDxWUjtWPDtVUjtWPDtPvOpWPDtVPNtWPDtKPDxVPNtVPDxsPNxWPNtVPNxWPOpWPDtVPNtVSk8VPDxVPNtVPNtVPNtVPNtVSjxWPNtVPNxWPOpWPDtVPNtWPE8VPDxVPO8VPDxVNbtVSjxWPDxWPDtVS9pWPDxWPDxWPOpWPDxWPDxWPNtVSjxWPDxWPDxVSjxWPNtVPNtVPNtVPNtVPNtKPDxWPDxWPNtVSjxWPDxWPDxVSjxWPNtVSjxWPNXVPNtVPNtVPNtVUjtVSksK3jtWPDtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNt'
god = 'ICAgICAgIAogICAgICAgICAgIFwkJCAgICAkJCAgICAgICAgICAgICAgICAKICAgICAgICAgICAgXCQkJCQkJCAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCnsyfUZyYW1ld29yayA6ezJ9ezB9IE9TSU5UIFNBTi57MH0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgezB9W3sxfSBSIHswfV0gezJ9INCg0LDQsdC+0YLQsNC10YIg0LIg0LrQvtC90YHQvtC70Lgg0YEgcm9vdCDQv9GA0LDQstCw0LzQuC4gezJ9ICAgCnsyfUdsb2JhbCB1cGRhdGV7MH0gQmxhY2sgSGF3ayB2LTIuMCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgezB9W3sxfSBOIHswfV0gezJ9INCg0LDQsdC+0YLQsNC10YIg0LIg0LrQvtC90YHQvtC70LgsINGC0L7Qu9GM0LrQviDQsdC10Lcgcm9vdCDQv9GA0LDQsi4gezB9ICAKezF9QmFmb21ldCBzb2Z0IHsxfSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7MH1bezF9IGRldiB7MH1dIHsyfSDQl9C90LDRh9C40YIg0LIg0YDQsNC30YDQsNCx0L7RgtC60LUuINCg0LDQsdC+0YLQsNC10YIg0YfQsNGB0YLQuNGH0L3Qvi4uezB9CiAnJycuZm9ybWF0KEdOU0wsIFJFREwsIFdIU0wpCgpiYW5uZXIzID0gJycnIHswfQoKIOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKVlyAgIOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilojilojilojilojilojilZfilojilojilojilojilojilojilZcgICAgICDilojilojilojilojilojilojilZcg4paI4paI4paI4paI4paI4paI4paI4pWX4paI4paI4pWX4paI4paI4paI4pWXICAg4paI4paI4pWX4paI4paI4paI4paI4paI4paI4paI4paI4pWXIHsxfXswfVt7Mn0gRGV2ZWxvcGVyIGJ5IHsxfUJhZm9tZXR7MX17MH1dCuKWiOKWiOKVlOKVkOKVkOKVkOKVkOKVneKVmuKWiOKWiOKVlyDilojilojilZTilZ3ilojilojilZTilZDilZDilojilojilZfilojilojilZTilZDilZDilZDilZDilZ3ilojilojilZTilZDilZDilojilojilZcgICAg4paI4paI4pWU4pWQ4pWQ4pWQ4paI4paI4pWX4paI4paI4pWU4pWQ4pWQ4pWQ4pWQ4pWd4paI4paI4pWR4paI4paI4paI4paI4pWXICDilojilojilZHilZrilZDilZDilojilojilZTilZDilZDilZ0gezF9ezB9W3syfSDQmNGB0L/QvtC70YzQt9GD0LnRgtC1INGBINGD0LTQvtCy0L7Qu9GM0YHRgtCy0LjQtdC8LnsxfXswfV0K4paI4paI4pWRICAgICAg4pWa4paI4paI4paI4paI4pWU4pWdIOKWiOKWiOKWiOKWiOKWiOKWiOKVlOKVneKWiOKWiOKWiOKWiOKWiOKVlyAg4paI4paI4paI4paI4paI4paI4pWU4pWdICAgIOKWiOKWiOKVkSAgIOKWiOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKVkeKWiOKWiOKVlOKWiOKWiOKVlyDilojilojilZEgICDilojilojilZEgICAgezF9ezB9W3syfSDQntCx0Y/Qt9Cw0YLQtdC70YzQvdC+INC/0YDQvtGH0LjRgtCw0Lkg0YHQvtCz0LvQsNGI0LXQvdC40LUuezF9ezB9XQrilojilo'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
