import '../styles/index.scss';

let view;

function render(spec, el) {
    view = new vega.View(vega.parse(spec))
                .renderer('canvas')
                .initialize(el)
                .hover()
                .run();
}

// Chart 1 - Vega
vega.loader()
    .load("/src/charts/chart1.json")
    .then(data => {
        return render(JSON.parse(data), "#chart1");
    });
