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

function validate()
{
	var is_valid = true;

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

		console.log(el, from, to, placeholder, value);

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

validate();