from playwright.sync_api import sync_playwright

def visitPage(url, pw):
    try:
        browser=pw.chromium.launch()
        page=browser.new_page()
        page.goto(url)
        return browser, page
    except Exception as e:
        print(f"Unable to connect to server with address: {url} \n\n\nRefer to error: {e}")

def main():
    with sync_playwright() as p:
        browser,page=visitPage("https://www.lkqpickyourpart.com", p)
        page.screenshot(path="hi.png")
        
        browser.close()

if __name__=="__main__":
    main()