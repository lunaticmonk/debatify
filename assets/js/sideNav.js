 // Initialize collapse button
 (function(){
  $(".button-collapse").sideNav({
  	menuWidth : 300,
  	edge : 'top'
  });


	var loginpanel = document.querySelector('#loginpanel');
	console.log(loginpanel);
	loginpanel.style.visibility = "hidden";

	var signinbtn = document.querySelector('#signinbtn');
	signinbtn.addEventListener('click',function(){
		console.log('hello');
		loginpanel.style.visibility = "visible";
		// loginpanel.style.transition = "opacity 5s";
		// loginpanel.style.opacity = "1";
	});
 })();
  // Initialize collapsible (uncomment the line below if you use the dropdown variation)
  //$('.collapsible').collapsible();
        

//Login panel
