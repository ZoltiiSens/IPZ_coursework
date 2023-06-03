'use strict'

function closePopup(){
	document.getElementById('active_background').removeAttribute('id');
	document.getElementById('active_popup').removeAttribute('id');
}

function createWeek(){
	document
		.getElementsByClassName('creation_popup')[0]
		.setAttribute('id', 'active_popup');
	document
		.getElementsByClassName('popup_background')[0]
		.setAttribute('id', 'active_background');
}

function editWeek(week_pk){
	document
		.getElementsByClassName(`editing_popup--${week_pk}`)[0]
		.setAttribute('id', 'active_popup');
	document
		.getElementsByClassName('popup_background')[0]
		.setAttribute('id', 'active_background');
}