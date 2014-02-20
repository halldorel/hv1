var lines, bars, graphs;

function reikna()
{
	var lanaListi = [];
	var formList = $('#lanalisti form div.row');
	formList.each(function(i)
	{
		var drasl = $(this).children('div');

		lanaListi[i] = {
			nafn 	: drasl.children('input.nafn').val(),
			haus	: drasl.children('div.haus').children('input.haus').val(),
			vextir	: drasl.children('div.vextir').children('input.vextir').val(),
			lengd	: drasl.children('div.lengd').children('input.lengd').val(),
			verdtr 	: ((drasl.children('div.checkbox').children().children('.verdtryggt')[0].checked) ? 1 : 0)
		}
		if (lanaListi[i].vextir >= 1) lanaListi[i].vextir *= 0.01;
	});

	var sparnadur = {
		greidslugeta 	: $('#greidslugeta').val(),
		hvenaer 		: $('#hvenaer').val(),
		upphaed			: $('#upphaed').val(),
		eign 			: $('#eign').val()
	};

	var reikningar = [];
	if ($('#180')[0].checked) reikningar.push({reikningur: "Kjörbók", vextir: 1.80});
	if ($('#445')[0].checked) reikningar.push({reikningur: "Sparireikningur", vextir: 4.45});
	if ($('#425')[0].checked) reikningar.push({reikningur: "Vaxtareikningur", vextir: 4.25});
	if ($('#190')[0].checked) reikningar.push({reikningur: "Landsbók", vextir: 1.90});

	var data = {
		lan 	: lanaListi,
		spar 	: sparnadur,
		reikn 	: reikningar
	}
	console.log(data);

	var json_data = JSON.stringify(data);

	$.ajax({
		type: 'GET',
		url: '/internet.py',
		data: {jsonstring : json_data},
		success: function(result) {
			console.log(result);
			renderResults(result);
		},
		error: function(result) {
			displayAlert('Mikil mistök í gangi hjá bakenda. Skamm.')
			console.log(result.responseText);
		}
	});
}

function renderResults(result)
{
	$('#results').css('display', 'block');
    $('#graphs').empty();
	renderLines(result.lanVenjulega, result.lanAukalega);
	renderBars(result.bestaGreidsluskiptingLana);
console.log(result.verdbolga);
	$('td#verdbolga-result').html("" + result.verdbolga + " %");
	$('td#lansupphaed-result').html("" + result.haestaMogulegtLan);
	$('td#raunvextir-result').html("" + result.maxAllt);
	$('td#borga-result').html("" + result.bestaGreidsluskiptingLana[0].nafn);

	var html = "";
	var result_el = $("#result-table");
	if(result_el.hasClass('hidden'))
		result_el.removeClass('hidden');

	$.each(result.sparnadurVaxtagrodi, function(key, val) {
		html += "<tr><td>" + val.nafn + "</td><td>" + val.vextir + " %</td><td>" + val.sparnadur + " kr.</td></tr>";
	});
	$("#vaxtagrodi").html(html);

	var html = ""
	$.each(result.timiAdTakmarki, function(key, val) {
		html += "<tr><td>" + val.nafn + "</td><td>" + val.vextir + " %</td><td>" + val.timi + " mánuðuðir</td></tr>";
	});
	$("#sparnadartakmark").html(html);

}

function renderLines(lv, la)
{
	for (var l in lv)
	{
		var row = $('<div class="row"><p class="lead">' + lv[l].nafn + '</p></div>');
		var g = $('<canvas id="lines' + l + '" width="600" height="250"></canvas>');
		row.append(g);
		$('#graphs').append(row);
		var heild = lv[l].val.heildargreidslur;
		console.log(heild);
		var label = []
		for (var i = 0; i < heild.length; i++)
		{
			label[i] = i + ' mán';
		}
		var auka = la[l].val.heildargreidslur;
		console.log(auka);
		for (var h in heild)
		{
			if (!auka[h]) auka[h] = 0.0;
		}
		var lineData = {
			labels : label,
			datasets : [
				{
					fillColor : "rgba(220,220,220,0.5)",
					strokeColor : "rgba(220,220,220,1)",
					pointColor : "rgba(220,220,220,1)",
					pointStrokeColor : "#fff",
					data : heild
				},
				{
					fillColor : "rgba(151,187,205,0.5)",
					strokeColor : "rgba(151,187,205,1)",
					pointColor : "rgba(151,187,205,1)",
					pointStrokeColor : "#fff",
					data : auka
				}
			]
		};
		var context = getLineCtx(l);
		context.create(lineData, GraphInit.lineOptions);
	}
}

function renderBars(bg)
{
	var names = [];
	var vals = [];
	for (var b in bg)
	{
		names[b] = bg[b].nafn;
		vals[b] = bg[b].vextir;
	}
	var barData = {
		labels : names,
		datasets : [
			{
				fillColor : "rgba(220,220,220,0.5)",
				strokeColor : "rgba(220,220,220,1)",
				data : vals
			}
		]
	};
	var row = $('<div class="row"><p class="lead">Hvaða lán á að borga upp?</p></div>');
	var g = $('<canvas id="bars' + 0 + '" width="600" height="250"></canvas>');
	row.append(g);
	$('#graphs').append(row);
	var context = getBarCtx(0);
	context.create(barData, GraphInit.barOptions);
}


var lan = 0;
$(document).ready(function () {

	var meira_btn = $("#meira-lan");
	var meira_tmp = $("#lan-tmp").html();
	var remove_btn = $("button.remove");
	var lana_list = $("#lanalisti");

	var graphs = $('#graphs');
	console.log(graphs);
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
		if(validate())
			reikna();
		else
			displayAlert("Vinsamlegast lagfærðu villur");
	});
});
