$(document).ready(function () {

	var meira_btn = $("#meira-lan");
	var meira_tmp = $("#lan-tmp").html();
	var lana_list = $("#lanalisti");
	
	var meira_compiled = _.template(meira_tmp);
	
	meira_btn.click(function() {
		console.log("clicked");
		lana_list.prepend(meira_compiled
	)});
});
