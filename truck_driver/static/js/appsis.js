'use strict';



document.addEventListener('DOMContentLoaded', () => {
	const inputCreateOrderStart = document.getElementById('id_form-0-adress_start');
	const inputCreateOrderEnd = document.getElementById('id_form-0-adress_end');
	const options = {
		componentRestrictions: {country: 'ru'},
		types: ['geocode'],
	}
	const autocompleteTWo = new google.maps.places.Autocomplete(inputCreateOrderStart, options);
	const autocomplete = new google.maps.places.Autocomplete(inputCreateOrderEnd, options);







});