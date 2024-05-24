class Job:
    def save_data(self, title, company, link, platform):
        return {
            "title":title,
            "company":company,
            "link":link,
            "platform" : platform
        }