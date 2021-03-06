Minji Lee, Sihyun Yu, Juan Lee, Sungwoo Jeon
# To-gather

## Project Summary
### (1) the problem we're addressing
While reading some materials, discussion with people is necessary to fully understand the content, but in most QnA platform, only questioners want to ask a question but answerers feel bothersome to the question which makes only one-direction interaction.  
### (2) what our solution is
In order to encourage people to answer more, we make the direct chain questioning system that make people feel obligated to reply more than before, and also make the system to represent the relationship between questioner and answerers like 'I answered your question before' or 'We are in same grade' by one sentence. 
### (3) What unique approach we're taking in your solution (how it's different from other similar solutions). 
Other question/answer platforms that already exist mostly value the professional presence of respondents and they use ways of rewarding users to increase user's chances of responding (such as 내공 in Naver 지식in, etc.), but we focused on the relationship between users to make feel like being friends so finally encourage the answer.

## Before we start the instruction,
__This time, we didn't get the 'REAL INPUT' characteristics (#2) from users, but only get the user's id on #1. People can log in again when they put the exact same id before, and all data (previous questions and answers) will be preserved. Under the circumstances, we give a random designation for each characteristics to users. Based on randomly assigned features, we find common points between users and send them together when they send a question. Later, when we test this with real users, we will substitute their actual character for each ID and conduct an real experiment with them based on it.__

__Plus, since we seperated Web Server for Front-end and Server for Back-end, we succeeded to host the Web Server, but we haven't hosted the Background Server yet. (Implemented by Python,  still finding ways...) Therefore, we need to turn on the Background Server for sending questions and answers to be evaluated in our Labtop/Desktop. Please contact us when you start to evaluate our high-fi prototype.__

juanlee@kaist.ac.kr

minji971010@kaist.ac.kr

j0070ak@kaist.ac.kr

yusihyunc@kaist.ac.kr

## Instruction

--------------------------------------------------------------------------------------------------------
### Warning
#### 1. You're highlighting need to be exist a single page. Pleae do not highlight beyond another page.
#### 2. You only can use ENGLISH for everything. (username, question, answer, etc.)
#### 3. Do not press all buttons such as 'ANSWER' more than two times. If you press once, just wait until the answer uploaded.
#### 4. If there is an error(offsetHeight error), please refresh. It will work again. (This is the error caused by the package we imported for implementation.)
#### 5. Please ask a question and answer at question in one line. (It means, DO NOT USE \n)
--------------------------------------------------------------------------------------------------------
![hifi1](./images/hifi1.JPG)
This is the very first interface when you enter our platform. 
1. Put your identified username on the yellow box #1.
2. Press the 'Click me!' button.
Then you can go in to the main screen.

There are 5 characteristics on yellow box #2. 

__You don't need to modify them. These will be automatically (and randomly) assigned, because we did not implement register page completely. Therefore, while testing to crowd, we will collect these information in offline to tha crowd then insert in our source code manually.__

--------------------------------------------------------------------------------------------------------
![hifi2](./images/hifi2.JPG)
This is the main interface for our platform. 

* Yellow box #3: the pdf space to show the reading materials. People can share this pdf and question with confirmed answers will annotated on this pdf.
* Yellow box #4: the left sidebar. Users can see their questions and current answer state.
* Yellow box #5: the right sidebar. When other people ask the question, it delivered directly to a user and it will show on the right sidebar with a sentence that represent the relationship with the questionor and user. 
--------------------------------------------------------------------------------------------------------
![hifi3](./images/hifi3.JPG)
1. Highlight the pdf that you don't understand.
* Yellow box #6: If you highlight something you don't understand, the yellow highlight will apper on the sentences.

#### Warning again: You're highlighting need to be exist a single page. Pleae do not highlight beyond another page. 

--------------------------------------------------------------------------------------------------------
![hifi4](./images/hifi4.JPG)
After you highlight the pdf, you can see this black text box immediately. 

1. Enter your question on this yellow box #7. 
2. Click the check button to send your question. After asking a question, the notification appears for second on the left sidebar then disappears; it means the question successfully sent to oter person.

#### Warning again: You only can use ENGLISH.

--------------------------------------------------------------------------------------------------------
![hifi5](./images/hifi5.JPG)
__※ This is the other user's interface who received a question.__

You can see the question that arrived from other users on your right sidebar. Note that this notification also includes common points.

1. Click the yellow box #8 to answer/ignore the question.

