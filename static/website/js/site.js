jQuery(document).ready(function() {
	$("#login_form").ajaxForm({
		success: function(response) {
			$("#login_form tbody").html(response);
		},
		error: function() {
			location.reload();
		}
	});
	$("#collect_form a").click(function(e) {
		e.preventDefault();
		$("#collect_form").submit();
	});

	// $('#open_collection_link').click(function(e) {
	// 	e.preventDefault();
	// 	show_collect_win();
	// });
});