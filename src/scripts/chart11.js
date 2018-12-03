export function chart11() {
    let chart = dc.lineChart('#chart11');
    let piechart = dc.pieChart('#chart11-2');

    let width = document.querySelector("#chart11").offsetWidth;
    let height = document.querySelector("#chart11").offsetHeight;

    d3.csv("../src/data/chart11.csv").then(data => {
        let keys = Object.keys(data[0]).slice(2);

        let parseDate = d3.timeParse("%b %e, %Y");

        let answers = {
            "Q1": "Don’t know",
            "Q2": "Myself",
            "Q3": "The government",
            "Q4": "The manufacturers"};

        // formating the data
        let formatedData = [];
        data.forEach(d => {
            let row;
            keys.forEach(e => {
                row = {
                    "Date": parseDate(d["Date"]),
                    "# Users": +d["# Users"]/keys.length,
                    "Field": e,
                    "Value": d[e]
                };
                formatedData.push(row);
            });
          });

          // creating the crossfilter
          let facts = crossfilter(formatedData);

          // line chart dimension and group
          let dateDim = facts.dimension(d => d["Date"]);
          let usersByDayGroup = dateDim.group().reduceSum(d => d["# Users"]);

          // pie chart dimension and group
          let fieldDim = facts.dimension(d => d["Field"]);
          let q1ByDayGroup = fieldDim.group().reduceSum(d => d["Value"]);


          let xScale = d3.scaleTime()
                         .range([0, width])
                         .domain(d3.extent(formatedData, d => d["Date"]));

          chart.width(width)
            .height(height)
            .margins({top: 50, right: 50, bottom: 50, left: 50})
            .y(d3.scaleLog()
              .clamp(true)
              .domain([1, 100000])
            )
            .x(xScale)
            .xUnits(d3.timeDays)
            .legend(dc.legend().x(width - 150).y(5).itemHeight(13).gap(5))
            .brushOn(true)
            .xAxisLabel("Day")
            .yAxisLabel("Log of # Users")
            .ordinalColors(['#2c7fb8'])
            .dimension(dateDim)
            .group(usersByDayGroup, "# Users")
            .renderArea(true)
            .renderDataPoints(true)
            .curve(d3.curveMonotoneX)
            .renderHorizontalGridLines(true)
            .renderVerticalGridLines(true)
            .yAxis()
              .tickValues([1, 10, 100, 1000, 10000, 100000])
                .tickFormat(d3.format("i"));


            // Pie chart
            piechart.width(width)
                    .height(height)
                    .slicesCap(4)
                    .innerRadius(100)
                    .externalLabels(50)
                    .externalRadiusPadding(50)
                    .drawPaths(true)
                    .dimension(fieldDim)
                    .group(q1ByDayGroup)
                    .label(d => {
                        return answers[d.key];
                    })
                    .legend(dc.legend().legendText( (d) => answers[d.name] ));

            piechart.onClick = function() {};

            dc.renderAll();
    });
}