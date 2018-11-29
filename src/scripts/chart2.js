let countries = ["United States", "United Kingdom", "Canada", "Brazil", "India", "Mexico"];

export function chart2() {
    let chart = document.querySelector("#chart2");

    let svg = d3.select("#chart2 svg").attr("width", chart.offsetWidth).attr("height", chart.offsetHeight);

    svg.selectAll("*").remove();

    let margin = {top: 20, right: 20, bottom: 30, left: 40};
    let width = +svg.attr("width") - margin.left - margin.right;
    let height = +svg.attr("height") - margin.top - margin.bottom;
    let g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    let x0 = d3.scaleBand()
                .rangeRound([0, width])
                .paddingInner(0.1);

    let x1 = d3.scaleBand()
                .padding(0.05);

    let y = d3.scaleLinear()
                .rangeRound([height, 0]);

    let tip = d3.tip().attr('class', 'd3-tip').html(d => {
        return "Ownage rate " + parseInt(+d.value) + "%";
    });
    svg.call(tip);

    d3.csv("../src/data/chart2.csv").then(data => {

        let filtered = data.filter((e => countries.includes(e.Country)));
        
        // Format the data
        filtered.forEach(e => {
            e["# Users"] = +e["# Users"];
            e["# Laptop"] = +e["# Laptop"];
            e["# Smart Phone"] = +e["# Smart Phone"];
            e.laptopRate = (e["# Laptop"] / e["# Users"])*100;
            e.smartphoneRate = (e["# Smart Phone"] / e["# Users"])*100;
        });

        let keys = ["laptopRate", "smartphoneRate"];
        let colorScale = d3.scaleOrdinal()
                        .range(["#7fcdbb", "#2c7fb8"]);

        x0.domain(filtered.map(d => d.Country));
        x1.domain(keys).rangeRound([0, x0.bandwidth()]);
        y.domain([0, 100]);

        g.append("g")
            .selectAll("g")
            .data(filtered)
            .enter().append("g")
            .attr("transform", d => { return "translate(" + x0(d.Country) + ",0)"; })
            .selectAll("rect")
            .data(d => { return keys.map(key => { return {key: key, value: d[key]}; }); })
            .enter().append("rect")
            .attr("x", d => { return x1(d.key); })
            .attr("y", d => { return y(d.value); })
            .attr("width", x1.bandwidth())
            .attr("height", d => { return height - y(d.value); })
            .attr("fill", d => { return colorScale(d.key); })
            .on('mouseover', tip.show)
            .on('mouseout', tip.hide);

        g.append("g")
            .attr("class", "axis")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x0));

        g.append("g")
            .attr("class", "axis")
            .call(d3.axisLeft(y).ticks(null, "s"));
    
        let legend = g.append("g")
                        .attr("font-family", "sans-serif")
                        .attr("font-size", 10)
                        .attr("text-anchor", "end")
                        .selectAll("g")
                        .data(keys.slice())
                        .enter().append("g")
                        .attr("transform", (d, i) => { return "translate(0," + i * 20 + ")"; });
    
        legend.append("rect")
                .attr("x", width - 19)
                .attr("width", 19)
                .attr("height", 19)
                .attr("fill", colorScale);
    
        legend.append("text")
                .attr("x", width - 24)
                .attr("y", 9.5)
                .attr("dy", "0.32em")
                .text(d => {
                    if (d === "laptopRate") {
                        return "Laptop";
                    }
                    return "Smartphone";
                });


    });
};

export function populateCountries() {
    let select = document.querySelector("#chart2-select .select select");
    select.onchange = onSelection;
    d3.csv("../src/data/chart2.csv").then(data => {
        let allCountries = data.map(d => d.Country);
        allCountries.forEach(e => {
            let selectString = countries.includes(e) ? "selected" : "";
            let htmlEl = '<option value="'+e+'" '+selectString+'>'+e+'</option>';
            select.insertAdjacentHTML('beforeend', htmlEl);
        });
    });

    function onSelection(event) {
        let opts = event.target.options;
        countries = [];
        for (let i = 0; i < opts.length; i++) {
            let e = opts[i];
            if (e.selected) {
                countries.push(e.value);
            }
        }
        chart2();
    }
}