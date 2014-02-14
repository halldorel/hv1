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


function reikna()
{
	var lanaListi = [];
	var formList = $('#lanalisti form div.row');
	formList.each(function(i)
	{
		var drasl = $(this).children('div');
		lanaListi[i] = {
			nafn 	: drasl.children('input.nafn').val(),
			haus	: drasl.children('input.haus').val(),
			vextir	: drasl.children('input.vextir').val(),
			lengd	: drasl.children('input.lengd').val(),
			verdtr 	: ((drasl.children('div.checkbox').children().children('.verdtryggt')[0].checked) ? 1 : 0)
		}
	});

	var sparnadur = {
		greidslugeta 	: $('#greidslugeta').val(),
		hvenaer 		: $('#hvenaer').val(),
		upphaed			: $('#upphaed').val()
	};

	var reikningar = [];
	if ($('#180')[0].checked) reikningar.append({reikningur: "Kjörbók", vextir: 1.80});
	if ($('#445')[0].checked) reikningar.append({reikningur: "Sparireikningur", vextir: 4.45});
	if ($('#425')[0].checked) reikningar.append({reikningur: "Vaxtareikningur", vextir: 4.25});
	if ($('#190')[0].checked) reikningar.append({reikningur: "Landsbók", vextir: 1.90});

	var data = {
		lan 	: lanaListi,
		spar 	: sparnadur,
		reikn 	: reikningar
	}

	$.ajax({
		type: 'GET',
		url: '/internet.py',
		data: JSON.stringify(data),
		success: function(result) {
			console.log(JSON.stringify(data));
			alert("snilld");
			console.log(result);
		},
		error: function() {
			alert("mistök");
		}
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
