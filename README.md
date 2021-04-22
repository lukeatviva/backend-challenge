# Backend Developer Challenge
To better gauge your skills as a backend developer, we would like you to complete the following challenge. This will help our interviewers assess your strengths, and frame the conversation through the interview process. Take as much time as you need, however we ask that you not spend more than a few hours. 

## Submission Instructions
1. Fork this project on GitHub. You will need to create an account if you don't already have one
2. Complete the challenge within your fork after reading below details.
3. Push all of your changes to your fork on GitHub and submit a pull request.

## Project Description
The project will consist of two parts:
1. Gather product information from a website and store it in a database
2. Create an api to interact with that data

## Collecting product information
For this task, you will scrape information from https://aliexpress.com
1. Go to category "Bags & Shoes" > "Men's Shoes" > "Casual Shoes"
2. Get the first 25 products in the results and gather the following information:
- title
- image url
- price
- shipping price if available
- star rating
- units sold
- store name
3. Save each item in a database. 
- every product should have a unique identifier
- Everytime the script is run, add additional items, but do not add duplicates.

You must use either Python or NodeJS for this script. You may use any open source browser library such as puppeteer or just regular fetch/requests.
You may also use any database such as MongoDB, SQLite, MySQL.

## API
1. For this part of the project you will create a rest API to interact with the data you saved in the previous task.
2. You are required to use Python/Flask for this task
- https://flask-restx.readthedocs.io/en/latest/quickstart.html
3. create endpoints to do the following:
- get a list of products (sorting and pagination is not required, but nice to have)
- get a single product by id
- update a single product by id (allow updating any of the fields mentioned in the first task)
- create a new product

If you need to make any assumptions in order to complete the task, make a note of them in your comments.

Your application should be easy to set up, have a clear step by step instructions on how to run your submission and should run on Linux distros such as ubuntu, centos or debian. It should not require any non open-source software.

There are many ways that this application could be built; we ask that you build it in a way that showcases one of your strengths (OOP, clean interface, clean code, extensible code, high code quailty, beautiful frontend...etc).

Once you're done, please submit a paragraph or two in your `README` about what you are particularly proud of in your implementation, and why.

## Evaluation
Evaluation of your submission will be based on the following criteria. 

1. Did your application fulfill the basic requirements?
2. Did you document the method for setting up and running your application?
3. Did you follow the instructions for submission?
4. Did you style your code in a way that it's easy to read and understand?
5. Did you go above and beyond? (Did your submission surprise us?)
6. Did you maintain clean code (indentation, comments, naming conventions)

## Note
Please submit clean code with proper indentation. Understand that the first thing we do is  
read your code, not run your code. If you fail to keep consistant indentation and  
the best practices in defining your functions and variable names, chances are  
we will not need to run your code to evaluate your skills.

## What's Next?
Once when you have submitted your work we will review your submission as soon as possible. 
Please note we will only contact the selected candidates for further consideration.
We thank you for taking the time to complete this development challenge and appreciate your interest in pursuing a career with us. 
