// JSON

var data = [
 {
   "outage": "2017/03/03",
   "feeder": 2611,
   "type": "OH",
   "category": "Equipment Failure",
   "lat": 47.5589842,
   "long": -122.3054883
 },
 {
   "outage": "2017/03/05",
   "feeder": 2623,
   "type": "UG",
   "category": "Trees/Wire Down",
   "lat": 47.64044891,
   "long": -122.3726307
 },
 {
   "outage": "2017/03/09",
   "feeder": 2625,
   "type": "OH",
   "category": "Equipment Failure",
   "lat": 47.65679411,
   "long": -122.3019232
 },
 {
   "outage": "2017/03/10",
   "feeder": 2712,
   "type": "OH",
   "category": "Bird/Animal",
   "lat": 47.66321716,
   "long": -122.3273836
 },
 {
   "outage": "2017/03/11",
   "feeder": 2715,
   "type": "OH",
   "category": "Equipment Failure",
   "lat": 47.65943792,
   "long": -122.3735795
 },
 {
   "outage": "2017/03/13",
   "feeder": 2656,
   "type": "OH",
   "category": "Bird/Animal",
   "lat": 47.63095492,
   "long": -122.3245173
 }
 ]

 // Intialize the grid
 var columns = [
    {
    name: "idlabel",
    label: "Label",
    editable: false,
    cell: "string"
 }, {
     name: "outage",
     label: "Outage Date",
     editable: false,
     cell: "string"
 }, {
     name: "feeder",
     label: "Feeder",
     editable: false,
     cell: "string"
 }, {
     name: "type",
     label: "Type",
     editable: false,
     cell: "string"
 }, {
     name: "category",
     label: "Category",
     editable: false,
     cell: "string"
 }];


// Date Picker
var locations = [];

// //Map
var map;
var markers = [];
var bounds;

// Create an array of alphabetical characters used to label the markers.
var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
var labelIndex = 0;

// Initialization
    $("#startDate").datepicker({
        dateFormat: "yy/mm/dd"
    }).datepicker("setDate", "2017/03/01");

    $("#endDate").datepicker({
        dateFormat: "yy/mm/dd"
    }).datepicker("setDate", "2017/03/15");

    var sd = $("#startDate").val()
    var ed = $("#endDate").val()
    console.log(sd);
    console.log(ed);

    var startDate = new Date(sd)
    var endDate = new Date(ed)

    var filterByDate = (ele) => {
        let outage = new Date(ele.outage)
        return startDate <= outage && outage <= endDate
    }

    let filteredData = data.filter(filterByDate)

    // for the map and markers
    filteredData.forEach(function(row, index) {
        row.idlabel = labels[index%labels.length];
        locations.push([row.feeder.toString(), row.long, row.lat,
          row.outage.toString(), row.type.toString(), row.category.toString() ]);
    });

    var powerRecordsFiltered = new Backbone.Collection(filteredData);
    var gridFiltered = new Backgrid.Grid({
        columns: columns,
        collection: powerRecordsFiltered
    });

  // Render the filter
    $("#main").empty();
    $("#main").append(gridFiltered.render().el);



// Change of Date Picker
$("#startDate").change(function() {
    //checkDate();
    var sd = $("#startDate").val()
    var ed = $("#endDate").val()
    console.log(sd);

    var startDate = new Date(sd)
    var endDate = new Date(ed)

    var filterByDate = (ele) => {
        let outage = new Date(ele.outage)
        return startDate <= outage && outage <= endDate
    }

    let filteredData = data.filter(filterByDate)

    // for the map and markers
    filteredData.forEach(function(row, index) {
        row.idlabel = labels[index%labels.length];
        locations.push([row.feeder.toString(), row.long, row.lat,
          row.outage.toString(), row.type.toString(), row.category.toString() ]);
    });


    var powerRecordsFiltered = new Backbone.Collection(filteredData);
    var gridFiltered = new Backgrid.Grid({
        columns: columns,
        collection: powerRecordsFiltered
    });
  // Render the filter
    $("#main").empty();
    $("#main").append(gridFiltered.render().el);

    deleteMarkers()
    for (i = 0; i < filteredData.length; i++) {
        genMarkers(locations, i);
    }
    labelIndex = 0; // Reset, Markers count from A everytime
});



