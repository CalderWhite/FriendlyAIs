var http = require('http');

var server = http.createServer(function(req, res) {
	console.log(req.socket.remoteAddress + " : " + req.method + " : " + req.url)
	var body = [];
	req.on('data', function(chunk) {
	  body.push(chunk);
	}).on('end', function() {
	  body = Buffer.concat(body).toString();
	  // at this point, `body` has the entire req body stored in it as a string
	  console.log(body);
	  if(body.username === "Gokai" && body.userid === "1"){
	  	var resBody = {
	  	"status" : "Good",
	  	"message" : "Proceed"
	  	}
	  }
	  else{
	  	var resBody = {
	  		"status" : "Bad",
	  		"message" : "Bad account request."
	  	}
	  }
	  res.writeHead(200,{"Content-Type" : "application/json"});
	  resData = new Buffer(JSON.stringify(resBody));
	  res.end(resData);
	});
}).listen(3000);
