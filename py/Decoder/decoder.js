var waktrinser = require('@methodwakfu-public/waktrinser');

//console.log(waktrinser.default.decodeString("[#1] PV",[155.0, 0.0, 1.0, 0.0, 0.0, 0.0],106));
//console.log(waktrinser.default.decodeString("[#1] Contrôle",[1.0, 0.0],106));
//console.log(waktrinser.default.decodeString("[#1] Maîtrise Zone",[10.0, 0.0],106));

var string = process.argv[2];
var parameters = JSON.parse(process.argv[3]);
var level =parseInt(process.argv[4]);

var parsedString = waktrinser.default.decodeString(string, parameters,level);
console.log(parsedString); 