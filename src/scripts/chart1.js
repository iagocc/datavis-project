export function chart1(selectCountryCallback) {
    let map = L.map('chart1').setView([20, 0], 2);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    // load data from a csv file
    d3.csv("../src/data/chart1.csv").then(function (data) {


        let colorScale = d3.scaleSequential(d3.interpolateYlGnBu);

        let colorFunction = function(feature) {
            return {
                fillColor: colorScale(feature.properties.rate),
                weight: 1,
                opacity: 1,
                color: 'gray',
                dashArray: '5',
                fillOpacity: 0.9
            };
        };

        let maxCount = parseFloat(Math.max.apply(Math, data.map(function(o) { return o.Count; })));

        d3.json("../src/data/world.json").then(geojson => {
            geojson.features.forEach(e => {
                let countryId = e.id;
                let countryProp = data.filter(e => e.Id == countryId);
                if(countryProp.length > 0) {
                    let count = countryProp[0].Count;
                    e.properties.rate = count / maxCount;
                    e.properties.count = count;
                } else {
                    e.properties.rate = 0;
                    e.properties.count = 0;
                }
            });

            let clickedCountry = {
                "name" : "Brazil",
                "layer" : null,
                "feature": null,
            };

            L.geoJson(geojson, {
                style: colorFunction,
                onEachFeature: (feature, layer) => {

                    // we must set this to clear when clicked in another layer
                    if (feature.properties.name === clickedCountry.name && clickedCountry.obj == null) {
                        clickedCountry.layer = layer;
                        clickedCountry.feature = feature;
                        layer.setStyle({fillColor: "red", fillOpacity: 0.7});
                    }

                    layer.bindTooltip("<b>" + feature.properties.name + "</b></br>" + feature.properties.count + " attended the survey");
                    layer.on("mouseover", e => {
                        if (e.target.feature.properties.name != clickedCountry.name) {
                            layer.setStyle({fillColor: "black", fillOpacity: 0.7});
                        }
                    });
                    layer.on("mouseout", e => {
                        if (e.target.feature.properties.name != clickedCountry.name) {
                            layer.setStyle(colorFunction(feature));
                        }
                    });
                    layer.on("click", e => {
                        // reset the color
                        clickedCountry.layer.setStyle(colorFunction(clickedCountry.feature));

                        // set the new clicked country
                        clickedCountry.name = e.target.feature.properties.name;
                        clickedCountry.layer = layer;
                        clickedCountry.feature = feature;

                        layer.setStyle({fillColor: "red", fillOpacity: 0.7});
                        selectCountryCallback(e.target.feature.id);
                    });
                }
            }).addTo(map);

            // Legend
            let legend = L.control({position: 'bottomright'});
            legend.onAdd = function (map) {

                let div = L.DomUtil.create('div', 'info legend'),
                    grades = [0, 0.2, 0.4, 0.6, 0.8, 1];

                // loop through our density intervals and generate a label with a colored square for each interval
                for (let i = 0; i < grades.length; i++) {
                    div.innerHTML +=
                        '<i style="background:' + colorScale(grades[i]) + '"></i> ' + '<br>';
                }

                return div;
            };

            legend.addTo(map);
        });

    });

};