* Red underline: This is a sentence that could encourage users to answer more.
--------------------------------------------------------------------------------------------------------
![hifi6](./images/hifi6.JPG)
You can see the text box bottom of the right sidebar.

1. If you want to ignore that question, press the Ignore button(Yellow box #10) then you can ignore that question.
2. If you want to answer that question, click the text box(Yellow box #9) and put your answer here. After that, press the Answer button.

Your answer will send to the questioner and he could check your answer.

#### Warning again: You only can use ENGLISH.
--------------------------------------------------------------------------------------------------------
![hifi7](./images/hifi7.JPG)
If someone answer your question, you can see your question on the left sidebar.

1. Click the yellow box #12 to see the current answers of the question.
2. On the bottom of the left sidebar, the first sentence is your question and there are current answers of that like a chain.
3. You can choose whether STOP or CONTINUE the answer chain.

--------------------------------------------------------------------------------------------------------
![hifi8](./images/hifi8.JPG)
Suppose that you press the CONTINUE. If someone answer your question again, you can see more answers below.

* Yellow box #14: Show the answer chain for the question.
* Yellow box #15: Press this stop button to cut the answer chain and upload your question and following answers on the pdf file. These are going to be shown to everyone else who share this file.
* Yellow box #16: Press this continue button to send your question to another people if you don't satisfied with current answers.
--------------------------------------------------------------------------------------------------------
![hifi9](./images/hifi9.JPG)
After you regist your question and answers, now everyone can see the highlights, question, and answers.

1. Put your curser on the highlight in the pdf file.
2. You can see the pop-up box that contain the question and answers. (Yellow box #17)
--------------------------------------------------------------------------------------------------------

## URL of our prototype
http://cs473-togather.herokuapp.com/

## URL of our Git repository
https://github.com/sleepy-juan/To-gather

## Libraries and frameworks
React, Bootstrap (+ react-pdf-highligter package https://www.npmjs.com/package/react-pdf-highlighter)

## Individual Reflections
### Minji Lee
I contributed to implement the UI of front-end register page with Sungwoo. I also worked with Shihyun and Juan to modify and maintain the front-end main page, and contributed to the reliable connection between front-end and back-end. And then I structured the common point between users with Sungwoo and modified the register page accordingly. 

Because I've never built an Internet site before, and I've never been to javascript, it's very difficult to start with understanding what that code means. I learned how to code and understand the structure of the code, starting at the bottom. One of the hardest things was to show a pdf at the front-end, to enable input into the connected requests, and then to send the answers as well. When I entered the question, it was difficult to send it to a higher structure and then send it back to the left or right sidebar structure to make it float or hide. In addition, combining Front-end and Back-end was very difficult. When I sent a question, for some unknown reason, the question continued to grow, creating a problem that filled the screen. The data structure difference between Front-end and Back-end caused problems with the id format of the interrogators and respondents, and the question and answer also continued to be inconsistent. There is an another problem that some parts of user's ID have been cut off with some probabilty when we send users id to the server and get it back, so we need to spend a lot of time working on it.

The most valuable thing about doing this hifi-project is understanding the structure of javascript and React. Unlike the past when I have no idea with React and Javascript code, now I can doing a code, debug, and solve problems. I think it was a very significant experience of creating something from nothing in my life. I found out that the most important thing is the perfectly knowing the whole structure of data and code  when we implementing. After knowing this, it's far more easier and quicker to do the job.

### Sihyun Yu
I contributed to implement almost parts of the main page as Front-end developer, also designed the main page. Furthermore, implemented the connection between register page and the main page: if completed sign up, then move to the main page with the user’s unique user name.  Lastly, I connected the implementation with implemented server (with Juan).

With the viewpoint of our problem and tasks, I found a React library for pdf-annotating (which is for main problem and concept) and made sidebars on left and right. On left sidebar, questions that the user himself/herself asked are visible as a notification. I made and implemented two buttons and their corresponding functions (which are Stop and Continue), which are directly related to our task 1. On the right sidebar, questions that someone asked to me are visible as notification (which are directly related to our task 1). On right sidebar notifications, I implemented common points to be visible (which is our task 2 and 3).  Furthermore, similar to left sidebar, I added and implemented functions for two buttons, Ignore and Answer, either to pass or ask to someone’s question.

Since it was very first time to implement something in web, I needed to use most of my time to study languages and concepts in Javascript, JSX, and so on. Many features in web-programming languages were different, (like rendering, state update…) and this was the most challenging part that I faced. Furthermore, at the first time, it was hard to understand the order of .css file to be applied. Therefore, I need to test a lot to get our desired display. 

After some studying, we decided to use React for development. However, there was a problem with version control issue since the version required for PDF viewer and PDF annotator are different. I consumed a lot of time to solve and manage this. 

The last and the most challenging and difficult part of the implementation was merging the Front-end one with the Back-end implementation. Databases that I imagined and Back-end teammates imagined were different, so there was a confusion to convert between then and visualize these in Front-end display. Plus, the unique ID for identifying the question and answers (which is implemented by deleting ‘0.’ to random double number on [0, 1]), sometimes sliced randomly while going to server, we consumed a lot of time to catch this issue. 

The most useful skill that I learned is the importance of synchronizing the format of database both in Front-end and Back-end at the first time. It means, it is very important to discuss enough about the format of database to use at the platform, because often conversions on both direction would not be easy to do. If both Back-end and Front-end use the same class (or database) for implementation, then the team does not have implement complex conversion for database to use. Furthermore, it is better to unify the language to implement. We used Python, pure Javascript, and. JSX for implementation. Importing and exporting between these files were not an easy thing to do. Therefore, considering the language issue for implementation will be helpful to consume less time to merge all of the implementation that workers did. Or, if we use different languages for different purpose, it would be better to find how to merge different formats BEFORE STARTING IMPLEMENATATION, because for some cases merging these two may be too challenging.

### Juan Lee
I was responsible for developing back-end server and communication module between clients. Since the project requires systematic movements on the server for many simultaneous users, such as passing a question to proper clients or managing time-out for all the questions moving on the system, I had to design the architecture and protocols for the system(Sungwoo helped me to design the protocols). The server is programmed with python, implementing a very basic HTTP parser inside for communicating with clients. Also, I coded communicating module for javascript, which is for applying to front-end. Lastly, I merged the server with common point tasks(Sungwoo, Minji) on the server, and with the front-end (Sihyun).

Firstly, I only had theoretical knowledge base for Web Server, which uses only HTTP and frequently limits the socket communication due to the security issue. I had to implement HTTP parser by myself without any built-in module in Python for solving CORS error which is a common security issue on the Web.
Secondly, since it seems easy to implement front page with javascript, I had to cover Python for server and Javascript for clients. However, I am not very familiar to javascript, and also it was very first time to implement customized networking with javascript, this was one of difficult part for me.
Lastly, networking was not so stable as I thought. Some ID for question was frequently cut when passing to the server, this has been unsolved bug until now. (Until now I am writing this report, we still have one week!) I think this is the biggest challenge for me.

Since there are not many students who have knowledge about network, I am often responsible for back-end. From this project, I learned some practical experiences and knowledges to implement Web Server, also useful libraries and languages such as javascript and Node.js. I hope I can apply these techniques for my other projects.

### Sungwoo Jeon
I contributed to implement basic parts of server with Juan, user interface for register page and right sidebar on main page, and common point. 
For server, I and Juan design basic protocol that contains necessary information for our high-fi prototype and make a server depend on our protocol. For user interface, I make selection windows in register page with several classification and make right sidebar with received questions and answering window. In our tasks, I implemented the common point between arbitrary users. Although there are selection windows in register page, I make user's information except username randomly in server because main point of our task is focus on sense of kinship with common point, not a registration with correct information. Furthermore, I implemented the common point for helping experience. Lastly, I implemented the common point for helping experience and users’ information with specific order of priority and sent the common point from Back-end to Front-end.

When we started to make a server, we didn’t know that what information needs for us for protocol; so, we had to fix our protocol continuously. For user interface, it was my first time to implement web with java script; so, I should learn the java script and make some example of user interface from the beginning. Also, we implemented Front-end and Back-end separately; and, each of code use different database and programming language. So, there need lots of time and debugging to merge Front-end and Back-end. 

The most useful skill that I learned is user interface in web and merging between front-end and back-end. It was my first time to implement web; so, I learned lots of information about java script and user interface for web during web programming. At first, I didn’t even know about lexical grammar in java script. As time goes by, I got used to web programming; and, learning is faster. Also, I implemented both of front-end and back-end; and, I did not expect how to merge both of them. However, as high-fi prototype developed, I could get the hang of merging between front-end and back-end with analyzing the code contrary to my expectations.

In order to encourage people to answer more, we make the direct chain questioning system that make people feel obligated to reply more than before, and also make the system to represent the relationship between questioner and answerers like 'I answered your question before' or 'We are in same grade' by one sentence. 
