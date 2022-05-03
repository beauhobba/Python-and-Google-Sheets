function doGet(e) {
  var id = e.parameter.id; 
  var ss = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Names");

  var length = ss.getLastRow();
  var width = ss.getLastColumn(); 

  var ids = ss.getRange(1, 1, length).getValues();

  var data = [];
  var first, last, email, phone = "";

  for(let i = 1; i < length; i++){
    if(ids[i] == parseInt(id)){
      data = (ss.getRange(i+1, 2, 1, width).getValues())[0]; 

      first = data[0];
      last = data[1];
      phone = data[2];
      email = data[3];

    }

  }
  return ContentService.createTextOutput(JSON.stringify({"data": {"first": first, "last": last, "phone": phone, "email": email}}))
}

