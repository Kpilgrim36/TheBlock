var button = $("#red_led_button");
var button2 = $("#yellow_led_button");
var button3 = $("#blinking_button")

button.click(function(){
	console.log(button.text());
	if(button.text() === "Red LED On"){
		$.ajax({
			url: "/red_led_on",
			type: "post",
			success: function(response){
				console.log(response);
				button.text("Red LED Off");
			}
		});
	}else{
		$.ajax({
			url: "/red_led_off",
			type: "post",
			success: function(){
				button.text("Red LED On");
			}
		})
	}
});

button2.click(function(){
	console.log(button2.text());
	if(button2.text() === "Yellow LED On"){
		$.ajax({
			url: "/yellow_led_on",
			type: "post",
			success: function(responsey){
				console.log(responsey);
				button2.text("Yellow LED Off");
			}
		});
	}else{
		$.ajax({
			url: "/yellow_led_off",
			type: "post",
			success: function(){
				button2.text("Yellow LED On");
			}
		})
	}
});

button3.click(function(){
	console.log(button3.text());
	if(button3.text() === "Loop On"){
		button3.text("Loop Off")
		$.ajax({
			url: "/blinking_thread",
			type: "post",
			success: function(responseblink){
				console.log(responseblink);
				button3.text("Loop Off");
			}
		});
	}else{
		$.ajax({
			url: "/blinking_off",
			type: "post",
			success: function(){
				button3.text("Loop On");
			}
		})
	}
});