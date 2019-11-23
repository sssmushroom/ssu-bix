var console = require("console");
var request = require("http");

module.exports.function = function main (input) {
  var json = request.getUrl("http://210.113.90.239:5000/res1.json",{
  });
  var obj = JSON.parse(json)
  console.log(obj)

  var test1 = [
    {"depart": "스파르탄 교육원",
    "title": "글로벌 SW 인턴십 프로그램",
    "URL": "https://fun.ssu.ac.kr/ko/program/all/view/1310",
    "thumbnailImage": "https://fun.ssu.ac.kr/attachment/view/43396/cover.png",
    "date": "2019.11.22(금) ~ 2019.12.20(금)"
    },
    
    {"depart": "교육과정혁신센터",
    "title": "두드림학기 공모전",
    "URL": "https://fun.ssu.ac.kr/ko/program/all/view/1285",
    "thumbnailImage": "https://fun.ssu.ac.kr/attachment/view/42901/cover.png",
    "date": "2019.11.22(금) 09:00 ~ 2019.12.20(금) 09:00"
    }
  ]

  return obj
}
