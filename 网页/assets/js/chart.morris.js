$(function(){
	
	/* Morris Area Chart */
	
	window.mA = Morris.Area({
	    element: 'morrisArea',
	    data: [
	        { y: '0701', a: 23},
	        { y: '0702', a: 24},
	        { y: '0703', a: 24},
	        { y: '0704', a: 25},
	        { y: '0705', a: 30},
	        { y: '0706', a: 28},
	        { y: '0707', a: 31},
	    ],
	    xkey: 'y',
	    ykeys: ['a'],
	    labels: ['temperature'],
	    lineColors: ['#1b5a90'],
	    lineWidth: 2,
     	fillOpacity: 0.5,
	    gridTextSize: 10,
	    hideHover: 'auto',
	    resize: true,
		redraw: true
	});
	
	/* Morris Line Chart */
	
	window.mL = Morris.Line({
	    element: 'morrisLine',
	    data: [
	        { y: '0701', a: 23, b: 25},
	        { y: '0702', a: 22,  b: 26},
	        { y: '0703', a: 23,  b: 25},
	        { y: '0704', a: 23,  b: 27},
	        { y: '0705', a: 25,  b: 35},
	        { y: '0706', a: 25,  b: 31},
	        { y: '0707', a: 27,  b: 35},
	    ],
	    xkey: 'y',
	    ykeys: ['b','a'],
	    labels: ['highest','lowest'],
	    lineColors: ['#ff9d00','#1b5a90'],
	    lineWidth: 1,
	    gridTextSize: 10,
	    hideHover: 'auto',
	    resize: true,
		redraw: true
	});
	$(window).on("resize", function(){
		mA.redraw();
		mL.redraw();
	});

});