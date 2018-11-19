# CS473 Introduction to Social Computing
Repository for Design Project of CS473, KAIST, 2018 Fall  

### About the Course
Human-computer interaction no longer only concerns a single user in front of their computer. An increasing number of modern systems are inherently social, involving a large group of users to collaborate, discuss, ideate, solve problems, and make decisions together via social interaction. This course focuses on crowdsourcing and social computing, two of the most important concepts in the era of interaction at scale. This course will cover major design issues and computational techniques in building crowdsourcing and social computing systems. [Course Page](https://www.kixlab.org/courses/cs473-fall-2018/index.html)

### About Design Project
You'll **DESIGN**, **BUILD**, and **TEST** your own crowdsourcing / social computing system. [Design Project](https://www.kixlab.org/courses/cs473-fall-2018/design-project.html)

### Collaborator
* Minji Lee
* Sihyun Yu
* Juan Lee
* Sungwoo Jeon

### Code Description
There are two folders inside our git repository that contain our implementation: Front-end, and Back-end.

#### Front end
Inside Front end, there is a folder demo-test, the place all of our codes for Front-end are contained. Most of our implementation is in folder src. There are three folders inside src folders as follows:

 * Roots
 
  1. Root.js : Includes react-router to implement display conversion from register page to our main page

 
 * assets

 contains some .js files which is related to PDF viewer and annotator package (not implemented by us, already implemented by other people), some icons for popup while asking the questions, and a few pdf file for test
  
 * components (which contains our main implementation for high-fi prototype)
  1. **AnswerHighlights.js**: A format file of example questions for our test on offline (for Left Sidebar)
  2. **App.js**: Import Register Page and Main viewer page.
  3. **Finished_answer.js**: Related to the rightdown side at the UI. Implementation of visualizing question and current answers fot the questions that come to me.
  4. **QuestionHighlights.js**: similar to Answerhighloights.js. Format file for testing on offline. (for Right Sidebar)
  5. **Register.js, Register.css**: Implementation for basic display for sign-in page (sending selected information to sever is not implemented; we will collect these data on offline to the crowd before test.)
  6. **Sidebar\_Left.js, Sidebar\_Left.css**: Implemenation and design for left sidebar. Question notification that user him/herself asked is visible with this code.
  7. **Sidebar\_Leftdown.js, Sidebar\_Leftdown.css**: Implementation and degisn for left sidebar on downside. Clicking either Stop or Continue button, quesioners can determine continue passing the question or not. If Stop, the question status become public and visible to all users. 
  8. **Sidebar\_Right.js, Sidebar\_Right.css**: Similar to left sidebar. Question notification that come to me is visible by notification. Common point is also visible in this alert.
  9. **Sidebar\_Rightdown.js, Sidebar\_Rightdown.css**: Similar to Sidebar\_Leftdown.js and .css. However, there are two buttons, Ignore and Answer, so user can determine ignoring or answering at the question. Furthermore, there's a textbox for answering.
  10. **Spinner.js, Spinner.css**: Already implemenet in our skeleton code (not implemented by us)
  11. **react-pdf-annottor**: For PDF annotating (not implemented by us, most files already implemented through package). For the file/Tip.js, we deleted some buttons which is useless to us. Furthermore, we newly implemented Tip_answer.js, to check the answer and corresponding questions if the status of the question becomes public.
  12. **Viewer.js, Viewer.css**: Our main function. enables PDF viewer, import all Sidebar codes, and set the state to be used as follows: 
```jsx
state = {
		highlights: [], 
		highlights_answer: [], 
		highlights_merged: [], 
		Qstate:null,
		Qstate_ans:null,
		currentAforQ:[""],
		currentAforQ_ans:[""],
		QID:null,
		QID_answer:null,
		answer:null,
		highlights_public: [],
		flag_left: false,
		flag_right: false,
		Qstate_tip:null,
		currentAforQ_tip:[""],
	};
``` 

#### Front end
 



Make sure to add a README file that briefly describes the code, e.g., main JavaScript file, or where main feature implementations are, etc. Several lines are enough.
