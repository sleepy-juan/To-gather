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
var PORT = '12345'

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

// sendPacket: packet, additional -> body
var sendPacket = function(packet, additional = null){
   packet.host = IP;
   packet.port = PORT;

   var body = '';
   var req = http.request(packet, function(res){
      res.on('data', function(chunk){
         body += chunk;
      });
   });

   if(additional != null) req.write(additional);
   req.end();

   return body;
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

   return body;
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
   var body = sendPacket({
      method: 'GET',
      headers: {
         'From':username,
         'CMD':'QUIT',
      }
   });
   console.log(body);
}

// POST - upload question
var post = function(username, question){
   var body = sendPacket({
      method: 'POST',
      headers: {
         'From':username,
         'CMD':'POST',
      }
   }, makeFormat(question));

   console.log(body);
}

// NTYQ - get question ids
var getQuestionIds = function(username){
   var body = sendPacket({
      method: 'GET',
      headers:{
         'From':username,
         'CMD':'NTYQ',
      }
   });

   var format = body.split('\r')[0]
   var response = body.split('\r')[1]
   console.log(response);

   return format.split('\n');
}

// GETQ - get question
var getQuestion = function(username, question_id){
   var body = sendPacket({
      method: "POST",
      headers: {
         'From':username,
         'CMD':'GETQ',
      }
   }, question_id);

   var format = body.split('\r')[0]
   var response = body.split('\r')[1]
   console.log(response);

   return parseFormat(format);
}

// ANSW - answer to question
var answer = function(username, answer){
   var body = sendPacket({
      method: "POST",
      headers: {
         'From':username,
         'CMD':'ANSW'
      }
   }, makeFormat(answer));

   console.log(body);
}

// NTYC - get confirms
var getConfirms = function(username){
   var body = sendPacket({
      method: 'GET',
      headers:{
         'From':username,
         'CMD':'NTYC',
      }
   });

   var format = body.split('\r')[0]
   var response = body.split('\r')[1]
   console.log(response);

   return format.split('\n');
}

// GETA - get answer
var getAnswer = function(username, question_id){
   var body = sendPacket({
      method: "POST",
      headers: {
         'From':username,
         'CMD':'GETA',
      }
   }, question_id);

   var format = body.split('\r')[0]
   var response = body.split('\r')[1]
   console.log(response);

   return parseManyFormat(format);
}

// ENDS - ends question
var endQuestion = function(username, question_id){
   var body = sendPacket({
      method: "POST",
      headers: {
         'From':username,
         'CMD':'ENDS',
      }
   }, question_id);

   console.log(body);
}

// LIST - get list of members
var getMembers = function(username){
   var body = sendPacket({
      method: "GET",
      headers: {
         'From':username,
         'CMD':'LIST',
      }
   });

   var format = body.split('\r')[0]
   var response = body.split('\r')[1]
   console.log(response);

   return format.split('\n');
}

// exports
module.exports = {
  quit: quit,
  post: post,
  getQuestionIds: getQuestionIds,
  getQuestion: getQuestion,
  answer: answer,
  getConfirms: getConfirms,
  getAnswer: getAnswer,
  endQuestion: endQuestion,
  getMembers: getMembers,
};