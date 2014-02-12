

var LineGraph = {
	ctx 		: null,
	chart 		: null,
	create 		: function(data, options) {
		this.ctx 	= $("#lines").get(0).getContext("2d");
		this.chart 	= new Chart(this.ctx).Line(data,options);
	}
};

var BarGraph = {
	ctx 		: null,
	chart 		: null,
	create 		: function(data, options) {
		this.ctx 	= $("#bars").get(0).getContext("2d");
		this.chart 	= new Chart(this.ctx).Bar(data,options);
	}
};


var GraphInit = {
	lineOptions : {			
		scaleOverlay 		: false,
		scaleOverride 		: false,
		scaleSteps 			: null,
		scaleStepWidth 		: null,
		scaleStartValue 	: null,
		scaleLineColor 		: "rgba(0,0,0,.1)",
		scaleLineWidth 		: 1,
		scaleShowLabels 	: true,
		scaleLabel 			: "<%=value%>",
		scaleFontFamily 	: "'Arial'",
		scaleFontSize 		: 12,
		scaleFontStyle 		: "normal",
		scaleFontColor 		: "#666",	
		scaleShowGridLines 	: true,
		scaleGridLineColor 	: "rgba(0,0,0,.05)",
		scaleGridLineWidth 	: 1,	
		bezierCurve 		: false,
		pointDot 			: true,
		pointDotRadius 		: 3,
		pointDotStrokeWidth : 1,
		datasetStroke 		: true,
		datasetStrokeWidth 	: 2,
		datasetFill 		: true,
		animation 			: true,
		animationSteps 		: 60,
		animationEasing 	: "easeOutQuart",
		onAnimationComplete : null
	},

	barOptions : {			
		scaleOverlay : false,
		scaleOverride : false,
		scaleSteps : null,
		scaleStepWidth : null,
		scaleStartValue : null,
		scaleLineColor : "rgba(0,0,0,.1)",
		scaleLineWidth : 1,
		scaleShowLabels : true,
		scaleLabel : "<%=value%>",
		scaleFontFamily : "'Arial'",
		scaleFontSize : 12,
		scaleFontStyle : "normal",
		scaleFontColor : "#666",
		scaleShowGridLines : true,
		scaleGridLineColor : "rgba(0,0,0,.05)",
		scaleGridLineWidth : 1,
		barShowStroke : true,
		barStrokeWidth : 2,
		barValueSpacing : 5,
		barDatasetSpacing : 1,
		animation : true,
		animationSteps : 60,
		animationEasing : "easeOutQuart",
		onAnimationComplete : null
	}
};
