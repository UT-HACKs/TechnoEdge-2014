function initialize() {
    var latlng = new google.maps.LatLng(35.709984,139.810703);
    var opts = {
            zoom: 15,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
    map = new google.maps.Map(document.getElementById("map_canvas"), opts);
    ary = []
    //google.maps.event.addListener(map, 'drag', dispLatLng);
}

function put_marker_on_center(){
    var latlng = map.getCenter();
    var mopts = {
        position: latlng,
        map: map
    };
    var marker = new google.maps.Marker(mopts);
    ary.push(marker)
}

function clear_all_marker(){
    for(var i = 0; i<ary.length; i++){
        ary[i].setMap(null);
    }
    ary = []
}


function dispLatLng(){
    var latlng = map.getCenter();
    var str = "[CENTER]=[" + latlng.lat() + "," + latlng.lng() + "]<br />";
    
    var latlngBounds = map.getBounds();
    var swLatlng = latlngBounds.getSouthWest();
    str = str + "[SouthWest]=[" + swLatlng.lat() + "," + swLatlng.lng() + "]<br />";
    
    var neLatlng = latlngBounds.getNorthEast();
    str = str + "[NorthEast]=[" + neLatlng.lat() + "," + neLatlng.lng() + "]";
    
    document.getElementById("latlng").innerHTML = str;
}