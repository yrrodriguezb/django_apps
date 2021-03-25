function getCookie(name) {
  var v = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
  return v ? v[2] : null;
}

function setCookie(name, value, path, days) {
  var d = new Date;
  d.setTime(d.getTime() + 24*60*60*1000*days);
  document.cookie = name + "=" + value + ";path="+ path + ";expires=" + d.toGMTString();
}

function csrfSafeMethod(method) {
  return (/^(GET|HEAD|OPTIONS|TRACE|POST)$/.test(method));
}

async function _fetch(url, options) {
  if (!csrfSafeMethod(options.method || 'POST'))
    throw new Error("Method not allowed");

  options.fn = options.fn || {};
  options.fn.Ok =  options.fn.Ok || function (data) { }, 
  options.fn.Error = options.fn.Error || function (err) { }

  var response = await fetch(url, options);

  var data = await (options.responseText ? response.text() : response.json());

  if (response.ok)  
    options.fn.Ok(data)
  else
    options.fn.Error(data)
}