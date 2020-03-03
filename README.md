# WikipediaSearcher

In this project, I have developed a prototype program that plays the Wikipedia game. This is where you start from a random wikipedia page and use the links on that page to navigate to eventually find your desired end goal page, while only staying on Wikipedia and not being able to go backwards.

I have done this using Python with the BeautifulSoup and requests libraries to scrape data from the Wikipedia web pages, sepcifically the links each one has. 

To navigate successfully, I have given the computer a basic heuristic to guide it towards the desired page. I have assumed that the number of common links that the desired page and another page point to sugest how similar they are, therefore guiding the program towards the final destination.

This is accomplished by scanning the desired page to see the other pages it points to. The program takes in a specified link or random page as input and discovers the Wikipedia links on it, storing them in a list. The program then goes through the list and scans each one, where it looks at the number of further links on that page it has in common to the desired page. After only scanning a suitable number of the links found, calculated so it is proportional to the size of the page traversed (by counting number of links found), it determines which link has the most further links in common with the destination page and chooses to traverse it; therefore restarting this process again until the end goal is found. 

To decrease the time in which it completes, I have designed it so that it automatically traverses any pages that have over 70 links in common to the desired page. This is because it should be a good choice to traverse and it saves time traversing more links that may not be useful which takes a lot of time. 

As this is still a prototype, there are a lot of things that can be improved, such as a more advanced heuristic or better scaling to how many links should be scanned on the page.