$("#endDate").change(function() {
  //checkDate();
  var sd = $("#startDate").val()
  var ed = $("#endDate").val()
  console.log(ed);

  var startDate = new Date(sd)
  var endDate = new Date(ed)

  var filterByDate = (ele) => {
      let outage = new Date(ele.outage)
      return startDate <= outage && outage <= endDate
  }

  let filteredData = data.filter(filterByDate)

  // for the map and markers
  filteredData.forEach(function(row, index) {
      row.idlabel = labels[index%labels.length];
      locations.push([row.feeder.toString(), row.long, row.lat,
        row.outage.toString(), row.type.toString(), row.category.toString() ]);
  });

  var powerRecordsFiltered = new Backbone.Collection(filteredData);
  var gridFiltered = new Backgrid.Grid({
      columns: columns,
      collection: powerRecordsFiltered
  });

  // Render the filter
    $("#main").empty();
    $("#main").append(gridFiltered.render().el);

    deleteMarkers()
    for (i = 0; i < filteredData.length; i++) {
        genMarkers(locations, i);
    }
    labelIndex = 0; // Reset, Markers count from A everytime
});


// Initialize the map
function initialize() {
    bounds = new google.maps.LatLngBounds();
    map = new google.maps.Map(
        document.getElementById("map_canvas"), {
            center: new google.maps.LatLng(47.6051199, -122.3370917),
            zoom: 10,
            mapTypeId: 'roadmap' //'terrain' //google.maps.MapTypeId.ROADMAP
        });
    //geocoder = new google.maps.Geocoder();

    for (i = 0; i < locations.length; i++) {
        genMarkers(locations, i);
    }
    labelIndex = 0; // Reset, Markers count from A everytime
}

// Generate the marker on the map
function genMarkers(locations, i) {
    var title = locations[i][0];
    var longitute = locations[i][1];
    var latitute = locations[i][2];
    var dateInfo = locations[i][3];
    var typeInfo = locations[i][4];
    var catInfo = locations[i][5];

    var marker = new google.maps.Marker({
        //icon: 'http://maps.google.com/mapfiles/ms/icons/red.png',
        map: map,
        position: {lat: latitute, lng: longitute},
        title: title,
        label: labels[labelIndex++ % labels.length],
        animation: google.maps.Animation.DROP,
    })

    markers.push(marker);
    infoWindow(marker, map, title, dateInfo, typeInfo, catInfo);
    bounds.extend(marker.getPosition());
    map.fitBounds(bounds);

}

// Generate the infowindow of the amp
var infoWindows = [];
// Marker Info Window
function infoWindow(marker, map, title, dateInfo, typeInfo, catInfo) {
    var html = "<div><h4>" + title + "</h4><p>" + dateInfo + "<br>" + typeInfo
        + ", " + catInfo + "</p></div>";
    marker.addListener('click', function() {

      //If infoWindows already exist, then close them.
      infoWindows.forEach(function(row) {
        if(row) row.close();
        infoWindows = [];
      });

      var iw = new google.maps.InfoWindow({
          content: html,
          maxWidth: 350
      });
      iw.open(map, marker);
      infoWindows.push(iw);
    });
}

// Deletes all markers in the array by removing references to them.
function deleteMarkers() {
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(null);
  }
  markers = [];
}


// Read the txt file and show the text on the dashboard
function readTextFile(file)
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText.split('\n');
                document.getElementById("tmr").innerHTML = allText[0];
                document.getElementById("chance").innerHTML = allText[1];
                document.getElementById("weather").innerHTML = allText[2];
                document.getElementById("equip").innerHTML = allText[3];
            }
        }
    }
    rawFile.send(null);
}

readTextFile("data/prediction.txt");
