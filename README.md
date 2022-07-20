## Google Search Results Parser
- Parse search result one page at a time
- export a csv file containing hr's name, position, company, email

## Steps of using the scripts
0. Search Google using query method and get result page(s)  
	 If the result has multiple pages, manually repeat the process for each page

1. paste all files into a folder,  including:
	 - regex_parser_google_search.py
	 - requirements.txt
	 - README.md (optional)
2. create a python venv
	 Open terminal at folder and run the following command and then  install all dependencies

```
python3 -m venv newvenv
pip install -r requirements.txt
```	 

3. Create a new file called temp.html in the folder
4. Go to result page, paste the source code into temp.html
5. Inspect the result page, find the class name for the following elements:
	 - Each result block (a block usually contains title(the link) and other info)
	 - Title for each block
	 - Info for each block

	Then replace in regex_parser_google_search.py:
	 - line 20's class name with block's class name
	 - line 23's class name with info's class name
	 - line 26's class name with title's class name
	Google's search result is dynamically generated for each user-agent, so class names vary for different machine (device, browser, etc.)

6. Run the code, and the exported file is named 'list_parser.csv'




