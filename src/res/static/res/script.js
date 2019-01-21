function reqListener () {
  console.log(this.responseText);
  var data = JSON.parse(this.responseText);
  var svg = document.getElementById('graphic');
  for (var key in data) {
  	console.log(data[key]["x"]);
  	
  	var g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
  	var rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
  	var text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  	var txtMsg = document.createTextNode("" + key + "-" + data[key]["places"]);
  	text.appendChild(txtMsg);

  	rect.setAttributeNS(null, 'x', data[key]['x']+"%");
  	rect.setAttributeNS(null, 'y', data[key]['y']+"%");
  	rect.setAttributeNS(null, 'width', data[key]['length']+"%");
  	rect.setAttributeNS(null, 'height', data[key]['width']+"%");
  	rect.setAttributeNS(null, 'fill', 'red');
  	
  	if (data[key]["shape"] === "OVAL") {
  		rect.setAttributeNS(null, 'rx', "5%");
  		rect.setAttributeNS(null, 'ry', "5%");
  	}

  	text.setAttributeNS(null, 'x', data[key]['x']+"%");
  	text.setAttributeNS(null, 'y', data[key]['y']+"%");
  	
  	var width = parseFloat(rect.getAttributeNS(null, 'width'));
  	text.setAttributeNS(null, 'dx', 0.4*width);
  	
  	var height = parseFloat(rect.getAttributeNS(null, 'height'));
  	text.setAttributeNS(null, 'dy', 2*height);
  	
  	g.appendChild(rect);
  	g.appendChild(text);

  	if (!data[key]['reserved']) {
  		var a = document.createElementNS('http://www.w3.org/2000/svg', 'a');
  		rect.setAttributeNS(null, 'class', "notReservedTable");
  		a.appendChild(g);
  		a.setAttributeNS(null, 'href', data[key]["link"]);
  		svg.appendChild(a);
  	} else {
  		rect.setAttributeNS(null, 'class', "reservedTable");
  		svg.appendChild(g);
  	}
  	

  	};
  	console.log(svg);
  };


var oReq = new XMLHttpRequest();
oReq.addEventListener("load", reqListener);
oReq.open("GET", "/get_tables");
oReq.send();
