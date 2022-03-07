# is601-project1


# For project 1 you need to do the following:
1. Create a flask application that contains at least 4 separate content pages and a home page.  Your content pages should use the F layout (Links to an external site.) and your homepage should use a Z layout (Links to an external site.).  You should use Bootstrap V5 for the project.  Your index page should be  an "advertisement" for yourself and have carousel slides for the technologies that you have learned so far.  You should link the carousel image to a page that contains your notes and explanation of what that technology does. 

2. You need to setup CI/CD process using GITHUB actions that does the following:

    When master is updated (Push or Merge after pull request) you need to trigger a workflow to update the Heroku prod app
    When any pull request to merge a branch to master is created, you need to run pytest and deploy to Heroku dev app.
    You need to have badges for production workflow and development workflow respectively on the Readme.MD file.


# Technology Web Page Requirements:
1. Git - Explain Branches, Merge, Commit, Tags, Repositories.

2. Docker - Explain containers, images, link to the project repository on docker hub, explain all the docker commands that you know.  Explain how to start the project and how to access the container with the terminal using just terminal commands and not PyCharm 

3. Python / Flask - Talk about testing with pytest and give examples from your code.  Explain how you created simple pages and how you tested it. Link to the project on Github Link to flask, flask Blueprint documentation, and flask testing with PyTest.  Explain the purpose of every file in the project using an outline that represents the directory and file structure of the project.


## Outline Example

    Project Root Folder <- Root of the project
        docker-compose.yml <- Orchestration file that contains the configuration to develop locally, it overrides the Dockerfile to run the flask development server instead of running the gunicorn server that is used for hosting on Heroku
        Dockerfile <-File used to create an image to run in a container that runs the program
4.  Continuous Integration and Deployment - Explain how you have the project setup to use GitHub Actions, How you can review code using a development server before merging pull requests, how you can deploy master to a production server.   Explain how you deploy an image of your project to Dockerhub when master is updated.  GitHub Actions Documentation (Links to an external site.).  

Read and cite / quote from these articles for CI/CD:

*https://www.martinfowler.com/articles/continuousIntegration.html (Links to an external site.)
*https://www.martinfowler.com/bliki/ContinuousDelivery.html (Links to an external site.)


# Submission Instructions 
Submit a link to the GitHub repository and you should have a link to the production and development versions running on the two heroku app servers respectively.  Any projects that do not have working versions of the app on both servers at the time of grading will receive a 0.