Minji Lee, Sihyun Yu, Juan Lee, Sungwoo Jeon
# To Gather
# Solution for Difficulties in Reading Academic Materials

## Problem statement
While reading academic materials, we encounter to difficulties to understand some concepts, vocabularies or intends of an author. These difficulties can be easily solved through discussion among people reading the same materials.  
However, unlike to questioner who has a strong motivation of curiosity, answerers are not clearly motivated by existing question-and-answer system.

## Tasks
Since we are willing to motivate answerers while discussing in reading materials via social computing, we have focused on social core functions rather than functions for implementing annotation.

### Our first social core function is Chain of Direct Questioning.
In most cases, we expect a questioner-oriented, kind, and detailed answer when we asked someone directly not to everyone. However, if we ask only one person, it could be low-quality or (s)he might not know the answer.  
Thus, we introduced the chain of direct questions. If someone asks a question, the question is delivered to a randomly chosen person. The person who got the question might feel responsibility since the question was only conveyed to him/her. After the answerer answers, the questioner can decide to confirm and finish the answering or to continue the answer chain. 

### Our second social core function is Common Point of Questioner and Answerer.
Even if the question is directly delivered to someone, it seems not enough to motivate answerer to answer the question. Unlike to privately question to friends, they do not know each other.  
We cannot make them as a real friend. However, we can find a common point of questioner and answer. We show the found common point to answerer, and this makes a stronger relationship between questioner and answerer. There can be many of examples, "I helped you before!", "We are taking the same course now!", "We both have the same interest in HCI," or "We are researchers in same field."

### The third social core function is Collecting Pokemon.
We expect people to think this platform is not an ordinary, boring QnA platform, but to think to feel the platform has some fun aspects like an online game.  
If answerer answers to the question, the answerer got randomly chosen Pokemon. This acts as a self-motivating factor for the answerer, and this would help people participate in our service. The more participation, the better chain of direct questioning is made because many people want to collect all Pokemon.

## Prototype

### Link to our prototype
[To-gather](https://invis.io/NTOSIH079RK#/327837398_Sign_IN) : https://invis.io/NTOSIH079RK#/327837398_Sign_IN

### Prototyping Tool
We used Sketch and Invision as a prototyping tool. We use these prototypes for a few reasons. First of all, they provided a familiar platform that we usually have used such as iOS UI or Android UI. Furthermore, the layer system was very similar to the one in Photoshop, so it was quite easy to get used of this platform. Also, the homepages offer detailed instructions for both program, so we can find how to do something whatever we want. Lastly, we are so fascinated the program visualizes hotspots very well between screen to screen.  
As mentioned, it was easy to organize the overall UI and make icons we want to create. However, some problems also occurred during our work. To begin with, making hotspots between the screen and screen was not an easy task. As we are adding hotspots in our workspace, it became more and more complicated, so we needed to consider a lot at the end of adding hotspots that we want. Plus, we tend to miss some hotspots even we thought it was finished, so we always need to double check it by executing the preview of our prototype.  
Lastly, synchronizing the project was one of the most challenging part or our prototype. We did all of our jobs in Sketch (including hotspots) and tried to sync it with Invision. We still don’t know the exact reason, but hotspots that we created in Sketch did not synchronize on Invision. Therefore, after a few tries, we needed to add the same hotspots In Invision again. 

### Representative Screenshots
![Title](./images/lofi1.png)  
To-gather is a platform that enables direct Q&A while reading materials.  
![Task 1](./images/lofi2.png)  
Requester’s question is passed to only one person, not available by all people. Answers would have more responsibility to answer the question, since the question if for you, not for all members. After answering at questions, it passes to another person again and again. (Task 1)  
![Task 1 - confirm](./images/lofi3.png)  
Requesters can determine to continue passing the question to another person or to stop answering at (s) he questions.  
![Task 3](./images/lofi4.png)  
If you answer at someone’s questions, you can collect the Pokemon that randomly given by each question. (Task 3)  
![Task 2](./images/lofi5.png)  
Rather than denoting the requester’s name, we show the common point between the questioner and answerers on answerer’s display.  (Task 2)  

### Design Choices
First of all, we will not support scrolling function and highlighting function on the pdf file for a few reasons. We think implementing many functions with pdf file is not an easy task and implementing this is not related to social interaction via computing. Instead, we will just add a simple function to switch the page in one file and shaping a square on the paper, not highlighting.  
Furthermore, we will not use much time on implementing register and uploading profile picture since this is not the point of social interaction that we want to focus on. For the test, we will give to random account and profile picture to test users. Therefore, to achieve task 1, we will get the information of the user in offline and add this information to accounts by our hands.  
Lastly, we will not implement any animations related to Pokemon, because our purpose is implementing collecting system in our UI, not making the sweet and cool Pokemon. 

### Instruction
1. At [Sign-in](https://invis.io/NTOSIH079RK#/327837398_Sign_IN) page, please click green sign in button to start.
2. Click the profile button at the left downside. Then you can check the page for your collected Pokemon for answering at questions. (Task 3)
3. Click ‘Back’ button to return to the main screen.
4. Now, click the question button on the right, ‘Does AMT ignore the ethical problem?’. Then you can access the page to answer that question. You can check that the things that you and questioners share each other are denoted. (Task 1 & 2)
5. You can either select back button to return to the previous screen or click ‘What is your answer banner’ on the right below to answer at the question. (This time we assume that you already typed your answer. You don’t need to type any text. Just click it.)
6. You can check the answer added to the question. Now click back button to return. 
7. Now we are going to ask a question. Click the square on the left side on the paper. 
8. You will see that part is highlighted with the blue line. You can add a question to that part. Click ‘What is your question’ banner on the right below at the platform to add a question. (This time we also assume that you already typed your question. You don’t need to type any text. Just click it.)
9. You see your question is added to the screen on the upside right. If you see the left below, there are some icons of people with the circle shape. This is a notification to your questions. Click the icon with character to check the answer at your question.
10. Now, you can select Continue or Enough button. Continue button means you want to continue the question passing to others, and Enough button means you are now satisfied with answers.  If you select Continue, you just go back to the previous screen, or if you select Enough, you can check the answers are fixed.
11. After that, click back button to return to the main page. If you want to the question and answer again, you can click the highlighted part to move on that part.

## Observations