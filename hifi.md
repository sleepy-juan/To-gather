Minji Lee, Sihyun Yu, Juan Lee, Sungwoo Jeon
# To-gather

## Project Summary
### (1) the problem we're addressing
While reading academic materials, we usually ask some questions to other people whenever we encounter to difficulties to understand some concepts but it's hard to get activate answers on already existed platform that you know like 'klms', 'classum', etc because of the dispersion of responsibility to be answered. 
### (2) what our solution is
In order to encourage people to answer more, we make the system for chain of direct questioning that seems to make people feel obligated to reply more than before and also add one sentence that could represent the relationship between questionor and user like 'I answered your question before' or 'We are in same grade'. 
### (3) What unique approach we're taking in your solution (how it's different from other similar solutions). 
Other question/answer platforms that already exist mostly value the professional presence of respondents, and they use ways of rewarding users to increase user's chances of responding (such as 내공 in Naver 지식in, etc.), but we focused on the relationship between users to encourage people to answer more.

## Instruction

## URL of your prototype
http://cs473-togather.herokuapp.com/

## URL of your Git repository
https://github.com/sleepy-juan/To-gather

## Libraries and frameworks


## Individual Reflections
### Minji Lee
I contributed to implement the UI of front-end register page with Sungwoo. I also worked with Shihyun and Juan to modify and maintain the front-end main page, and contributed to the reliable connection between front-end and back-end. And then I structured the common point between users with Sungwoo and modified the register page accordingly. 

Because I've never built an Internet site before, and I've never been to javascript, it's very difficult to start with understanding what that code means. I learned how to code and understand the structure of the code, starting at the bottom. One of the hardest things was to show a pdf at the front-end, to enable input into the connected requests, and then to send the answers as well. When I entered the question, it was difficult to send it to a higher structure and then send it back to the left or right sidebar structure to make it float or hide. In addition, combining Front-end and Back-end was very difficult. When I sent a question, for some unknown reason, the question continued to grow, creating a problem that filled the screen. The data structure difference between Front-end and Back-end caused problems with the id format of the interrogators and respondents, and the question and answer also continued to be inconsistent. There is an another problem that some parts of user's ID have been cut off with some probabilty when we send users id to the server and get it back, so we need to spend a lot of time working on it.

The most valuable thing about doing this hifi-project is understanding the structure of javascript and React. Unlike the past when I have no idea with React and Javascript code, now I can doing a code, debug, and solve problems. I think it was a very significant experience of creating something from nothing in my life.

### Sihyun Yu
I contributed to implement almost parts of the main page as Front-end developer, also designed the main page. Furthermore, implemented the connection between register page and the main page: if completed sign up, then move to the main page with the user’s unique user name.  Lastly, I connected the implementation with implemented server (with Juan).

With the viewpoint of our problem and tasks, I found a React library for pdf-annotating (which is for main problem and concept) and made sidebars on left and right. On left sidebar, questions that the user himself/herself asked are visible as a notification. I made and implemented two buttons and their corresponding functions (which are Stop and Continue), which are directly related to our task 1. On the right sidebar, questions that someone asked to me are visible as notification (which are directly related to our task 1). On right sidebar notifications, I implemented common points to be visible (which is our task 2 and 3).  Furthermore, similar to left sidebar, I added and implemented functions for two buttons, Ignore and Answer, either to pass or ask to someone’s question.

Since it was very first time to implement something in web, I needed to use most of my time to study languages and concepts in Javascript, JSX, and so on. Many features in web-programming languages were different, (like rendering, state update…) and this was the most challenging part that I faced. Furthermore, at the first time, it was hard to understand the order of .css file to be applied. Therefore, I need to test a lot to get our desired display. 

After some studying, we decided to use React for development. However, there was a problem with version control issue since the version required for PDF viewer and PDF annotator are different. I consumed a lot of time to solve and manage this. 

