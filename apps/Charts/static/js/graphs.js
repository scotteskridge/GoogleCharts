

function drawVisualization(DataTable) {
  // Some raw data (not necessarily accurate)
  var data = google.visualization.arrayToDataTable(DataTable);


  var options = {
    title : 'Monthly Coffee Production by Country',
    vAxis: {title: 'Cups'},
    hAxis: {title: 'Month'},
    curveType: 'function',
    seriesType: 'line',
    series: {0: {type: 'line', lineWidth : 0, pointSize: 5 }}
  };

  var chart = new google.visualization.ComboChart(document.getElementById('chart_div'));
  chart.draw(data, options);
}
