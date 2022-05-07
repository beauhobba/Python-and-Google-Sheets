function doGet(e) {
  var id = e.parameter.id; 
  var ss = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Names");

  var length = ss.getLastRow();
  var width = ss.getLastColumn(); 

  // check what task the user has specified 
  if(e.parameter.task){
    var task = e.parameter.task

    // do functions related to ids here 
    if(e.parameter.id){
        var id = e.parameter.id; 
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

        switch(task){
        case 'getFirstName':
            return ContentService.createTextOutput(JSON.stringify({"data": {"first": first}}));
        case 'getPhone':
            return ContentService.createTextOutput(JSON.stringify({"data": {"phone": phone}}));
        default:
            return ContentService.createTextOutput(JSON.stringify({"data": {"first": first, "last": last, "phone": phone, "email": email}}))
        }
    }
  }

  if(e.parameter.task.includes("getNames")){
    var first_name = ([].concat.apply([], ss.getRange(2, 2, length-1).getValues()));
    var last_name = ([].concat.apply([], ss.getRange(2, 3, length-1).getValues()));

    var full_names = [];
    for(let i = 0; i <length-1; i++){
      full_names.push(first_name[i]+ " "+last_name[i]); 
    }

    if(!e.parameter.filter){
      if(e.parameter.task.includes("first")){
        return ContentService.createTextOutput(JSON.stringify({"data": {"names": first_name}}));
      }else if(e.parameter.task.includes("last")){
        return ContentService.createTextOutput(JSON.stringify({"data": {"names": last_name}}));
      }else{
        return ContentService.createTextOutput(JSON.stringify({"data": {"names": full_names}}));
      }


    }else{
      // Perform a filtered task 
      var names_return = full_names.filter(element => element.toLowerCase().includes(e.parameter.filter.toLowerCase()));
      return ContentService.createTextOutput(JSON.stringify({"data": {"filtered_names": names_return}}));
    }
  }
}