The last and the most challenging and difficult part of the implementation was merging the Front-end one with the Back-end implementation. Databases that I imagined and Back-end teammates imagined were different, so there was a confusion to convert between then and visualize these in Front-end display. Plus, the unique ID for identifying the question and answers (which is implemented by deleting ‘0.’ to random double number on [0, 1]), sometimes sliced randomly while going to server, we consumed a lot of time to catch this issue. 

The most useful skill that I learned is the importance of synchronizing the format of database both in Front-end and Back-end at the first time. It means, it is very important to discuss enough about the format of database to use at the platform, because often conversions on both direction would not be easy to do. If both Back-end and Front-end use the same class (or database) for implementation, then the team does not have implement complex conversion for database to use. Furthermore, it is better to unify the language to implement. We used Python, pure Javascript, and. JSX for implementation. Importing and exporting between these files were not an easy thing to do. Therefore, considering the language issue for implementation will be helpful to consume less time to merge all of the implementation that workers did.

### Juan Lee
I was responsible for developing back-end server and communication module between clients. Since the project requires systematic movements on the server for many simultaneous users, such as passing a question to proper clients or managing time-out for all the questions moving on the system, I had to design the architecture and protocols for the system(Sungwoo helped me to design the protocols). The server is programmed with python, implementing a very basic HTTP parser inside for communicating with clients. Also, I coded communicating module for javascript, which is for applying to front-end. Lastly, I merged the server with common point tasks(Sungwoo, Minji) on the server, and with the front-end (Sihyun).

Firstly, I only had theoretical knowledge base for Web Server, which uses only HTTP and frequently limits the socket communication due to the security issue. I had to implement HTTP parser by myself without any built-in module in Python for solving CORP error which is a common security issue on the Web.
Secondly, since it seems easy to implement front page with javascript, I had to cover Python for server and Javascript for clients. However, I am not very familiar to javascript, and also it was very first time to implement customized networking with javascript, this was one of difficult part for me.
Lastly, networking was not so stable as I thought. Some ID for question was frequently cut when passing to the server, this has been unsolved bug until now. (Until now I am writing this report, we still have one week!) I think this is the biggest challenge for me.

Since there are not many students who have knowledge about network, I am often responsible for back-end. From this project, I learned some practical experiences and knowledges to implement Web Server, also useful libraries and languages such as javascript and Node.js. I hope I can apply these techniques for my other projects.

### Sungwoo Jeon
I contributed to implement basic parts of server with Juan, user interface for register page and right sidebar on main page, and common point. 
For server, I and Juan design basic protocol that contains necessary information for our high-fi prototype and make a server depend on our protocol. For user interface, I make selection windows in register page with several classification and make right sidebar with received questions and answering window. In our tasks, I implemented the common point between arbitrary users. Although there are selection windows in register page, I make user's information except username randomly in server because main point of our task is focus on sense of kinship with common point, not a registration with correct information. Furthermore, I implemented the common point for helping experience. Lastly, I implemented the common point for helping experience and users’ information with specific order of priority and sent the common point from Back-end to Front-end.

When we started to make a server, we didn’t know that what information needs for us for protocol; so, we had to fix our protocol continuously. For user interface, it was my first time to implement web with java script; so, I should learn the java script and make some example of user interface from the beginning. Also, we implemented Front-end and Back-end separately; and, each of code use different database and programming language. So, there need lots of time and debugging to merge Front-end and Back-end. 

The most useful skill that I learned is user interface in web and merge between front-end and back-end. It was my first time to implement web; so, I learned lots of information about java script and user interface for web during web programming. At first, I didn’t even know about lexical grammar in java script. As time goes by, I got used to web programming; and, learning is faster. Also, I implemented both of front-end and back-end; and, I did not expect how to merge both of them. However, as high-fi prototype developed, I could get the hang of merging between front-end and back-end with analyzing the code contrary to my expectation.
