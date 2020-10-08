'use strict';

document.addEventListener('DOMContentLoaded', () => {
	const spanKilo = document.getElementById('in_kilo'),
		  createOrder = document.getElementById('form_create'),
		  formCreateOrder = document.getElementById('form_create_order'),
	      resultCalculate = document.getElementById('result'),
		  subInput = document.getElementById('cal'),
		  formCalculate = document.getElementById('distance_form'),
	      inputCreateOrderStarts = document.getElementById('from_places'),
		  inputCreateOrderEnds = document.getElementById('to_places'),
		  subInputTwo = document.getElementById('cal_two'),
	      options = {
				componentRestrictions: {country: 'ru'},
				types: ['geocode'],
		  };
	const autocompleteTWo = new google.maps.places.Autocomplete(inputCreateOrderStarts, options);
	const autocomplete = new google.maps.places.Autocomplete(inputCreateOrderEnds, options);


	function calculateDistance(){ // функция рассчета дистанции api google maps
		var origin = inputCreateOrderStarts.value;
		var destination = inputCreateOrderEnds.value;

		var service = new google.maps.DistanceMatrixService();
		service.getDistanceMatrix(
		{
			origins: [origin],
			destinations: [destination],
			travelMode: 'DRIVING',
			avoidHighways: false,
			avoidTolls: false,
		}, callback);
	}
	function callback(response, status) { //расчет дистанции и времени
		if (status === 'OK') {
			var origin = response.originAddresses[0];
			var destination = inputCreateOrderEnds.value;
			let distance = response.rows[0].elements[0].distance;			
			let duration = response.rows[0].elements[0].duration; 
			let distance_in_kilo = distance.value / 1000;
			let duration_text = duration.text;
			let duration_value = duration.value;
			if (resultCalculate.style.display != 'none') {
				spanKilo.innerHTML = distance_in_kilo.toFixed(0);
				document.getElementById('duration_text').innerHTML = duration_text;
				document.getElementById('from').innerHTML = origin;
				document.getElementById('to').innerHTML = destination;
				if (document.getElementById('form_prices')) {
					document.getElementById('prices').innerHTML = +document.getElementById('form_prices').value;
					document.getElementById('price_kilos').innerHTML = +(document.getElementById('form_prices').value / distance_in_kilo).toFixed(2);
				} 
				if (document.getElementById('form_price_kilos').value != '') {
					document.getElementById('price_kilos').innerHTML = document.getElementById('form_price_kilos').value;
					document.getElementById('prices').innerHTML = +(document.getElementById('form_price_kilos').value * distance_in_kilo).toFixed(2);
				}
			}
			if (formCreateOrder.style.display != 'none') {
				console.log('1');

				console.log('2');
				document.getElementById('id_form-0-adress_start').value = origin;
				document.getElementById('id_form-0-adress_end').value = destination;
				document.getElementById('id_form-0-time_in_distance').value = duration_text;
				document.getElementById('id_form-0-distance').value = distance_in_kilo.toFixed(0);
				if (document.getElementById('form_prices')) {
					console.log('3');
					document.getElementById('id_form-0-price').value = +document.getElementById('form_prices').value;
					document.getElementById("id_form-0-price_on_kilo").value = +(document.getElementById('form_prices').value / distance_in_kilo).toFixed(2);
				}
				if (document.getElementById('form_price_kilos').value != '') {
					console.log('4');
					document.getElementById('id_form-0-price_on_kilo').value = document.getElementById('form_price_kilos').value;
					document.getElementById('id_form-0-price').value = +(document.getElementById('form_price_kilos').value * distance_in_kilo).toFixed(2);
				}
				console.log('5');
				//inputDisabled(); 
			}
		}
	}

 
		
	

	subInput.addEventListener('click', function(e) { //вызов 
		if (resultCalculate.style.display != 'none') {
			e.preventDefault();
			calculateDistance();
		} 
		// if(resultCalculate.style.display == 'none') {
		// 	e.preventDefault();
		// 	formCreateOrder.style.display = 'inline';
		// 	if (document.getElementById('from_places') & document.getElementById('to_places')) {
		// 		console.log('display_in');
		// 	}
		// }
	});

	// блок скрытия цены
	const addDistanceInput = document.getElementById('form_price_kilos');
	const addDistancePrice = document.getElementById('form_prices');
	function addDistance() {
		if (addDistanceInput != '') {
			addDistancePrice.disabled = true;
		} 
		if (addDistanceInput.value == '') {
			addDistancePrice.disabled = false;
		}	}
	function addDistanceKilo() {
		if (addDistancePrice) {
			addDistanceInput.disabled = true;
		}
		if (addDistancePrice.value == '') {
			addDistanceInput.disabled = false;
		}
	}
	
	addDistanceInput.addEventListener('keyup', addDistance);
	addDistancePrice.addEventListener('keyup', addDistanceKilo);

	//Добавляем форму заполнения заказа
	createOrder.addEventListener('click', () => {
		resultCalculate.style.display = 'none';
		document.getElementById('title').innerHTML = 'Заполните адреса и цену нажмите продолжить';
		subInput.style.display = 'none';
		subInputTwo.style.display = 'inline';		
	});
	// Добавление города отправки
	function addCityStart() {
		let cityStart = document.getElementById('id_form-0-citi_start'),
			tmp = '';
		autocompleteTWo.getPlace().address_components.forEach(function(item) {
		tmp = item.long_name;
		if(item.types) {
			item.types.forEach(function(t) {
				switch(t) {
					case 'locality': cityStart.value = 'г.' + tmp;
					break;
				}

			});
		}
	});	
	}
	// Добавление города финиша
	function addCityEnd() {
		let cityEnd = document.getElementById('id_form-0-citi_end'),
			tmp = '';
		autocomplete.getPlace().address_components.forEach(function(item) {
		tmp = item.long_name;
		if(item.types) {
			item.types.forEach(function(t) {
				switch(t) {
					case 'locality': cityEnd.value = 'г.' + tmp;
					break;
				}

			});
		}
	});	
	}

	subInputTwo.addEventListener('click', (e) => {
		document.getElementById('title').innerHTML = 'Проверьте данные и заполните пустые поля';
		formCalculate.style.display = 'none';
		formCreateOrder.style.display = 'inline';
		e.preventDefault();
		calculateDistance();
		addCityStart();
		addCityEnd();
	});
	// function inputDisabled() {
	// 	document.getElementById('id_form-0-data_publish').type = 'datetime-local';
	// 	let inputFor =  document.querySelectorAll('input');
	// 	for (let i = 0; i < inputFor.length; i++ ) {
	// 		if(inputFor[i].type != 'submit' && inputFor[i].value != '') {
	// 			inputFor[i].disabled = true;
	// 		}if(document.getElementById('id_form-0-count')) {
	// 			document.getElementById('id_form-0-count').disabled = false;
	// 		}	
	// 	}

	//}


});