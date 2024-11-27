from crewai_tools import BrowserbaseLoadTool
# Initialize the tool with the Browserbase API key and Project ID
tool_1 = BrowserbaseLoadTool()


from crewai_tools import ScrapeWebsiteTool

# To enable scrapping any website it finds during it's execution
tool_2 = ScrapeWebsiteTool()

# Initialize the tool with the website URL, 
# so the agent can only scrap the content of the specified website
tool_2 = ScrapeWebsiteTool(website_url='https://en.wikipedia.org/wiki/Wikipedia')

# Extract the text from the site
text = tool_2.run()
print(text)
