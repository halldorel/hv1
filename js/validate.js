// Fékk isNumber lánað af
// http://stackoverflow.com/questions/18082/validate-numbers-in-javascript-isnumeric
// Takk, internet. Lofa að skila fallinu aftur.

function isNumber(n)
{
	return !isNaN(parseFloat(n)) && isFinite(n);
}

function mark(el)
{
	el.parent().addClass('has-error');
}

function unmark(el)
{
	if(el.parent().hasClass('has-error'))
	{
		el.parent().removeClass('has-error');
	}
}

function displayAlert(alert)
{
	var alert_box = $("#alerts");
	if(alert === undefined)
		alert_box.html('');
	else
		alert_box.append('<div class="alert alert-danger alert-dismissable">' + alert + '<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button></div>');
}

function validate()
{
	displayAlert();

	var is_valid = true;
	var some_checked = $('input[type="checkbox"]:checked').length > 0;

	if(!some_checked) { displayAlert('Velja verður a.m.k. einn sparnaðarreikning'); }

	$("input[type='number']").each(function(){
		var el = $(this);
		var from = parseFloat(el.attr('from'));
		var to = parseFloat(el.attr('to'));
		var placeholder = el.attr('placeholder');
		var value = el.val();

		if(isNaN(from))
			from = Number.MIN_VALUE;
		if(isNaN(to))
			to = Number.MAX_VALUE;

		if(value === undefined || value === "" || value == "" || !isNumber(value))
		{
			is_valid = false;
			mark(el);
		}

		else
		{
			if((value < from) || (value > to))
			{
				is_valid = false;
				mark(el);
			}
			else
			{
				unmark(el);
			}
		}
	});

	return is_valid;
}