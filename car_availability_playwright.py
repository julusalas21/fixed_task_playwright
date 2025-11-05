from playwright.sync_api import sync_playwright

def visitPage(url, pw):
    try:
        browser=pw.chromium.launch()
        page=browser.new_page()
        page.goto(url)
        return browser, page
    except Exception as e:
        print(f"Unable to connect to server with address: {url} \n\n\nRefer to error: {e}")

def pageSearch(page,query):
    search=page.get_by_placeholder("Enter Year, Make or Model")
    search.press_sequentially(query)
    search.press("Enter")



def debug(page):
    i=0
    for x in page.get_by_role('link').all():
        print(x.inner_text())
        print(x.inner_html)
        #page.screenshot(path=f"example{i}.png")
        i+=1

def main():
    with sync_playwright() as p:
        browser,page=visitPage("https://www.lkqpickyourpart.com", p)
        page.get_by_text("VIEW OUR INVENTORY").click()
        #page.wait_for_load_state("networkidle")
        page.screenshot(path="hi.png")
        print(page.url)
        page.get_by_title("Please Select A Valid Location").click()
        page.get_by_title("Please Select A Valid Location").select_option(label="Ontario")
        #locationbox=page.get_by_role("select", name="locationBox")#.select_option("inner-html=Ontario")
        page.screenshot(path="hi2.png")
        pageSearch(page, "del sol")
        #page.screenshot(path="hi.png")
        page.wait_for_load_state("networkidle")
        page.screenshot(path="hi3.png")
        browser.close()

if __name__=="__main__":
    main()