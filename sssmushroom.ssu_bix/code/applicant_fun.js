var console = require("console");
var request = require("http");

module.exports.function = function applicant_fun (input) {
  var json = request.getUrl("http://210.113.90.239:8081/fun/applicant",{
  });
  var obj = JSON.parse(json)

  return obj
}
