$(document).ready(function(){
	$('.open_modal').click(function(event){
		event.preventDefault();
		var href = $(this).attr('href');
		var title = $(this).attr('title-popup');
		if (!title){
			title = $(this).text();
		}
		var height_popup = $(this).attr("height-popup");
		$('#myModalLabel').text(title);
	    $('#myModal').modal('show');
	    $('#myModal iframe').attr('src', href);
	    $('#myModal iframe').attr('height', height_popup);
	});
});

