// Created by Jerry

// Outage history in JSON format
var data = [
  {
    "outage": "2017-03-01",
    "feeder": 2740,
    "type": "OH",
    "category": "Equipment Failure",
    "lat": 47.57750899,
    "long": -122.3843712
  },
  {
    "outage": "2017-03-03",
    "feeder": 2774,
    "type": "OH",
    "category": "Equipment Failure",
    "lat": 47.71501145,
    "long": -122.3640997
  },
  {
    "outage": "2017-03-07",
    "feeder": 2813,
    "type": "OH",
    "category": "Bird/Animal",
    "lat": 47.59792217,
    "long": -122.3056206
  },
  {
    "outage": "2017-03-08",
    "feeder": 2646,
    "type": "UG",
    "category": "Bird/Animal",
    "lat": 47.5894435,
    "long": -122.2924809
  },
  {
    "outage": "2017-03-13",
    "feeder": 2658,
    "type": "UG",
    "category": "Bird/Animal",
    "lat": 47.6611623,
    "long": -122.3881626
  },
  {
    "outage": "2017-03-15",
    "feeder": 2780,
    "type": "OH",
    "category": "Trees/Wire Down",
    "lat": 47.7055021,
    "long": -122.3106227
  },
  {
    "outage": "2017-03-17",
    "feeder": 2749,
    "type": "UG",
    "category": "Equipment Failure",
    "lat": 47.5410907,
    "long": -122.3377455
  },
  {
    "outage": "2017-03-19",
    "feeder": 2608,
    "type": "OH",
    "category": "Bird/Animal",
    "lat": 47.6761786,
    "long": -122.3196484
  },
  {
    "outage": "2017-03-20",
    "feeder": 2647,
    "type": "OH",
    "category": "Bird/Animal",
    "lat": 47.5729189,
    "long": -122.2940163
  },
  {
    "outage": "2017-03-22",
    "feeder": 2707,
    "type": "OH",
    "category": "Equipment Failure",
    "lat": 47.65206104,
    "long": -122.3100913
  },
  {
    "outage": "2017-03-25",
    "feeder": 2754,
    "type": "UG",
    "category": "Bird/Animal",
    "lat": 47.6141061,
    "long": -122.3078544
  },
  {
    "outage": "2017-03-29",
    "feeder": 2736,
    "type": "UG",
    "category": "Bird/Animal",
    "lat": 47.5446761,
    "long": -122.3757294
  }
 ]


// Define grid formatting
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


// Global varible
// for the storage of filtered data info for genMarker
var locations = [];
var markers = [];
// for map infowindow
var infoWindows = [];
// for initialize the map
var bounds;
var map;
// Create an array of alphabetical characters used to label the markers.
var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
var labelIndex = 0;


// Generate filtered data by date and pass the info to genMarkers
function genFilteredByDate() {
    // get the stardate and enddate by the datepicker
    var sd = $("#startDate").val()
    var ed = $("#endDate").val()
    var startDate = new Date(sd)
    var endDate = new Date(ed)

    // generate filtered data according to the date range from datepicker
    var filterByDate = (ele) => {
        let outage = new Date(ele.outage)
        return startDate <= outage && outage <= endDate
    }
    let filteredData = data.filter(filterByDate)

    // Empty the global variable container every time
    locations = [];

    // Parse the filtered data for the map and markers and store in "locations"
    filteredData.forEach(function(row, index) {
        row.idlabel = labels[index%labels.length];
        locations.push([row.feeder.toString(), row.long, row.lat,
          row.outage.toString(), row.type.toString(), row.category.toString(),
          row.idlabel.toString() ]);
    });

    // Render the grid
    var powerRecordsFiltered = new Backbone.Collection(filteredData);
    var gridFiltered = new Backgrid.Grid({
        columns: columns,
        collection: powerRecordsFiltered
    });
    $("#main").empty();
    $("#main").append(gridFiltered.render().el);

    // Delete the markers from the old map
    deleteMarkers()

    // Generate Markers based on the # of filteredData
    for (i = 0; i < filteredData.length; i++) {
        genMarkers(locations, i);
    }

    // Reset the labelIndex for the next time use
    labelIndex = 0; // Reset, Markers count from A everytime
}


// Initialize the google map
function initialize() {
    bounds = new google.maps.LatLngBounds();
    map = new google.maps.Map(
        document.getElementById("map_canvas"), {
            center: new google.maps.LatLng(47.6051199, -122.3370917),
            zoom: 10,
            mapTypeId: 'roadmap' //'terrain'
        });

    // Initialization of the date picker
    $("#startDate").datepicker({
        dateFormat: "yy/mm/dd"
    }).datepicker("setDate", "2017/03/01");

    $("#endDate").datepicker({
        dateFormat: "yy/mm/dd"
    }).datepicker("setDate", "2017/03/20");

    genFilteredByDate()
}


// Action after the change of Date Picker - startDate
$("#startDate").change(function() {
    genFilteredByDate()
});

// Action after the change of Date Picker - endDate
$("#endDate").change(function() {
    genFilteredByDate()
});


// Generate the marker on the map
function genMarkers(locations, i) {
    var title = locations[i][0];
    var longitute = locations[i][1];
    var latitute = locations[i][2];
    var dateInfo = locations[i][3];
    var typeInfo = locations[i][4];
    var catInfo = locations[i][5];
    var labelInfo = locations[i][6];

    var marker = new google.maps.Marker({
        map: map,
        position: {lat: latitute, lng: longitute},
        title: title,
        label: labelInfo,
        animation: google.maps.Animation.DROP,
    })

    // map: fit bound, info window
    markers.push(marker);
    infoWindow(marker, map, title, dateInfo, typeInfo, catInfo);
    bounds.extend(marker.getPosition());
    map.fitBounds(bounds);
}


// Generate the infowindow of the map
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


// Read the txt file line by line and show the text on the dashboard
function readTextFile(file) {
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
};


// Read the designated text file
readTextFile("data/prediction.txt");
