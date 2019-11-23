var console = require("console");
var request = require("http");

module.exports.function = function get_info_cse (input) {
  var json = request.getUrl("http://210.113.90.239:8081/cse/notice",{
    format: 'json',
    cacheTime: 0
  });
  console.log(json)
  return json
}
