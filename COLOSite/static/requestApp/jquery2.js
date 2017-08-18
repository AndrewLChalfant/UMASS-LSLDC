$(document).ready(function() {
	//EXPORT PENDING USERS TO EXCEL SPREADSHEET
  $("#btnExport").click(function(e) {
  	//getting data from our table
    var data_type = 'data:application/vnd.ms-excel';
    var table_div = document.getElementById('table');
    var table_html = table_div.outerHTML.replace(/ /g, '%20');

    var a = document.createElement('a');
    a.href = data_type + ', ' + table_html;
    a.download = 'LSLDC COLO Pending' + '.xls';
    a.click();
    e.preventDefault();
    });
  
  //EXPORT APPROVED USERS TO EXCEL SPREADSHEET - ERRORS FORMATTING
  $("#btnExportApproved").click(function(e) {
    e.preventDefault();

    //getting data from our table
    var data_type = 'data:application/vnd.ms-excel';
    var table_div = document.getElementById('table2');
    var table_html = table_div.outerHTML.replace(/ /g, '%20');

    var a = document.createElement('a');
    a.href = data_type + ', ' + table_html;
    a.download = 'LSLDC COLO Approved' + '.xls';
    a.click();
  });  
});
