from scrapy.spiders import Spider
import json
from tutorial.items import FoxPerson



class FoxNewsSpider(Spider):
    name = "fox_people"
    allowed_domains = ["foxnews.com"]
    start_urls = ["http://api.foxnews.com/v2/person?site=fox-news&role=personality&rows=300&callback=foo"]

    def parse(self, response):

        peopleJson = response.body.decode(response.encoding)

        try:
            start = peopleJson.index("(") + len("(")
            end = peopleJson.index(")", start)
            peopleJson = peopleJson[start:end]
        except ValueError:
            return ""

        peopleJson = json.loads(peopleJson)
        peopleCount = peopleJson["response"]["numFound"]

        peopleObjects = []
        print(peopleCount)


        for i in range(0,peopleCount):
            new_person = FoxPerson()
            full_name = peopleJson["response"]["docs"][i]["name"]

            new_person["url"] = peopleJson["response"]["docs"][i]["url"]
            new_person["first_name"] = full_name.split(" ")[0]

            if len(full_name.split(" ")) > 2:
                new_person["last_name"] = full_name.split(" ")[1] + " " + full_name.split(" ")[2]
            else:
                new_person["last_name"] = full_name.split(" ")[1]

            peopleObjects.append(new_person)
            print(new_person)

        return peopleObjects




