from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Keep headless=False to debug
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        viewport={"width": 1920, "height": 1080},
        # Add more headers if needed
    )
    page = context.new_page()
    
    # Navigate with a delay to avoid detection
    page.goto('https://ma.indeed.com/jobs?q=web+developer&l=&radius=25&from=searchOnDesktopSerp%2Cwhatautocomplete%2CwhatautocompleteSourceStandard&vjk=01449305a38465c0', timeout=60000)
    time.sleep(5)  # Simulate human reading time

    # Scroll logic (keep your existing code)
    last_height = page.evaluate("document.body.scrollHeight")
    while True:
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)  # Longer delay between scrolls
        new_height = page.evaluate("document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    content = page.content()
    with open('content.html', 'w', encoding='utf-8') as f:
        f.write(content)
    browser.close()