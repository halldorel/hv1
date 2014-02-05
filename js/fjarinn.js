$(document).ready(function () {

	var meira_btn = $("#meira-lan");
	var meira_tmp = $("#lan-tmp").html();
	var remove_btn = $("button.remove");
	var lana_list = $("#lanalisti");

	lana_list.delegate('button.remove', 'click', function (e) {
		$(this).parent().parent().slideToggle(100, function () {this.remove();});
	});
	
	var meira_compiled = _.template(meira_tmp);
	
	meira_btn.click(function() {
		//console.log("clicked");
		lana_list.append(meira_compiled);
	});

	remove_btn.click(function() {
		this.parent().remove();
	})
});
