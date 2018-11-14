/*
   client.js
   - a client javascript module for connecting to python server
   - Use modified version of HTTP/1.1, GET and POST only.

   author @ Juan Lee (juanlee@kaist.ac.kr)
*/

// includes
var http = require('http')

// constants
var IP = '127.0.0.1'
var PORT = '12346'

/*
   Server Protocols
   - GET    QUIT
   - POST   POST
   - GET    NTYQ
   - POST   GETQ
   - POST   ANSW
   - GET    NTYC
   - POST   GETA
   - POST   ENDS
   - GET    LIST
   - OR
*/

// requestPromise
// - syncronous data communication
const requestPromise = (packet, additional = null) =>
   new Promise((resolve, reject) => {
      const isPostWithData = packet && packet.method === "POST" && additional !== null;
      if(isPostWithData && (!packet.headers || !packet.headers["Content-Length"])) {
         packet = Object.assign({}, packet, {
            headers: Object.assign({}, packet.headers, {
               "Content-Length": additional.length,
            })
         });
      }

      const body = [];
      const req = http.request(packet, res => {
         res.on('data', chunk => {
            body.push(chunk);
         });
         res.on('end', () => {
            res.body = Buffer.concat(body);
            resolve(res);
         });
      });

      req.on('error', e => {
         reject(e);
      });

      if (isPostWithData){
         req.write(additional);
      }
      req.end();
   });

// sendPacket: packet, additional -> body
var sendPacket = async function(packet, additional = null){
   packet.host = IP;
   packet.port = PORT;
   
   const bodyPromise = await requestPromise(packet, additional);
   return bodyPromise.body.toString();
}

// makeFormat: format -> string
var makeFormat = function(format){
   var body = '';
   body += format.content.user + '\n';
   body += format.comment.text + '\n';
   body += format.content.text + '\n';
   body += format.content.common + '\n';

   body += format.position.boundingRect.x1.toString() + '\n';
   body += format.position.boundingRect.y1.toString() + '\n';
   body += format.position.boundingRect.x2.toString() + '\n';
   body += format.position.boundingRect.y2.toString() + '\n';
   body += format.position.boundingRect.width.toString() + '\n';
   body += format.position.boundingRect.height.toString() + '\n';

   var rects_size = format.position.rects.length;
   body += rects_size.toString() + '\n';
   format.position.rects.forEach(function(rect){
      body += rect.x1.toString() + '\n';
      body += rect.y1.toString() + '\n';
      body += rect.x2.toString() + '\n';
      body += rect.y2.toString() + '\n';
      body += rect.width.toString() + '\n';
      body += rect.height.toString() + '\n';
   });

   body += format.position.pageNumber.toString() + '\n';
   body += format.id;

   return body.trim();
}

// parseFormat: string -> format
var parseFormat = function(body){
   var lines = body.split('\n');
   var rects = [];
   var rects_size = parseInt(lines[10]);

   for(var i =0; i < rects_size; i++){
      rects.push({
         x1: parseFloat(lines[11 + i*6]),
         y1: parseFloat(lines[11 + i*6 + 1]),
         x2: parseFloat(lines[11 + i*6 + 2]),
         y2: parseFloat(lines[11 + i*6 + 3]),
         width: parseFloat(lines[11 + i*6 + 4]),
         height: parseFloat(lines[11 + i*6 + 5]),
      });
   }

   return {
      content: {
         user: lines[0],
         text: lines[2],
         common: lines[3],
      },
      position: {
         boundingRect: {
            x1: parseFloat(lines[4]),
            y1: parseFloat(lines[5]),
            x2: parseFloat(lines[6]),
            y2: parseFloat(lines[7]),
            width: parseFloat(lines[8]),
            height: parseFloat(lines[9]),
         },
         rects: rects,
         pageNumber: parseInt(lines[-2]),
      },
      comment: {
         text: lines[1],
      },
      id: lines[-1],
   }
}

// body -> list of formats
var parseManyFormat = function(body){
   var lines = body.split('\n');
   var num_lines = lines.length;
   var formats = [];

   var i = 0;
   while(i < num_lines){
      var size = parseInt(lines[i++]);
      var format = parseFormat(lines.slice(i, i+size).join('\n'));
      formats.push(format);
      i += size;
   }

   return formats;
}

// QUIT - disconnect from server
var quit = function(username){
   return sendPacket({
      method: 'GET',
      headers: {
         'From':username,
         'CMD':'QUIT',
      }
   });
}

// POST - upload question
var post = function(username, question){
   question.content.user = username;
   var additional = makeFormat(question);
   return sendPacket({
      method: 'POST',
      headers: {
         'From':username,
         'CMD':'POST',
         'Content-Length': additional.length,
      }
   }, additional);
}

// NTYQ - get question ids
var getQuestionIds = function(username){
   return sendPacket({
      method: 'GET',
      headers:{
         'From':username,
         'CMD':'NTYQ',
      }
   });
}

// GETQ - get question
var getQuestion = function(username, question_id){
   return sendPacket({
      method: "POST",
      headers: {
         'From':username,
         'CMD':'GETQ',
         'Content-Length':question_id.length,
      }
   }, question_id);

   /*
   if(body === ''){
      console.log("server is not on");
      return null;
   }

   var format = body.split('\r')[0].trim();
   var response = body.split('\r')[1].trim();
   console.log(response);

   return parseFormat(format);
   */
}

// ANSW - answer to question
var answer = function(username, answer){
   answer.content.user = username;
   var additional = makeFormat(answer);
   return sendPacket({
      method: "POST",
      headers: {
         'From':username,
         'CMD':'ANSW',
         'Content-Length':additional.length,
      }
   }, additional);
}

// NTYC - get confirms
var getConfirms = function(username){
   return sendPacket({
      method: 'GET',
      headers:{
         'From':username,
         'CMD':'NTYC',
      }
   });

   /*
   if(body === ''){
      console.log("server is not on");
      return [];
   }

   var format = body.split('\r')[0].trim();
   var response = body.split('\r')[1].trim();
   console.log(response);

   return format.split('\n');
   */
}

// GETA - get answer
var getAnswer = function(username, question_id){
   return sendPacket({
      method: "POST",
      headers: {
         'From':username,
         'CMD':'GETA',
         'Content-Length':question_id.length,
      }
   }, question_id);

   /*
   if(body === ''){
      console.log("server is not on");
      return null;
   }

   var format = body.split('\r')[0].trim();
   var response = body.split('\r')[1].trim();
   console.log(response);

   return parseManyFormat(format);
   */
}

// ENDS - ends question
var endQuestion = function(username, question_id){
   return sendPacket({
      method: "POST",
      headers: {
         'From':username,
         'CMD':'ENDS',
         'Content-Length':question_id.length,
      }
   }, question_id);
}

// LIST - get list of members
var getMembers = function(username){
   return sendPacket({
      method: "GET",
      headers: {
         'From':username,
         'CMD':'LIST',
      }
   });

   /*
   if(body === ''){
      console.log("server is not on");
      return [];
   }

   var format = body.split('\r')[0].trim();
   var response = body.split('\r')[1].trim();
   console.log(response);

   return format.split('\n');
   */
}

// exports
export default {
  quit: quit,
  post: post,
  getQuestionIds: getQuestionIds,
  getQuestion: getQuestion,
  answer: answer,
  getConfirms: getConfirms,
  getAnswer: getAnswer,
  endQuestion: endQuestion,
  getMembers: getMembers,
  parseFormat: parseFormat,
};
