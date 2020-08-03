function getEngineHasGas(){
  var e = document.getElementById("uiEngineHasGas");
  var result = e.options[e.selectedIndex].value;
  return result;
}

function getHasWarranty(){
  var e = document.getElementById("uiHasWarranty");
  var result = e.options[e.selectedIndex].value;
  return result;
}

function getIsExchangeable(){
  var e = document.getElementById("uiIsExchangeable");
  var result = e.options[e.selectedIndex].value;
  return result;
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var manufacturer = document.getElementById("uiManufacturer");
  var model = document.getElementById("uiModel");
  var transmission = document.getElementById("uiTransmission");
  var color = document.getElementById("uiColor");
  var engineFuel = document.getElementById("uiEngineFuel");
  var engineType = document.getElementById("uiEngineType");
  var body = document.getElementById("uiBody");
  var state = document.getElementById("uiState");
  var driveTrain = document.getElementById("uiDriveTrain");
  var engineHasGas = getEngineHasGas();
  var HasWarranty = getHasWarranty();
  var IsExchangeable = getIsExchangeable();
  var odometerValue = document.getElementById("uiOdometerValue");
  var yearProduced = document.getElementById("uiYearProduced");
  var engineCapacity = document.getElementById("uiEngineCapacity");
  var numberOfPhotos = document.getElementById("uiNumberOfPhotos");
  var upCounter = document.getElementById("uiUpCounter");
  var durationListed = document.getElementById("uiDurationListed");
  var estPrice = document.getElementById("uiEstimatedPrice");

   var url = "http://127.0.0.1:5000/predict_used_car"; 

  $.post(url, {
    manufacturers: manufacturer.value,
    models: model.value,
    transmission: transmission.value,
    color: color.value,
    engine_fuel: engineFuel.value,
    engine_type: engineType.value,
    body: body.value,
    state: state.value,
    drivetrain: driveTrain.value,
    odometer_value: parseFloat(odometerValue.value),
    year_produced: parseFloat(yearProduced.value),
    engine_has_gas: engineHasGas,
    engine_capacity: parseFloat(engineCapacity.value),
    has_warranty: HasWarranty,
    is_exchangeable: IsExchangeable,
    number_of_photos: parseFloat(numberOfPhotos.value),
    up_counter: parseFloat(upCounter.value),
    duration_listed: parseFloat(durationListed.value)
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2> <br> $" + data.estimated_price.toString() + "</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
   var url = "http://127.0.0.1:5000/get_manufacturers_name"; 
  $.get(url,function(data, status) {
      console.log("got response for get_manufacturers_name request");
      if(data) {
          var manufacturers = data.manufacturers;
          var uiManufacturer = document.getElementById("uiManufacturer");
          $('#uiManufacturer').empty();
          for(var i in manufacturers) {
              var opt = new Option(manufacturers[i]);
              $('#uiManufacturer').append(opt);
          }
      }
  })
  var url = "http://127.0.0.1:5000/get_models_name"; 
  $.get(url,function(data, status) {
    console.log("got response for get_models_name request");
    if(data) {
        var models = data.models;
        var uiModel = document.getElementById("uiModel");
        $('#uiModel').empty();
        for(var i in models) {
            var opt = new Option(models[i]);
            $('#uiModel').append(opt);
        }
    }
})
var url = "http://127.0.0.1:5000/get_transmission_name"; 
$.get(url,function(data, status) {
  console.log("got response for get_transmission_name request");
  if(data) {
      var transmission = data.transmission;
      var uiTransmission = document.getElementById("uiTransmission");
      $('#uiTransmission').empty();
      for(var i in transmission) {
          var opt = new Option(transmission[i]);
          $('#uiTransmission').append(opt);
      }
  }
})
var url = "http://127.0.0.1:5000/get_color_name"; 
$.get(url,function(data, status) {
  console.log("got response for get_color_name request");
  if(data) {
      var color = data.color;
      var uiColor = document.getElementById("uiColor");
      $('#uiColor').empty();
      for(var i in color) {
          var opt = new Option(color[i]);
          $('#uiColor').append(opt);
      }
  }
})
var url = "http://127.0.0.1:5000/get_engineFuel_name"; 
$.get(url,function(data, status) {
  console.log("got response for get_engineFuel_name request");
  if(data) {
      var engineFuel = data.engineFuel;
      var uiEngineFuel = document.getElementById("uiEngineFuel");
      $('#uiEngineFuel').empty();
      for(var i in engineFuel) {
          var opt = new Option(engineFuel[i]);
          $('#uiEngineFuel').append(opt);
      }
  }
})
var url = "http://127.0.0.1:5000/get_engineType_name"; 
$.get(url,function(data, status) {
  console.log("got response for get_engineType_name request");
  if(data) {
      var engineType = data.engineType;
      var uiEngineType = document.getElementById("uiEngineType");
      $('#uiEngineType').empty();
      for(var i in engineType) {
          var opt = new Option(engineType[i]);
          $('#uiEngineType').append(opt);
      }
  }
})
var url = "http://127.0.0.1:5000/get_body_name"; 
$.get(url,function(data, status) {
  console.log("got response for get_body_name request");
  if(data) {
      var body = data.body;
      var uiBody = document.getElementById("uiBody");
      $('#uiBody').empty();
      for(var i in body) {
          var opt = new Option(body[i]);
          $('#uiBody').append(opt);
      }
  }
})
var url = "http://127.0.0.1:5000/get_state_name"; 
$.get(url,function(data, status) {
  console.log("got response for get_state_name request");
  if(data) {
      var state = data.state;
      var uiState = document.getElementById("uiState");
      $('#uiState').empty();
      for(var i in state) {
          var opt = new Option(state[i]);
          $('#uiState').append(opt);
      }
  }
})
var url = "http://127.0.0.1:5000/get_drivetrain_name"; 
$.get(url,function(data, status) {
  console.log("got response for get_drivetrain_name request");
  if(data) {
      var drivetrain = data.drivetrain;
      var uiDriveTrain = document.getElementById("uiDriveTrain");
      $('#uiDriveTrain').empty();
      for(var i in drivetrain) {
          var opt = new Option(drivetrain[i]);
          $('#uiDriveTrain').append(opt);
      }
  }
});
}

window.onload = onPageLoad;