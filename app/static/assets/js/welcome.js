(function(){
	$('.dropdown-button').dropdown({
		belowOrigin : false
	});
	$('.modal-trigger').leanModal();
	$('collapsible').collapsible({
		accordion: false
	});
	append();
})();

function grab(){
		//alert('hello');
		var question = document.querySelector('#textarea1').value;
		var topic = document.querySelector('#topic').value;
		var div1 = document.createElement('div');
		var div3 = document.createElement('i');
		div1.innerHTML = topic;
		div1.appendChild(div3);
		div3.classList.add('material-icons');
		div3.innerHTML = "view_list";
		var div2 = document.createElement('div');
		var z = document.createElement('p');
		div2.appendChild(z);
		z.innerHTML = question;
		div2.classList.add('collapsible-body');
		div1.classList.add('collapsible-header');
		var node = document.createElement('LI');
		node.appendChild(div1);
		node.appendChild(div2);
		//console.log(node);
		return node;
	}	
	function append(){
		var raisebtn = document.querySelector('#raisebtn');
		raisebtn.addEventListener('click',function(){
			var newNode = grab();
			//sendNode();
			var accordion = document.querySelector('#accordion');
			accordion.appendChild(newNode);
		});
	}

	// function sendNode(){
	// 	var xhttp = new XMLHttpRequest();
	// 	var url = "{{url_for('auth.index')}}"
	// 	var question = document.querySelector('#textarea1').value;
	// 	var topic = document.querySelector('#topic').value;
	// 	var params = ('TOPIC = topic&QUESTION = question')
	// 	console.log(params);
	// 	xhttp.open('POST',url,true);
	// 	console.log('hello');
	// 	xhttp.onreadystatechange = function() {//Call a function when the state changes.
 //    		if(xhttp.readyState == 4 && xhttp.status == 200) {
 //        	console.log(xhttp.responseText);
 //    		}
	// 	}
	// 	xhttp.send(params);
	// }