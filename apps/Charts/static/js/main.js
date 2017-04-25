$(document).ready(function () {

  google.charts.load('current', {'packages':['corechart']});
  // google.setOnLoadCallback(scatterCombo);
  formData = {};

  $.ajax({
  type:"GET",
  url:"/pageLoad",
  data: formData,
  success: function(jsonreponse){
    google.charts.setOnLoadCallback(
        function() { // Anonymous function that calls drawChart1 and drawChart2
        drawVisualization(jsonreponse["DefualtData"]);
      });
    }
  });
});
