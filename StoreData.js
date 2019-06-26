var request = require("request");

var options = { method: 'POST',
  url: 'URL[DEVICE]',
  headers:
   { 'cache-control': 'no-cache',
     'content-type': 'application/json;ty=4',
     'x-m2m-origin': 'access-id:access-password [key in account]' },
  body: '\r\n{\r\n  "m2m:cin": {\r\n    "cnf": "message",\r\n    "con": "\r\n      {\r\n      \t \\"status\\": \\"0\\",\r\n         \\"dim\\": \\"10\\"\r\n      }\r\n    "\r\n  }\r\n}' };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});