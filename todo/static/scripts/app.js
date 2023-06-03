'use strict'

function closePopup(){
	console.log(12123123)
	console.log(document.getElementById('active_background'))
	console.log(document.getElementById('active_popup'))
	document
		.getElementById('active_background')
		.removeAttribute('id');
	document
		.getElementById('active_popup')
		.removeAttribute('id');

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

function editTodo(todo_pk){
	document
		.getElementsByClassName(`editing_popup--${todo_pk}`)[0]
		.setAttribute('id', 'active_popup');
	document
		.getElementsByClassName('popup_background')[0]
		.setAttribute('id', 'active_background');
}

function editDay(todo_pk, day_pk){
	let day_input = document.getElementById(`change_day--${ todo_pk }--${day_pk}`);
	let day_img = document.getElementById(`img_day--${ todo_pk }--${day_pk}`);
	let current_val = 0;
	console.log(day_input.value)
	if (day_input.value !== "5"){
		current_val = +day_input.value + 1;
	}
	day_input.value = current_val;
	day_img.src = `/static/images/${current_val}.svg`
}