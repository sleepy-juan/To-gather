Minji Lee, Sihyun Yu, Juan Lee, Sungwoo Jeon
# To Gather
# Solution for Difficulties in Reading Academic Materials

### Problem statement
We want to solve the difficulty while reading academic materials such as books, online lectures, papers and so on.

### Problem background
Many university students need to read and watch a lot of materials for their study. For instance, we often read HCI papers and watch TED speech in Introduction to Social Computing Class, read the textbook in most classes, read a lot of papers for their study, and so on. However, due to many reasons, many students have difficulty to understand these materials. Our groupmates shared our experiences, some of us felt difficulty since they are not familiar with reading/watching something in English, and also a few of us felt so hard because the contents in materials are so professional in sometimes. This is not a problem that only KAIST students experience. There is a [nature science article](https://www.nature.com/news/it-s-not-just-you-science-papers-are-getting-harder-to-read-1.21751) argues the hardness of reading science papers. Also, there are some articles about [how to read difficult books](https://bookriot.com/2017/11/09/reading-difficult-books/) and [how to understand difficult books](https://www.thoughtco.com/how-to-understand-a-difficult-book-1857120). All the articles mention that it is necessary to ‘talk each other’ who are reading the same material. It is certain that understanding these stuffs is important to get new knowledge and do further study about certain area. Therefore, we decided to solve this problem by using social computing.

### Motivation (Why social computing?)
It is because all people has a difficulty with a different reason and different part of the materials. Therefore, by sharing and helping each other, it will be much easier to understand one book/paper/lecture. Since each material has a different content and all people have different points with confusion, machine is hard to help 	this problem. Furthermore, if there is a person who initially couldn’t understand certain part but finally succeed to understand that part, that person can explain to others how (s)he could understand that part with similar viewpoint who does not understand the part yet. This explanation might be much helpful than individual expert’s single explanation, since some contents are too trivial to them already, which makes bad explanation. Therefore, by making human-human social interaction via social computing, many people can easily read and understand the thing, and also gather and summarize the contents of certain material.

### HMW questions (at least 10)
1. **How might we make difference between pre-existing similar platform(like Google Docs, KLMS) and our project idea?**
2. **How might we make people use our project?**
3. **How might we design the UI much easier to read and see the contents?**
4. How might we control the quality of answers?
5. How might we know wrong answers/discussions?
6. How might we connect offline reading and online social computing to increase accessibility?
7. How might we break the wall of language?
8. How might we protect the copyright of certain file?
9. How might we determine the role of people such as administrator/participants?
10. How might we organize and visualize all the discussions and QnAs?

### Solution ideas for your HMW questions (at least 10 * 3 HMWs)
1. **How might we make difference between pre-existing similar platform(like Google Docs, KLMS) and our project idea?**
  - **Classum**: It has a quite difficuly UI to organize the material, discussion, and questions. Even if professors and TAs try to upload some reading materials for class as a form of notice, it is very difficult to distinguish them from other students' questions.
  - **KLMS**: It has a problem in accessibility, so that students are hard to use KLMS frequently. Old and multi-step layers in UI, instructor-centered UI make it harder. Also, it is very hard to discuss some problem on KLMS. It seems to be more unilateral notice platform between instructor and student.
  - Slack: Slack is just messenger, so it's not easy to discuss actively while reading a paper online. We can't see the paper and it's comment both intuitively.
  - Acrobat: We can't discuss on Acrobat online in real time.
  - **Google docs/sheet/slides**: There is no 'google pdf', so we can't easily share our feedbacks for pdf file (paper, textbook, video, ...) on google service.
  - Papers: It mainly focuses on the personal paper management, so it is easy to read and manage the paper but hard to discuss with others.
  - Evernote: Evernote is designed for individual users, so interaction between people is limited to the sharing of files.
  - Piazza: We mostly focused on the reading materials than piazza, so it is different to read and comment simultaneously. 
  - Kakao Open chat: No feedback or comment for the material, and just one-depth discussion with people exists.
  - Facebook group page: Hard to get some feedbacks, and to open to discuss freely. Also, 'Hate Speech' property or copyright problem are emerging.

2. **How might we make people use our project?**
  - **Not only using text, can extend the format of the answer/help such as picture, voice, code, movie, and so on such that the answerer can easily explain something to the questioner.** 
  - **Using directory access format, we can easily upload/check the question. For example, if someone has a question in 15th line, 252 page, biochemistry book, we can just upload the question by typing the command “question /Biochemistry/252/15/ “Question message” ”. Then the tag will be created to the designated line with the question message. This will increase the accessibility by decreasing the time to re-open the pdf file, recheck and find the page and line of the textbook in online.** 
  - **We can create a level of the account, and as level increases, we can offer more beautiful UIs that can make our pdf file much prettier. (such as the number of colors of highlighter)**
  - If we use this in class, we can use this as real grading with how much (s)he contributed to certain file.
  - Like github grass system, we can visualize the amount of contribution. 
  - Adding the level system, we can differentiate the accessibility to datas.
  - We can send notices to our users that they can immediately check what is updated.
  - People can easily sign up to our system, linking with Facebook, Kakao, KAIST Portal, and so on.
  - People would use this platform more if this provides website, IOS and android.
  - We can encourage people to participate more if we give some coins for someone who work actively and (s)he can extend his(her) homework due by using that coin.

3. **How might we design the UI much easier to read and see the contents?**
  - **We provide online to offline service. By dragging some questions and answers to the document you want to print, you can read it which contains the discussions that you read again with the paper.**
  - **There is a hypertext/link function between file-file/comments-comments in our program. Therefore, by clicking this, you can directly move to other place in our service.**
  - **We can control the visibility of certain question/answer/discussion. That is, if there is a tag such that you already know or solved, you can hide that tag to prevent too many tags exists in our display.**
  - We can use vote system to sort all the comments, the comments with a lot of vote comes up on the thread.
  - We can set the different color settings for different question/answer/discussion categories, so users can easily visualize what’s going on with certain file without reading the detail.
  - We can add a hashtag system to categorize the question, so the users can find similar question/answer/discussion not only in one file but also at many files. 
  - Users can customize the UI to make more friendly display for each user. 
  - We can set a rule for adding comment or furthermore discussion as a rule in backchannel in our class. 
  - We can support to users that be able to copy, drag & drop, file share in clipboard.
  - For the users who only want to show summary/introduction/only discussions, we can add a visual setting for showing just summary / discussions / Q&As. 
