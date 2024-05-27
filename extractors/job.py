class Job:
    def save_data(self, position, company, link, platform):
        return {
            "position":position,
            "company":company,
            "link":link,
            "platform" : platform
        }