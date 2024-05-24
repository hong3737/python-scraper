from extractors.wanted import Wanted
from extractors.wwr import Wwr
from file import save_to_file


keyword = input("What do you want to search for?")


wanted = Wanted()
content = wanted.get_pages(keyword)
save_to_file(keyword, wanted.scrape_page(content))




