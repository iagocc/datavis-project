export function chart12(selectedCountries) {
    let chart = document.querySelector("#chart12");

    let svg = d3.select("#chart12 svg").attr("width", chart.offsetWidth).attr("height", chart.offsetHeight);

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
        return "# of people who knows the tecnology: " + parseInt(+d.value) + "";
    });
    svg.call(tip);

    d3.csv("../src/data/chart10_bonus.csv").then(data => {
        // get the name of the fields
        let keys = Object.keys(data[0]).slice(2, -1);

        let overall = {"Country": "Overall Mean", "Code":"Overall"};
        const numberOfAttends = data.reduce((a, e) => parseInt(a) + parseInt(e["# Users"]), 0);

        keys.forEach(key => {
            overall[key] = data.reduce((a, e) => parseInt(a) + parseInt(e[key]), 0);
            overall[key] = parseInt(overall[key]) / parseFloat(data.length);
        });

        data.push(overall);

        let filtered = data.filter((e => selectedCountries.includes(e.Code)));
        
        // Formating the data
        let allValues = [];
        filtered.forEach(e => {
            keys.forEach(att => {
                e[att] = +e[att];
                allValues.push(e[att]);
            });
        });

        let colorScale = d3.scaleOrdinal()
                        .range(["#7fcdbb", "#2c7fb8"]);

        x0.domain(keys);
        x1.domain(selectedCountries).rangeRound([0, x0.bandwidth()]);
        y.domain([0, Math.max(...allValues)]);

        g.append("g")
            .selectAll("g")
            .data(filtered)
            .enter().append("g")
            .attr("transform", d => { return "translate(" + x1(d.Code) + ",0)"; })
            .selectAll("rect")
            .data(d => { return keys.map(key => { return {key: key, value: d[key], country: d["Code"]}; }); })
            .enter().append("rect")
            .attr("x", d => { return x0(d.key); })
            .attr("y", d => { return y(d.value); })
            .attr("width", x1.bandwidth())
            .attr("height", d => { return height - y(d.value); })
            .attr("fill", d => { return colorScale(d.country); })
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
                        .data(filtered.slice())
                        .enter().append("g")
                        .attr("transform", (d, i) => { return "translate(0," + i * 20 + ")"; });
    
        legend.append("rect")
                .attr("x", width - 19)
                .attr("width", 19)
                .attr("height", 19)
                .attr("fill", d => colorScale(d.Code));
    
        legend.append("text")
                .attr("x", width - 24)
                .attr("y", 9.5)
                .attr("dy", "0.32em")
                .text(d => { return d.Country; });

    });
}