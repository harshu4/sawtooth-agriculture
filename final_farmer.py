#the goal will be to make the maps compatible to inputs and hence create a nice best all in one path setter


<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title>Animate a point along a route</title>
<meta name="viewport" content="initial-scale=1,maximum-scale=1,user-scalable=no" />
<script src="https://api.mapbox.com/mapbox-gl-js/v1.8.1/mapbox-gl.js"></script>
<link href="https://api.mapbox.com/mapbox-gl-js/v1.8.1/mapbox-gl.css" rel="stylesheet" />
<style>
	body { margin: 0; padding: 0; }
	#map { position: absolute; top: 0; bottom: 0; width: 100%; }
</style>
</head>
<body>
<style>
.overlay {
position: absolute;
top: 10px;
left: 10px;
}

.overlay button {
font: 600 12px/20px 'Helvetica Neue', Arial, Helvetica, sans-serif;
background-color: #3386c0;
color: #fff;
display: inline-block;
margin: 0;
padding: 10px 20px;
border: none;
cursor: pointer;
border-radius: 3px;
}

.overlay button:hover {
background-color: #4ea0da;
}
</style>
<script
src="https://api.tiles.mapbox.com/mapbox.js/plugins/turf/v2.0.0/turf.min.js"
charset="utf-8"
></script>

<div id="map"></div>
<div class="overlay">
<button id="replay">Replay</button>
</div>

<script>
  var origin = [[73.1812,22.3072],[72.8311,21.1702],[72.9342,20.5992]];
  var sum_1 = 0
  var sum_2 = 0
  for (i=0;i<origin.length;i++){
    sum_1 = sum+origin[i][0]
    sum_2 = sum+origin[i][1]
  }

	mapboxgl.accessToken = 'pk.eyJ1IjoidXBlc2hhY2siLCJhIjoiY2s3Nm41dmdsMGM5NzNncGJkMHRyZ2lxbSJ9.CZdCabNilfXCwIKYUwiYnA';
var map = new mapboxgl.Map({
container: 'map',
style: 'mapbox://styles/mapbox/streets-v11',
    center: [sum_1/origin.length,sum_2/origin.length],
zoom: 8
});

for (i=0;i<origin.length;i++){
    if (i == 0){
    var el = document.createElement('div');
    el.className = 'marker';
    el.style.backgroundImage =
    'url(https://i.ibb.co/5vSfVhz/farmer-3.jpg)';
    el.style.width = 51 + 'px';
    el.style.height = 75 + 'px';

    el.addEventListener('click', function() {
    window.alert('foo');
    });

    new mapboxgl.Marker(el)
    .setLngLat(origin)
    .addTo(map);
}
else {
var el2 = document.createElement('div');
el2.className = 'marker2';
el2.style.backgroundImage = 'url(https://i.ibb.co/wcDG3zX/ss.jpg)';
el2.style.width = 60 + 'px';
el2.style.height = 60 + 'px';

el2.addEventListener('click', function() {
window.alert('foo');

});

new mapboxgl.Marker(el2)
.setLngLat(destination)
.addTo(map);

}


}





// A simple line from origin to destination.
var route = {
'type': 'FeatureCollection',
'features': []
};

for (i=0;i<origin.length;i++){
    route.features.push({
    'type': 'Feature',
    'geometry': {
    'type': 'LineString',
    'coordinates': origin[i]
    })
}

// A single point that animates along the route.
// Coordinates are initially set to origin.
var point = {
'type': 'FeatureCollection',
'features': [
{
'type': 'Feature',
'properties': {},
'geometry': {
'type': 'Point',
'coordinates': origin
}
}
]
};

// Calculate the distance in kilometers between route start/end point.
var lineDistance = turf.lineDistance(route.features[0], 'kilometers');

var arc = [];

// Number of steps to use in the arc and animation, more steps means
// a smoother arc and animation, but too many steps will result in a
// low frame rate
var steps = 500;

// Draw an arc between the `origin` & `destination` of the two points
for (var i = 0; i < lineDistance; i += lineDistance / steps) {
var segment = turf.along(route.features[0], i, 'kilometers');
arc.push(segment.geometry.coordinates);
}

// Update the route with calculated arc coordinates
route.features[0].geometry.coordinates = arc;

// Used to increment the value of the point measurement against the route.
var counter = 0;

map.on('load', function() {


  map.loadImage(
  'https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Cat_silhouette.svg/400px-Cat_silhouette.svg.png',
  function(error, image) { if (error) console.log('error');
map.addImage('cat', image);})

// Add a source and layer displaying a point which will be animated in a circle.
map.addSource('route', {
'type': 'geojson',
'data': route
});

map.addSource('point', {
'type': 'geojson',
'data': point
});

map.addLayer({
'id': 'route',
'source': 'route',
'type': 'line',
'paint': {
'line-width': 4,
'line-color': '#007cbf'
}
});

map.addLayer({
'id': 'point',
'source': 'point',
'type': 'symbol',
'layout': {
'icon-rotate': ['get', 'bearing'],
'icon-rotation-alignment': 'map',
'icon-allow-overlap': true,
'icon-ignore-placement': true
}

});
  map.addImage('pulsing-dot', pulsingDot, { pixelRatio: 2 });

function animate() {
// Update point geometry to a new position based on counter denoting
// the index to access the arc.
point.features[0].geometry.coordinates =
route.features[0].geometry.coordinates[counter];

// Calculate the bearing to ensure the icon is rotated to match the route arc
// The bearing is calculate between the current point and the next point, except
// at the end of the arc use the previous point and the current point
point.features[0].properties.bearing = turf.bearing(
turf.point(
route.features[0].geometry.coordinates[
counter >= steps ? counter - 1 : counter
]
),
turf.point(
route.features[0].geometry.coordinates[
counter >= steps ? counter : counter + 1
]
)
);

// Update the source with this new data.
map.getSource('point').setData(point);

// Request the next frame of animation so long the end has not been reached.
if (counter < steps) {
requestAnimationFrame(animate);
}

counter = counter + 1;
}

document.getElementById('replay').addEventListener('click', function() {
// Set the coordinates of the original point back to origin
point.features[0].geometry.coordinates = origin;

// Update the source layer
map.getSource('point').setData(point);

// Reset the counter
counter = 0;

// Restart the animation.
animate(counter);
});

// Start the animation.
animate(counter);
});
</script>

</body>
</html>