const crypto = require('crypto-js');
const nonce = CryptoJS.lib.WordArray.random(16).toString(CryptoJS.enc.Base64);
const created = new Date().toISOString();
const password = pm.environment.get("password");
const digest = CryptoJS.SHA1(
  CryptoJS.enc.Base64.parse(nonce) +
  CryptoJS.enc.Utf8.parse(created) +
  CryptoJS.enc.Utf8.parse(password)
).toString(CryptoJS.enc.Base64);

pm.request.headers.add({
  key: 'Content-Type',
  value: 'text/xml;charset=UTF-8'
});

// Вставить в XML-тело:
// <wsse:Nonce EncodingType="...#Base64Binary">{{nonce}}</wsse:Nonce>
// <wsu:Created>{{created}}</wsu:Created>
// <wsse:Password Type="...#PasswordDigest">{{digest}}</wsse:Password>
