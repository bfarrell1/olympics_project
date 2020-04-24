Highcharts.chart('chart', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Medal Count'
    },
    xAxis: {
        categories: ['Gold', 'Silver', 'Bronze']
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Number of medals'
        },
        stackLabels: {
            enabled: true,
            style: {
                fontWeight: 'bold',
                color: ( // theme
                    Highcharts.defaultOptions.title.style &&
                    Highcharts.defaultOptions.title.style.color
                ) || 'gray'
            }
        }
    },
    legend: {
        align: 'right',
        x: -30,
        verticalAlign: 'top',
        y: 25,
        floating: true,
        backgroundColor:
            Highcharts.defaultOptions.legend.backgroundColor || 'white',
        borderColor: '#CCC',
        borderWidth: 1,
        shadow: false
    },
    tooltip: {
        headerFormat: '<b>{point.x}</b><br/>',
        pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
    },
    plotOptions: {
        column: {
            stacking: 'normal',
            dataLabels: {
                enabled: true
            }
        }
    },
    series: [{
        name: 'Summer',
        data: [goldcount, silvercount, bronzecount]
    }, {
        name: 'Winter',
        data: [wintergoldcount, wintersilvercount, winterbronzecount]
    }]
    })
