	
'use strict';
function initMap() {
	const input_lat = document.getElementById('lat');
	const input_lng = document.getElementById('lng');

	let pos = { lat: +input_lat.value, lng: +input_lng.value }
	let opt = new google.maps.Map(document.getElementById("map"), {
		center: pos,
		zoom: 18
	});

	let myMap = new google.maps.Map(document.getElementById('map'), opt);

	let marker = new google.maps.Marker({
		position: pos,
		map: myMap,
	});
	const input  = document.getElementById("id_form-0-adress");
	const options = {
		componentRestrictions: {country: 'ru'},
		types: ['geocode'],
	}
	const autocomplete = new google.maps.places.Autocomplete(input, options)
	

}



document.addEventListener('DOMContentLoaded', () => {

/*	const inputOnlyready = document.getElementById("id_form-0-name");
	inputOnlyready.setAttribute('readonly', 'true');
*/


});



