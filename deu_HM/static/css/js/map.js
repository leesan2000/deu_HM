mapboxgl.accessToken = 'pk.eyJ1IjoibGVlc2FuNjQiLCJhIjoiY2xrNnptbWtkMDNpYjNrbnoxZHltZmhtbiJ9.hDEJKjc9Cq2708RJIHigIA';
        const map = new mapboxgl.Map({
            container: 'map', // container ID
            style: 'mapbox://styles/mapbox/streets-v12', // style URL
            center: [-58.381632, -34.603736], // starting position [lng, lat]
            zoom: 9, // starting zoom
        });