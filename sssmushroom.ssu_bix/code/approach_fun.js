var console = require("console");
var request = require("http");

module.exports.function = function approach_fun (input) {
  var json = request.getUrl("http://210.113.90.239:8081/fun/approach",{
  });
  var obj = JSON.parse(json)
  return obj
}
