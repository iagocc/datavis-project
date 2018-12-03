export function chart9(selectedCountry) {
    let chart = document.querySelector("#chart9");

    let svg = d3.select("#chart9 svg").attr("width", chart.offsetWidth).attr("height", chart.offsetHeight);

    svg.selectAll("*").remove();

    let margin = {top: 20, right: 20, bottom: 30, left: 40};
    let width = +svg.attr("width") - margin.left - margin.right;
    let height = +svg.attr("height") - margin.top - margin.bottom;
    let g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");
    let padding = 1;
    let colorScale = d3.scaleSequential(d3.interpolateViridis);

    function forceSimulation(nodes, centroids) {
        return d3.forceSimulation(nodes)
            .force('center', d3.forceCenter(width/2 + 100, height/2 + 25))
            .force('collide', d3.forceCollide(d => { return d.radius + padding; }))
            .force('cluster', d3.forceCluster().centers(d => centroids[d.cluster]).strength(0.5));
      }

    d3.csv("../src/data/chart9_bonus.csv").then(data => {

        let filtered = data.filter(e => e.Code === selectedCountry);
        let keys = Object.keys(data[0]).slice(1, -1);
        let sum = keys.reduce((a, c) => parseInt(a) + parseInt(filtered[0][c]), 0);
        let centroids = [];

        let dataset = [];
        // Will be 250 circles, so we must multiply the ratio by 250
        keys.forEach(k => {
            filtered[0][k] = parseInt(250*(filtered[0][k] / sum));
            let clusterNumber = keys.indexOf(k);
            for (let i = 0; i < filtered[0][k]; i++) {
                let obj = {
                    "group": k, 
                    "country": filtered[0].Country,
                    "radius": 3,
                    "cluster": +clusterNumber,
                    "x": Math.cos(clusterNumber / keys.length * 2 * Math.PI) * 250 + width / 2 + Math.random(),
                    "y": Math.sin(clusterNumber / keys.length * 2 * Math.PI) * 150 + height / 2 + Math.random()
                };
                dataset.push(obj);
                if (!centroids[clusterNumber]) centroids[clusterNumber] = obj;
            }
        });

        let nodes = g
            .selectAll("circle")
            .data(dataset)
            .enter()
            .append("circle")
            .attr("class", "node")
            .attr("r", d => d.radius)
            .attr("stroke", d => d3.color(colorScale(d.cluster/10.0)).darker())
            .attr("fill", d => colorScale(d.cluster/10.0));

        let ticked = () => {
            nodes
              .attr("cx", d => d.x)
              .attr("cy", d => d.y);
        };

        let legend = g.append("g")
                        .attr("font-family", "sans-serif")
                        .attr("font-size", 10)
                        .attr("text-anchor", "end")
                        .selectAll("g")
                        .data(keys)
                        .enter().append("g")
                        .attr("transform", (d, i) => { return "translate(0," + i * 20 + ")"; });

        legend.append("rect")
                .attr("x", width - 19)
                .attr("width", 19)
                .attr("height", 19)
                .attr("fill", d => colorScale(keys.indexOf(d)/10.0));

        legend.append("text")
                .attr("x", width - 24)
                .attr("y", 9.5)
                .attr("dy", "0.32em")
                .text(d => d);

        const simulation = forceSimulation(dataset, centroids).on("tick", ticked);
    });
}