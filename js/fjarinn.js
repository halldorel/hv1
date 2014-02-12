var barData = {
	labels : ["Krummi","Smálán","Yfirdráttur","Húsnæði"],
	datasets : [
		{
			fillColor : "rgba(220,220,220,0.5)",
			strokeColor : "rgba(220,220,220,1)",
			data : [65,59,45,5]
		}
	]
};

var lineData = {
	labels : ["1","2","3","4","5","6","7"],
	datasets : [
		{
			fillColor : "rgba(220,220,220,0.5)",
			strokeColor : "rgba(220,220,220,1)",
			pointColor : "rgba(220,220,220,1)",
			pointStrokeColor : "#fff",
			data : [65,64,63,61,60,57,55]
		},
		{
			fillColor : "rgba(151,187,205,0.5)",
			strokeColor : "rgba(151,187,205,1)",
			pointColor : "rgba(151,187,205,1)",
			pointStrokeColor : "#fff",
			data : [65,62,59,57,55,52,51]
		}
	]
};

var lanaListi = [];
function Lan(nafn, upph, vextir, lengd, verdtr)
{
	this.nafn 	= nafn;
	this.upph 	= upph;
	this.vextir = vextir;
	this.lengd 	= lengd;
	this.verdtr = verdtr || false;
}

function reikna()
{
	var formList = $('#lanalisti form div.row');
	formList.each(function(i)
	{
		$(this).children('div').each(function(i)
		{
			console.log($(this).children('input'));
		});
	});
}

var lan = 0;
$(document).ready(function () {

	var meira_btn = $("#meira-lan");
	var meira_tmp = $("#lan-tmp").html();
	var remove_btn = $("button.remove");
	var lana_list = $("#lanalisti");

	lana_list.delegate('button.remove', 'click', function (e) {
		$(this).parent().parent().parent().slideToggle(100, function () {this.remove();});
		lan--;
	});
	
	var meira_compiled = _.template(meira_tmp);
	
	meira_btn.click(function() {
		lana_list.append(meira_compiled);
		lan++;
	});

	remove_btn.click(function() {
		this.parent().remove();
	});

	$('#reikna').click(function() {
		reikna();
	});

	var lines = LineGraph.create(lineData, GraphInit.lineOptions);
	var bars = BarGraph.create(barData, GraphInit.barOptions);
});
