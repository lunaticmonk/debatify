$(document).ready(function(){
    $('.modal-trigger').leanModal();

$('.dropdown-button').dropdown();

function myfunc(){
	console.log('hello');
}
});

// //AJAX part of upvote
// var upvotebtn = document.querySelector('#upvotebtn');

// upvotebtn.addEventListener('click',function(){
// 	console.log('clicked');
// 	var xhttp = new XMLHttpRequest();
// 	xhttp.onreadystatechange  = function(){
// 		console.log('changed');
// 	};
// 	xhttp.open('GET','{{url_for('auth.upvote')}}',true);
// 	xhttp.send();																							
// });